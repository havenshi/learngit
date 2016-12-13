#!/usr/bin/env python
import os
from collections import defaultdict
from datetime import datetime
from urllib   import urlretrieve
from urlparse import urljoin
from zipfile  import ZipFile

import pytz # pip install pytz

# Step 1: find time zone from city
def findtz(city):
    geonames_url = 'http://download.geonames.org/export/dump/'
    basename = 'cities15000' # all cities with a population > 15000 or capitals
    filename = basename + '.zip'

    # get file
    if not os.path.exists(filename):
        urlretrieve(urljoin(geonames_url, filename), filename)

    # parse it
    city2tz = defaultdict(set)
    with ZipFile(filename) as zf, zf.open(basename + '.txt') as file:
        for line in file:
            fields = line.split(b'\t')
            if fields: # geoname table http://download.geonames.org/export/dump/
                name, asciiname, alternatenames = fields[1:4]
                timezone = fields[-2].decode('utf-8').strip()
                if timezone:
                    for acity in [name, asciiname] + alternatenames.split(b','):
                        acity = acity.decode('utf-8').strip()
                        if acity:
                            city2tz[acity].add(timezone)

    for tzname in city2tz[city]:
        now = datetime.now(pytz.timezone(tzname))
        return "%s" % (tzname)


# Step 2: get local flying time and convert to standard
fmt = '%m-%d-%Y %H:%M'
city1=findtz(raw_input("Fly from the city:"))
d1 = datetime.strptime(raw_input('Enter Departure Time in the format mm-dd-yyyy hour:minute:'), fmt)
city2=findtz(raw_input("Fly to the city:"))
d2 = datetime.strptime(raw_input('Enter Arrival Time in the format mm-dd-yyyy hour:minute:'), fmt)

import pytz, datetime
local1 = pytz.timezone (city1)
local1_dt = local1.localize(d1, is_dst=None)
utc1_dt = local1_dt.astimezone (pytz.utc)
local2 = pytz.timezone (city2)
local2_dt = local2.localize(d2, is_dst=None)
utc2_dt = local2_dt.astimezone (pytz.utc)


# Step 3: calculate difference
from datetime import datetime
import time
# convert to unix timestamp in seconds
d1_ts = time.mktime(utc1_dt.timetuple())
d2_ts = time.mktime(utc2_dt.timetuple())
elapsed = (d2_ts-d1_ts)/60

days=elapsed//(24*60)
hours=elapsed%(24*60)//60
minutes=elapsed%(24*60)%60
print ("The flight time is: "+str(int(days))+" days "+str(int(hours))+" hours "+str(int(minutes))+" minutes")


