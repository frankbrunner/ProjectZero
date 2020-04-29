class db_struct():
    def __init__(self):
        self.Table.Demand = "Demand"
        pass

class Demand():
    def __init__(self):
        #Table Definition
        self.tablename = "Demand"
        #Row Definition
        self.demand = "demand"
        self.release_application_id = "release-application_id"
        self.supply_id = "supply_id"
        self.status = "status"

        # List of all Rows to create tables automatic
        self.rows = [self.demand,
                     self.release_application_id,
                     self.supply_id,
                     self.status]


        #List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("int(250)")
        self.types.append("int(250)")
        self.types.append("int(1)")

class Applications():
    def __init__(self):
        #Table definition
        self.tablename = "Applications"
        #Row Definition
        self.name = "name"
        # List of all Rows to create tables automatic
        self.rows = [self.name]
        # List with types to create tables automatic
        self.types = ["varchar(250)"]

class Releases():
    def __init__(self):
        #Table definition
        self.tablename = "Releases"
        #Row Definition
        self.year = "year"
        self.type = "type"
        self.name = "name"
        # List of all Rows to create tables automatic
        self.rows = [self.year,
                     self.type,
                     self.name]
        # List with types to create tables automatic
        self.types = ["int(4)"]
        self.types.append("varchar(250)")
        self.types.append("varchar(250)")

class Projects():
    def __init__(self):
        #Table definition
        self.tablename = "Projects"
        #Row Definition
        self.number = "number"
        self.description = "description"
        # List of all Rows to create tables automatic
        self.rows = [self.number,
                     self.description]
        # List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("varchar(250)")

class Testobject():
    def __init__(self):
        #Table definition
        self.tablename = "Testobject"
        #Row Definition
        self.project_id = "project_id"
        self.demand_id = "demand_id"
        self.planning_item_id = "planning_item_id"
        self.release_id = "release_id"
        # List of all Rows to create tables automatic
        self.rows = [self.project_id,
                     self.demand_id,
                     self.planning_item_id,
                     self.release_id]
        # List with types to create tables automatic
        self.types = ["int(250)"]
        self.types.append("int(250)")
        self.types.append("int(250)")
        self.types.append("int(250)")

class Testobject_Release():
    def __init__(self):
        #Table definition
        self.tablename = "Testobject_Release"
        #Row Definition
        self.testobject_id = "testobject_id"
        self.release_id = "release_id"
        # List of all Rows to create tables automatic
        self.rows = [self.testobject_id, self.release_id]
        # List with types to create tables automatic
        self.types = ["int(250)",
                      "int(250)"]

class Release_Application():
    def __init__(self):
        #Table definition
        self.tablename = "Release_Application"
        #Row Definition
        self.testobject_release_id = "testobject_release_id"
        self.application_id = "application_id"
        # List of all Rows to create tables automatic
        self.column = [self.testobject_release_id, self.application_id]
        # List with types to create tables automatic
        self.types = ["int(250)",
                      "int(250)"]

