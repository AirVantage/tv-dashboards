#!/bin/bash

/usr/bin/python get_bug_count.py
/usr/bin/python get_stash_metrics.py

/usr/bin/scp counters.json swir@zahia.anyware:/home/swir/Dev/platformdashboard/dashboardUI/scripts/
/usr/bin/scp stash.json  swir@zahia.anyware:/home/swir/Dev/platformdashboard/dashboardUI/scripts/

echo "zahia tv updated"