from flask import Flask
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


@app.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()

        conn.close()

        return f"""
        <h1>Inventory Application</h1>
        <p>Database Connection Successful</p>
        <p>MariaDB Version: {version[0]}</p>
        """

    except Exception as e:
        return f"""
        <h1>Inventory Application</h1>
        <p>Database Connection Failed</p>
        <p>{str(e)}</p>
        """, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
