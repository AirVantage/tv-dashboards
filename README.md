TV dashboards
=============

Build it
-----

    # Image based on minideb:
    sudo docker build -t airvantage/tv-dashboards -f Dockerfile.minideb .
    # or based on alpine (default):
    sudo docker build -t airvantage/tv-dashboards -f Dockerfile .

Run it
-----

As a standalone app:

    sudo docker run -d -p 8080:8080 --name="engtv" airvantage/tv-dashboards

If docker version is >= 1.11, one can also limit the log file size and number:

    sudo docker run -d --log-driver=json-file --log-opt max-size=10m --log-opt max-file=10 -p 8080:8080 --name="engtv" airvantage/tv-dashboards

And with a bash shell:

    sudo docker run -t -i -p 8080:8080 --name="engtv" airvantage/tv-dashboards /bin/bash

Then

    cd /home/engtv
    ./engtv.sh

Summary
-------

This dashboard is based on revealjs with dynamic content retrieved and served by a python Flask application running on port 8080.
A valid access to JIRA is requested as well as an account on Github, thus the login page described below.

Get started
-----------

1. Access http://localhost:8080/login
2. Enter valid credentials (i.e. able to access the PLTBUGS and INCIDENT JIRA projects and Github AirVantage repositories)
3. Rolling pages should show total bug counts, blocker and critical bug counts, open incidents and oldest update amongst open bugs, plus the count of open bugs on Github
4. Counters shoud be updated automatically every 5 minutes

One can view detailed counters at http://localhost:8080/counters
