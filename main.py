import os
from flask import Flask, render_template, url_for, redirect, request
from flask import abort
from members import members
import content
import pdb
# from flask_table import Table, Col, LinkCol

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
        members[member]['img'] = 'img/logos/logo_general.png'

# @app.route("/join-page")
# @app.route("/labs/")
# def labs():
#     return render_template("labs.html", labs=content.labs)

@app.route("/labs/<name>")
def lab(name=None):
    if name in content.labs.keys():
        # if "table" in content.labs[name]["content"]:
        #     items = [Item('Name1', 'Description1', 'google.com'),
        #     Item('Name2', 'Description2', 'google.com'),
        #     Item('Name3', 'Description3', 'google.com')]
        #     # Or, equivalently, some dicts
        #     items = [dict(name='Name1', description='Description1'),
        #     dict(name='Name2', description='Description2'),
        #     dict(name='Name3', description='Description3')]
        #     table = ItemTable(items)
        #     return render_template("lab.html", lab=content.labs[name], members=members, table=table)

        return render_template("lab.html", lab=content.labs[name], members=members)
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

##### TEMP PAGE FOR SP21 POSTER SESSION #####
@app.route("/poster-symposium-sp21")
def posters():
    posters = {
        'cogsci': {
            '[TBD]': "example.pdf",
        },
        'physics': {
            '[TBD]': "example.pdf",
            '[Example Poster]': "example.pdf"
        },
        'bio': {
            '[TBD]': "example.pdf"
        },
        'data': {
            '[TBD]': "example.pdf"
        },
        'compbio': {
            '[TBD]': "example.pdf"
        },
    }
    return render_template("posters-sp21.html", labs=content.labs, lab_ordering=content.labOrder, posters=posters)

##### TEMP PAGE FOR SP21 POSTER SESSION #####

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
