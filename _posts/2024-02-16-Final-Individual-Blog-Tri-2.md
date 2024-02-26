---
toc: true
comments: true
layout: post
title: Individual CPT Final
description: CPT Individual Review
type: hacks
courses: { compsci: {week: 23} }
---

## Atlas

>- Over the course of this trimester the CPT project was a fun, yet overwhelming experience for me. It required a lot of creativity, thoughtfullness and organization, which my atlas team was able to accomplish
>- The plan for the cpt project was to create a website called Atlas which would be money related an accessible to the public. We were each planning to create a seperate feature. Torin was gonna do a search stock function where upon searching a specific stock it would display a great amount of facts about that stock including a real-time graph. Nandan was planning on creating a feature involving crypto, where each user would be given a certain amount of currency to then buy a coin which would change price immediately assuming millions of people were buying it at the same time, obviously randomized. Varun wanted to have a similar feature to Torins and Nandans, so he decided to create a stocks feature where a user could buy and sell certain stocks that we set as available for purchase. Finally, my feature was going to be real estate, where any user could browse through an address or area in san diego county to find a house they're interested in buying. Facts such as sq feet, beds, baths, and price were displayed including an image of the house. 
<br>
<br>

## Meeting CPT Requirements: 

<br>

| Collegeboard Requirements | Me |
|---------------------------|----|
| Instructions for input from one of the following: the user, a device, an online data stream, a file. | My feature takes in input from the user, and returns a specific amount of houses depending on the entered info. Users may only watch, admin can delete or edit houses. |
| Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the users purpose. | An example of a collection of data that is stored, is of the collection of houses on the backend that gets updated when an admin alters the change. This alters SQLite database, adding those changes. It helps fulfill our program’s purpose because all the data we have is given to any users interested in buying a house in San Diego County.|
| At least one procedure that contributed to the program’s intended purpose where you have defined: the name, return type, one or more parameters: | This procedure has a name: createURL, return type: a string (the URL), and parameters: It takes two parameters - address (the address to be encoded and used in the URL) and an optional parameter k (API key with a default value). ![]({{site.baseurl}}/images/final2.png) |
| An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure | This function shows sequencing: follows a sequence of steps within the "get" method to handle different cases depending on the value of the 'type' parameter. Shows selection: conditionals such as if, elif, else. Shows iteration: for loop that iterates over the houses in the database. The algorithm fetches house data and constructs a JSON response, then returned by the get method. ![]({{site.baseurl}}/images/final.png)|
| Calls to your student-developed procedure: | call to createURL , where the address is passed in as a parameter ![]({{site.baseurl}}/images/final4.png) |
| Instructions for output (tactile, audible, visual, or ) based on input and program functionality | Fetch code that displays the table with address, beds, baths, price and square feet based on the users inputted address and distance. ![]({{site.baseurl}}/images/final5.png)

## Collegeboard Video Requirements: 

[Link to Video](https://github.com/jm1021/sergiStudent/assets/142563800/8fa3bd89-7063-4b2d-973b-7782ceeb2e0f)

| Collegeboard Requirements | My Video |
|---------------------------|----------|
| Input to program | Seen in video, login and inputting address and distance |
| At least one aspect of the functionality of your program | Houses displayed, redirected to page with image and info about house.  |
| Output produced by program: | Display of houses. When logged in as admin, removing/editing a house alters database.  |
| My video does not have: | any distinguishing information, voice narration |
| My video is | a .mp4, 1 minute in length, less than 30MB in file size. |


### Main Commits/Pull Request for my feature:

>- [Pull Request](https://github.com/TDWolff/cpt/compare/457aa6827ea9579f28f0aa4497a841ffb04a0d1c..670bc0f86cfb4855354b3ea3d6eda998286f2201)
>- Unfortunately, due to an accident my changes to the fork of the repository were deleted, and all evidence of commits was gone except for a pull request that I was able to add before this occurance. The link above shows all my changes to this cpt fork and many important "commits."
>- My first most important commit was adding the actual house.py API with the data I was able to gather stored in a CSV file. Using a migration file I was able to migrate the data from the CSV file into a table inside thr SQLite databse called house. 
>- My second most important commit was when I was able to implement a JWT token to my house feature where an admin would be able to delete any house in the database while a user would be unauthorized. This was changed in the house.py delete function
>- Eventually I decided it would be cool to internally be able to edit the price, sqfeet, baths, beds, etc of the house, so I altered the PUT function in this same file and implemented a token into it for ADMIN to be able to edit information about certain houses. 
>- Another main commit was when I created the houseDetails.md file in the frontend, this would mean that once a user pressed on a house it would redirect to a page displaying the image of the house and its information in a more organized structure. 

### Main Commits for our project:

>- [Important Commit](https://github.com/sergi1207/atlas/commit/9723dda6d3f1c43091024b399138b34a9a564ca0) 
>- This was an important commit since Torin was able to implement most of our features into one page, having some integrity and union for our Atlas project. However, this commit had the most errors and most fixing which is why I believe it was very vital to our success. 
>- [Important Commit](https://github.com/sergi1207/atlas/commit/e0f9a66e60cde7bf175e3e0738fd50b960842890)
This commit right here might have not been as important but it sure did have many errors that altered our webpage and its logic. This commit allowed the users table to finally display and didnt allow for non registered/logged in users to delete or edit changes. 
>- [Final Commit](https://github.com/sergi1207/atlas/commit/5fa72571bfaca7290f99a17596ed427579879424)
This was our final commit really, where we finished up our project and had it all intergrated and ready for presenting. This was also a commit we had after fixing a CORS issue, which was appearing everywhere, making us stress out. Having almost everything working helped us relax and debug for the rest of the week. 


