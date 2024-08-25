from flask import Flask, render_template, request

app = Flask(__name__, template_folder="/Users/joelaiweithai/Downloads/templates")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Specify a different port using the 'port' keyword argument
    app.run(port=5002)
