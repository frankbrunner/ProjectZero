class db_struct():
    def __init__(self):
        self.Table.Demand = "Demand"
        pass

class Demand():
    def __init__(self):
        #Table Definition
        self.name = "Demand"
        #Row Definition
        self.demand = "demand"
        self.release_application_id = "release-application_id"
        self.supply_id = "supply_id"
        self.status = "status"

        # List of all Rows to create tables automatic
        self.column = [self.demand,
                     self.release_application_id,
                     self.supply_id,
                     self.status]


        #List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("int(250)")
        self.types.append("int(250)")
        self.types.append("int(1)")

class Application():
    def __init__(self):
        #Table definition
        self.table_name = "Applications"
        #Row Definition
        self.name = "name"
        self.type = "type_application"
        # List of all Rows to create tables automatic
        self.column = [self.name,self.type]
        # List with types to create tables automatic
        self.types = ["varchar(250)"]
        self.types.append("varchar(250)")

class Releases():
    def __init__(self):
        #Table definition
        self.table_name = "Releases"
        #Row Definition
        #A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'
        self.name = "name"
        self.datefrom = "date_from"
        self.dateto = "date_to"
        self.type = "type_release"
        # List of all Rows to create tables automatic
        self.column = [self.name,
                       self.datefrom,
                       self.dateto,
                       self.type]

        # List with types to create tables automatic
        self.types=["varchar(250)"]
        self.types.append("date")
        self.types.append("date")
        self.types.append("varchar(250)")

class Projects():
    def __init__(self):
        #Table definition
        self.name = "Projects"
        #Row Definition
        self.number = "number"
        self.description = "description"
        # List of all Rows to create tables automatic
        self.column = [self.number,
                     self.description]
        # List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("varchar(250)")

class User():
    def __init__(self):
        #Table definition
        self.table_name = "User"
        #Row Definition
        self.firstname = "firstname"
        self.secondname = "secondname"
        self.pensum = "pensum"
        self.team = "team"
        self.type = "type_user"
        # List of all Rows to create tables automatic
        self.column = [self.firstname,
                       self.secondname,
                       self.pensum,
                       self.team,
                       self.type]
        # List with types to create tables automatic
        self.types = ["varchar(250)"]
        self.types.append("varchar(250)")
        self.types.append("int(250)")
        self.types.append("int(250)")
        self.types.append("int(250)")

class Team():
    def __init__(self):
        #Table definition
        self.table_name = "Team"
        #Row Definition
        self.name= "name"
        self.type = "type_user"
        # List of all Rows to create tables automatic
        self.column = [self.name,
                       self.type]
        # List with types to create tables automatic
        self.types = ["varchar(250)"]
        self.types.append("varchar(250)")


class TestObject():
    def __init__(self):
        #Table definition
        self.name = "Testobject"
        #Row Definition
        self.project = "project"
        self.demand = "demand"
        self.supply = "supply"
        self.release = "release_name"
        # List of all Rows to create tables automatic
        self.column = [self.project,
                     self.demand,
                     self.supply,
                     self.release]
        # List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("int(250)")
        self.types.append("int(250)")
        self.types.append("varchar(250)")

class Project_Applications():
    def __init__(self):
        #Table definition
        self.name = "Project_Applications"
        #Row Definition
        self.project = "project"
        self.application = "application"
        self.release = "release_name"
        # List of all Rows to create tables automatic
        self.column = [self.project,
                     self.application,
                     self.release]
        # List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("varchar(250)")
        self.types.append("varchar(250)")

class Project_Releases():
    def __init__(self):
        #Table definition
        self.name = "Project_Releases"
        #Row Definition
        self.release  = "release_name"
        self.project = "project"
        # List of all Rows to create tables automatic
        self.column = [self.release,self.project]
        # List with types to create tables automatic
        self.types = ["varchar(250)"]
        self.types.append("int(250)")

class Release_Application():
    def __init__(self):
        #Table definition
        self.name = "Release_Application"
        #Row Definition
        self.testobject_release_id = "testobject_release_id"
        self.application_id = "application_id"
        # List of all Rows to create tables automatic
        self.column = [self.testobject_release_id, self.application_id]
        # List with types to create tables automatic
        self.types = ["int(250)",
                      "int(250)"]

