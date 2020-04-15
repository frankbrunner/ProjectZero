from ProjectZero.src.ps_db_functions_global import *
import unittest


class pz_Testobject(db_functions):
    def __init__(self, User, Passwd, Database):
        super().__init__(User, Passwd, Database)
        self.obj_Testobject = Testobject()
        self.tableName = self.obj_Testobject.tablename

    def createTestobject(self, Porject_id=0, Demand_id=0, Planning_Item_id=0, Application_id=0):
        #Return Code
        #0 Project successfull insert
        #1 Project allready exis
        #2 any Failure
        rows = self.obj_Testobject.rows
        values = [str(Porject_id), str(Demand_id),str(Planning_Item_id),str(Application_id)]
        select=self.obj_Testobject.project_id

        condition=self.obj_Testobject.project_id
        condition_value = Porject_id

        returnValue = self.checkIfExists(self.tableName,condition,condition_value)
        if returnValue==False:
            sql = self.sqlGenearatorInsert(self.tableName,rows,values)
            self.insertData(sql,values)
        else:
            return 1
        return returnValue

    def getTestobjectID(self, ProjectNumber):
        #Return the id of Testobject
        #Return 0 if not exists
        obj_join = Projects()

        sql = 'SELECT ' + self.obj_Testobject.tablename + '.id'\
              ' FROM ' + self.obj_Testobject.tablename + \
              ' INNER JOIN ' + obj_join.tablename +\
              ' ON ' + self.obj_Testobject.tablename + '.' + self.obj_Testobject.project_id + '=' + obj_join.tablename + '.id ' \
              'WHERE ' + obj_join.number +'="' + str(ProjectNumber) +'"';

        result=self.readData(sql)

        if len(result) == 0 :
            return 0
        else:
            result = result[0]
            result = result[0]
        return result



testobect = pz_Testobject("dbuser", "34df!5awe", "ProjectZero")
from ProjectZero.src.pz_db_functions_projects import *
project = pz_Projects("dbuser", "34df!5awe", "ProjectZero")

class MyTestCase(unittest.TestCase):

    def test_a_createTestobject(self):
        self.assertEqual(project.createProject(4856, "Test Project"), 0)
        projectID = project.getProjectId(4856)

        self.assertEqual(testobect.createTestobject(projectID), 0)
        self.assertEqual(testobect.createTestobject(projectID), 1)

    def test_b_getTestobjectID(self):
        self.assertGreater(testobect.getTestobjectID(4856),0)
        self.assertEqual(testobect.getTestobjectID(4000), 0)

    def test_z_deleteProject(self):
        self.assertEqual(project.deleteProject(4856), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)