import content

from flask import Flask, render_template, url_for, redirect, request, abort
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import argon2
from api import oauth2
import handler
import json
import google.oauth2.credentials


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tokens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'dev'

db = SQLAlchemy(app)

class Credential(db.Model):
    email = db.Column(db.String(254), primary_key=True)
    access_token = db.Column(db.String(120), unique=True, nullable=False)
    refresh_token = db.Column(db.String(45), unique=True, nullable=False)

def update(cred):
    item = Credential.query.get(cred.email)
    if item:
        db.session.delete(item)
        db.session.add(cred)
    else:
        db.session.add(cred)
    db.session.commit()

navProjects = [
    {
        "url": "/projects/{}".format(x),
        "name": content.research[x]["navbar"]
    } for x in content.research
][1:]

navLabs = [
    {
        "url": "/projects/{0}-ulab".format(content.labs[x]["short_name"]),
        "app-url": "/labs/{}".format(content.labs[x]["short_name"]),
        "name": content.labs[x]["full_name"]
    } for x in content.labs
][:]

# cache useful info to prevent reloading
projects = dict()
labs = dict()
founders = None
advisors = None
team = None

@app.context_processor
def utility_processor():
    return dict(navProjects=navProjects)

@app.context_processor
def utility_processor1():
    return dict(navLabs=navLabs)

@app.route("/")
def index():
    return render_template("main-page.html")

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

@app.route("/software-jobs")
@app.route("/software-jobs/<category>")
def getSoftware(category="ATG"):
    return render_template("software-jobs.html", software_jobs=content.software_jobs, jobCategory=category)


@app.route("/corporate-jobs")
@app.route("/corporate-jobs/<category>")
def getCorporate(category="ATG"):
    return render_template("corporate-jobs.html", corporate=content.corporate, jobCategory=category)

@app.route("/lab")
@app.route("/lab/<name>")
@app.route("/lab/<name>/<category>")
@app.route("/labs")
@app.route("/labs/<name>")
@app.route("/labs/<name>/<category>")
def lab(name="placeholder", category = "Lab Management"):
    global labs
    if name not in labs:
        labs[name] = content.labs[name].copy()
    #     labs[name]['img'] = url_for('static', filename=labs[name]['img'])
    return render_template("labs.html", lab_jobs=labs[name], jobCategory=category)

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
def getJobs():
    return render_template("job-landing-page.html", labs=content.labs)

@app.route("/lab-jobs")
@app.route("/lab-jobs/<name>")
def getTabs(name = "aerospace"):
    global labs
    if name not in labs:
        labs[name] = content.labs[name].copy()
    return render_template("tabs.html", lab_name=name, lab_jobs=labs[name])

@app.route("/join-page")
@app.route("/join-page/<category>")
def getJoin(category="1st Year"):
    f=open("log.txt",'w')
    f.write("banana \n" )
    f.close()
    return render_template("join-page.html", join=content.join_info, jobCategory=category, joinOrder=content.join_infoOrder)

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

# Handling post requests for service engine
@app.route("/service-engine", methods = ['GET', 'POST'])
def service_handler():
    if request.method == 'GET':
        return render_template("404.html"), 204
    else:
        auth = request.authorization
        if auth.username == "gform" and argon2.verify(auth.password, '$argon2i$v=19$m=512,t=2,p=2$YiyltJby3jvnnBMipPQeow$p9gD0N2ALbdOspN9IMFM9g'):
            data = request.get_json()
            handler.handle(data)
            return render_template('404.html'), 204
        else:
            abort(401)

@app.route("/oauth2callback/<service>")
def auth_callback(service=None):
    if not service:
        return render_template('404.html'), 204
    credentials, email = oauth2.finish_auth(service)
    cred = Credential(email=email, refresh_token=credentials.refresh_token)
    update(cred)
    return redirect(url_for('index'))

@app.route("/auth/<service>")
def auth_service(service=None):
    if not service:
        return render_template('404.html'), 204
    return oauth2.begin_auth(service)

@app.route("/test")
def test():
    from api import gmailAPI as gmail
    cred = Credential.query.get('eucbital@berkeley.edu')
    if not cred:
        abort(404)

    with open('api/client_secret.json') as json_data:
        d = json.load(json_data)

    client_id = d["web"]["client_id"]
    client_secret = d["web"]["client_secret"]
    token_uri = d["web"]["token_uri"]

    credentials = google.oauth2.credentials.Credentials(
        None,
        refresh_token=cred.refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri=token_uri)

    gmail.send_email('eucbital@berkeley.edu', 'eucbital@berkeley.edu', 'i hate you', 'end thyself', credentials)
    abort(404)

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
