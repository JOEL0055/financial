from flask import Flask, render_template
import os

# Initialize the Flask application
app = Flask(__name__, template_folder="templates")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Print the template folder path for debugging
    print(f"Template folder: {app.template_folder}")
    print(f"Index exists: {os.path.exists(os.path.join(app.template_folder, 'index.html'))}")
    
    # Run the Flask app
    app.run(debug=True, port=5002)
