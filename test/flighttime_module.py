#!/usr/bin/env python
import os
from collections import defaultdict
from datetime import datetime
from datetime import *
from urllib   import urlretrieve
from urlparse import urljoin
from zipfile  import ZipFile
import pytz, datetime
import time
import pytz # pip install pytz

class flightTime:
    def findtz(self,city):
        geonames_url = 'http://download.geonames.org/export/dump/'
        basename = 'cities15000' # all cities with a population > 15000 or capitals
        filename = basename + '.zip'

        if not os.path.exists(filename):
            urlretrieve(urljoin(geonames_url, filename), filename)

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
            now = datetime.datetime.now(pytz.timezone(tzname))
            return "%s" % (tzname)


    def ft(self,data1,data2,data3,data4):
        fmt = '%m-%d-%Y %H:%M'
        city1=self.findtz(data1)
        d1 = datetime.datetime.strptime(data2, fmt)
        city2=self.findtz(data3)
        d2 = datetime.datetime.strptime(data4, fmt)


        local1 = pytz.timezone (city1)
        local1_dt = local1.localize(d1, is_dst=None)
        utc1_dt = local1_dt.astimezone (pytz.utc)
        local2 = pytz.timezone (city2)
        local2_dt = local2.localize(d2, is_dst=None)
        utc2_dt = local2_dt.astimezone (pytz.utc)


        d1_ts = time.mktime(utc1_dt.timetuple())
        d2_ts = time.mktime(utc2_dt.timetuple())
        elapsed = (d2_ts-d1_ts)/60

        days=elapsed//(24*60)
        hours=elapsed%(24*60)//60
        minutes=elapsed%(24*60)%60
        return ("The flight time is: "+str(int(days))+" days "+str(int(hours))+" hours "+str(int(minutes))+" minutes")


if __name__=="__main__":
    answer=flightTime()
    data1, data2, data3, data4 = "Beijing","12-14-2016 06:00","Seattle","12-13-2016 14:00"
    print answer.ft(data1,data2,data3,data4)