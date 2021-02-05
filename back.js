$(function(){

    $('#searchClick').click(function(){
        let usertext = $("#userbox").val();
        console.log(usertext);
        window.location.href = 'results.html' + '#' + usertext;
     })
});

$(function(){
    var usertext = window.location.hash.substring(1)
    $(".card-title").text(usertext);
});