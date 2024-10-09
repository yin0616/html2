let text = "hello";
//javascript dom元素 document.xxxx
//dom元素api
//<p></p>
let element = document.createElement("p");//global avriable

//網頁剛開始載入進來page load
window.onload = function(){
    document.body.appendChild(element);
    setInterval(changeText,1000);//1秒(s)=1000毫秒
    changeText();
}

//Timer
//過一段時間後要更改文字內容
function changeText(){
    if(element.textContent == text){
        element.textContent = "";
    }else{
        let letterToType = text [element.textContent.length];
        element.textContent += letterToType;
        if(letterToType == " "){
            changeText();
        }
    }
}