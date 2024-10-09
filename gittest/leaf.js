let leaves;
window.onload = function(){
    leaves = document.querySelectorAll("body >img[data-autumn]");
    for(let i=0; i<leaves.length;i++){
        leaves[i].style.left = i*window.innerWidth/leaves.length + "px";
        leaves[i].style.top = -leaves[i].height +"px";
    }
    setInterval(move,50);
}
function move(){
    for(let i=0;i<leaves.length;i++){
        let newPos = parseInt(leaves[i].style.top)+2;
        if(newPos > window.innerHeight){
            newPos = -leaves[i].height;
        }
        leaves[i].style.top = newPos + "px";
    }
    
}