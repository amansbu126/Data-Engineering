import pandas as pd
from sqlalchemy import create_engine

# Load CSV into pandas
#df = pd.read_csv(C:\Users\Aman Kumar\OneDrive\11-05-2025 AWS Sachin\Sample Data\sales_data.csv", parse_dates=["OrderDate", "ShipDate"])

#df = pd.read_csv(r"C:\Users\Aman Kumar\OneDrive\11-05-2025 AWS Sachin\Sample Data\sales_data.csv", parse_dates=["OrderDate", "ShipDate"])
df = pd.read_csv("C:/Users/Aman Kumar/OneDrive/11-05-2025 AWS Sachin/Sample Data/Salescsvfile.csv", parse_dates=["order_date", "ship_date"])

# Rename columns to match the PostgreSQL table (optional, only if needed)
df.columns = [col.lower().replace(" ", "_") for col in df.columns]

# Database connection info — replace with your actual values
db_user = ""
db_password = ""
db_host = ""
db_port = ""
db_name = ""
db_schema = ''

# Create connection string
#engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
    connect_args={"options": f"-c search_path={db_schema}"}
)
# Load data to PostgreSQL (table must already exist)
df.to_sql(
    "sales_data",
    engine,
    index=False,
    if_exists="replace"  # or "append"
)


print("✅ CSV data uploaded successfully to RDS PostgreSQL!")
