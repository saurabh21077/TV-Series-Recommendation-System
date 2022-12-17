from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect, url_for, stream_template, stream_with_context
from cryptography.fernet import Fernet
from datetime import date
import json
from imdb import Cinemagoer
from Classifier import KNearestNeighbours

app = Flask(__name__)

with open('movie_data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open('movie_titles.json', 'r+', encoding='utf-8') as f:
    movie_titles = json.load(f)
    
genres = ['Action','Adult','Adventure','Animation','Biography','Comedy','Crime','Documentary','Drama','Family','Fantasy','Film-Noir','Game-Show','History','Horror','Music','Musical','Mystery','News','Reality-TV','Romance','Sci-Fi','Short','Sport','Talk-Show','Thriller','War','Western','\\N']
movies = [title[0] for title in movie_titles]
sorted_movies = []
no_years=[]
for title in movie_titles:
    if title[4]=="\\N":
        no_years.append((title[0],'Not found'))
    else:
        sorted_movies.append((title[0],title[4]))
sorted_movies = sorted(sorted_movies, key=lambda x: x[1], reverse=True)
sorted_movies.append(no_years)

def KNN_Movie_Recommender(test_point, k):
    # Create dummy target variable for the KNN Classifier
    target = [0 for item in movie_titles]
    # Instantiate object for the Classifier
    model = KNearestNeighbours(data, target, test_point, k=k)
    # Run the algorithm
    model.fit()
    # Print list of 10 recommendations < Change value of k for a different number >
    table = []
    # print('KNN recommendations')
    for i in model.indices:
        # Returns back movie title and imdb link
        # print(movie_titles[i])
        table.append([movie_titles[i][0], movie_titles[i][2], movie_titles[i][3], data[i][-1]])
    # print('KNN recommendations ended')
    return table

@app.route("/", methods = ["GET", "POST"])
@app.route("/loginPage", methods = ["GET", "POST"])
def loginPage():
    # print("login page started")
    users_df = pd.read_csv("Users.csv")
    key = bytes.fromhex("47513459507931446361376559686c66394971506f4353725a34453846664354413155506f4f6e4a7755493d")
    fernet = Fernet(key)
    user_id = ""
    password = ""
    user_type = ""
    message = ""
    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")
        user_type = request.form.get("user_type")
    
    if user_type == "New User":
        if user_id == "":
            message = "User Id cannot be empty!"
        elif user_id in users_df["User ID"].values:
            message = "User Id already exists! Please try a different one."
        else: 
            enc_password = fernet.encrypt(password.encode())
            users_df = users_df.append({"User ID": user_id, "Password": enc_password.decode(), "Genre":""}, ignore_index = True)
            users_df.to_csv("Users.csv", index = False)
            message = "User details have been saved successfully!"
            # return redirect(url_for("afterFirstLogin", user_id = user_id))
    elif user_type == "Existing User":
        user_list = users_df.index[users_df["User ID"] == user_id].tolist()
        if user_id == "":
            message = "User Id cannot be empty!"
        elif len(user_list) == 0:
            message = "Invalid user name!"
        elif password != fernet.decrypt(users_df.iloc[user_list[0]]["Password"].encode()).decode():
            message = "Invalid password!"
        else:
            userChoice_list = str(users_df.iloc[user_list[0]]["Genre"])
            # print(userChoice_list)
            if userChoice_list=="nan":
                return redirect(url_for("afterFirstLogin", user_id = user_id))
            else:
                return redirect(url_for("userHomePage", user_id = user_id, userChoice_list=userChoice_list))     
    return render_template("loginPage.html", message = message)

@app.route("/afterFirstLogin/<user_id>", methods = ["GET", "POST"])
def afterFirstLogin(user_id):
    # print("login page started")
    if request.method == 'POST':
        glist = request.form.getlist("checkbox")
        g = ', '.join(glist)
        users_df = pd.read_csv("Users.csv")
        user_list = users_df.index[users_df["User ID"] == user_id].tolist()
        users_df.iloc[user_list[0]]["Genre"] = g
        users_df.to_csv("Users.csv", index = False)
        return redirect(url_for("userHomePage", user_id = user_id, userChoice_list=g))
    else:    
        genre_ls = ['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western', '\\N']
        
        msg = "Please Select Genre"
    return render_template("afterFirstLogin.html", msg = msg, user_id = user_id, genre_ls = genre_ls)


@app.route("/userHomePage/<user_id>/userChoice_list=<userChoice_list>", methods = ["GET", "POST"])
def userHomePage(user_id, userChoice_list=""):
    # print("user Home page started")
    msg = userChoice_list
    sel_gen = userChoice_list.split(', ')
# #     sel_gen = ['Action', 'Adventure', 'Horror', 'Thriller']
    print(sel_gen)
    imdb_score = 10
    no_of_reco = 5
    test_point = [1 if genre in sel_gen else 0 for genre in genres]
#     print(test_point)
    test_point.append(imdb_score)
    test_point.append(date.today().year)
    print(test_point)
    table = KNN_Movie_Recommender(test_point, no_of_reco)
    for movie, titleid, ratings, startDate in table:
        print(str(movie)+" "+str(titleid)+" "+ str(ratings)+" "+str(startDate))
    
    recoms = []
    # Creating an instance of the Cinemagoer class
    ia = Cinemagoer()

    # Getting movie by IMDb ID
    #('0468569')
    for r in table:
        show_id = r[1][2:] 
        show_details = ia.get_movie(show_id)
        rec_keys = show_details.keys()
        # print(rec_keys)
        
        title=""
        year=str(r[3])
        cover_url="\static\images\default_cover.jpeg"
        director=""
        s_genres=""
        plot_outline="Plot not found for this series!"
        rating=str(r[2])
        
        if 'title' in rec_keys:
            title = show_details['title']
        if 'year' in rec_keys:
            year = str(show_details['year'])
        if 'full-size cover url' in rec_keys:
            cover_url = show_details['full-size cover url']
        elif 'cover url' in rec_keys:
            cover_url = show_details['cover url']
        if 'directors' in rec_keys:
            director = str(show_details['directors'])
        elif 'director' in rec_keys:
            director = str(show_details['director'])
        if 'genres' in rec_keys:
            s_genres = " ".join(show_details['genres'])
        if 'plot outline' in rec_keys:
            plot_outline = show_details['plot outline']
        elif 'plot' in rec_keys:
            plot_outline = " ".join(show_details['plot'])
        if 'rating' in rec_keys:
            rating = str(show_details['rating'])
            
        print(rating)
        print(title)
        recoms.append(( title, year, cover_url, director, s_genres, plot_outline, rating))
    
    # return app.response_class(stream_template("userHomePage.html", msg=msg, recommendations = recoms, user_id = user_id))
    # print('table started')
    # print(recoms)
    # print('table ended')
    # rows = iter_all_rows()
    # return app.response_class(stream_template("userHomePage.html", msg=msg, recommendations = recoms, user_id = user_id))
    return render_template("userHomePage.html", msg=msg, recommendations = recoms, user_id = user_id)



@app.route("/homePage", methods = ["GET", "POST"])
def homePage():
    recoms = []
    if request.method == 'POST':
        sel_movie = request.form.get("sel_movie")
        # year
        # imdb_score = 9
        no_of_reco = request.form.get("no_of_reco")
        print(sel_movie)
        # print("selected_movie")
        # print(sel_movie)
        # print("records")
        # print(no_of_reco)
        # print("home page started")
        # print("selected_movie2=",sel_movie)
        # print("records2=",no_of_reco)
        test_points = data[movies.index(sel_movie)]
        table = KNN_Movie_Recommender(test_points, int(no_of_reco)+1)

        for movie, titleid, ratings, startDate in table:
            print(str(movie)+" "+str(titleid)+" "+ str(ratings)+" "+str(startDate))

        # Creating an instance of the Cinemagoer class
        ia = Cinemagoer()

        # Getting movie by IMDb ID
        #('0468569')
        for r in table:
            print(r)
            if r[0]==sel_movie:
                continue
            show_id = r[1][2:] 
            show_details = ia.get_movie(show_id)
            rec_keys = show_details.keys()
            # print(show_details.values())
            
            title=""
            year=str(r[3])
            cover_url="\static\images\default_cover.jpeg"
            director=""
            s_genres=""
            plot_outline="Plot not found for this series!"
            rating=str(r[2])
            
            if 'title' in rec_keys:
                title = show_details['title']
            if 'year' in rec_keys:
                year = str(show_details['year'])
            if 'full-size cover url' in rec_keys:
                cover_url = show_details['full-size cover url']
            elif 'cover url' in rec_keys:
                cover_url = show_details['cover url']
            if 'directors' in rec_keys:
                director = str(show_details['directors'])
            elif 'director' in rec_keys:
                director = str(show_details['director'])
            if 'genres' in rec_keys:
                s_genres = " ".join(show_details['genres'])
            if 'plot outline' in rec_keys:
                plot_outline = show_details['plot outline']
            elif 'plot' in rec_keys:
                plot_outline = " ".join(show_details['plot'])
            if 'rating' in rec_keys:
                rating = str(show_details['rating'])
            
            print(rating)
            print(title)
            recoms.append((title, year, cover_url, director, s_genres, plot_outline, rating))
    
    return render_template("homePage.html", recommendations=recoms, movies=sorted_movies)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5013)

