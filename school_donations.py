from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson import json_util

app = Flask(__name__)

MONGOD_HOST = 'localhost'
MONGOD_PORT = 27017
#DBS_NAME = 'donorsUSA'
#COLLECTION_NAME = 'projects'
DBS_NAME = 'heroku_xcm7j7hz'
COLLECTION_NAME = 'opendata_projects_clean'
MONGO_URI = 'mongodb://root:clareoc2014@ds019143.mlab.com:19143/heroku_xcm7j7hz'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False
          }


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/donorsUS/projects")
def donor_projects():
    connection = MongoClient(MONGO_URI)
    #connection = MongoClient(MONGOD_HOST, MONGOD_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=20000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects


if __name__ == '__main__':
    app.run(debug=True)
