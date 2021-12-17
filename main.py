from flask import Flask, render_template, request
import requests
import smtplib
from os import environ

app = Flask(__name__)


blog_data_url = "https://api.npoint.io/7cbd26ff7358764fee64"
blog_response = requests.get(blog_data_url)
blog_data_json = blog_response.json()
test123 = "test"

@app.route('/')
def all_blog_posts():
    return render_template("index.html", blog_posts=blog_data_json)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<blog_id>')
def post_page(blog_id):
    return render_template("post.html", blog_id=blog_id, blog_posts=blog_data_json)


if __name__ == "__main__":
    app.run(debug=True)