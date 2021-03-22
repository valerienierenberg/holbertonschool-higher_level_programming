# 0x12-javascript-warm_up

This project marks our first exposure to JavaScript in the curriculum. All files will be interpreted on Ubuntu 14.04 LTS using node (version 10.14.x), and code will be semistandard compliant (version 14.x.x). Rules of Standard + semicolons on top.


## Learning Objectives

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between var, const and let
* What are all the data types available in JavaScript
* How to use the if, if ... else statements
* How to use comments
* How to affect values to variables
* How to use while and for loops
* How to use break and continue statements
* What is a function and how do you use functions
* What does a function that does not use any return statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file


## File Descriptions

* 0-javascript_is_amazing.js - script that prints “JavaScript is amazing”. (not allowed to use var, and print using console.log())
* 1-multi_languages.js - script that prints 3 lines: (same restrictions apply as task 0)
    * The first line: “C is fun”
    * The second line: “Python is cool”
    * The third line: “JavaScript is amazing”
* 2-arguments.js - script that prints a message depending of the number of arguments passed:
    * If no arguments are passed to the script, print “No argument”
    * If only one argument is passed to the script, print “Argument found”
    * Otherwise, print “Arguments found”
* 3-value_argument.js - script that prints the first argument passed to it:
    * If no arguments are passed to the script, print “No argument”
    * Not allowed to use 'length'
* 4-concat.js - script that prints two arguments passed to it, in the following format: “ is ”
* 5-to_integer.js - script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
    * If the argument can’t be converted to an integer, print “Not a number”
    * Not allowed to use try/catch
* 6-multi_languages_loop.js - script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop (must use while or for loop, not if else)
* 7-multi_c.js - script that prints x times “C is fun”
    * If the first argument can’t be converted to an integer, print “Missing number of occurrences”
    * Must use for/while loop
* 8-square.js - script that prints a square, where the first argument is the size of the square
    * If the first argument can’t be converted to an integer, print “Missing size”
    * Must use the character X to print the square
    * Must use while/for loop
* 9-add.js - prints the addition of 2 integers - first arg is first int, second arg is second int
    * Must define a function with this prototype: function add(a, b)
* 10-factorial.js - computes and prints a factorial
    * Must use a function, and must be done recursively
* 11-second_biggest.js - searches the second biggest integer in the list of arguments.
* 12-object.js - update given script to replace the value 12 with 89
    ```
    #!/usr/bin/node
    const myObject = {
    type: 'object',
    value: 12
    };
    console.log(myObject);
    /*
    YOUR CODE HERE
    */
    console.log(myObject);
    ```
* 13-add.js - function that returns the addition of 2 integers.
    * Function must be visible from outside
* 100-let_me_const.js - file that modifies the value of myVar to 333
    ```
    #!/usr/bin/node
    myVar = 89;
    require('./100-let_me_const')
    console.log(myVar);
    guillaume@ubuntu:~/0x12$ ./100-main.js
    333
    ```
* 101-call_me_moby.js - function that executes x times a function.
    * The function must be visible from the outside
    * Prototype: function (x, theFunction)
* 102-add_me_maybe.js - function that increments and calls a function.
    * The function must be visible from outside
    * Prototype: function (number, theFunction)
* 103-object_fct.js - Updates the given script by adding a new function incr that increments the integer value
    ```
    guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
    #!/usr/bin/node
    const myObject = {
    type: 'object',
    value: 12
    };
    console.log(myObject);
    /*
    YOUR CODE HERE
    */
    myObject.incr();
    console.log(myObject);
    myObject.incr();
    console.log(myObject);
    myObject.incr();
    console.log(myObject);

    guillaume@ubuntu:~/0x12$ ./103-object_fct.js 
    { type: 'object', value: 12 }
    { type: 'object', value: 13, incr: [Function] }
    { type: 'object', value: 14, incr: [Function] }
    { type: 'object', value: 15, incr: [Function] }
    guillaume@ubuntu:~/0x12$ 
    ```
