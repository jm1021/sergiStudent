---
toc: true
comments: true
layout: post
title: Key Concepts
description: Key Concepts For CPT Project
type: plans
courses: { compsci: {week: 18} }
---


### HTML5 Table
- organizes th labels, td in input types, onlick action
<br><br>

<table>
    <tr>
        <th><label for="name">Name</label></th>
        <th><label for="email">Email</label></th>
        <th><label for="password">Password</label></th>
        <th><label for="phone">Phone</label></th>
    </tr>
    <tr>
        <td><input type="text" name="name" id="name" required></td>
        <td><input type="email" name="email" id="email" placeholder="abc@xyz.org" required></td>
        <td><input type="password" name="password" id="password" required></td>
        <td><input type="tel" name="phone_num" id="phone_num"
            pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
            placeholder="999-999-9999"></td>
        <td ><button onclick="create_User()">Create</button></td>
    </tr>
</table>

<br><br>

### HTML5 Form
- organizes input, form action vs onclick, p labels and input, combine with CSS

<br><br>

<form action="create_User()">
    <p><label>
        Name:
        <input type="text" name="name" id="name" required>
    </label></p>
    <p><label>
        User ID:
        <input type="text" name="uid" id="uid" required>
    </label></p>
    <p><label>
        Password:
        <input type="password" name="password" id="password" required>
        Verify Password:
        <input type="password" name="passwordV" id="passwordV" required>
    </label></p>
    <p><label>
        Phone:
        <input type="tel" name="phone_num" id="phone_num"
            pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
            placeholder="999-999-9999">
    </label></p>
    <p><label>
        Birthday:
        <input type="date" name="dob" id="dob">
    </label></p>
    <p>
        <button>Create</button>
    </p>
</form>

<br><br>

### JS Fetch and Response 
- After Input call action
- Extract data from DOM
- Build url
- Fetch
- Add response to end of table

<br><br>

function create_User(){
    // extract data from inputs
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const phone = document.getElementById("phone").value;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer my-token',
        },
    };
    //url for Create API
    const url='/crud_api/create/' + name + '/' + email+ '/' + password + '/' + phone;
    //Async fetch API call to the database to create a new user
    fetch(url, requestOptions).then(response => {
        // prepare HTML search result container for new output
        const resultContainer = document.getElementById("result");
        // trap error response from Web API
        if (response.status !== 200) {
            const errorMsg = 'Database response error: ' + response.status;
            console.log(errorMsg);
            // Email must be unique, no duplicates allowed
            document.getElementById("pswError").innerHTML =
                "Email already exists in the table";
            return;
        }
        // response contains valid result
        response.json().then(data => {
            console.log(data);
            //add a table row for the new/created userId
            const tr = document.createElement("tr");
            for (let key in data) {
                if (key !== 'query') {
                    //create a DOM element for the data(cells) in table rows
                    const td = document.createElement("td");
                    console.log(data[key]);
                    //truncate the displayed password to length 20
                    if (key === 'password'){
                        td.innerHTML = data[key].substring(0,17)+"...";
                    }
                    else{
                        td.innerHTML = data[key];}
                    //add the DOM data element to the row
                    tr.appendChild(td);
                }
            }
            //append the DOM row to the table
            table.appendChild(tr);
        })
    })
}

<br><br>

### Steps: 

>**Data Extraction:**
>- It starts by extracting data from HTML input elements with the IDs "name," "email," "password," and "phone."

const name = document.getElementById("name").value;
const email = document.getElementById("email").value;
const password = document.getElementById("password").value;
const phone = document.getElementById("phone").value;

>**Request Options**
>- It sets up options for the HTTP request. In this case, it's configured for a POST request, indicating that it's sending data to the server. It also includes headers like content type and authorization.

const requestOptions = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer my-token',
    },
};

>**API URL**
>- It constructs the URL for the API endpoint by appending the extracted data to the endpoint path.

const url='/crud_api/create/' + name + '/' + email+ '/' + password + '/' + phone;

>**API Call**
>- It uses the fetch function to make an asynchronous (non-blocking) POST request to the specified API endpoint (URL) with the provided options.

fetch(url, requestOptions).then(response => { /* ... */ });

>**Response Handling**
>- If the response status from the server is not 200 (OK), it indicates an error. In this case, it logs an error message and displays a user-friendly error message on the webpage.
If the response is successful (status 200), it assumes the server has processed the registration, and it handles the JSON response data.
It logs the data to the console and dynamically updates the webpage by creating a new table row (<tr>) with user details.

>**Displaying Results**
>- It appends the newly created table row to an existing HTML table on the webpage, displaying the registered user's information.


### HTML and JS Display Table: 
- JavaScript below shows elements needed to construct the rows of data in the table:
- JSON is required, it is hardcoded in this example. Typically JSON will come from a JavaScript fetch.
- JSON object is required, it is created from JSON string. This allows access to to elements in JSON using JavaScript dot notation (user._name)
- DOM editing is a huge part of the remainder of this example. DOM elements often nest inside of other DOM elements. For instance each td is nested in tr. Find examples of DOM create and append in the code below.
- Notice the definition of table and build you own map or visual of how these things are put together.

<br><br>


/*
<table>
  <thead>
  <tr>
    <th>Name</th>
    <th>ID</th>
    <th>Actions</th>
  </tr>
  </thead>
  <tbody id="table">
    <!-- javascript generated data -->
  </tbody>
</table>

    
    // Static json, this can be used to test data prior to API and Model being ready
const json = '[{"_name": "Thomas Edison", "_uid": "toby"}, {"_name": "Nicholas Tesla", "_uid": "nick"}, {"_name": "John Mortensen", "_uid": "jm1021"}, {"_name": "Eli Whitney", "_uid": "eli"}, {"_name": "Hedy Lemarr", "_uid": "hedy"}]';

    // Convert JSON string to JSON object
const data = JSON.parse(json);
    
    // prepare HTML result container for new output
const table = document.getElementById("table");
data.forEach(user => {
    
    // build a row for each user
    const tr = document.createElement("tr");
    
    // td's to build out each column of data
    const name = document.createElement("td");
    const id = document.createElement("td");
    const action = document.createElement("td");
    
    // add content from user data          
    name.innerHTML = user._name; 
    id.innerHTML = user._uid; 
    
    // add action for update button
    var updateBtn = document.createElement('input');
    updateBtn.type = "button";
    updateBtn.className = "button";
    updateBtn.value = "Update";
    updateBtn.style = "margin-right:16px";
    updateBtn.onclick = function () {
      alert("Update: " + user._uid);
    };
    action.appendChild(updateBtn);

    // add action for delete button
    var deleteBtn = document.createElement('input');
    deleteBtn.type = "button";
    deleteBtn.className = "button";
    deleteBtn.value = "Delete";
    deleteBtn.style = "margin-right:16px"
    deleteBtn.onclick = function () {
      alert("Delete: " + user._uid);
    };
    action.appendChild(deleteBtn);  

    // add data to row
    tr.appendChild(name);
    tr.appendChild(id);
    tr.appendChild(action);

    // add row to table
    table.appendChild(tr);
});

<br><br>

## JSON: 
>- [JSON Overview](https://jm1021.github.io/sergiStudent//2024/01/09/JSON-lesson.html)

<br>

## DOM: 
>- [DOM Overview]()