# print("Starting test_db.py")
# try:
#     import mysql.connector
#     print("Imported mysql.connector")
#     conn = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password='',
#         database='loginsystem'
#     )
#     print("Connected to database successfully")
#     conn.close()
# except Exception as e:
#     print(f"An error occurred: {type(e).__name__}: {e}")



import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='loginsystem'
    )
    if conn.is_connected():
        print("Successfully connected to the database")
    conn.close()
except Error as e:
    print(f"Error: {e}")