import mysql.connector

# Database connection details
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'yes',
    'database': 'crud_db'
}

try:
    conn = mysql.connector.connect(**db_config)
    print("Content-Type: text/html\n")
    print("Connected successfully!")
    conn.close()
except mysql.connector.Error as err:
    print("Content-Type: text/html\n")
    print(f"Error: {err}")
