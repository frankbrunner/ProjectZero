//import './global_functions.js';
//refesh menue jquery event handler 
refresh_dom();
//creating objects for that site
app_obj = new ApplicationsParameters()
backen_call = new CallBackend();

//loading site 
onload();
function onload()
{
    app_obj.action = "list";
    backen_call = new CallBackend();
    //get application and draw table
    backen_call.call_backend(app_obj, draw_table);
    //clear the input field from value
    g_clear_input_values('#app_update');
}
function draw_table(results)
{   
    table_id = "#apptable";
    html_table_header = g_get_table_header(results);
    html_table_content =g_get_table_content(results);
    //add on element
    $(table_id).on().empty().append(html_table_header);
    $(table_id).on().append(html_table_content);
    g_add_event_hover(table_id);
    g_add_event_click(table_id,"#app_update");
    //after added elements to dom use the refresch function
    refresh_dom();
}
//needed function for that site
function modify_object(action)
{
    app_obj.action = action;
    backen_call.call_backend(app_obj,defaultcallback);
    onload();
    
}
//button inteaction for that site
$("#create").on("click",function(){
    //set the needed Value on the class
    app_obj.name = $( '#app_update' ).val();
    modify_object("create");
});
$("#update").on("click",function(){
    //set the needed Value on the class
    app_obj.name = $('#app_update' ).attr('name');
    app_obj.updatevalue =  $( '#app_update' ).val();
    modify_object("update");
});
$("#delete").on("click",function(){
    //set the needed Value on the class
    app_obj.name = $('#app_update' ).attr('name');
    modify_object("delete");
});


