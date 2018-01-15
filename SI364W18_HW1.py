## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

import requests
import json
from string import Template
import sys
from sys import stderr

def print_err(*args, **kwargs):
    print(*args, file=stderr, **kwargs)

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications.
## Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
app = Flask(__name__)
app.debug = True
@app.route('/')
def hello_to_you():
    return 'Hello'

@app.route('/class')
def welcome():
    return 'Welcome to SI 364!'



## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>'
##you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille',
## you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about
## the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different
## data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }

@app.route('/movie/<moviename>')
# def movie(moviename):
#     return '<h1>Welcome to {}</h1>'.format(moviename)

def get_itunes_data(moviename):# Get specifics of how to write this from knowledge about REST APIs in Python -- see textbook -- and iTunes API documentation
    baseurl = "https://itunes.apple.com/search?entity=movie&attribute=movieTerm"
    params_diction = {}
    params_diction["term"] = moviename
    resp = requests.get(baseurl,params=params_diction)
    text = resp.text
    python_obj = json.loads(text)
    return str(python_obj)
    # album_titles = []
    # for item in python_obj["results"]:
    #     album_titles.append(item) # This turns out where you find the album name in the nested data
    #     # all_titles = "<br>".join(album_titles) # join by the <br> tag, which means 'line break' in html#
    #     return str(album_titles)
    #     # return str(all_titles)#return a string -- must return a string to render on the page


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question,
##you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>".
##For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

@app.route('/question',methods=["GET","POST"])
def question():
    formstring = """<br>
    <form action="/question" method='POST'> <br>
    <input type="number" name="num"> Enter your favorite number: <br>
    <input type="submit" value="Submit">
    """
    if request.method == "POST":
        entered = request.form['num']
        entered_X2 = int(entered) * 2
        return 'Double your favorite number is {}'.format(str(entered_X2))
    else:
        return formstring

## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.




@app.route('/problem4form',methods=["GET","POST"])
def problem4():
    form2 = """<br>
    <form action="/problem4form" method='POST'> <br>
    Enter your name:<br>
    <input type="text" name="name"> <br> <br>
    Please choose Adele: <br>
    <input type="radio" name="option1" value="1"> I like Adele<br>
    <input type="radio" name="option2" value="2"> I like Beyonce<br><br>
    <input type="checkbox" name="option3" value="3"> I'm awesome!!<br><br>

    <input type="submit" value="Submit">
    """
    if request.method == "POST":
        name = request.form['name']
        # form23 = """"<form action="/problem4form" method='POST'> <br>You're so awesome {}".format(name)"""
        entered1 = request.form['option1']
        if entered1 == '1':
            return (""" <iframe src="https://www.youtube.com/embed/YQHsXMglC9A" width="853" height="480" frameborder="0" allowfullscreen></iframe>""") + "You are so awesome {}".format(name)
        # entered2 = request.form['option2']
        # if entered2 == '2':
        #     return (""" <iframe src="https://www.youtube.com/embed/jZVQD9piv7A" width="853" height="480" frameborder="0" allowfullscreen></iframe>""")
    #
    else:
        return form2


if __name__ == '__main__':
    app.run()
