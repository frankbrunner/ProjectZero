from src.classes.db_functions import DB_Functions
from src.classes.db_shema import *
from src.classes.bl_functions import *


class Applications():
    def __init__(self):
        self.db_shema = Application()
        # generate the db function object, db function finally call the database
        self.db_functions = DB_Functions()
        self.bl_functions = BLFunctions()

    def create(self, data_object, debug=False):
        # check in DB if record for PI allready exist the check is using the name colum to verify
        does_record_exist = self.db_functions.checkIfExists(self.db_shema.table_name, self.db_shema.name, data_object["name"], True)
        # if record exist return according value 2 vor allready exist
        if does_record_exist:
            return 2
        # prepare data to write in database it needs in two seperate dict and verify with db_struct
        data_object = self.bl_functions.value_pairs_to_dicts(data_object, self.db_shema.column)
        # create finaly the record
        return_value = self.db_functions.record_create(self.db_shema.table_name, data_object[0], data_object[1], debug=True)
        # cleanup object instances
        # debug mode
        self.bl_functions.debug(debug, return_value)
        # return value true or false
        return return_value

    def update(self, data_object, debug=False):
        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist = self.db_functions.checkIfExists(self.db_shema.table_name, self.db_shema.name, data_object["name"])
        # if record exist return True
        if not does_record_exist:
            return 2
        #needs to set the old name that came over the name variable
        name_old =  data_object["name"]
        #now the old name has to ovverreide with the new name
        data_object["name"] = data_object["updatevalue"]
        # prepare data to write in database it needs in two seperate dict and verify with db_struct
        data_object_value_pairs = self.bl_functions.value_pairs_to_dicts(data_object, self.db_shema.column)
        # create finaly the record
        return_value= self.db_functions.record_update(self.db_shema.table_name, data_object_value_pairs[0], data_object_value_pairs[1], self.db_shema.name, name_old)
        # debug mode
        self.bl_functions.debug(debug,return_value)
        # return value true or false
        return return_value

    def delete(self,data_object,debug=False):
        # check in DB if record for PI allready exist the check is using the project colum to verify
        does_record_exist = self.db_functions.checkIfExists(self.db_shema.table_name, self.db_shema.name, data_object["name"], True)
        # if record exist return according value 2 vor allready exist
        if not does_record_exist:
            return 2
        return_value = self.db_functions.delete_record(self.db_shema.table_name, self.db_shema.name, data_object["name"])
        return return_value

    def list(self,debug=False):
        #Returns an List that inclues a list for all availabel attributes include a list wiht all values
        # generate the db function object, db function finally call the database
        return_value = self.db_functions.list_records(self.db_shema)
        self.bl_functions.debug(debug,return_value)
        return (return_value)

