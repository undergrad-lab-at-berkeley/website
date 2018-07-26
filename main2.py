import os
from flask import Flask, render_template, url_for, redirect, request
from flask import abort
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
    return render_template("index.html", labs=content.labs, lab_ordering=content.lab_ordering)

@app.route("/about")
def about():
    founders = content.founders
    for name in founders:
        if founders[name]['img']:
            founders[name]['img'] = url_for('static', filename=founders[name]['img'])
        else:
            founders[name]['img'] = url_for('static', filename='img/temp_pic.png')

    advisors = content.advisors
    for name in advisors:
        if advisors[name]['img']:
            advisors[name]['img'] = url_for('static', filename=advisors[name]['img'])
        else:
            advisors[name]['img'] = url_for('static', filename='img/temp_pic.png')

    team = content.team

    for name in team:
        if team[name]['img']:
            team[name]['img'] = url_for('static', filename=team[name]['img'])
        else:
            team[name]['img'] = url_for('static', filename='img/temp_pic.png')

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