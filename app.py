#!/usr/bin/python3
from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine

app = Flask(__name__)

#   Function to load jobs from the database
def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        #   Convert Sql Alchemy Legacy row to list of dictionaries
        result_dict = []

        for res in result.all():
            result_dict.append(dict(res))
    return result_dict


@app.route('/')
def hello_devtime():
    JOBS = load_jobs()
    return render_template("index.html", jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    JOBS = load_jobs()
    return jsonify(JOBS)

if __name__ == ("__main__"):
    app.run('0.0.0.0', 5500, debug=True)