---
toc: true
comments: true
layout: post
title: Debugging Event
description: Debugging Event
type: hacks
courses: { compsci: {week: 23} }
---


# Debugging:

## Prerequisites:
>- A backend API implemented using Flask.
>- VS Code
>- Developer Tools

## Step 1: 
>- Go to your backend, start it with debugging enabled 
>- Specifically, main.py is what you should be looking for

## Step 2: Set Breakpoint at the Beginning of Endpoint Code
>- Identify the endpoint you want to debug in your backend code. 
>- Place a breakpoint at the beginning of your endpoint
>- def get(self):
            t = request.args.get('type')
>- set the breakpoint below the function to stop the program from getting the information

## Step 3: Run Frontend with Split Screen Loading Source for API Fetch
>- Open your frontend codebase in your code editor. Identify the component or function responsible for making the API request. 
>- Great places to set your breakpoint would be at the fetch, .then and .catch
>- These breakpoints pause you before you can continue to the next line

## Step 4: Run Frontend, Capture Break at Fetch, Examine Body
>- Now, run your frontend.
>- It should hit the breakpoints set in the Fetch API call. 
>- Examine the request and response bodies using the browser's developer tools.

## Step 5: Press Play on Frontend, Observe Stop Inside of Backend
>- Resume the execution of the frontend code (press play).
>- This should trigger the backend to continue its execution.
>- Observe the breakpoints hit in your backend code.
>- You should get redirected to the backend automatically. 

## Step 6: Press Step Over on Backend Until Obtaining Data from Database
>- Here, you can step over the code to see all the colleted data
>- In this example it would be the Address, Distance, cookie, etc. 

## Step 7: Press Play Button to End Backend Debugging Session
>- To Resume the execution of your backend code (press play)
>- This will conclude the backend debugging session.

## Stop 8: Frontend Debugging
>- Resume your debugging on the frontend by pressing continue (play button)

## Step 9: Step In Until You See Data
>- You can continue or step in oto acquire the data requested on the frontend. 
>- In this case, it would be nearby houses to the address searched.  

Images will be included in the git issue. 




