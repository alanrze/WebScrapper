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
        $.ajax({
        data : userInput,
            url:'http://72.176.215.95:5000/success/'+userInput,
            success: function(data) {
                for(var x in data.Results){
                    let copy = $(".template").clone()
    		    copy.removeClass("template")
    		    copy.removeClass("d-none")
    		    copy.find(".card-title").text(data.Results[x].name)
                    copy.find(".item-price").text(("$" + data.Results[x].price))
                    copy.find(".card-website").text(data.Results[x].store)
                    copy.find(".card-website").attr("href",data.Results[x].redirectURL)

                    //If combo item, it shows multiple pics
                    if(data.Results[x].combo > 1){
                         let temp = data.Results[x].combo
                         console.log(data.Results[x].combo)

                         let i = 0
                         for(i=0; i<temp; i++) {
                             let temp=document.createElement('div')
                             let imageCopy=document.createElement('img')
                             temp.classList.add("col-xs-6")
                             imageCopy.src=data.Results[x].pic[i]
                             imageCopy.style="max-height: 300px; max-width: 300px;"
                             temp.appendChild(imageCopy)
                             copy.find('#imgBucket').append(temp)
                         }
                    }
                    else{
                        copy.find(".card-img").removeClass("d-none")
                        copy.find(".card-img").attr("src",data.Results[x].pic)
                    }

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
