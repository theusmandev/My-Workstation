# # test_mysql.py
# print("Testing MySQL connector import")
# try:
#     import mysql.connector
#     print("MySQL connector imported successfully")
# except Exception as e:
#     print(f"Error importing mysql.connector: {e}")




# # test_mysql.py (or sqll.py)
# print("Testing MySQL connector import")
# try:
#     import mysql.connector
#     print("MySQL connector imported successfully")
# except Exception as e:
#     print(f"Error importing mysql.connector: {e}")


# print("Starting connection test", flush=True)
# try:
#     import mysql.connector
#     print("MySQL connector imported", flush=True)
#     conn = mysql.connector.connect(
#         host='127.0.0.1',
#         user='root',
#         password='',
#         database='loginsystem'
#     )
#     print("Connected successfully", flush=True)
#     conn.close()
# except Exception as e:
#     print(f"Connection error: {e}", flush=True)
# print("Test complete", flush=True)










# import sys
# print("Starting connection test", flush=True)
# try:
#     import mysql.connector
#     print("MySQL connector imported", flush=True)
#     print("Attempting connection", flush=True)
#     conn = mysql.connector.connect(
#         host='127.0.0.1',
#         user='root',
#         password='',
#         database='loginsystem'
#     )
#     print("Connected successfully", flush=True)
#     conn.close()
# except Exception as e:
#     print(f"Connection error (Exception): {e}", flush=True)
# except BaseException as e:
#     print(f"Critical error (BaseException): {e}", flush=True)
#     sys.exit(1)
# except:
#     print("Unknown error occurred during connection", flush=True)
#     sys.exit(1)
# print("Test complete", flush=True)










import sys
import mysql.connector
print("Starting connection test", flush=True)
try:
    print("MySQL connector version:", mysql.connector.__version__, flush=True)
    print("Attempting connection", flush=True)
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='loginsystem'
    )
    print("Connected successfully", flush=True)
    conn.close()
except Exception as e:
    print(f"Connection error (Exception): {e}", flush=True)
except BaseException as e:
    print(f"Critical error (BaseException): {e}", flush=True)
    sys.exit(1)
except:
    print("Unknown error occurred during connection", flush=True)
    sys.exit(1)
print("Test complete", flush=True)