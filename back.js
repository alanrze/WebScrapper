$(function(){
    $('#searchClick').click(function(){
        let usertext = $("#userbox").val();
        console.log(usertext);
        window.location.href = 'results.html' + '#' + usertext;
     })
});

//BestBuy
$(function(){
    var usertext = window.location.hash.substring(1)

    function runPy(userInput) {
        $.ajax({
        data : userInput,
            url:'http://localhost:5000/success/'+userInput,
            success: function(data) {
                for(var x in data.Results[0].BBlistings){
                    let copy = $(".template").clone()
    		    copy.removeClass("template")
    		    copy.removeClass("d-none")
    		    copy.find(".card-title").text(data.Results[0].BBlistings[x].name)
                    copy.find(".card-img").attr("src",data.Results[0].BBlistings[x].pic)
                    copy.find(".item-price").text(data.Results[0].BBlistings[x].price)
                    copy.find(".card-website").text(data.Results[0].BBlistings[x].store)
                    copy.find(".card-website").attr("href",data.Results[0].BBlistings[x].redirectURL)
                
    		    $(".cardHolder").append(copy)
                    console.log("New card made...")
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

//Walmart
$(function(){
    var usertext = window.location.hash.substring(1)

    function runPy(userInput) {
        $.ajax({
        data : userInput,
            url:'http://localhost:5000/success/'+userInput,
            success: function(data) {
                for(var x in data.Results[1].WMlistings){
                    let copy = $(".template").clone()
    		    copy.removeClass("template")
    		    copy.removeClass("d-none")
    		    copy.find(".card-title").text(data.Results[1].WMlistings[x].name)
                    copy.find(".card-img").attr("src",data.Results[1].WMlistings[x].pic)
                    copy.find(".item-price").text(data.Results[1].WMlistings[x].price)
                    copy.find(".card-website").text(data.Results[1].WMlistings[x].store)
                    copy.find(".card-website").attr("href",data.Results[1].WMlistings[x].redirectURL)
                
    		    $(".cardHolder").append(copy)
                    console.log("New card made...")
	        }                                                
                console.log(data)
            }
        });
    }
    
    runPy(usertext);
});
