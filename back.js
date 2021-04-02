$(function(){
    $('#searchClick').click(function(){
        let usertext = $("#userbox").val();
        console.log(usertext);
        window.location.href = 'results.html' + '#' + usertext;
     })
});

$(function(){
    var usertext = window.location.hash.substring(1)

    function runPy(userInput) {
        console.log("HI3")
        $.ajax({
        data : userInput,
            url:'http://localhost:5000/success/'+userInput,
            success: function(data) {
                for(var x in data.BBlistings){
                    let copy = $(".template").clone()
    		    copy.removeClass("template")
    		    copy.removeClass("d-none")
    		    copy.find(".card-title").text(data.BBlistings[x].name)
                    copy.find(".card-img").attr("src",data.BBlistings[x].pic)
                    copy.find(".item-price").text(data.BBlistings[x].price)
                    copy.find(".card-website").text(data.BBlistings[x].store)
                    copy.find(".card-website").attr("href",data.BBlistings[x].redirectURL)
                
    		    $(".cardHolder").append(copy)
	        }                                                
                console.log(data)
            }
        });
    }
    
    runPy(usertext);

     $('#searchClick-results').click(function(){
         let usertext = $("#userboxResults").val();
         console.log(usertext);
         window.location.href = 'results.html' + '#' + usertext;
         location.reload();
         runPy(usertext);
     })
});
