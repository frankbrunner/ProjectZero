import json
from ProjectZero.src.functions_testobjects import pz_Testobject
from ProjectZero.src.functions_projects import pz_Projects
from ProjectZero.src.functions_releases import pz_Releases

from flask import Flask, render_template,request,escape
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

dbuser = "dbuser"
password = "34df!5awe"
db = "ProjectZero"

testobject = pz_Testobject(dbuser,password,db)
projects = pz_Projects(dbuser,password,db)
releases = pz_Releases(dbuser,password,db)



@app.route('/')
def hello():
    #name = request.args.get("name", "World")
    return (render_template("demand.html", name="Frank Brunner"))

@app.route('/api/')
def api():
    print(request.args.get("function"))
    if request.args.get("function") == "gettestobjects":
        result = testobject.getTestobject()
    if request.args.get("function") == "getprojects":
        result = projects.getProjects()
    if request.args.get("function") == "savetestobject":
        result = testobject.createTestobject(request.args.get("projectnumber"))
    if request.args.get("function") == "getrelease":

        result = testobject.getAllReleases(request.args.get("projectnumber"),True)
    if request.args.get("function") == "getreleases":
        result = releases.getReleases()
    if request.args.get("function") == "addrelease":

        result = testobject.addRelease(request.args.get("projectnumber"),request.args.get("releasename"),True)
    return json.dumps(result)



if __name__=='__main__':
    app.run(debug=True, host="192.168.1.25")