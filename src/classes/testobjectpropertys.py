class TestObjectPropertys():
    def __init__(self,test_object_id):
        self.test_object_id = test_object_id
        self.type = 1
        self.demand = None
        self.supply = None



theObject = TestObjectPropertys(1)

for property, value in vars(theObject).items():
    print (property, ": ", value)