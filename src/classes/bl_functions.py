from src.classes.db_shema import *
class BLFunctions():
    def __init__(self):
        # set the test object Id Variable
        pass

    def value_pairs_to_dicts(self,data_object,column_to_verify):
        #this function returns a list of two list objects colums an and values
        columns = []
        values = []
        for attribute in data_object:
            if self.verify_column(column_to_verify, attribute):
                columns.append((attribute))
                values.append(data_object[attribute])
        #create the data object for return
        data = [columns,values]
        return data

    def verify_column(self, column_to_verify1, attribute):
        # return True if not excludes find
        return_value = False
        for item in column_to_verify1:
            if item == str(attribute):
                return_value = True
                break
        return return_value

    def debug(self,debug,value):
        if debug:
            print (value);

    def get_data_shema(self, attribute):
        # if Attribute is known in a valid Table a datashema object (table) will be returned
        # if Attribute is not known in the Tablen Return 0
        # if Attribute multiple avaivable Return 1
        data_tables = [Project_Applications(), Project_Releases()]
        return_value = None
        multiple_entry_check = 0
        for table in data_tables:
            for column in table.column:
                if column == attribute:
                    return_value = table
                    multiple_entry_check += 1
        if multiple_entry_check > 1:
            return_value = 2
        return return_value
