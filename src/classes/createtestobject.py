from src.classes.db_functions import DB_Functions

class CreateTestObject():
    def __init__(self, test_object_id):
        # set the test object Id Variable
        self.test_object_id = test_object_id

    def create_test_object(self,type,):
        # generate the db function object, db function finaly call the database
        db_functions = DB_Functions()
        # returns dict object attributes to retur
        attributes = db_functions.get_data_from_table(self.test_object_id)
        return attributes

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
