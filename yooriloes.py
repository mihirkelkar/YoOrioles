#!/usr/bin/python
def readSchedule():
  fp = open('orioles.date', 'r')
  dates = [ii.strip() for ii in fp.readlines()]
  print dates


readSchedule()  