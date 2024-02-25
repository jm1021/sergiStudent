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

![]({{site.baseurl}}/images/atlas.png)

## Meeting CPT requirements

>- Before starting our project our group had to make sure we were meeting the CPT requirements, which where mostly CRUD operations, SQLite dabatases, JWT Tokens and more. 

>- Throughout Atlas CRUD operations were seen when an Admin could login and delete or edit a users account using a JWT Token that would either get accepted or denied, depending on its role of user or admin. This was also implemented in my personal feature where the admin could delete or edit certain houses in the database while the users could not. If a user was trying to delete or edit something only the admin could, they would get unathorized, thus redirected to a 403 page. 
<br>
![]({{site.baseurl}}/images/housedelete.png)
<br>

>- We used SQLite databases to hold data such as users who signed up, transaction log of users, and a certain amount of houses in san diego country currecntly on SALE. Using CRUD operations our different tables in the database would indeed get altered. 
<br>
![]({{site.baseurl}}/images/db.png)
<br>

>- As mentioned earlier we utilized JWT Tokens which authorized certain users known as admins to have more flexibility than others. This was implemented by adding a _role column to our users database that would check to see whether a user is User or Admin, then the active cookie would be checked for this role and allow CRUD operations or unauthorize

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
