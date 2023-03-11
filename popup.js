let bgpage = chrome.extension.getBackgroundPage();

let items = bgpage.items
let images = bgpage.itemsImg
let user = bgpage.user

console.log(images.length)    
console.log(images[0])
console.log(images[0].backgroundImage.length)


for (var i = 0; i < images.length; i++){

    itemRow = document.createElement("div")
    img = document.createElement('img')
    img.setAttribute("class","itemImg")
    
    img.src = images[i].backgroundImage.substring(5,images[i].backgroundImage.length - 2)
    itemRow.appendChild(img)
    console.log(itemRow)
    document.body.appendChild(itemRow)
}





    