from src.classes.db_functions import DB_Functions
from src.classes.db_shema import *

class GetTestObject():
    def __init__(self):
        # set the test object Id Variable
        pass

    def create_test_object(self,data_object,debug=False):
        #generate the db function object, db function finally call the database
        db_functions = DB_Functions()
        # set table name form struct class Testobject
        obj_struct = TestObject()
        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist= db_functions.checkIfExists(obj_struct.name,obj_struct.project, data_object["project"])
        #if record exist return according value 2 vor allready exist
        if does_record_exist:
            return 2
        #prepare data to write in database it needs in two seperate dict and verify with db_struct
        data_object = self.value_pairs_to_dicts(data_object,obj_struct.column)
        #create finaly the record
        return_value= db_functions.record_create(obj_struct.name,data_object[0],data_object[1],debug=True)
        #cleanup object instances
        del obj_struct
        #debug mode
        self.debug(debug,return_value)
        # return value true or false
        return return_value

    def update_test_object(self, data_object, debug=False):
        #generate the db function object, db function finally call the database
        db_functions = DB_Functions()
        # set table name form struct class Testobject
        obj_struct = TestObject()
        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist= db_functions.checkIfExists(obj_struct.name, obj_struct.project, data_object["project"])
        #if record exist return according value 2 vor allready exist
        if not does_record_exist:
            return 2
        #prepare data to write in database it needs in two seperate dict and verify with db_struct
        data_object_value_pairs = self.value_pairs_to_dicts(data_object, obj_struct.column)
        #create finaly the record
        return_value= db_functions.record_update(obj_struct.name, data_object_value_pairs[0], data_object_value_pairs[1], obj_struct.project, data_object["project"])
        #cleanup object instances
        del obj_struct
        #debug mode
        self.debug(debug,return_value)
        # return value true or false
        return return_value

    def get_test_object(self,data_object,debug=False):
        #generate the db function object, db function finaly call the database
        #Returns the a value pair obect with onl
        table_object = TestObject()

        db_functions = DB_Functions()
        attributes = db_functions.get_data_from_table(table_object, table_object.project, data_object["project"])
        #add the releases to the objcet
        table_attribute = Project_Releases()
        attribute_value = db_functions.get_attribute_from_table(table_attribute,table_attribute.release,table_object.project, data_object["project"])
        attributes = self.add_attribute_to_list(attributes, table_attribute.release, attribute_value)
        #add the applicatio to the objcet
        table_applications = Project_Applications()
        attribute_value = db_functions.get_attribute_from_table(table_applications,table_applications.application,table_object.project, data_object["project"])
        attributes = self.add_attribute_to_list(attributes, table_applications.application, attribute_value)

        return attributes

    def add_attribute_to_list(self, list, attribute_name, attribute_value):
        if attribute_name != None:
            attribute_list = []
            x = 0
            for item in attribute_value:
                attribute_list.append(attribute_value[x][0])
                x +=1
            list[attribute_name] = attribute_list
        return list

    def delete_test_object(self,data_object,debug=False):
        # generate the db function object, db function finally call the database
        db_functions = DB_Functions()
        # set table name form struct class Testobject
        table = TestObject()
        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist = db_functions.checkIfExists(table.name, table.project, data_object["project"])
        # if record exist return according value 2 vor allready exist
        if not does_record_exist:
            return 2
        return_value = db_functions.delete_record(table.name,table.project,data_object["project"])
        del table
        return return_value

    def list_test_objects(self,debug=False):
        #Returns an List that inclues a list for all availabel attributes include a list wiht all values
        # generate the db function object, db function finally call the database
        db_functions = DB_Functions()
        # set table name form struct class Testobject
        table = TestObject()
        return_value = db_functions.list_records(table)
        self.debug(debug,return_value)
        return (return_value)

    def add_attribute(self, data_object, debug=False):
        #generate the db function object, db function finally call the database
        db_functions = DB_Functions()
        data_shema = self.get_data_shema(data_object["attribute"])
        print(data_object)
        does_record_exist = db_functions.checkIfExists(data_shema.table_name, [data_shema.project, data_object["attribute"]], [data_object["project"], data_object["attributevalue"]], debug=True)
        #exit condition
        if does_record_exist:
            return 1
        #preprar date object for data save to db
        data_object[0]=["project",data_object["attribute"]]
        data_object[1] = [data_object["project"],data_object["attributevalue"]]

        # create finaly the record
        return_value = db_functions.record_create(data_shema.table_name, data_object[0], data_object[1], debug=True)
        return return_value



    def get_data_attribute_according_type(self, data_shema):
        x=0
        columns=[]
        for column in data_shema.column:
            columns[x] = column
        return columns

    def value_pairs_to_dicts(self,data_object,column_to_verify):
        #this function returns a list of two list objects colums an and values
        columns = []
        values = []
        print (data_object)
        for attribute in data_object:
            if self.verify_column(column_to_verify, attribute):
                columns.append((attribute))
                values.append(data_object[attribute])
        #create the data object for return
        data = [columns,values]
        return data

    def verify_column(self, column_to_verify, attribute):
        #return True if not excludes find
        return_value = False
        for item in column_to_verify:
            if item == str(attribute):
                return_value = True
                break
        return return_value

    def debug(self,debug,value):
        if debug:
            print (value);

# x = GetTestObject()
# x.create_test_object()

# import unittest
#
# getTestObject = GetTestObject(1)
#
# class MyTestCase(unittest.TestCase):
#     def getAttributes(self):
#         attributes = []
#         attributes =  getTestObject.get_attributes()
#         print (attributes)
#         getTestObject.print_out()
#

# if __name__ == '__main__':
#     unittest.main(verbosity=2)

