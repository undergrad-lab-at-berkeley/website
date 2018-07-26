import os
from flask import Flask, render_template, url_for, redirect, request
from flask import abort
from members import members
import content
import pdb

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

navLabs = []
for x in content.labs:
    if content.labs[x]["status"] == 'Active':
        navLabs.append({
            "url": "/labs/{}".format(x),
            "name": content.labs[x]["full_name"]
        })
for member in members:
    if not members[member]['img']:
        members[member]['img'] = 'img/temp_pic.png'

@app.route("/join-page")
@app.route("/labs/")
def labs():
    return render_template("labs.html", labs=content.labs)

@app.route("/labs/<name>")
def lab(name=None):
    if name in content.labs.keys():
        return render_template("lab.html", lab=content.labs[name])
    else:
        return render_template('404.html'), 404

@app.context_processor
def utility_processor1():
    return dict(navLabs=navLabs)

@app.route("/")
def index():
    return render_template("index.html", labs=content.labs, lab_ordering=content.labOrder)

@app.route("/about")
def about():
    founders = { name: members[name] for name in content.foundersOrder }
    advisors = { name: members[name] for name in content.advisorsOrder }
    team = { name: members[name] for name in content.teamOrder }
    return render_template("about.html", founders=founders, advisors=advisors, team=team, foundersOrder=content.foundersOrder)

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