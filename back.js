var dataG
var dataOG

$(function(){
    $('#searchClick').click(function(){
        let usertext = $("#userbox").val();
        console.log(usertext);
        window.location.href = 'results.html' + '#' + usertext;
     })
});

$(function(){
    var usertext = window.location.hash.substring(1)

    function sortLH(x){
        x.Results.sort(function(a, b){
            return a.price - b.price
        })
    }

    function sortHL(x){
        x.Results.sort(function(a, b){
            return b.price - a.price
        })
    }
  
    function addCards(data){
        $(".current").remove()
        for(var x in data.Results){
            let copy = $(".template").clone()
            copy.removeClass("template")
            copy.removeClass("d-none")
            copy.addClass("current")
            copy.find(".card-title").text(data.Results[x].name)
            copy.find(".item-price").text(("$" + data.Results[x].price))
            if(data.Results[x].stock == "In Stock"){
                copy.addClass("IS")
                copy.find(".card-website").text(data.Results[x].store)
            }
            else if(data.Results[x].stock == "OOS"){
                copy.addClass("OOS")
                copy.find(".card-website").text(data.Results[x].store + " - OOS")
                copy.find(".card-website").attr("style", "color:#c10808")
            }
            copy.find(".card-website").attr("href",data.Results[x].redirectURL)

            //If combo item, it shows multiple pics
            if(data.Results[x].combo > 1){
                let temp = data.Results[x].combo
                console.log(data.Results[x].combo)

                copy.find(".card-img-primary").attr("src",data.Results[x].pic[0])
                for(let i=1; i<temp; i++) {
                    //let temp=document.createElement('div')
                    //let imageCopy=document.createElement('img')
                    let imageCopy = document.createElement('img')
                    //temp.classList.add("col-xs-6")
                    imageCopy.src=data.Results[x].pic[i]
                    console.log(data.Results[x].pic[i])
                    imageCopy.id = i
                    imageCopy.style="max-height: 100px; max-width: 100px;"
                    //temp.appendChild(imageCopy)
                    //copy.find('#secImageHolder').append(temp)
                    console.log(temp)
                    copy.find(".secImageHolder").append(imageCopy)
                }
            }
            else{
                copy.find(".card-img-primary").removeClass("d-none")
                copy.find(".card-img-primary").attr("src",data.Results[x].pic)
                console.log(data.Results[x].pic)
            }

        copy.find(".imageHolder").removeClass(".templateIMG2H")
        $(".cardHolder").append(copy)
        console.log("New card made...")
	}
    }

    function saveData(x){
        dataOG = x
        dataG = JSON.parse(JSON.stringify(x))
    }

    function runPy(userInput) {
        $.ajax({
        data : userInput,
            url:'http://72.176.215.95:5000/success/'+userInput,
            success: function(data) {
                saveData(data)
                addCards(data)
                $("#radioBM").attr("checked","checked")
                dataOG = data
                console.log(dataG)
            }
        });
    }
    
    runPy(usertext)

    $("#radioLH").click(function (){
        if ($("#radioLH").is(":checked")){
            sortLH(dataG)
            addCards(dataG)
            console.log("hello")
        }
    })

    $("#radioHL").click(function (){
        if ($("#radioHL").is(":checked")){
            sortHL(dataG)
            addCards(dataG)
        }
    })

    $("#radioBM").click(function (){
        if ($("#radioBM").is(":checked")){
            addCards(dataOG)
            console.log(dataOG)
        }
    })

    $('#searchClick-results').click(function(){
        let usertext = $("#userboxResults").val();
        console.log(usertext);
        window.location.href = 'results.html' + '#' + usertext;
        location.reload();
        runPy(usertext);
    })
});
