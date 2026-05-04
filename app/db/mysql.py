import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sunny@6801",
        database="ai_logistics",
        auth_plugin="mysql_native_password"
    )