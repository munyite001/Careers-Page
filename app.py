#!/usr/bin/python3
from flask import Flask, render_template, jsonify
from database import load_job_from_db, load_jobs

app = Flask(__name__)


@app.route('/')
def hello_devtime():
    JOBS = load_jobs()
    return render_template("index.html", jobs=JOBS)


@app.route('/job/<id>')
def show_job(id):
    job=load_job_from_db(id)
    if not job:
        return "Not Found!", 404
    return render_template("job.html", job=job)

@app.route('/api/jobs')
def list_jobs():
    JOBS = load_jobs()
    return jsonify(JOBS)

if __name__ == ("__main__"):
    app.run('0.0.0.0', 5500, debug=True)