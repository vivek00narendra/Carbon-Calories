window.addEventListener("load", function(event) {
    document.getElementsByTagName('button')[0].addEventListener("click", submitData)

    function submitData(e){
        let inputs = document.getElementsByTagName('input')
        console.log(inputs[0].value)
        const message = {
            id : 'popup',
            username: inputs[0].value,
            password: inputs[1].value
            
        }
        const jsonString = JSON.stringify(message)
        console.log(jsonString)
        var xmlhttp = new XMLHttpRequest()
        xmlhttp.open("POST", "https://carbon-calories.nn.r.appspot.com/loginpopup")
        xmlhttp.setRequestHeader("Content-Type", "application/json")
        xmlhttp.send(jsonString)
        
        xmlhttp.onload = function () {
            const data = JSON.parse(xmlhttp.response)
            console.log(data)
            if (data.message == "success"){
                console.log("hello")
                chrome.runtime.sendMessage(message);
                window.location.href='popup.html'
                
            }
        }
        

    }
}

)
