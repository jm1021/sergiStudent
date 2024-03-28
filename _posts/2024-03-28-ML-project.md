---
toc: true
comments: true
layout: post
title: ML Project Review Ticket
description: ML Project Part 2
type: tangibles
courses: { compsci: {week: 28} }
---

![]({{site.baseurl}}/images/ML2.png)
>- This is the frontend for my ML house project. 
>- Users interested in finding a house can input a certain number of beds, baths, square feet and price. 
>- The output will be a house from a dataset that matches (as close as it can get in terms of machine learning) to those requirements. 


<br><br>

![]({{site.baseurl}}/images/ML.png)
>- This shows the output
>- The output consists of the top 3 closely matched houses to the data entered
>- It provides with the address of the house which can then be entered into the house searcher

<br><br>

![]({{site.baseurl}}/images/ML3.png)
>- This is the backend code
>- It uses machine learning to predict a closely related house
>- Each of the 3 houses goes in order of closeness
>- The data is located in a CSV file I downloaded from a redfin API

<br><br>

![]({{site.baseurl}}/images/ML4.png)
>- This is the frontend code
>- It displays the table created to keep it all organized
>- The prediction is achieved through a POST request to the backend

<br><br>

![]({{site.baseurl}}/images/ML5.png)
>- The original data was 2 beds, 2 baths, 2000 square feet, and 10 million
>- The house data from the data set is 3 beds, 2 baths, 1550 square feet and roughly 10 million, the model says it's a 94% match from the dataset. 
>- This shows how my model works and utilizes ML to have an estimate of the house data entered. 