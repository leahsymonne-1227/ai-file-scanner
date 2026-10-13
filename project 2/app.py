# Bring in the Flask tools this file uses.
from flask import Flask, render_template, request

# connection to the web app.
app = Flask(__name__)


# this is for flask to show it has access to the main page: /
@app.route("/")
# define is a function of finding the web app
def home():
    # define is for creating the function for what happens when someone does 
    #something on the homepage
    return render_template("data to google sheets.html")
# return is just something to check it's running
# render_template is because we have to put the main html, and all htmls in a template
#folder for flask to work 
#it also sends the page to the browser rather than it just being local

# Receive the form when its submit button is clicked.
@app.route("/submit-review", methods=["POST"])
#we use post as a way to say move the data away from the url
def submit_review():
    # Read each answer using the matching name from the HTML form.
    #make variables from the information on the form
    customer_name = request.form["customer_name"]
    product = request.form["product"]
    review = request.form["review"]

    # Show the answers in the terminal just to check it's working
    print(customer_name)
    print(product)
    print(review)

    # Send a confirmation back to the browser.
    return "Flask received your review!"
