# ITStudyNotes

# Github basics:
## Adding an existing project to GitHub using the command line  
https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/#platform-linux  
## README file:
README file is for documentation. So it can be in any text format, such as README.txt, READ.ME or README.md (Markdown language, which is also been used in Git Wiki).
The file name of README is usually in upper case, because the smaller ASCII code of the upper-case file name makes it appear on the top of the file list.
# HTML & CSS
## Center align (text & elements)
### Text
Horizontally center align text is easy, just define the text's **parent** element with css as:  
text-align: center;  
To vertically align a single-line text, you need to define the parent element's height and the line's **line height**, or in Chinese 行距，as the text never center vertically with in its parent element, the only way to do so is to specify the line heigh, or 行距, as the same height of the parent element, and all these should be **set in the parent element**:  
  height: 100px;  
  line-height: 100px;   
  vertical-align: middle;  
If the text is not a single line, you need to put it into a div element and use the following method for elements.
### elements
There are many ways to **horizontally center align** an element, one of which is:  
Define the element to be centered **itself** as:  
margin: auto;/*css code*/  
It is a little tricky to **vertically center align** an element.  
The only way to vertically center an element is putting it into a table cell, and it will be centered by default. There is no way to get the element away from the vertical center of a table cell. If you want the text in the div go to the top of the table cell, use this code to the div:  
height: 100%;
## Background color of parent and child elements
If the parent and child elements have different background colors, the child element's color will be on top and cover the parent one, as long as the child element has a size (width and height). If the child element doesn't have a size, the parent element's background color appears.
The ways for an element to get size:  
1. to be defined
2. to have an child element that has a size
3. to be a part of a table and the elements in the same row and column have sizes.
## Parent and child elements' sizes
If the parent element's size is not defined and the child's size is, the parent element will automatically adjust its size to fit the child element.
# JavaScript
## JavaScript's defects:  
### 1. == and ===
In JavaScript, you should always use === to compare to variables, since == automatically converts the two variables before comparing them, often causing very strange results.
### var and no var
If you declare a variable without a var before it, JS will make it a generall variable. As a result, if you forget to put a var before a variable that you intend to make local, it might be confused with other variables with the same name. 
One solusion is to put 'use strict'; at the beginning of every JS file. With this configuration, declarations without an var are donsidered errors.

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
# GUI-Packaging-Android&Windows

Andorid projects can be packaged as Apps for different OSs, such as APK for Android or exe for Windows.

Buildozer is such a tool for Android. Installation and using guide:  
https://kivy.org/docs/guide/packaging-android.html

But it might cause a computer death.

Python-for-android is another option to create an APK:  
https://python-for-android.readthedocs.io/en/latest/quickstart/

py2exe is for building Window executiable files:  
http://www.py2exe.org/index.cgi/Tutorial

A Windows computer is needed to test it.
