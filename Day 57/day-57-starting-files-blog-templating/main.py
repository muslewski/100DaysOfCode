from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    posts_url = "https://api.npoint.io/c1ed661c59aa87c9b59f"
    response = requests.get(posts_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<blog_id>")
def get_post(blog_id):
    posts_url = "https://api.npoint.io/c1ed661c59aa87c9b59f"
    response = requests.get(posts_url)

    all_posts = response.json()
    post = all_posts[int(blog_id) - 1]

    title = post["title"]
    body = post["body"]
    return render_template("post.html", title=title, body=body)


if __name__ == "__main__":
    app.run(debug=True)
