from ProjectZero.src.functions_projects import *
from ProjectZero.src.functions_releases import *

dbuser = "dbuser"
password = "34df!5awe"
db = "ProjectZero"

projects = pz_Projects(dbuser,password,db)
releases = pz_Releases(dbuser,password,db)

class dataLoad():
    def loadPorjects(self):
        projectNumber= [4026,4033,4079]
        projectDesciption = ["PF Chip 21","Leon","IPATON"]
        x=0
        for item in projectNumber:
            projects.createProject(item,projectDesciption[x])
            x +=1


    def loadReleases(self):
        dateFrom = ["2020-01-30","2020-02-25"]
        dateTo = ["2020-01-30","2020-02-25"]
        releaseName = ["RE20A","RE20B"]
        x=0
        for item in dateFrom:
            releases.createRelease(item,dateTo[x],releaseName[x])
            x +=1



dataLoad = dataLoad()
if __name__ == '__main__':
    dataLoad.loadPorjects()
    dataLoad.loadReleases()