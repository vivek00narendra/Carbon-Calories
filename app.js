
window.addEventListener("load", function(event) {
    var items = document.getElementsByClassName("css-9s1jr8 ei50f4d0"); 
    var itemsImg = document.getElementsByClassName("css-128ipej");
    console.log(itemsImg)
    itemIDs = []
    itemsImgs = []

    for(var i = 0; i < items.length; i++){
        
        itemIDs.push(items[i].id) 
        itemsImgs.push(itemsImg[i].style)
        console.log(itemsImgs[i])
    }
    
    
    
    let message ={
        id : 'content',
        itemArray : itemIDs,
        itemImgArray : itemsImgs
    }
    console.log(message)
    console.log(message.itemImgArray.length)
    chrome.runtime.sendMessage(message);
    
    console.log(document.getElementsByClassName('css-dldxm2 edzik9p0'))
    document.getElementsByClassName('css-dldxm2 edzik9p0')[0].addEventListener("click", function(event){
    console.log('hello')
    let message ={
        id :'send'
    }
    chrome.runtime.sendMessage(message)
})
})



