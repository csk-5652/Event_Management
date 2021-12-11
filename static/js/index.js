// onchange
// onclick
// onmousedown
// onmouseover
// onkeydown
// onload
// func for booking form 

// function Cancel_func(){
//     alert("Booking cancel")
// }

function logout_func(){
    alert("You logout successfully")
}

// Animation

// variable declaration 
var i=0;
var txt='Welcome to Eventila';
var speed=150;

// function for typing Animation

function typewriter(){
    if (i<txt.length){
        document.getElementById("typ").innerHTML+=txt.charAt(i);
        i++;
        setTimeout(typewriter,speed);
    }
}
typewriter() //print func 
