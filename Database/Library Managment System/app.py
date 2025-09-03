from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

def get_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-1234\\SQLEXPRESS;"
        "Database=BookStoreDB;"
        "Trusted_Connection=yes;"
    )
    return conn

@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT BookID, Title, Author, Price FROM Books")
    books = cursor.fetchall()
    conn.close()
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
