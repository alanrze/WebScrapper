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
    //console.log("HI")
    function runPy() {
    console.log("HI2")
    $.ajax({
    //type: "POST",
    data : usertext,
        url:'http://localhost:5000/success/'+usertext,
        success: function(data) {                                                
            console.log(data)
        }
    });
}
runPy()
});
