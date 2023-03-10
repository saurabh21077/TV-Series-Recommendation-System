# TV SERIES RECOMMENDATIONS AND REVIEWS

**INSTRUCTOR:** Dr. Pravesh Biyani \
**TAs:** Raashid Altaf, Mohd. Siraj Ansari, Gitansh Raj Satija

**GROUP:** \
**Yukti Goswami (MT21109)** \
**Saurabh Pandey (MT21077)** 

link : [Click here to visit our site](http://143.244.135.235:8044)

## <ins>WORKING OF THE PROJECT:</ins>
![Flow Diagram of Website](https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/flow%20diagram.jpg)

**1. FIRST-TIME USER / NON-REGISTERED USER:** \
The project's Login/Register Page is where it all begins. The user must create an account on the website with a username and password. 

The username must be unique, not empty, and unrelated to any other user. The notice "User ID cannot be empty" is shown on the webpage if the field is empty. A message appears if a user enters a username that has already been registered "User Id already exists! Please try a different one." 

Since the user is registering as a new user for the first time, they must choose "New User" as their user type. When a user successfully registers with a website, a notification stating "User details have been saved successfully!" appears, and the user's information is stored in the Users.csv file.

After successfully saving the information, the user can follow the steps of a registered user.

**2. REGISTERED USER:** \
The user must check in to the website using the username and password they used to register after arriving at the Login/Register Page. 

The notice "User ID cannot be empty" is displayed on the webpage if the username box is empty. "Invalid user name!" is displayed if the user provides a username that does not match any username in the Users.csv. 

Additionally, a password checker ensures that the user inputs the correct password when signing in; otherwise, the notice "Invalid Password" is displayed. 

The user is taken to a genre selection screen where they can choose their preferred genre upon logging in for the first time or if they have yet to indicate their preferences. Check boxes allow users to pick several genres. When a user clicks the "Submit" button, their selected genre is recorded in the Users.csv file, and they are then sent to the "Series Recommendation" page.

Depending on the genres they select while registering, the user's top 5 series recommendations are shown on the recommendation page. **<ins>Recommendations can take some time to load as information is fetched using Cinemagoer library.</ins>** When displaying the recommendations, the most recently broadcast series are given precedence.

The user is also given the opportunity to get recommendations based on the series name by selecting the "Get recommendations by Series name" button displayed on this page. The user is taken to a different page which asks for user input for the series name and number of recommendations.

To avoid confusion if the series have similar titles, a drop-down list displays the names of the series together with the years in which they were broadcasted. The most recent series that have aired are given priority in recommendations if the series does not have an air year. However, if a series has an air year, then shows aired within that time are recommended.

The recommendations are presented as a list, and each recommendation includes the details listed below:
- Series cover Image
- Series title
- Year in which the series was aired
- Series Rating according to IMDB
- Series Genres
- Series Description

## <ins>CONTRIBUTIONS:</ins>
**SAURABH PANDEY**
- Creating and Designing the models and flow of the project.
- Extracted the whole dataset from the IMDB. The dataset was distributed into many tables therefore:
    - Cleaned the dataset by keeping only the rows for TV series.
    - Extracted the required information from various tables containing different information 
    - Merged them together using Series ID as a unique key to get the required information.
    - (Unused code) Writing code for dynamically merging different datasets and extracting meaningful columns and data.
- Created KNN_Movie_Recommender function that applies KNearestNeighbour algorithm on the dataset and recommends the series on the basis of genre and also on the basis of Series name.
- Integration of flask with python for userHomePage, homePage.
- Fetching data from movies using Cinemagoer.
    - Fetching all data required to show in recommendation.
- Created JSON files movie data and movie title.
- Also collaborated in UI designs.
- Integration of different developed module into one complete project.
- Deployment of the project onto the server using gunicorn


**YUKTI GOSWAMI**
- Implemented the functionalities for fetching and storing User details.
- Cleaned the datasets and merged different linguistic datasets together but could not use it as it contained many faults.
- Implemented the functionality of fetching users genre choice from the website and storing it into the database. 
- Integration of flask with python for loginPage, afterFirstLogin.
- Implemented the User Interface (UI) for:
  - Login Page
  - Home Page
  - User Home Page
  - After first login
  - Information display of each Series
- Creating Flow Diagram for understanding of project using Miro board.
- Collaborated in Python codes and models.
- Creating Readme and documentations for the project.
- Showcasing the project progress in timely manner using presentations.
- Deployment of the project onto the server using gunicorn



## <ins>SCREENSHOTS:</ins>
<p> 
  Login Page<br>
  <img src="https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/loginpage1.png">
    
  
  Login page with successful registration message. <br>
  <img src="https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/loginpage2.png">
    
  
  After First Login - Genre Selection page <br>
  <img src="https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/afterfirstlogin.png">
    
  
   User Home Page<br>
  <img src="https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/userHomepage.png">
    
   
   Home Page for getting recommendation from Series Name<br>
  <img src="https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/getreccom.png">
    
   
  List view<br>
  <img src="https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/list%20view.png">
    
</p>


