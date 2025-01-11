from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    name = "Sahil"
    return render_template('index.html', random_number=random_number, current_year=current_year, name=name)


@app.route('/guess/<name>')
def guess(name):
    name = name.capitalize()
    response_age = requests.get(f"https://api.agify.io?name={name}")
    age = response_age.json().get("age")

    response_gender = requests.get(f"https://api.genderize.io?name={name}")
    gender = response_gender.json().get("gender")

    print(age)
    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c1ed661c59aa87c9b59f"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == '__main__':
    app.run(debug=True)