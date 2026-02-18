from flask import Flask, render_template
import sqlite3
 
app = Flask(__name__)
 
def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    conn.close()
    return data
 
@app.route("/")
def dashboard():
    employees = get_data()
 
    total = len(employees)
    available = sum(1 for e in employees if e[4] == "Available")
    deployed = sum(1 for e in employees if e[4] == "Deployed")
    partial = sum(1 for e in employees if e[4] == "Partial")
 
    return render_template(
        "index.html",
        employees=employees,
        total=total,
        available=available,
        deployed=deployed,
        partial=partial
    )
 
if __name__ == "__main__":
    app.run()
