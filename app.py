from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

# Initialize the app
app = Flask(__name__)

# Routes
@app.route("/")
def home():
    jobs_list = load_jobs_from_db()

    return render_template("home.html",
        jobs=jobs_list,
        company_name='Jovian'
        )

@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_jobs_from_db())

if __name__ == "__main__":
    app.run(debug=True)