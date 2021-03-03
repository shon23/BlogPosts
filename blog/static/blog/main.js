var head = document.querySelector("#mouseover")

head.addEventListener('mouseover', function(){
    head.style.color = 'black';
})
head.addEventListener('mouseout', function(){
    head.style.color = 'white';
})
console.log("Connected!")