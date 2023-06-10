from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
app = Flask(__name__)


class Project:
    def __init__(self, name, link, coverimage):
        self.name = name
        self.link = link
        self.coverimage = coverimage


yaejiFG = Project("Yaeji - For Granted", "#", "/static/images/for_granted_cover.jpg")
boogie = Project("boogie", "#", "/static/images/boogie_cover.jpg")
project_list = [yaejiFG, boogie]


@app.route("/")
def index():
    return render_template("homepage.html", projects=project_list)


@app.route("/sendmail/", methods=["POST"])
def sendemail():
    if request.method == "POST":
        name = request.form["name"]
        subject = request.form["Subject"]
        email = request.form['_replyto']
        message = request.form['message']


if __name__ == "__main__":
    app.run(debug=True)
