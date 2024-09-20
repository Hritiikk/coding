import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="flight_prices",  # Make sure this database exists
        user="your_user",
        password="your_password"
    )
    return conn

def insert_flight_data(conn, flight_data):
    cursor = conn.cursor()
    query = """INSERT INTO flights (origin, destination, departure_date, price) 
               VALUES (%s, %s, %s, %s)"""
    cursor.execute(query, flight_data)
    conn.commit()
