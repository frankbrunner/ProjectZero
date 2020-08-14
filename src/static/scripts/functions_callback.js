
function defaultcallback(result)
{
    console.log(result);
}
function no_callback(){

}
function draw_table(results)
{
    var add_on_element ="#maintable";
    html_table_header = get_table_header(results);
    html_table_content = get_table_content(results);
    //add on element
    $(add_on_element).on().empty().append(html_table_header);
    $(add_on_element).on().append(html_table_content);
    add_event_click("#maintable");
    add_event_hover("#maintable");
    //after added elements to dom use the refresch function
    refresh_dom();

    //add the select function to table 
}
function get_table_header(results){
    //local variablen declaraion
    var table_header="";

    //begin of the header
    table_header += "<thead><tr>";
    //get all values for column
    for (i = 0; i < results[0].length; i++) 
    { 
        //get the value from the array name 
        table_header += "<th>"+results[0][i]+"</th>"; //header 
    }
    //end of the header section
    table_header += "</tr></thead> "; 

    return table_header;
}
function get_table_content(results)
{   
    var table_content;
    //begin of the content
    table_content = "<tbody>"
    for (i = 0; i < results[1].length; i++) 
    { 
        //at that position we set also the id to the project value as uniq identifier
        table_content += "<tr id="+results[1][i][0]+">";

        for (x = 0; x< results[1][i].length;x++)
        {
            table_content += "<td>"+results[1][i][x]+"</td>";
        }
  
        table_content += "</tr>"; 
    }
    table_content += "</tbody>"
    //end of the content
    return table_content;
}
function add_event_click(idelement)
{
    var table = $(idelement).DataTable();
    $(idelement +' tbody').on( 'click', 'tr', function () {
        open_objectdetail_page($(this).attr('id'));
  
        // if ( $(this).hasClass('selected') ) {
        //     $(this).removeClass('selected');
        // }
        // else {
        //     table.$('tr.selected').removeClass('selected');
        //     $(this).addClass('selected');
        // }
    });
}
function add_event_hover(idelement)
{
    var table = $(idelement).DataTable();
    $(idelement +' tr').hover(function () 
    {
        $(this).addClass('hover');
    },
    function(){
        $(this).removeClass('hover');
    });
}
function open_objectdetail_page(id)
{
    set_cookies("project_id",id)
    $( location ).attr("href", "http://192.168.1.24:5000/testobject");
}
function set_cookies(name, value)
{
    document.cookie = name+"="+value;
 
}