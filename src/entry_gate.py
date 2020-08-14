from flask import Flask, render_template,request
from src.classes.gettestobject import GetTestObject
from src.classes.applications import Applications
from src.classes.stammdaten import Stammdaten
import json

webapp = Flask(__name__)

@webapp.route('/')
def index():
    return (render_template("index.html"))

@webapp.route('/testobject')
def display_testobject():
    return (render_template("testobject.html"))

@webapp.route('/createtestobject')
def display_creaettestobject():
    return (render_template("createtestobject.html"))

@webapp.route('/application')
def display_application():
    return (render_template("application.html"))

@webapp.route('/release')
def display_release():
    return (render_template("release.html"))

@webapp.route('/user')
def display_user():
    return (render_template("user.html"))

@webapp.route('/api/')
def api():
    return_value = ""
    if request.args.get("function") == "get":
        data_obj = request.args.to_dict()
        # creating instance of testobject
        list_object = GetTestObject()
        # hit the methode to gader all data from db
        return_value = json.dumps(list_object.get_test_object(data_obj,True))
        # return object with all avaivable data
        del  list_object

    if request.args.get("function") == "create":
        #creat data object of value/pairs from all testobjekt attributes
        data_obj = request.args.to_dict()
        # creating instance of testobject
        list_object = GetTestObject()
        # hit the methode to save all attributes to db
        return_value = json.dumps(list_object.create_test_object(data_obj, True))
        del data_obj,list_object

    if request.args.get("function") == "update":
        #creat data object of value/pairs from all testobjekt attributes
        data_obj = request.args.to_dict()
        # creating instance of testobject
        list_object = GetTestObject()
        # hit the methode to save all attributes to db
        return_value = json.dumps(list_object.update_test_object (data_obj, True))
        del data_obj,list_object

    if request.args.get("function") == "delete":
        #creat data object of value/pairs from all testobjekt attributes
        data_obj = request.args.to_dict()
        # creating instance of testobject
        list_object = GetTestObject()
        # hit the methode to save all attributes to db
        return_value = json.dumps(list_object.delete_test_object(data_obj, True))
        del data_obj,list_object

    if request.args.get("function") == "list":
        # creating instance of testobject
        list_object = GetTestObject()
        # hit the methode to save all attributes to db
        return_value = json.dumps(list_object.list_test_objects(True))
        del list_object

    if request.args.get("function") == "stammdaten":
        #creat data object of value/pairs from all testobjekt attributes
        data_obj = request.args.to_dict()
        # creating instance of testobject
        stammdaten = Stammdaten(data_obj)
        # hit the methode to save all attributes to db
        return_value = json.dumps(stammdaten.modify(True))
        print (return_value)
        del data_obj,stammdaten

    if request.args.get("function") == "addattribute":
        #creat data object of value/pairs from all testobjekt attributes
        data_obj = request.args.to_dict()
        # creating instance of testobject
        test_obj = GetTestObject()
        # hit the methode to save all attributes to db
        return_add_attribute=json.dumps(test_obj.add_attribute(data_obj, True))
        del data_obj,test_obj

    return (return_value)


if __name__=='__main__':
    webapp.run(debug=True, host='0.0.0.0')