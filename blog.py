#!/usr/bin/env python

from flask import Flask, url_for

app = Flask(__name__)

titles = ["First post", "Second Post"]

posts = ["hello this is a test post", "hello this is my second post"]

# /post/1/
@app.route("/post/<n>")
def show_post(n):
    try:
        post = ""
        post += titles[int(n) - 1] + "<br />\n" + "_________" + "<br />\n" +  posts[int(n) - 1]
        return post
    except IndexError:        
	return "post does not exist!"

@app.route("/")
def list_posts():
    html = ""
    for i in range(len(titles)):
        title = titles[i]
        html += '<a href="/post/' + str(i+1) + '">' + title + '</a><br />\n'
    return html

app.run(debug=True)


    
