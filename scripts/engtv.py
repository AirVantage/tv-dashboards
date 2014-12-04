from flask import Flask, request, send_file, jsonify
from jira.client import JIRA
import sys
from datetime import datetime
from dateutil import parser

webserver = Flask(__name__)
jira_login = ""
jira_password = ""
counter = {}

@webserver.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return send_file('www/login.html')
    else:
        global jira_login
        global jira_password
        jira_login = request.form['jira_login'].strip()
        jira_password = request.form['jira_password'].strip()
        log("logged as: " + jira_login)
        return send_file('www/index.html')

@webserver.route("/engtv")
def index():
    return send_file('www/index.html')

@webserver.route("/counters")
def counters():
    global counter
    return jsonify(counter)

@webserver.route("/update")
def update():
    update_counters()
    return send_file('www/index.html')

def log(message):
    # write to stderr as flask is handling stdout
    sys.stderr.write(str(message) + "\n")

def update_counters():
    global jira_login
    global jira_password
    if jira_login != "":
        log("About to update counters...")
        jira = JIRA(options = {'server': 'https://issues.sierrawireless.com/', 'verify': False}, basic_auth=(jira_login, jira_password))
        jql = 'project = PLTBUGS AND type = Bug AND status in (Open, Reopened, Incomplete)'
        page_size = 100
        result_count = page_size
        total_open_bugs = 0
        oldest_update = "9999-99-99"
        oldest_update_key = ""
        start_at = 0
        global counter
        counter['labels'] = {}
        counter['total'] = {}
        while result_count == page_size:
            issues = jira.search_issues(jql, expand="changelog", fields="priority,labels,updated", startAt=start_at, maxResults=page_size)
            result_count = len(issues)
            start_at += page_size
            total_open_bugs += result_count
            for issue in issues:
                priority = issue.fields.priority.name
                if priority not in counter['total']:
                    counter['total'][priority] = 0
                counter['total'][priority] += 1
                labels = issue.fields.labels
                for label in labels:
                    if label not in counter['labels']:
                        counter['labels'][label] = {}
                    if priority not in counter['labels'][label]:
                        counter['labels'][label][priority] = 0
                    counter['labels'][label][priority] += 1
                updated = issue.fields.updated
                if str(updated) < oldest_update:
                    oldest_update = str(updated)
                    oldest_update_key = issue.key
        counter["open_bugs"] = total_open_bugs
        now = datetime.today()
        diff = now - parser.parse(oldest_update[:19])
        counter["last_update_of_counters"] = now 
        counter["oldest_update"] = str(diff.days) + " days" 
        counter["oldest_update_key"] = oldest_update_key 
        counter["open_bugs_blocker_critical"] = 0
        if counter['total'].has_key('Blocker'):
            counter["open_bugs_blocker_critical"] += counter['total']['Blocker']
        if counter['total'].has_key('Critical'):
            counter["open_bugs_blocker_critical"] += counter['total']['Critical']
        log("counters updated: %d open bugs" % total_open_bugs)

if __name__ == '__main__':
    webserver.config["CACHE_TYPE"] = "null"
    webserver.run(host='0.0.0.0', port=int('8080'))
