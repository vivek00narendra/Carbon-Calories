

chrome.runtime.onMessage.addListener(receiver);

var items = "No Items";
var itemsImg = "No Items"
var user = {username : "",
password : ""}

function receiver (message, sender, sendResponse){
    if (message.id == 'content'){
        items = message.itemArray;
        itemsImg = message.itemImgArray
        console.log('1')
    }else if (message.id == 'popup'){
        user.username = message.username
        user.password = message.password
        console.log('2')
    }else{
        console.log("send to backend")
    }
       
    
};  

