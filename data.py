import mysql.connector
import pandas as pd

def get_data(username,password,database, table):
    connection = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database=database
        )
    cursor = connection.cursor()

    query = f"SELECT * FROM {table}"
    cursor.execute(query)

    data = cursor.fetchall()
    df = pd.DataFrame(data)

    connection.close()

    return df