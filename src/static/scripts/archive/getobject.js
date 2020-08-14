
class TestObject {
    constructor(Object_id) {
        this.object_id = Object_id;
    }

    get_test_object(callback_functions){
        $.ajax({
            type:"get",
            url:"http://192.168.1.25:5000/api/",
            dataType:"json",
            data:{function: "gettestobject",objectid:this.object_id},
            success: function(response)
            {
                callback_functions(response);
            }
        })
    }
}

function show_results(results)
{
    console.log(results.type);
}

testobject = new TestObject(100);
testobject.get_test_object(show_results);



