// Section of global used variable constants and functions
var projecNumber;
var releases;
var release;
var applications;
var applicationList=[];
var appendHtml;
var randomID = 1000;
var visibilityStatus = "hide";
var switcher = 0;

//section of generel Fuctions an selectors
$("#divMain").on("mouseover","tr",function()
{
    $(this).addClass("hover");
})
$("#divMain").on("mouseout","tr",function()
{
    $(this).removeClass("hover");
})

class Testobject{
    constructor(Projectnumber){
        this.ProjectNummber = projectnumber;


    }
    getProjectnumber(projectnumber){
        return projectnumber
    }
    getReleases(projectnumber)
    {

    }

}
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
            releases = [];
            
                for (i=0;i <response.length; i++)
                {   randomID = randomID +1;
                    //class release tabel is used to remove the block always bevor create
                    addhtml += '<table value="'+response[i][0]+'" class="u-full-width releasetable">';
                    addhtml += '<thead>';
                    addhtml += '<tr>';
                    addhtml += "<th><b>"+response[i][0]+"</b></th>";
                    addhtml += "</tr>";
                    addhtml += '</thead>';

                    addhtml += '<tbody>';
                    addhtml += '<tr  id="'+randomID+'"  >';
                    addhtml += '<td  style="padding-left:15%" >+ application</td>';
                    addhtml += '</tr>';
                    addhtml += '</tbody>'; 
                    addhtml += '</table>';            
                }
            $("#releaseHead").on().empty().append("<th>Project: "+projecNumber+"</th>");
            $('.releasetable').on().remove();
            $("#tableRelease").on().after(addhtml);
            $("#plusRelease").on().attr("style","block");   
            hideElement("divSelectReleases")   
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
function setValue(){

}
function getApplicationslist(selector)
{

    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "getapplicationlist"},
        success: function(response)
        {
        
                for (i=0;i <response.length; i++)
                {
                    applicationList[i]=response[i];
                } 
            addhtml = '<div id="divAddApplication">';    
            addhtml += addSelections(applicationList); 
            addhtml += addsubmitButton("addapp","add");
            
            addhtml += "</div>";  

            $("#divAddApplication").on().remove();
            $("#"+selector+"").on().closest("table").after(addhtml);
            $("#divAddApplication").on();

        }
    })
}
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
                    addhtml += '<tr id="addRelease">+ application</tr>'


                    console.log("return"+addhtml)

                }
             
            $("#releases").empty().append(addhtml);
            getRelease(projecNumber);
            
        }       
    })
}
function addApplication(Release,Project,Application)
{
    console.log(Release,ProjectNummber,Application);
    $.ajax({
        type:"get",
        url:"http://192.168.1.25:5000/api/",
        dataType:"json",
        data:{function: "addapplication",release:Release, 
                                         project: Project,
                                         application:Application},
        success: function(response)
        {         
            $("#releases").empty().append(addhtml);
            getRelease(projecNumber);
            
        }       
    })
}
function hideElement(element2Hide)
{
    $('#'+element2Hide).hide();
}
function showElement(element2Show)
{
    $('#'+element2Show).show();
}
function getApplications(Project,Releases)
{
    applications=[]
    for (x=0;x <Releases.length; x++){
        $.ajax({
            type:"get",
            url:"http://192.168.1.25:5000/api/",
            dataType:"json",
            data:{function: "getapplications",project:Project,releas:Releases[x]},
            success: function(response)
            {
                for (i=0;i <response.length; i++){
                    applications.push(response[i]);
                }
                console.log("Applications."+applications);
            }
        })
    }
}
function addApplications(Project,Releas,Application,FunctionSuccess)
{
    applications=[]
    for (x=0;x <Releases.length; x++){
        $.ajax({
            type:"get",
            url:"http://192.168.1.25:5000/api/",
            dataType:"json",
            data:{function: "addapplications",project:Project,releas:Releas,application:Application},
            success: function(response)
            {
 
                FunctionSuccess;

            }
        })
    }
}
function addSelections(options){
    addhtml = '<select class="u-full-width">';
   
    for(i=0;i < options.length;i++){
        
        addhtml += '<option ';
        addhtml += 'value="'+options[i]+'">';
        addhtml += options[i][0];
        addhtml += '</option>'
    }
    addhtml += '</select>';

    return addhtml;
}
function addsubmitButton(id,value){

    addhtml = '<input class="button-primary" ';
    addhtml += 'id="'+id+'" type="button" value="'+value+'"></input>';
    return addhtml
}
$("#saveTestObject").mouseup(function()
{
    saveTestobject()
})
$("#table tbody").on("click","tr",function()
{
    if ( $(this).hasClass('onclick') ) {
        $(this).removeClass('onclick');
    } else {
        $('#table tr.onclick').removeClass('onclick');
        $(this).addClass('onclick');
    }
    console.log("click table tbody");
    projecNumber = $(this).text();

    getRelease($(this).text());

})
$("#tableRelease tbody").on("click","tr",function()
{
  
    if ( $(this).hasClass('onclick') ) {
        $(this).removeClass('onclick');
    } else {
        $('#tableRelease tr.onclick').removeClass('onclick');
        $(this).addClass('onclick');
    }

    //console.log(add_htmlSelections(getApplicationslist()));
    // getApplicationslist();
    getApplicationslist($(this).attr("id"));

 
})
$("#saveRelease").mouseup(function()
{
    addRelease($("#selectReleases :selected").text(),projecNumber);
    hideElement("divSelectReleases")
})
$("#plusRelease tbody").on("click",function()
{

    if (visibilityStatus == "hide"){
        showElement("divSelectReleases")
        getReleases();
        visibilityStatus = "shown";
    }else{
        hideElement("divSelectReleases")
        visibilityStatus = "hide";
    }
})
$("#divMain").on("click","tr",function()
{
    var ID=($(this).attr("id"));

    if (ID > 1000){
        if(switcher == 0){
            getApplicationslist(ID);
            release = $(this).closest("table").attr("value");
            switcher = 1;
        }else{
            $("#divAddApplication").remove();
            switcher = 0;
        }
    }
})
$("#addapp").mouseup(function()
{
   //var application = $(this).text();
   console.log("test");
   //addApplications(projecNumber,release,application)
})

//Release Div Section


getTestobjects();
getProjects()
hideElement("divSelectReleases")



