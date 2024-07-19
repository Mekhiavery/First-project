import psycopg2
import getpass

def connect_to_db():
    """ Connect to the PostgreSQL database server """
    password = getpass.getpass('Password for user mekhi: ')
    conn = psycopg2.connect(
        dbname="stock_marketsql",
        user="mekhi",
        password=1979,
        host="localhost"
    )
    return conn

def get_table_info(conn, table_name):
    """ Retrieve and print the first 10 rows and column details from a specified table """
    cur = conn.cursor()

    # Fetching the first 10 rows of the table
    cur.execute(f"SELECT * FROM {table_name} LIMIT 10;")
    rows = cur.fetchall()
    
    # Fetching column information
    cur.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name}';")
    columns = cur.fetchall()

    print(f"\nTable: {table_name}")
    print("Columns and Data Types:")
    for col in columns:
        print(f"{col[0]} ({col[1]})")
    
    print("\nFirst 10 Rows:")
    for row in rows:
        print(row)

    cur.close()

def main():
    """ Connect to the database and print details for specified tables """
    conn = connect_to_db()
    try:
        # Specify your table names here
        tables = ['Companies', 'Stocks', 'Markets']
        for table in tables:
            get_table_info(conn, table)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
