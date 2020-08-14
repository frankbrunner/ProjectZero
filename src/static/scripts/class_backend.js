
class CallBackend {

    call_backend(dataobject,callback_functions){

        $.ajax({
            type:"get",
            url:"http://192.168.1.24:5000/api/",
            dataType:"json",
            data:dataobject,
            success: function(response)
            {
                callback_functions(response);
            }
        })
    }
}




