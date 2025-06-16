# # # import mysql.connector
# # # class DB:
# # #     def __init__(self):
# # #         try:
# # #             self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='loginsystem')
# # #             self.mycursor = self.conn.cursor()
# # #         except:
# # #             print("Some Error Occured")
# # #         else:
# # #             print("Connected to the database successfully")








# # import mysql.connector

# # class DB:
# #     def __init__(self):
# #         print("Attempting to connect to database")
# #         try:
# #             self.conn = mysql.connector.connect(
# #                 host='localhost',
# #                 user='root',
# #                 password='',
# #                 database='loginsystem'
# #             )
# #             self.mycursor = self.conn.cursor()
# #             print("Connected to the database successfully")
# #         except Exception as e:
# #             print(f"Error connecting to MySQL: {e}")
# #             self.conn = None
# #             self.mycursor = None

























































































































































































































































# # # import mysql.connector
# # # import bcrypt
# # # import os
# # # from dotenv import load_dotenv

# # # load_dotenv()

# # # class db:
# # #     def __init__(self):
# # #         try:
# # #             self.conn = mysql.connector.connect(
# # #                 host=os.getenv('DB_HOST', 'localhost'),
# # #                 user=os.getenv('DB_USER', 'root'),
# # #                 password=os.getenv('DB_PASSWORD', ''),
# # #                 database=os.getenv('DB_NAME', 'loginsystem')
# # #             )
# # #             self.cursor = self.conn.cursor()
# # #             self.create_users_table()
# # #             print("Connected to the database successfully")
# # #         except mysql.connector.Error as err:
# # #             print(f"Database connection failed: {err}")
# # #             raise

# # #     def create_users_table(self):
# # #         try:
# # #             self.cursor.execute("""
# # #                 CREATE TABLE IF NOT EXISTS users (
# # #                     id INT AUTO_INCREMENT PRIMARY KEY,
# # #                     username VARCHAR(255) UNIQUE NOT NULL,
# # #                     password VARCHAR(255) NOT NULL
# # #                 )
# # #             """)
# # #             self.conn.commit()
# # #         except mysql.connector.Error as err:
# # #             print(f"Error creating table: {err}")
# # #             raise

# # #     def register_user(self, username, password):
# # #         if not username or not password:
# # #             print("Username and password cannot be empty")
# # #             return False
# # #         try:
# # #             self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
# # #             if self.cursor.fetchone():
# # #                 print("Username already exists")
# # #                 return False
# # #             hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# # #             self.cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
# # #                              (username, hashed_password))
# # #             self.conn.commit()
# # #             return True
# # #         except mysql.connector.Error as err:
# # #             print(f"Error during registration: {err}")
# # #             return False

# # #     def authenticate_user(self, username, password):
# # #         try:
# # #             self.cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
# # #             result = self.cursor.fetchone()
# # #             if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
# # #                 return True
# # #             return False
# # #         except mysql.connector.Error as err:
# # #             print(f"Error during login: {err}")
# # #             return False

# # #     def __del__(self):
# # #         try:
# # #             self.cursor.close()
# # #             self.conn.close()
# # #             print("Database connection closed")
# # #         except mysql.connector.Error:
# # #             pass













# import pymysql
# import sys

# class DB:
#     def __init__(self):
#         print("Attempting to connect to database", flush=True)
#         try:
#             self.conn = pymysql.connect(
#                 host='127.0.0.1',
#                 port=3306,
#                 user='root',
#                 password='',
#                 database='loginsystem'
#             )
#             self.mycursor = self.conn.cursor()
#             print("Connected to the database successfully", flush=True)
#         except Exception as e:
#             print(f"Error connecting to MySQL: {e}", flush=True)
#             self.conn = None
#             self.mycursor = None
#     def register(self,name,email,password):
#         self.mycursor.execute('''
# Insert into 'users' ('id','name',email','password') Values (NULL, '{}','{}','{}')
# '''.format(name,email,password))
#         self.conn.commit()
#         print("User registered successfully", flush=True)
        


import pymysql
import sys

class DB:
    def __init__(self):
        print("Attempting to connect to database", flush=True)
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='',
                database='loginsystem'
            )
            self.mycursor = self.conn.cursor()
            print("Connected to the database successfully", flush=True)
        except Exception as e:
            print(f"Error connecting to MySQL: {e}", flush=True)
            self.conn = None
            self.mycursor = None

    def register(self, name, email, password):
        if not self.conn or not self.mycursor:
            print("Database connection not available", flush=True)
            return False
        try:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            self.mycursor.execute(query, (name, email, password))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Registration error: {e}", flush=True)
            return False

    def authenticate_user(self, email, password):
        if not self.conn or not self.mycursor:
            print("Database connection not available", flush=True)
            return False
        try:
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            self.mycursor.execute(query, (email, password))
            user = self.mycursor.fetchone()
            return user is not None
        except Exception as e:
            print(f"Authentication error: {e}", flush=True)
            return False