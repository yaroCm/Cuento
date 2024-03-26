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
            # Realizar una consulta en la tabla
            sql = "SELECT * FROM example_table"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("Resultado de la consulta:", result)
    finally:
        # Cerrar la conexión a la base de datos
        connection.close()

    return {
        'statusCode': 200,
        'body': 'Consulta realizada con éxito'
    }
