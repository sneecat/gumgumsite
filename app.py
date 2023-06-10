from flask import Flask, render_template, request, url_for, redirect
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
app = Flask(__name__)


class Project:
    def __init__(self, name, link, coverimage, ):
        self.name = name
        self.link = link
        self.coverimage = coverimage


yaejiFG = Project("Yaeji - For Granted", "#", "/static/images/for_granted_cover.jpg")
boogie = Project("Big Room Boogie", "#", "/static/images/boogie_cover.jpg")
project_list = [yaejiFG, boogie]


@app.route("/")
def index():
    return render_template("homepage.html", projects=project_list)


@app.route("/<project_name>")
def project_view(project_name):
    print("project name")
    print(str(project_name))
    for project in project_list:
        print(project.name)
        if str(project_name) == project.name:
            return render_template("project_page.html", target_project=project)


if __name__ == "__main__":
    app.run(debug=True)
