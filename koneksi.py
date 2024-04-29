import mysql.connector
import pandas as pd

def connect_database(username, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database="steam_library"
        )
        return connection

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

def close_database(connection):
    if connection is not None and connection.is_connected():
        connection.close()

def insert_data(username, password, table, data):

    connection = connect_database(username, password)
    
    if connection is None:
        print("Error connecting to database")
        return False

    try:
        cursor = connection.cursor()
        sql = f"INSERT INTO {table} ({','.join(data.keys())}) VALUES ({','.join(['%s' for _ in data.values()])})"
        val = tuple(data.values())
        print(data)
        cursor.execute(sql, val)
        connection.commit()
        print("Data inserted successfully!")
        return True
    except Exception as e:
        print(f"Error inserting data: {str(e)}")
        connection.rollback() 
        return False
    finally:
        close_database(connection)

def get_data(username,password, table):
    connection = connect_database(username, password)
    cursor = connection.cursor()

    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    data = cursor.fetchall()
    df = pd.DataFrame(data)

    connection.close()

    return df