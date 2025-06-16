import pymysql
print("Starting pymysql connection test", flush=True)
try:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='',
        database='loginsystem'
    )
    print("Connected successfully", flush=True)
    conn.close()
except Exception as e:
    print(f"Connection error: {e}", flush=True)
print("Test complete", flush=True)