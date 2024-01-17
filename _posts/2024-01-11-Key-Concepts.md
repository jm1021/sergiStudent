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

<br>

## Local Storage: 

export class LocalStorage{
    constructor(keys){
        this.keys = keys;
        console.log("browser local storage available: "+String(this.storageAvailable));
    }

    get storageAvailable(){ //checks if browser is able to use local storage
        let type = "localStorage";
        let storage;
        try {
          storage = window[type];
          const x = "__storage_test__";
          storage.setItem(x, x);
          storage.removeItem(x);
          return true;
        } catch (e) {
          return (
            e instanceof DOMException &&
            // everything except Firefox
            (e.code === 22 ||
              // Firefox
              e.code === 1014 ||
              // test name field too, because code might not be present
              // everything except Firefox
              e.name === "QuotaExceededError" ||
              // Firefox
              e.name === "NS_ERROR_DOM_QUOTA_REACHED") &&
            // acknowledge QuotaExceededError only if there's something already stored
            storage &&
            storage.length !== 0
          );
        }
    }

    save(key){ //save a particular key
        if(!this.storageAvailable){return}; //check if local storage is possible
        window.localStorage.setItem(key,this[key]);
    }
    
    load(key){//load a particular key
        if(!this.storageAvailable){return}; //check if local storage is possible
        this[key] = window.localStorage.getItem(key);
    }

    saveAll(){ //saves data for all keys in this.keys
        if(!this.storageAvailable){return}; //check if local storage is possible
        Object.keys(this.keys).forEach(key => {
            window.localStorage.setItem(key,this[key]);
        });
    }

    loadAll(){//loads data from all keys in this.keys
        if(!this.storageAvailable){return}; //check if local storage is possible
        Object.keys(this.keys).forEach(key => {
            this[key] = window.localStorage.getItem(key);
        });
    }
}

export default LocalStorage;

>**Getters**

>- the getter: storageAvailable, this getter returns true if your browser is capable of using Local Storage, otherwise it returns an error message.

>**Functions**

>- the function save(key), this function saves the value this.key to the local storage with the respective key
- the function load(key), this function loads the value from the local storage with the respective key to this.key
- the function saveAll(), this function saves all of the values of this.key from the class’ this.keys to local storage
- the function loadAll(), this function load all of the values from the local storage from the class’ this.keys to their respective this.key

## Controller Class

import LocalStorage from "./LocalStorage.js";
import GameEnv from "./GameEnv.js";
import GameControl from "./GameControl.js";

export class Controller extends LocalStorage{
    constructor(){
        var keys = {currentLevel:"currentLevel",gameSpeed:"gameSpeed"}; //default keys for localStorage
        super(keys); //creates this.keys
    }

<br>

>-  Import LocalStorage, GameEnv, and GameControl, and export controller class
>- Run the initialization after a different time than the constructor. This is used to update the current level and start the eventListeners.

<br>

//separated from constructor so that class can be created before levels are added
    initialize(){ 
        this.loadAll(); // load data
        
        if(this[this.keys.currentLevel]){ //update to active level
            GameControl.transitionToLevel(GameEnv.levels[Number(this[this.keys.currentLevel])]);
        }
        else{ //if not currentLevel then set this.currentLevel to 0 (default)
            this[this.keys.currentLevel] = 0;
        }

        if(this[this.keys.gameSpeed]){ //update to custom gameSpeed
           GameEnv.gameSpeed = Number(this[this.keys.gameSpeed]);
        }
        else{ //if not gameSpeedthen set this.gameSpeed to GameEnv.gameSpeed (default)
            this[this.keys.gameSpeed] = GameEnv.gameSpeed;
        }
        
        window.addEventListener("resize",()=>{ //updates this.currentLevel when the level changes
            this[this.keys.currentLevel] = GameEnv.levels.indexOf(GameEnv.currentLevel);
            this.save(this.keys.currentLevel); //save to local storage
        });

        window.addEventListener("speed",(e)=>{ //updates this.gameSpeed when a speed event is fired
            this[this.keys.gameSpeed] = e.detail.speed();
            GameEnv.gameSpeed = this[this.keys.gameSpeed]; //reload or change levels to see effect
            this.save(this.keys.gameSpeed); //save to local storage
        })
 
    }

<br>

>- This code is a getter, it creates a table. The table is used to include level tags and the level number.


<br>

    get levelTable(){
        var t = document.createElement("table");
        //create header
        var header = document.createElement("tr");
        var th1 = document.createElement("th");
        th1.innerText = "#";
        header.append(th1);
        var th2 = document.createElement("th");
        th2.innerText = "Level Tag";
        header.append(th2);
        t.append(header);

        //create other rows
        for(let i = 0;i < GameEnv.levels.length;i++){
            var row = document.createElement("tr");
            var td1 = document.createElement("td");
            td1.innerText = String(i);
            row.append(td1);
            var td2 = document.createElement("td");
            td2.innerText = GameEnv.levels[i].tag;
            td2.addEventListener("click",()=>{ // when player clicks on level name
                GameControl.transitionToLevel(GameEnv.levels[i]); //transition to that level
            })
            row.append(td2);
            t.append(row);
        }

        return t; //returns <table> element
    }

<br>    

>- Used for the speedDiv, changes the gameSpeed setting. 

    
    get speedDiv(){
        var div = document.createElement("div"); //container

        var a = document.createElement("a"); //create text
        a.innerText = "Game Speed";
        div.append(a);

        var input1 = document.createElement("input"); //create inputfeild
        input1.type = "number"; //type number (1234...)
        const event = new CustomEvent("speed", { detail: {speed:()=>input1.value} });
        input1.addEventListener("input",()=>{ //after input feild is edited
            window.dispatchEvent(event); //dispatch event to update game speed
        })
        div.append(input1);
        
        return div; //returns <div> element
    }
}

export default Controller;

<br>

## Changes in the game.md file

<br>

#gameBegin, #controls, #gameOver, #settings {
      position: relative;
        z-index: 2; /*Ensure the controls are on top*/
    }

<br>

>- To add an extra button:

<br>

.sidenav {
      position: fixed;
      height: 100%; /* 100% Full-height */
      width: 0px; /* 0 width - change this with JavaScript */
      z-index: 3; /* Stay on top */
      top: 0; /* Stay at the top */
      left: 0;
      overflow-x: hidden; /* Disable horizontal scroll */
      padding-top: 60px; /* Place content 60px from the top */
      transition: 0.5s; /* 0.5 second transition effect to slide in the sidenav */
      background-color: black; 
    }
<br>

<div id="mySidebar" class="sidenav">
  <a href="javascript:void(0)" id="toggleSettingsBar1" class="closebtn">&times;</a>
</div>

<br>

>- Sidebar: 

<br>

<div id="canvasContainer">
    <div id="gameBegin" hidden>
        <button id="startGame">Start Game</button>
    </div>
    <div id="controls"> <!-- Controls -->
        <!-- Background controls -->
        <button id="toggleCanvasEffect">Invert</button>
    </div>
    <div id="settings"> <!-- Controls -->
        <!-- Background controls -->
        <button id="toggleSettingsBar">Settings</button>
    </div>
    <div id="gameOver" hidden>
        <button id="restartGame">Restart</button>
    </div>
</div>

<br>
