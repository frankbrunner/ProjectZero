var projecNumber=225;



function getTestobjects()
{
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "gettestobjects"},
        success: function(response)
        {
            var addhtml="";
            var i;

                for (i=0;i <response.length; i++)
                {
                    addhtml += "<tr>";
                    addhtml += "<td>"+response[i][0]+"</td>";
                    addhtml += "</tr>";
                }
            $("#testobjectbody").empty().append(addhtml);
        }       
    })
}
function getProjects()
{
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "getprojects"},
        success: function(response)
        {
            var addhtml="";
            var i;

                for (i=0;i <response.length; i++)
                {
                    addhtml += '<option ';
                    addhtml += 'id="projects" value="'+response[i][0]+'">';
                    addhtml += response[i][0];
                    addhtml += '</option>'
                    console.log(addhtml)

                }
             
            $("#projects").empty().append(addhtml);
        }       
    })
}
function saveTestobject()
{
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "savetestobject",projectnumber: $("#projects :selected").text(),
                shortdescription:$("#shortDescription").val()},
        success: function(response)
        {
            getTestobjects();
        }       
    })
}
$("#saveTestObject").mouseup(function()
{
    saveTestobject()
})
$("#table tbody").on("mouseover","tr",function()
{
    $(this).addClass("hover");
})
$("#table tbody").on("mouseout","tr",function()
{
    $(this).removeClass("hover");
})
$("#table tbody").on("click","tr",function()
{
    if ( $(this).hasClass('onclick') ) {
        $(this).removeClass('onclick');
    } else {
        console.log("else");
        $('#table tr.onclick').removeClass('onclick');
        $(this).addClass('onclick');
    }
    projecNumber = $(this).text();
    getRelease($(this).text());
});

function getRelease(ProjectNummber)
{
    var test = ProjectNummber;
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "getrelease",projectnumber:ProjectNummber},
        success: function(response)
        {
            var addhtml="";
            var i;

                for (i=0;i <response.length; i++)
                {
                    
                    addhtml += "<tr>";
                    addhtml += "<td>"+response[i][0]+"</td>";
                    addhtml += "</tr>";
                    console.log("return"+addhtml)                
                }
            $("#releaseHead").empty().append("<th>Project: "+projecNumber+"</th>");
            $("#releases").empty().append(addhtml);
            $("#plusRelease").attr("type","button");       
        }       
    })
}
function getReleases()
{
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "getreleases"},
        success: function(response)
        {
            var addhtml="";
            var i;

                for (i=0;i <response.length; i++)
                {
                    addhtml += '<option ';
                    addhtml += 'value="'+response[i][0]+'">';
                    addhtml += response[i][0];
                    addhtml += '</option>'
                    console.log("testobject:"+addhtml)

                }
             
            $("#selectReleases").empty().append(addhtml);
        }       
    })
}
$("#plusRelease").on("click",function()
{
    getReleases();
    
})

function addRelease(ReleaseName,ProjectNummber)
{
    console.log(ReleaseName);
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "addrelease",releasename:ReleaseName, projectnumber: ProjectNummber},
        success: function(response)
        {

            var addhtml="";
            var i;

                for (i=0;i <response.length; i++)
                {
                    addhtml += "<tr>";
                    addhtml += "<td>"+response[i][0]+"</td>";
                    addhtml += "</tr>";
                    console.log("return"+addhtml)

                }
             
            $("#releases").empty().append(addhtml);
            
        }       
    })
}
$("#saveRelease").mouseup(function()
{
    addRelease($("#selectReleases :selected").text(),projecNumber);
    getRelease(projecNumber);
})

getTestobjects();
getProjects()

