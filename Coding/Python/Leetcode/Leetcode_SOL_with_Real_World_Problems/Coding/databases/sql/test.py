# print("Testing")
# import sys
# try:
#     from db import DB
#     print("Imported DB")
# except Exception as e:
#     print(f"Error importing DB: {e}")
#     sys.exit(1)

# try:
#     db = DB()
#     print("DB object created")
# except Exception as e:
#     print(f"Error creating DB object: {e}")
#     sys.exit(1)

# print("Program complete")







#pymysyql
print("Testing", flush=True)
import sys
try:
    from db import DB
    print("Imported DB", flush=True)
except taxeption as e:
    print(f"Error importing DB: {e}", flush=True)
    sys.exit(1)

try:
    db = DB()
    print("DB object created", flush=True)
except Exception as e:
    print(f"Error creating DB object: {e}", flush=True)
    sys.exit(1)

print("Program complete", flush=True)