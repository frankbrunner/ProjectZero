import json
from flask import Flask, render_template,request,escape
app = Flask(__name__)



@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    return (render_template("layouts/main.html", name="Frank Brunner"))




if __name__=='__main__':
    app.run(debug=True, host="127.0.0.1")