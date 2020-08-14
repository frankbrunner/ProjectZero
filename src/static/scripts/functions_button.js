
class  ViewPage{
    constructor(page_name){
        this.function = "displaypage";
        this.name = page_name;
    }
}

function view_list_page(page_name)
{
    //create a new ViewPage object
    view_page = new ViewPage(page_name);
    //create a new CallBacken object
    backen_call = new CallBackend();
    //passing the object to the call backend function because no callback
    //function ist needet the nocallback is used 
    backen_call.call_backend(view_page,draw_table,no_callback);
}
//every function that needs to work after DOM has been changed needs to be in here
function refresh_dom(){

    $("#button_modify_testobject").on('click',function()
    {
        $( location ).attr("href", "http://192.168.1.24:5000/testobject");
    })

    $("#button_list").on('click',function()
    {
        $( location ).attr("href", "http://192.168.1.24:5000");
    })
    $("#button_create").on('click',function()
    {
        $( location ).attr("href", "http://192.168.1.24:5000/createtestobject");
    })
    $("#button_application").on('click',function()
    {
        $( location ).attr("href", "http://192.168.1.24:5000/application");
    })
    $("#button_release").on('click',function()
    {
        $( location ).attr("href", "http://192.168.1.24:5000/release");
    })
    $("#button_user").on('click',function()
    {
        $( location ).attr("href", "http://192.168.1.24:5000/user");
    })

}

