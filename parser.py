# -*- coding: utf-8 -*-

import linecache
import re




def parseInd (tupList):
	output = []
	i = 0
	for tupl in tupList:
		buff = (i, tupl[0], tupl[1])
		i += 1
		output.append(buff)
	return output

