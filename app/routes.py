from flask import Flask

app = flask(__name__)

@app.get("/")
def index():
    me = {
        "first-name": "Moses",
        "last-name": "KY",
        "hobbies": "soccer",
        "is_online": True
            }
         return me   