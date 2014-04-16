from jira.client import JIRA
from datetime import datetime
from dateutil import parser
from json import dump
from jira_credentials import jira_login,jira_password

jira = JIRA(options = {	'server': 'https://issues.sierrawireless.com/'}, basic_auth=(jira_login,jira_password))

page_size = 100
result_count = page_size
start_at = 0
counter = {}
counter['labels'] = {}
counter['total'] = {}
while result_count == page_size:
    issues = jira.search_issues('project = PLTBUGS AND type = Bug AND status in (open, Reopened, Incomplete)', 
        expand="changelog", startAt=start_at, maxResults=page_size)
    result_count = len(issues)
    start_at += page_size
    
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
with open('counters.json', 'w') as outfile:
    dump(counter, outfile)