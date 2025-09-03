from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"   # agar express edition hai to localhost\\SQLEXPRESS likho
        "Database=BookStoreDB;"
        "Trusted_Connection=yes;"
    )

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
