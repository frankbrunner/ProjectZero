import unittest
from ProjectZero.src.ps_db_functions_global import db_functions
from ProjectZero.src.pz_db_functions_applications import *

sql = db_functions("dbuser","34df!5awe","ProjectZero")


class MyTestCase(unittest.TestCase):
    unittest.TestLoader.sortTestMethodsUsing = None

    def test_a_inserProject01(self):
        self.assertEqual(sql.insertProject(4287, "Erstes Project"), 0)

    def test_b_inserProject02(self):
        self.assertEqual(sql.insertProject(4288, "Zweites Project"), 0)

    def test_c_inserProjectSameValue(self):
        self.assertEqual(sql.insertProject(4287, "Erstes Project"), 1)

    # def test_d_getProjects(self):
    #     resault = sql.getProjects()
    #     record = resault[0]
    #     id = record[0]
    #     number = record[1]
    #     description = record[2]
    #     #get Project with specivic id
    #     self.assertEqual(sql.getProjects(id), [(id,number,str(description))])

    def test_e_insertRelease(self):
        self.assertEqual(sql.insertRelease(2020,"MDR","MDR04"),0)
        self.assertEqual(sql.insertRelease(2020, "Major", "RE20A"), 0)
        self.assertEqual(sql.insertRelease(2020, "Maior", "RE20B"), 0)
        self.assertEqual(sql.insertRelease(2020, "Maior", "RE20C"), 0)
        self.assertEqual(sql.insertRelease(2020, "MDR", "MDR04"), 1)

    # def test_h_getReleases(self):
    #     self.assertEqual(sql.getReleases(),[(2020, 'MDR', 'MDR04'), (2020, 'MDR', 'MDR06')])

    def test_f_createTestObject(self):
        project_id = sql.getProjectId(4288)
        self.assertEqual(sql.createTestobject(project_id, 0, 0, 0), 0)
        project_id = sql.getProjectId(4287)
        self.assertEqual(sql.createTestobject(project_id, 0, 0, 0), 0)

    def test_g_getTestObject(self):
        self.assertEqual(sql.getTestobjectID(4288), 1)

    def test_h_createDemand(self):
        demand = 60
        testobject = sql.getTestobjectID(4288)
        release = sql.getReleaseID("RE20A")

        sql.createDemand(demand,testobject,release,1,0)

    def test_i_getDemand(self):
        print(sql.getDemand(454))

    def test_j_recordDelete01(self):
        self.assertEqual(sql.deleteProject(4287), 0)

    def test_k_recordDelete02(self):
         self.assertEqual(sql.deleteProject(4288), 0)

    def test_l_deleteReleaseRecord(self):
        self.assertEqual(sql.deleteRelease("Description", "MDR04"), 0)
        self.assertEqual(sql.deleteRelease("Description", "MDR06"), 0)

    def test_m_createApplication(self):

        Applications.createApplication("CRMPF")


if __name__ == '__main__':

    unittest.main(verbosity=2)

