from flask import Flask, render_template, request, url_for, redirect
import os
import re
import glob
from pathlib import Path
app = Flask(__name__)


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s


class Project:
    def __init__(self, title, project_id):
        self.title = title
        self.__create_link()
        self.project_id = project_id
        self.static_path = "/static/projects/{}".format(project_id)
        self.cover_image = self.static_path + "/cover.jpg"

    def __create_link(self):
        self.link = "/" + slugify(self.title)

    def image_paths(self):
        jpg_images = glob.glob1(os.getcwd() + self.static_path, "*.jpg")
        png_images = glob.glob1(os.getcwd() + self.static_path, "*.png")
        print(jpg_images + png_images)
        all_images = jpg_images + png_images
        all_images.remove("cover.jpg")
        return all_images


yaejiFG = Project("Yaeji - For Granted", "for_granted")
boogie = Project("Big Room Boogie", "big_room_boogie")
yaejiOneMore = Project("Yaeji One More Tour", "one_more")
project_list = [yaejiFG, boogie, yaejiOneMore]


@app.route("/")
def index():
    return render_template("homepage.html", projects=project_list)


@app.route("/<project_slug>")
def project_view(project_slug):
    for project in project_list:
        if str(project_slug) in project.link:
            return render_template("project_page.html", target_project=project, projects=project_list)


@app.route("/contact")
def contact_view():
    return render_template("contact_page.html", projects=project_list)


if __name__ == "__main__":
    app.run(debug=True)
