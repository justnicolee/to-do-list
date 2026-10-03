
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route("/tasks")
def home():

    return render_template("tdl.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():

    newtask = request.form["newtsk"]

    tasks.append(newtask)

    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete_task(index):

    tasks.pop(index)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)