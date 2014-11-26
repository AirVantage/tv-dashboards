TV dashboards
=============

!!! WARNING !!!
-------

On-going containerization of engineering TV dashboard

Summary
-------

Theses pages are deployed on the R&D TV
The main page is teamtv.html that launches other pages cyclically. Two timeslots are dedicated to the display of bug counts during UI and API dailies.

Get started
-----------

1. Deploy these files on an web server directory
2. Accessing JIRA related dashboards requires an initial successful login on JIRA
3. Accessing SonarQube related pages requires an initial successful login on SonarQube
4. Then, from the TV screen, access <your server URI>/teamtv.html, e.g.: [R&D TV](http://zahia.anyware/dashboard/teamtv.html). Note that a blank page is displayed during the first 15 s.

Scripts
-------
Python scripts are providing TV web pages with data from JIRA (bug counts) and Stash (Pending pull-requests)
Required python libs are: `jira-python, pandas, python-dateutil, requests`
Both scripts import `jira_credentials.py` that MUST contain:
    jira_login='<YOUR JIRA LOGIN>'
    jira_password='<YOUR JIRA PASSWORD>'
