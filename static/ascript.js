$(document).ready(function () {
    var id;

    $.get("/api/get_id",function(data){
        id = data.id
        console.log(id);

    var url="/api/teachers/list?user_id="+id;
    console.log(url);
    $.get(url,function(data){
        for (i = 0; i < data.length; i++){
            $("#teacher_div").append('<p id="p'+i+'">'+JSON.stringify(data[i])+'</p>');
            $("#teacher_div").append('<button id="butt'+i+'" onclick="delete_teacher(' + data[i].id + ')" >Del</button>');
        }
    });

    });



});