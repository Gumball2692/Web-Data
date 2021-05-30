from flask import Flask
import sqlite3

database = "awsome_job.db"
app = Flask(__name__)


@app.route("/")
def web_recruitme():
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS stocks (name text, url text)''')
        cursor.execute("INSERT INTO stocks VALUES ('00','https://github.com/awesome-jobs/vietnam/issues/2502')")
        cursor.execute("INSERT INTO stocks VALUES ('01','https://github.com/awesome-jobs/vietnam/issues/2501')")
        cursor.execute("INSERT INTO stocks VALUES ('02','https://github.com/awesome-jobs/vietnam/issues/2500')")
        cursor.execute("INSERT INTO stocks VALUES ('03','https://github.com/awesome-jobs/vietnam/issues/2499')")
        for row in cursor.execute("SELECT * FROM stocks WHERE url='https://github.com/awesome-jobs/vietnam/issues/2502'").fetchall():
            tags = []
        cursor.execute("select name, url from stocks")
        conn.commit()
        for title, url in cursor.fetchall():
            tag = "<div><a href = {}>{}</a></div>".format(url, title)
            tags.append(tag)

        result = (
            "<html><head><title>Jobs IT</title>"
            "<style>a {text-decoration: none;"
            "line-height: 2;}"
            "a:hover {color: blue;}</style></head>"
            "<body>IT JOBS" + "\n".join(tags) + "</body></html>"
            )
    
    return result

if __name__ == "__main__":
    app.run(debug=True)