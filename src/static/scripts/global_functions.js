function g_clear_input_values(element)
{
    $(element).val('');
}
function g_add_event_click(idelement,target_element)
{
    var table = $(idelement).DataTable();
    var name;
    $(idelement +' tbody').on( 'click', 'tr', function () {
        name = $(this).attr("id");
    $(target_element).val(name);
    $(target_element).attr('name',name);


    });
}
function g_add_event_hover(idelement)
{
    var table = $(idelement).DataTable();

    $(idelement +' tbody').on( 'mouseover', 'tr', function () {
        $(this).addClass('selected');
    
    });
    $(idelement +' tbody').on( 'mouseout', 'tr', function () {
        $(this).removeClass('selected');
    
    });
}
function g_get_table_content(results)
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
function g_get_table_header(results) 
{   
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
