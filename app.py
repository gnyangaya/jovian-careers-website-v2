from flask import Flask, render_template, jsonify

# Initialize the app
app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 1,000,000'
    },

    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 1,500,000'
    },

    {
        'id': 3,
        'title': 'Front-End Engineer',
        'location': 'Remote',
        'salary': 'Rs. 1,200,000'
    },

    {
        'id': 4,
        'title': 'Back-End Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    }
]

# Routes
@app.route("/")
def home():
    return render_template("home.html",
        jobs=JOBS,
        company_name='Jovian'
        )

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)