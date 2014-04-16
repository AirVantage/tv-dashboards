#!/usr/bin/python

import pandas as pd
from pandas import Series
from pandas import DataFrame
import requests as requests
from pandas import datetime
from datetime import timedelta
from json import dump
from jira_credentials import jira_login,jira_password

r = requests.get('https://stash.sierrawireless.local/rest/api/1.0/projects/AVCLOUD/repos/airvantage/pull-requests?limit=1000',
    auth=(jira_login,jira_password), verify=False)

created=[]
updated=[]

for pullrequest in r.json()['values']:
    created.append(pullrequest['createdDate'])
    updated.append(pullrequest['updatedDate'])
    
df = DataFrame({'created':created,'updated':updated})
now = eval(datetime.now().strftime('%s')) * 1000
df['difftime'] = now - df['updated']
oldest_update = timedelta(milliseconds=int(df['difftime'][df['difftime'].idxmax()]))

status = {'in_progress': len(df), 'oldest': oldest_update.days}

with open('stash.json', 'w') as outfile:
    dump(status, outfile)