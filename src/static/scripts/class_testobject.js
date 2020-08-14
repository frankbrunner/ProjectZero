class TestObjectParameters{
    constructor() {
        this.objectid = 1;
        this.project = 4572;
        this.demand = 200;
        this.supply = 150;
        this.function = "list";
        this.applications;
        this.addattributetype;
        this.addattributevalue;
        //attribute to sort
        this.listsortby = ""
        //order up ord down
        this.listsortorder = ""
    }
}

class ApplicationsParameters{
    constructor() {
        this.name = "test";
        this.function = "stammdaten";
        this.type = "type_application";
        this.action= "";
        this.updatevalue="";
        //attribute to sort
        this.listsortby = ""
        //order up ord down
        this.listsortorder = ""
    }
}

class ReleaseParameters{
    constructor() {
        this.name = "test";
        this.function = "stammdaten";
        //the underscore ist used because release is a reserve attribute in sql
        this.type = "type_release";
        this.action= "";
        this.updatevalue="";
        //attribute to sort
        this.listsortby = ""
        //order up ord down
        this.listsortorder = ""
    }
}








