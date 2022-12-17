# TV SERIES RECOMMENDATIONS AND REVIEWS

**INSTRUCTOR:** Dr. Pravesh Biyani \
**TAs:** Raashid Altaf, Mohd. Siraj Ansari, Gitansh Raj Satija

**GROUP:** \
**Yukti Goswami (MT21109)** \
**Saurabh Pandey (MT21077)** 

## <ins>WORKING OF THE PROJECT:</ins>
![Flow Diagram of Website](https://github.com/saurabh21077/TV-Series-Recommendation-System/blob/main/Flow%20Diagram.jpg)

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

Depending on the genres they select while registering, the user's top 5 series recommendations are shown on the recommendation page. When displaying the recommendations, the most recently broadcast series are given precedence.

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


**YUKTI GOSWAMI**


## <ins>SCREENSHOTS:</ins>
<p> 
  <img src="", width="250">
  <img src="", width="250">
</p>


