import os
import pandas as pd
import pyodbc
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
CNXN_STR = os.getenv("SQLSERVER_CNXN")

# Define CSVs and their columns
TABLES = [
    ("Accounts", ["AccountId","AccountName","Industry","BillingCity","OwnerUserId","CreatedDate"]),
    ("Contacts", ["ContactId","AccountId","FirstName","LastName","Email","Phone","CreatedDate"]),
    ("Opportunities", ["OpportunityId","AccountId","OwnerUserId","Name","StageName","Amount","CloseDate","IsWon","CreatedDate"]),
]

def load_csv_to_df(base, cols):
    path = os.path.join("data", f"{base}.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    df = pd.read_csv(path)
    return df[cols].drop_duplicates()

# Connect and load data into SQL Server
with pyodbc.connect(CNXN_STR) as cn:
    cur = cn.cursor()
    for tbl, cols in TABLES:
        df = load_csv_to_df(tbl, cols)
        print(f"Loading {tbl}...")

        # Create staging table
        staging = f"#{tbl}_stg"
        col_defs = ",".join([f"[{c}] NVARCHAR(4000)" for c in cols])
        cur.execute(f"CREATE TABLE {staging} ({col_defs});")

        # Insert data into staging
        placeholders = ",".join(["?"]*len(cols))
        cur.fast_executemany = True
        cur.executemany(
            f"INSERT INTO {staging} ({','.join('['+c+']' for c in cols)}) VALUES ({placeholders})",
            df.astype(str).values.tolist(),
        )

        # Merge data
        pk = cols[0]
        update_set = ",".join([f"T.[{c}] = S.[{c}]" for c in cols[1:]])
        insert_cols = ",".join([f"[{c}]" for c in cols])
        insert_vals = ",".join([f"S.[{c}]" for c in cols])

        cur.execute(f"""
            MERGE dbo.{tbl} AS T
            USING {staging} AS S
            ON T.[{pk}] = S.[{pk}]
            WHEN MATCHED THEN UPDATE SET {update_set}
            WHEN NOT MATCHED BY TARGET THEN INSERT ({insert_cols}) VALUES ({insert_vals});
            DROP TABLE {staging};
        """)
    cn.commit()

print("✅ ETL completed successfully!")
