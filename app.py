#!/usr/bin/python3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Nairobi, Kenya',
        'salary': 'Ksh 100,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Mombasa, Kenya',
        'salary': 'Ksh 120,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Ksh 120,000'
    },
    {
        'id': 1,
        'title': 'Backend Engineer',
        'location': 'Nairobi, Kenya',
        'salary': 'Ksh 200,000'
    }
]

@app.route('/')
def hello():
    return render_template("index.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == ("__main__"):
    app.run('0.0.0.0', 5500, debug=True)