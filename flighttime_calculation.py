#!/usr/bin/env python
import os
from collections import defaultdict
from datetime import *
from urllib   import urlretrieve
from urlparse import urljoin
from zipfile  import ZipFile
import datetime
import time
import pytz
from Tkinter import *
import tkMessageBox

class flightTime:
    def findtz(self,city):
        geonames_url = 'http://download.geonames.org/export/dump/'
        basename = 'cities15000'
        filename = basename + '.zip'

        if not os.path.exists(filename):
            urlretrieve(urljoin(geonames_url, filename), filename)

        city2tz = defaultdict(set)
        with ZipFile(filename) as zf, zf.open(basename + '.txt') as file:
            for line in file:
                fields = line.split(b'\t')
                if fields:
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
        return ("Your flight time is: "+str(int(days))+" days "+str(int(hours))+" hours "+str(int(minutes))+" minutes")

class HavenButtons:
    def __init__(self,master):
        frame=Frame(master, width=300, height=250)
        frame.pack()

        self.label_ff = Label(frame, text="Enter the city and time (mm-dd-yyyy 24:00) you fly from", fg="blue")
        self.label_ft = Label(frame, text="Enter the city and time (mm-dd-yyyy 24:00) you fly to", fg="blue")
        self.label_1 = Label(frame, text="Fly from:")
        self.label_2 = Label(frame, text="Departure time:")
        self.label_3 = Label(frame, text="Fly to:")
        self.label_4 = Label(frame, text="Arrival time:")
        self.entry_1 = Entry(frame)
        self.entry_2 = Entry(frame)
        self.entry_3 = Entry(frame)
        self.entry_4 = Entry(frame)

        self.label_ff.grid(row=0, columnspan=2, sticky=W)
        self.label_1.grid(row=1, sticky=E)
        self.label_2.grid(row=2, sticky=E)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)

        self.label_ft.grid(row=3, columnspan=2, sticky=W)

        self.label_3.grid(row=4, sticky=E)
        self.label_4.grid(row=5, sticky=E)
        self.entry_3.grid(row=4, column=1)
        self.entry_4.grid(row=5, column=1)

        self.okButton = Button(frame, text="Ok", command=self.printMessage)
        self.okButton.pack(side=LEFT)
        self.okButton.grid(row=6, columnspan=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)
        self.quitButton.grid(row=6, column=1, columnspan=2)

    def printMessage(self):
        s = flightTime()
        content=s.ft(self.entry_1.get(), self.entry_2.get(), self.entry_3.get(), self.entry_4.get())
        tkMessageBox.showinfo("Show result", content)


root = Tk()
b=HavenButtons(root)
root.mainloop()