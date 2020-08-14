
class CallBackend {
    constructor(Object_id) {
        this.object_id = Object_id;
    }

    call_backend(backend_function,callback_functions){
        $.ajax({
            type:"get",
            url:"http://192.168.1.25:5000/api/",
            dataType:"json",
            data:{function:backend_function,objectid:this.object_id},
            success: function(response)
            {
                callback_functions(response);
            }
        })
    }
}


//testobject = new CallBackend(100);
//testobject.call_backend("gettestobject",show_backend_resaults_on_console);



