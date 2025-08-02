from flask import Flask, render_template, request, redirect

app = Flask(__name__)
messages = []

@app.route("/")
def index():
    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    msg = request.form["message"]
    messages.append(msg)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
