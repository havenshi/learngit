#!/usr/bin/env python
import os
from collections import defaultdict
from datetime import datetime
from urllib   import urlretrieve
from urlparse import urljoin
from zipfile  import ZipFile

import pytz # pip install pytz

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
                for city in [name, asciiname] + alternatenames.split(b','):
                    city = city.decode('utf-8').strip()
                    if city:
                        city2tz[city].add(timezone)

print("Number of available city names (with aliases): %d" % len(city2tz))

#
n = sum((len(timezones) > 1) for city, timezones in city2tz.iteritems())
print("")
print("Find number of ambigious city names\n "
      "(that have more than one associated timezone): %d" % n)

#
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
city = "Zurich"
for tzname in city2tz[city]:
    now = datetime.now(pytz.timezone(tzname))
    print("")
    print("%s is in %s timezone" % (city, tzname))
    print("Current time in %s is %s" % (city, now.strftime(fmt)))