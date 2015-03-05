TV dashboards
=============

Build it
-----

    sudo docker build -t closet:5000/engtv .

Run it
-----

As a standalone app:

    sudo docker run -d -p 8080:8080 --name="engtv" closet:5000/engtv

With a bash shell:

    sudo docker run -t -i -p 8080:8080 --name="engtv" closet:5000/engtv /bin/bash

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
2. Enter valid credentials (i.e. able to access the PLTBUGS JIRA project and Github AirVantage reposotories)
3. Rolling pages should shown total bug counts, blocker and critical bug counts and oldest update amongst open bugs, plus the count of open bugs on Github
4. Counters shoud be updated automatically every 5 minutes

One can view detailed counters at http://localhost:8080/counters
