from flask import Flask, render_template, request
from generator.ai_generator import generate_website

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        code = generate_website(prompt)
        return render_template("result.html", code=code)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
