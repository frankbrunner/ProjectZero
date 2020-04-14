
from Ressourcenplanning.src.rp_db_struct import *
from Ressourcenplanning.src.rp_db_functions import *

class rp_Applications(db_functions):
    def __index__(self):
        pass

    def createApplication(self, ApplicationName):
        #Return Codes
        #0 Project successfull insert
        #1 Project allready exist
        #2 any Failure
        obj_Applications = Applications()
        table = obj_Applications.tablename
        rows = [obj_Applications.name]
        values = [str(ApplicationName)]
        select = obj_Applications.name
        return (self.checkAndInsert(table,rows,values,select))