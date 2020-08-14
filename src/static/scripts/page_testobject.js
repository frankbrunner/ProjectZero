//refesh menue jquery event handler 
refresh_dom();
//cookie handling 
//the cookie string needs to split in array 
project_id = document.cookie.split("=");
project_id = project_id[1];

//loading site
testobjekt = new TestObjectParameters();
testobjekt.function = "get";
testobjekt.project = project_id;  

backen_call = new CallBackend();
backen_call.call_backend(testobjekt,set_formvalues);

app_obj = new ApplicationsParameters();
app_obj.function = "listapplication";
backen_call.call_backend(app_obj,set_app_select);

//needed function for that site
function set_formvalues(result){
    //form values hat to be updateed
    console.log(result);
    $("#demand").val(result.demand);
    option = $('<option></option>').attr("value", result.project).text(result.project);
    $("#project").empty().append(option);
}
function modify_object(action)
{
    testobjekt.function = action;
    testobjekt.project = $( "select#project option:checked" ).val();
    testobjekt.demand = $( "#demand" ).val();
    backen_call.call_backend(testobjekt,defaultcallback);
}
function set_app_select(results){
    //handel call back with al list of applications
    var option;
    for (i = 0; i < results[1].length; i++) 
    { 
       option = option +"<option value="+results[1][i][0]+">"+results[1][i][0]+"</option>";
    }
    $("#applications").empty().append(option);
}
function add_attribute(attributetype,attributevalue)
{
    testobjekt.function = "addattribute";
    testobjekt.attribute = attributetype;
    testobjekt.attributevalue = attributevalue
    
    backen_call.call_backend(testobjekt,set_formvalues);
}

//button inteaction for that site
$("#update").on("click",function(){
    modify_object("update");
});
$("#delete").on("click",function(){
    modify_object("delete");
});
$("#add_app").on("click",function(){
    add_attribute("application",$("#applications").val())
});
$("#add_release").on("click",function(){
    add_attribute("release",$("#release").val())
});

