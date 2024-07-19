import psycopg2
import getpass

def connect_to_db():
    password = getpass.getpass('Password for user mekhi: ')
    conn = psycopg2.connect(
        dbname="stock_marketsql",
        user="mekhi",
        password=1979,
        host="localhost"
    )
    return conn

def perform_queries(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name AS Company_Name, s.date AS Date, s.open_price AS Open
        FROM Companies c
        JOIN Stocks s ON c.id = s.company_id
        WHERE c.name = 'Apple Inc.'
        ORDER BY s.date;
    """)
    results = cur.fetchall()
    for result in results:
        print(result)
    cur.close()

def main():
    conn = connect_to_db()
    try:
        perform_queries(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
