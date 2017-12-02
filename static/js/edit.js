$(document).ready(function(){
    $(".flip").click(function(){
        $(this).next(".panel").slideToggle("slow");
    });
});
