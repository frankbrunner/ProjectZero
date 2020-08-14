//refesh menue jquery event handler 
refresh_dom();
//loading site
testobjekt = new TestObjectParameters()
backen_call = new CallBackend();

//needed function for that site
function modify_object(action)
{
    testobjekt.function = action;
    testobjekt.project = $( "#project" ).val();
    backen_call.call_backend(testobjekt,defaultcallback);
}

//button inteaction for that site
$("#create").on("click",function(){
    modify_object("create");
});