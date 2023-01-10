











const btn = document.getElementById("button2")
function myFunction() {
btn.disabled = true;
btn.style.color = "red";
setTimeout(()=>{
    btn.disabled = false;
    console.log('Button Activated')}, parseInt(document.getElementById('firstinput').value)*1000)
}
function p() {
    console.log("button clicked");
    myFunction()
}