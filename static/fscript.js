$(document).ready(function () {

    $("#add_user_div").hide();
    var show = true;
    $("#formoid").ajaxForm(function (data) {
        alert(data.msg);
    });
    $("#logout_button").click(function () {
        $.get("api/logout",function(data){alert(data.msg); $("#show_user_div").empty();});
    });


    $("#add_user_butt").click(reg);
    function reg(){
        $("#add_user_div").toggle();
        $("#show_teacher_div").hide();
        $("#show_user_div").hide();
        $("#show_student_div").hide();
    }

    $("#add_user_form").ajaxForm(function (data) {
        alert(data.msg);
    });

    $("#show_user_div").hide();
    $("#show_user_butt").click(su);
    function su() {
        $("#show_teacher_div").hide();
        $("#add_user_div").hide();
        $("#show_student_div").hide();
        $.get("api/users", function(data){
            for(i = 0; i < data.length;i++){
                $("#show_user_div").append("<p>"+JSON.stringify(data[i])+"</p>");
            }
         });
        $("#show_user_div").toggle();
    }

    $("#show_teacher_div").hide();
    $("#show_teacher_butt").click(st);
    function st() {
        $("#add_user_div").hide();
        $("#show_user_div").hide();
        $("#show_student_div").hide();
        $.get("api/teachers/list", function(data){
            for(i = 0; i < data.length;i++){
                $("#show_teacher_div").append("<p>"+JSON.stringify(data[i])+"</p>");
            }
         });
        $("#show_teacher_div").toggle();
    }


    $("#show_student_div").hide();
    $("#show_student_butt").click(ss);
    function ss() {
        $("#show_teacher_div").hide();
        $("#show_user_div").hide();
        $("#add_user_div").hide();

        $.get("api/students/list", function(data){
            for(i = 0; i < data.length;i++){
                $("#show_student_div").append("<p>"+JSON.stringify(data[i])+"</p>");
            }
         });
        $("#show_student_div").toggle();
    }


});