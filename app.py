from flask import Flask, render_template

# Initialize the app
app = Flask(__name__)

# Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "<h2>This is the About Page 🚀</h2>"

if __name__ == "__main__":
    app.run(debug=True)