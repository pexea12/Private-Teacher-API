$(document).ready(function () {
    $("#user_id_s").hide();
    $("#user_id_t").hide();
    $.get("/api/getid",function(data){
        var idt = data.id
        $(".user_id").val(idt);
    });

    var show = true;
    $("#add_teacher_form").ajaxForm(function (data) {
        alert(data.msg);
    });
    $("#add_student_form").ajaxForm(function (data) {
        alert(data.msg);
    });

});