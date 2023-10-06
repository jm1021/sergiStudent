---
toc: true
comments: false
layout: post
title: Review Ticket 5
description: Here I will be going over our accomplishments and troubles. 
type: tangibles
courses: { compsci: {week: 5} }
---

# Week 5

## Review Ticket

### What We Did:
This week we worked on our Web Development test. Ishan Lincoln Sergi and I worked on the hacks and practiced to present them. We input and ran the code and made sure we were prepared.

### Issues for this week:
First, we had an issue in where some of our running code wasn't disposing our preferred output. After "swapping" the links on js with HTML the expected output of "switched" wasn't appearing. We added a missing piece of code to resolve our issues. Lincoln and I had issues with our teacher repository not updating the new files, we tried committing and pulling, which fortunately worked for me but Lincoln had to create a new teacher repository.

# Markdown and HTML Basics

## Markdown
Clear demonstration of Markdown syntax with heading and paragraph examples.
Proper use of Markdown conventions for creating headings and paragraphs.
## HTML
HTML examples are well-structured, featuring heading and paragraph tags.
Each HTML tag is accompanied by a Markdown description, enhancing understanding for users familiar with Markdown.
Attributes:
Good explanation of attributes in HTML tags with the concept of name/value pairs.
A practical example of an <a> (anchor) tag with an href attribute is provided.
## Sample Markdown vs HTML Tags
A comparison between Markdown and HTML tags is presented, showcasing the syntax differences.
Examples include image tags, link tags, bold and italic text, emphasizing the transition from Markdown to equivalent HTML.
## More Tags in HTML
The introduction of additional HTML tags like <p>, <button>, and <div> is beneficial for learners.
The nested structure of <div> elements is explained, illustrating how tags can be organized inside each other.

## Conclusion
The content effectively introduces users to the basics of Markdown and HTML. The side-by-side comparison aids in understanding the transition from Markdown to HTML, making it a useful resource for beginners.

# JavaScript Basics - Variables, Strings, Numbers, Arrays, and Objects

## Variables:
Clear examples of variable declaration, assignment, and logging are provided.
Proper use of console.log() helps users understand variable values and types.

## Strings:
String manipulation functions like substring(), toUpperCase(), toLowerCase(), and includes() are demonstrated.
Each function is appropriately explained, and practical examples are given.

## Numbers:
Useful information about number operations (+, -, *, /, %) and formatting (.toString(), Math.round(), .toFixed()) is covered.
Practical examples enhance comprehension of number-related concepts.

## Arrays:
Introduction to arrays with examples of declaration and access.
Array manipulation methods like push(), shift(), and pop() are demonstrated.

## Objects:
Clear explanation and examples of object creation, access, and manipulation are provided.
Proper use of dot notation and square bracket notation is highlighted.
## Conclusion:
The JavaScript basics tutorial effectively introduces users to key concepts, providing a solid foundation for further learning. The inclusion of practical examples enhances the user's understanding and application of JavaScript fundamentals.

# JavaScript DOM Manipulation and Functions Review

## Description:
The provided code demonstrates various aspects of JavaScript DOM manipulation and functions. Below is a detailed review:

## Accessing DOM Elements:
Example #1 shows the use of document.getElementById to access an HTML element by its ID.
The retrieved element is logged to the console, illustrating the structure of the DOM.

## Getting Data within HTML Element:
Example #2 introduces the use of .innerHTML to retrieve data within an HTML element.
The inner HTML of the element is logged, showcasing how to access the content.

## Setting Data within HTML Element:
Example #3 demonstrates updating the inner HTML of an element using the assignment operator.
The updated inner HTML is logged to the console.

## Creating Elements:
Example #4 creates a new p element using document.createElement and sets its content.
The new element is logged, highlighting the process of element creation.

## Issue and Solution - Placing Element in HTML:
Example #5 addresses the issue of the created element not being placed in the HTML.
The solution involves using appendChild to add the element to a specified location in the HTML.

## Functions in JavaScript with DOM:
Example #6 defines a function (createPTag) that creates a p element with specified text.
The function is used to create a p element, which is then added to the HTML.

## OnClick Event:
Example #7 introduces the OnClick event, triggering the creation of a p element when a button is clicked.
Two functions (createPTag and addPTagOnButton) are used in conjunction with the event.

## Conclusion:
The code effectively covers various aspects of DOM manipulation and functions in JavaScript. It provides a comprehensive understanding of accessing, modifying, and creating elements within the DOM. The use of functions enhances code readability and reusability.

# JavaScript Basics - Console, Variables, Operators, and Conditional Statements

## Description:
The provided code covers fundamental JavaScript concepts, including console output, data types, operators, and conditional statements. Below is a detailed review:

## Console Output:
Example #1 demonstrates the use of console.log to output text to the console.
Clear instructions are provided on how to view the console in various browsers.

## Storing Data:
The section emphasizes the importance of understanding how data is stored in programming, introducing the concept of Data Abstraction.
Basic data types in JavaScript (string, number, boolean) are explained.

## Name the Data and Accessing Data:
The process of creating variables using the var keyword and accessing data by using the variable name is explained.
Examples #3 and #4 show the creation of variables and logging them along with their types.

## String Operators:
Example #5 illustrates string concatenation and string comparison using operators like == and !==.
The assignment operator (=) is demonstrated for changing the value of a variable.
## Number Operators:
Example #6 covers number operators (+, -, *, /, %) and their usage.
Number comparison with operators like ===, !==, <, >, <=, and >= is demonstrated.

## Conditional Statements:
Example #7 introduces conditional statements (if, else if, else) based on the example of setting an alarm.
Clear explanations and comments accompany the code, making it beginner-friendly.

## Conditional Statements + Operators:
Example #8 extends the use of conditional statements by incorporating comparison operators.
The if, else if, else structure is utilized to handle different cases.

## Conclusion:
The code effectively covers foundational concepts of JavaScript, providing a solid introduction to variables, operators, and conditional statements. It serves as a beginner-friendly resource for understanding essential programming principles.


# JavaScript - Debugging

## Hack 1 Changes Made:
Introduced a variable letterNumber to represent the position of the alphabet letter.
Used a for loop to iterate through alphabetList.
Checked if the current index i matches the specified letterNumber.
If there's a match, printed the corresponding alphabet letter and its position.

## Feedback:
The loop condition in for (var i = 0; i < alphabetList; i++) should be for (var i = 0; i < alphabetList.length; i++) to iterate over the array properly.
The printed output message includes a hardcoded "1" in "is letter number 1 in the alphabet". It should be the actual position.
Review for Segment 3: Odd Numbers

## Hack 2 Changes Made:

Corrected the loop condition to while (i < 10) to print odd numbers below 10.
Adjusted the loop increment to i += 2 to ensure odd numbers are pushed into the array.

## Feedback:

The loop condition while (i < 10) should be while (i <= 10) to include the number 10.
The variable name evens is misleading; consider renaming it to odds for clarity.
Review for Segment 4: Filtering Numbers

## Hack 3 Changes Made:

Adjusted the loop condition to while (i <= 100) to include 100.
In the for loop, directly iterate through the array elements rather than using for (var i of numbers).

## Feedback:

The loop condition while (i < 100) is correct, but the loop could be simplified as for (var i = 1; i <= 100; i++).
The logic inside the loop could be improved to correctly filter multiples of 2 or 5.
Review for Challenge: Menu Calculation

## Hack 4 Changes Made:

Added a function calculateTotal(item) to calculate the total cost based on the selected menu item.
Updated the code to call this function for the specified item ("burger"). Added all other items present to calculate the total. 

## Feedback:

The toFixed(2) method is used to round the menu item prices to two decimal places, which is a good practice for currency representation.
The code should be expanded to handle multiple items and accumulate the total cost.

## Conclusion:
The provided code shows understanding of basic JavaScript concepts. Feedback provided aims to enhance correctness and clarity. Further improvements could be made based on the specific comments for each code segment.

# Accomplishments: 
## JavaScript Basics - Variables, Strings, Numbers, Arrays, and Objects
II
### Variables:
- ✔️ Clear examples of variable declaration, assignment, and logging.
- ✔️ Proper use of `console.log()` for understanding variable values and types.

### Strings:
- ✔️ Demonstrated string manipulation functions (`substring()`, `toUpperCase()`, `toLowerCase()`, `includes()`).
- ✔️ Clear explanations with practical examples.

### Numbers:
- ✔️ Covered number operations (`+, -, *, /, %`) and formatting (`.toString()`, `Math.round()`, `.toFixed()`).
- ✔️ Practical examples enhanced comprehension of number-related concepts.

### Arrays:
- ✔️ Introduced arrays with examples of declaration and access.
- ✔️ Demonstrated array manipulation methods (`push()`, `shift()`, `pop()`).

### Objects:
- ✔️ Clear explanation and examples of object creation, access, and manipulation.
- ✔️ Highlighted proper use of dot notation and square bracket notation.

#### Conclusion:
- ✔️ The JavaScript basics tutorial provides a solid foundation with practical examples.

## JavaScript DOM Manipulation and Functions Review

### Accessing DOM Elements:
- ✔️ Example #1 demonstrates the use of `document.getElementById`.
- ✔️ Illustration of DOM structure through console logging.

### Getting Data within HTML Element:
- ✔️ Example #2 introduces the use of `.innerHTML` for data retrieval.
- ✔️ Clear demonstration of accessing content within an HTML element.

### Setting Data within HTML Element:
- ✔️ Example #3 shows updating inner HTML using the assignment operator.
- ✔️ Logged the updated inner HTML for verification.

### Creating Elements:
- ✔️ Example #4 demonstrates creating a new `p` element with content.
- ✔️ Console log illustrates the process of element creation.

### Issue and Solution - Placing Element in HTML:
- ✔️ Example #5 addresses the issue of placing the created element in HTML.
- ✔️ Solution involves using `appendChild` to add the element to a specified location.

### Functions in JavaScript with DOM:
- ✔️ Example #6 defines a function (`createPTag`) and uses it to create a `p` element.
- ✔️ Showcases the application of functions in DOM manipulation.

### OnClick Event:
- ✔️ Example #7 introduces the OnClick event for dynamic element creation.
- ✔️ Two functions (`createPTag` and `addPTagOnButton`) are utilized effectively.

#### Conclusion:
- ✔️ The code comprehensively covers various aspects of DOM manipulation and functions.

## JavaScript Basics - Console, Variables, Operators, and Conditional Statements

### Console Output:
- ✔️ Example #1 demonstrates the use of `console.log` for text output.
- ✔️ Clear instructions on viewing the console in different browsers.

### Storing Data:
- ✔️ Emphasized the importance of understanding data storage and introduced Data Abstraction.
- ✔️ Explained basic data types (string, number, boolean) in JavaScript.

### Name the Data and Accessing Data:
- ✔️ Explained the process of creating variables and accessing data.
- ✔️ Examples #3 and #4 illustrate variable creation and logging.

### String Operators:
- ✔️ Example #5 covers string concatenation and comparison using operators.
- ✔️ Demonstrated the assignment operator for variable value change.

### Number Operators:
- ✔️ Example #6 covers number operators (`+, -, *, /, %`) and their usage.
- ✔️ Demonstrated number comparison with various operators.

### Conditional Statements:
- ✔️ Example #7 introduces conditional statements (if, else if, else) with the alarm example.
- ✔️ Clear explanations and comments enhance beginner-friendliness.

### Conditional Statements + Operators:
- ✔️ Example #8 extends conditional statements using comparison operators.
- ✔️ Effective use of the if, else if, else structure to handle different cases.

#### Conclusion:
- ✔️ The code provides a solid introduction to JavaScript fundamentals.

## JavaScript - Debugging

### Hack 1 Changes Made:
- ✔️ Introduced a variable `letterNumber` to represent the position of the alphabet letter.
- ✔️ Used a for loop to iterate through `alphabetList`.
- ✔️ Checked if the current index `i` matches the specified `letterNumber`.
- ✔️ Printed the corresponding alphabet letter and its position.
### Hack 2 Changes Made:
- ✔️ Corrected the loop condition to `while (i <= 10)` to print odd numbers below 10.
- ✔️ Adjusted the loop increment to `i += 2` to ensure odd numbers are pushed into the array.
### Hack 3 Changes Made:
- ✔️ Adjusted the loop condition to `while (i <= 100)` to include 100.
- ✔️ In the for loop, directly iterate through the array elements rather than using `for (var i of numbers)`.
### Hack 4 Changes Made:
- ✔️ Added a function `calculateTotal(item)` to calculate the total cost based on the selected menu item.
- ✔️ Updated the code to call this function for the specified item ("burger"). Added all other items present to calculate the total.
#### Conclusion:
- ✔️ The provided code shows understanding of basic JavaScript concepts.
- ✔️ Feedback provided aims to enhance correctness and clarity.

# Comments: 
- The HTML Wireframe is pretty cool, although I don't think it follows the rubric 