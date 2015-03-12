# -*- coding: utf-8 -*-

import linecache
import re


'''
def 
	f = open(dc.in,'r')
	lines = f.read().splitlines()
	f.close()
	return lines





def addId(tupleList):
	for tup in tupleList:
'''

ind = 0
def addIndex(tup):
	newtup = (ind, tup[0], tup[1])
	ind ++
	return newtup

def parser(stanArray):
	indexedEntry = map(addIndex, stanArray)
	return indexedEntry
