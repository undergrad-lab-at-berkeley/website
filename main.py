import os
from flask import Flask, render_template, url_for, redirect
import content
# from api import googleSheetAPI as sheetAPI

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

navProjects = [
    {
        "url": "/projects/{}".format(x),
        "name": content.research[x]["navbar"]
    } for x in content.research
][1:]

# cache useful info to prevent reloading
projects = dict()
founders = None
advisors = None
team = None

@app.context_processor
def utility_processor():
    return dict(navProjects=navProjects)

@app.route("/")
def index():
    return render_template("main-page.html")

@app.route("/join-page")
@app.route("/join-page/<category>")
def getJoin(category="1st Year"):
    print(category)
    return render_template("join-page.html", join=content.join, jobCategory=category)

@app.route("/aboutus")
def aboutus():
    global founders
    if not founders:
        founders = content.founders.copy()
        for name in founders:
            founders[name]['img'] = url_for('static', filename=founders[name]['img'])

    global advisors
    if not advisors:
        advisors = content.advisors.copy()
        for name in advisors:
            advisors[name]['img'] = url_for('static', filename=advisors[name]['img'])

    global team
    if not team:
        team = content.team.copy()
        for name in team:
            team[name]['img'] = url_for('static', filename=team[name]['img'])

    return render_template("aboutus.html", founders=founders, advisors=advisors, team=team, foundersOrder=content.foundersOrder)

@app.route("/new-student")
@app.route("/new-student/<category>")
def getStudent(category="Statistical Modeling and Deep Learning"):
    return render_template("new-student.html", student=content.student, jobCategory=category)

@app.route("/corporate-jobs")
@app.route("/corporate-jobs/<category>")
def getCorporate(category="ATG"):
    return render_template("corporate-jobs.html", corporate=content.corporate, jobCategory=category)

@app.route("/project")
@app.route("/project/<name>")
@app.route("/projects")
@app.route("/projects/<name>")
def project(name="placeholder"):
    global projects
    if name not in projects:
        projects[name] = content.research[name].copy()
        projects[name]['img'] = url_for('static', filename=projects[name]['img'])
    return render_template("projects.html", content=projects[name])

@app.route("/ulab-jobs")
@app.route("/jobs/<category>")
def getJobs(category="Computer Science"):
    return render_template("job-board.html", jobs=content.jobs, jobCategory=category)

@app.route("/bootcamp")
def bootcamp():
    global founders
    if not founders:
        founders = content.founders.copy()
        for name in founders:
            founders[name]['img'] = url_for('static', filename=founders[name]['img'])

    global advisors
    if not advisors:
        advisors = content.advisors.copy()
        for name in advisors:
            advisors[name]['img'] = url_for('static', filename=advisors[name]['img'])

    global team
    if not team:
        team = content.team.copy()
        for name in team:
            team[name]['img'] = url_for('static', filename=team[name]['img'])

    return render_template("bootcamp.html", founders=founders, advisors=advisors, team=team, foundersOrder=content.foundersOrder)

##################### Error Handling #####################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

#################### Main App #####################
if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)
