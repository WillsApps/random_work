from sqlite3 import connect

from beartype.typing import Any, Dict, List
from flask import Flask, jsonify, request

from general_utils.threading import Manager

app = Flask(__name__)
queue = Manager()


def insert_log(productivity_score: int, activity: str):
    conn = connect("productivity.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productivity_log (productivity_score, activity) VALUES (?, ?)",
        (productivity_score, activity),
    )
    conn.commit()
    conn.close()


def get_logs() -> List[Dict[str, Any]]:
    conn = connect("productivity.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productivity_log")
    rows = cursor.fetchall()
    conn.close()
    return rows


@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200


@app.route("/api/log", methods=["POST"])
def post_log():
    data = request.get_json()
    productivity_score = data.get("productivity_score")
    activity = data.get("activity")
    # Process the data
    queue.put((insert_log, {"productivity_score": productivity_score, "activity": activity}))
    return jsonify({"message": "Data received", "received_data": data}), 200


@app.route("/api/data", methods=["GET"])
def get_data():
    # Fetch and return data
    return jsonify({"message": "Data sent", "data": {}}), 200


def setup_db():
    conn = connect("productivity.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productivity_log (
    id INTEGER PRIMARY KEY,
    productivity_score INTEGER, 
    activity TEXT,
    _inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    setup_db()
    app.run(debug=True)
