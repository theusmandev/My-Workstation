from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)


def get_connection():
    return pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=localhost;"      # agar Express edition hai to localhost\\SQLEXPRESS
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

# ✅ Add Book (Form Page)
@app.route("/add", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        price = request.form["price"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (Title, Author, Price) VALUES (?, ?, ?)", (title, author, price))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))
    return render_template("add_book.html")

# ✅ Edit Book (Update)
@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        price = request.form["price"]

        cursor.execute("UPDATE Books SET Title=?, Author=?, Price=? WHERE BookID=?", (title, author, price, book_id))
        conn.commit()
        conn.close()
        return redirect(url_for("home"))

    cursor.execute("SELECT BookID, Title, Author, Price FROM Books WHERE BookID=?", (book_id,))
    book = cursor.fetchone()
    conn.close()
    return render_template("edit_book.html", book=book)

# ✅ Delete Book
@app.route("/delete/<int:book_id>")
def delete_book(book_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE BookID=?", (book_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
