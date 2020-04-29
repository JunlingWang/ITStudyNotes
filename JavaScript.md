# JavaScript
## JavaScript's defects:  
### 1. == and ===
In JavaScript, you should always use === to compare to variables, since == automatically converts the two variables before comparing them, often causing very strange results.
### 2. var and no var
If you declare a variable without a var before it, JS will make it a generall variable. As a result, if you forget to put a var before a variable that you intend to make local, it might be confused with other variables with the same name. 
One solusion is to put 'use strict'; at the beginning of every JS file. With this configuration, declarations without an var are considered errors.

## Adjust an element's height:  
function myFunction() {  
    document.getElementById("frame").style.height = "500px"; /*Adjust the element's height*/  
}  

## Fit an element's height to the browser window dynamically:  
In the script.js file, write this code:  
function fitSize()    
&nbsp{    
                var heights = window.innerHeight;  
                document.getElementById("frame").style.height = heights + "px";  
            }  
              
window.onresize = function() {  /*this function is called when the window is resized*/  
                fitSize();  
            };  
If you want to fit the size while the window is opening, code the 〈body〉tag like this:  
〈body onload="fitSize()"  〉
When the page is loaded, call this JS function-->
## Write html code into a div
document.getElementById("demo").innerHTML = "〈div id = 'test'〉〈/div〉";  
## Pass the value of an HTML field to another  
document.getElementById("receiver").value = document.getElementById("sender").value  





