import sys
import os
import json
import pymysql

def lambda_handler(event, context):
    # Configurar la conexión a la base de datos
    connection = pymysql.connect(
        host='lab01-db-instance.cpo6yqaim4wy.us-east-1.rds.amazonaws.com',
        user='admin',
        password='adminadmin',
        database='lab01db',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        # Realizar la conexión a la base de datos
        with connection.cursor() as cursor:
            # Realizar una inserción en la tabla
            sql = "INSERT INTO example_table (name, age) VALUES (%s, %s)"
            val = ("John", 30)  # Example data for insertion
            cursor.execute(sql, val)

            # Commit the transaction
            connection.commit()

            print("Se insertaron", cursor.rowcount, "filas.")
    finally:
        # Cerrar la conexión a la base de datos
        connection.close()

    return {
        'statusCode': 200,
        'body': 'Inserción realizada con éxito'
    }
