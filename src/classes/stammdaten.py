from src.classes.db_functions import DB_Functions
from src.classes.db_shema import *
from src.classes.bl_functions import *


class Stammdaten():
    def __init__(self,data_obj):
        self.data_obj = data_obj
        self.const_db_shemas = [Releases(),Application()]
        #self.db_shema = Releases()
        # generate the db function object, db function finally call the database
        self.db_functions = DB_Functions()
        self.bl_functions = BLFunctions()

    def modify(self, debug = False):
        #set the modification flag
        return_value=0
        action = self.data_obj["action"]
        db_shema = self.get_data_shema(self.data_obj["type"],self.const_db_shemas)
        if action == "create":
            self.create(self.data_obj,db_shema,True)
        if action == "update":
            self.update(self.data_obj,db_shema,True)
        if action == "delete":
            self.delete(self.data_obj,db_shema,True)
        if action == "list":
           return_value = self.list(db_shema,True)
        return return_value

    def create(self, data_object,db_shema, debug=False):
        # check in DB if record for PI allready exist the check is using the name colum to verify
        does_record_exist = self.db_functions.checkIfExists(db_shema.table_name, db_shema.name, data_object["name"], True)
        # if record exist return according value 2 vor allready exist
        if does_record_exist:
            return 2
        # prepare data to write in database it needs in two seperate dict and verify with db_struct
        data_object = self.bl_functions.value_pairs_to_dicts(data_object, db_shema.column)
        # create finaly the record
        return_value = self.db_functions.record_create(db_shema.table_name, data_object[0], data_object[1], debug=True)
        # cleanup object instances
        # debug mode
        self.bl_functions.debug(debug, return_value)
        # return value true or false
        return return_value

    def update(self, data_object,db_shema, debug=True):
        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist = self.db_functions.checkIfExists(db_shema.table_name, db_shema.name, data_object["name"])
        # if record exist return True
        if not does_record_exist:
            return 2
        #needs to set the old name that came over the name variable
        name_old =  data_object["name"]
        #now the old name has to ovverreide with the new name
        data_object["name"] = data_object["updatevalue"]
        # prepare data to write in database it needs in two seperate dict and verify with db_struct
        data_object_value_pairs = self.bl_functions.value_pairs_to_dicts(data_object, db_shema.column)
        # create finaly the record
        return_value= self.db_functions.record_update(db_shema.table_name, data_object_value_pairs[0], data_object_value_pairs[1], db_shema.name, name_old)
        # debug mode
        self.bl_functions.debug(debug,return_value)
        # return value true or false
        return return_value

    def delete(self,data_object,db_shema,debug=False):

        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist = self.db_functions.checkIfExists(db_shema.table_name, db_shema.name, data_object["name"], True)

        # if record exist return according value 2 vor allready exist
        if not does_record_exist:
            return 2

        return_value = self.db_functions.delete_record(db_shema.table_name, db_shema.name, data_object["name"])
        return return_value

    def list(self,db_shema,debug=False):
        #Returns an List that inclues a list for all availabel attributes include a list wiht all values
        # generate the db function object, db function finally call the database
        return_value = self.db_functions.list_records(db_shema)
        print (return_value)
        self.bl_functions.debug(debug,return_value)
        return (return_value)

    def get_data_shema(self, type, data_shemas):
        # if type is known in a valid Table a datashema object (table) will be returned
        # if type is not known in the Tablen Return 0
        # if type multiple avaivable Return 1
        return_value = None
        multiple_entry_check = 0
        for table in data_shemas:
            for column in table.column:
                if column == type:
                    return_value = table
                    multiple_entry_check += 1
        if multiple_entry_check > 1:
            return_value = 2
        return return_value