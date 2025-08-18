# # import sys
# # from db import DB
# # class Flipkart:
# #     def __init__(self):
# #         self.db = DB()
# #         self.menu()
# #     def menu(self):
# #         user_input = input("""
# # Welcome to Flipkart!
# #                     1. Enter 1 to Register
# #                     2. Enter 2 to Login
# #                     3. Enter 3 to Exit
# #                     """)    
# #         if user_input == '1':
# #             self.register()
# #         elif user_input == '2':
# #             self.login()    
# #         else:
# #             print("Exiting the application. Goodbye!")
# #             sys.exit()
   

# # if __name__ == "__main__":
# #     try:
# #         Flipkart()
# #     except Exception as e:
# #         print(f"An error occurred: {e}")

# # # import sys
# # # from db import db

# # # class Flipkart:
# # #     def __init__(self):
# # #         self.db = db()
# # #         self.menu()

# # #     def menu(self):
# # #         while True:
# # #             user_input = input("""
# # # Welcome to Flipkart!
# # # 1. Register
# # # 2. Login
# # # 3. Exit
# # # Please enter your choice: """)
# # #             if user_input == '1':
# # #                 self.register()
# # #             elif user_input == '2':
# # #                 self.login()
# # #             elif user_input == '3':
# # #                 print("Exiting the application. Goodbye!")
# # #                 sys.exit()
# # #             else:
# # #                 print("Invalid input. Please try again.")

# # #     def register(self):
# # #         username = input("Enter a username: ").strip()
# # #         password = input("Enter a password: ").strip()
# # #         if self.db.register_user(username, password):
# # #             print("Registration successful!")
# # #         else:
# # #             print("Registration failed.")

# # #     def login(self):
# # #         username = input("Enter your username: ").strip()
# # #         password = input("Enter your password: ").strip()
# # #         if self.db.authenticate_user(username, password):
# # #             print(f"Welcome back, {username}!")
# # #         else:
# # #             print("Login failed. Incorrect username or password.")

# # # if __name__ == "__main__":
# # #     try:
# # #         Flipkart()
# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")







# #pymysql








# import sys
# from db import DB

# class Flipkart:
#     def __init__(self):
#         print("Initializing Flipkart class", flush=True)
#         try:
#             self.db = DB()
#             print("DB object created", flush=True)
#         except Exception as e:
#             print(f"Error creating DB object: {e}", flush=True)
#             sys.exit(1)
#         self.menu()

#     def menu(self):
#         print("Displaying menu", flush=True)
#         user_input = input("""
# Welcome to Flipkart!
#                     1. Enter 1 to Register
#                     2. Enter 2 to Login
#                     3. Enter 3 to Exit
#                     """)
#         if user_input == '1':
#             print("Calling register", flush=True)
#             self.register()
#         elif user_input == '2':
#             print("Calling login", flush=True)
#             self.login()
#         else:
#             print("Exiting the application. Goodbye!", flush=True)
#             sys.exit(0)

#     def register(self):
#         print("Register function called", flush=True)
#         # Placeholder for register logic
#         pass

#     def login(self):
#         print("Login function called", flush=True)
#         # Placeholder for login logic
#         pass

# if __name__ == "__main__":
#     print("Starting app.py", flush=True)
#     try:
#         Flipkart()
#     except Exception as e:
#         print(f"An error occurred in main: {e}", flush=True)
#         sys.exit(1)
#     def register(self):
#         name = input("Enter your name: ")
#         email = input("Enter your email: ")
#         password = input("Enter your password: ")
#         if self.db.register(name, email, password):
#             print("Registration successful!")
            
#         else:
#             print("Registration failed. Please try again.")
#         self.menu()








import sys
from db import DB

class Flipkart:
    def __init__(self):
        print("Initializing Flipkart class", flush=True)
        try:
            self.db = DB()
            print("DB object created", flush=True)
        except Exception as e:
            print(f"Error creating DB object: {e}", flush=True)
            sys.exit(1)
        self.menu()

    def menu(self):
        print("Displaying menu", flush=True)
        while True:  # Loop to keep menu active
            user_input = input("""
Welcome to Flipkart!
                    1. Enter 1 to Register
                    2. Enter 2 to Login
                    3. Enter 3 to Exit
                    """)
            if user_input == '1':
                print("Calling register", flush=True)
                self.register()
            elif user_input == '2':
                print("Calling login", flush=True)
                self.login()
            elif user_input == '3':
                print("Exiting the application. Goodbye!", flush=True)
                sys.exit(0)
            else:
                print("Invalid input. Please try again.", flush=True)

    def register(self):
        print("Register function called", flush=True)
        name = input("Enter your name: ").strip()
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            if self.db.register(name, email, password):
                print("Registration successful!", flush=True)
            else:
                print("Registration failed. Please try again.", flush=True)
        except Exception as e:
            print(f"Registration error: {e}", flush=True)
        self.menu()

    def login(self):
        print("Login function called", flush=True)
        email = input("Enter your email: ").strip()
        password = input("Enter your password: ").strip()
        try:
            if self.db.authenticate_user(email, password):
                print(f"Welcome back, {email}!", flush=True)
            else:
                print("Login failed. Incorrect email or password.", flush=True)
        except Exception as e:
            print(f"Login error: {e}", flush=True)
        self.menu()

if __name__ == "__main__":
    print("Starting app.py", flush=True)
    try:
        Flipkart()
    except Exception as e:
        print(f"An error occurred in main: {e}", flush=True)
        sys.exit(1)