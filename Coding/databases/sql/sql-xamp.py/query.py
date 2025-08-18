import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       
        database="company" 
    )
    print("✅ Connected to MySQL!")
except Exception as e:
    print("❌ Connection failed:", e)
    exit()

cursor = conn.cursor()
cursor.execute("SELECT * FROM clean_employees")
rows = cursor.fetchall()

print("🔍 Rows fetched:", len(rows))
for row in rows:
    print(row)

cursor.close()
conn.close()
