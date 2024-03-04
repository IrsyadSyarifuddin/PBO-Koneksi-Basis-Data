import mysql.connector

def connect_database(username, password):
    try:
        connection = mysql.connector.connect(
            


            
        )
        return connection

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

def close_database(connection):
    if connection is not None and connection.is_connected():
        connection.close()
