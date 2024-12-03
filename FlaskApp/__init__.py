from flask import Flask
from flask import request
from flask import abort

from Y2024 import *

year = "2024"

app = Flask(__name__)

@app.route("/day/<int:dayNo>", methods = ['GET', 'POST'])
def index(dayNo: int):
    try:
        dayHandler = globals().get(f"day{dayNo}").process
    except:
        abort(404, f"day{dayNo} has not yet been implemented")

    if callable(dayHandler):
        return (dayHandler(request, year, dayNo))
    else:
        abort(500, f"Interface spec violation for day{dayNo}")

if __name__ == "__main__":
    app.run()