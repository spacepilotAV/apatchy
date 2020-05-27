#!/usr/bin/python
# apatchy frontend
# (c) spv 2020
# gpl v2

import sys, os
import libapatchy

PATH_1 = sys.argv[1]
PATH_2 = sys.argv[2]
OUT_1  = sys.argv[3]
OUT_2  = sys.argv[4]

if sys.version_info[0] == 3:
	raw_input = input

willUsePrePatches	= "--pre" in sys.argv
debugOutput		= "--debug" in sys.argv
makeTarPatches		= "--tar" in sys.argv

def prepatch(PATH):
    os.system("rm -rf " + PATH + "/Spotlight")
    os.system("rm -rf " + PATH + "/Assistant")
    os.system("rm -rf " + PATH + "/CoreDuet")
    os.system("rm -rf " + PATH + "/Carrier*")
    os.system("rm -rf " + PATH + "/Oper*")
    os.system("rm -rf " + PATH + "/Logs")
    os.system("rm -rf " + PATH + "/AggregateDictionary")
    os.system("rm -rf " + PATH + "/SMS")
    os.system("rm -rf " + PATH + "/Caches")



if willUsePrePatches:
    prepatch(PATH_1)
    prepatch(PATH_2)

try:
	os.mkdir(OUT_2)
	os.mkdir(OUT_1)
except FileExistsError:
	pass
except:
	print("error")


libapatchy.patch(PATH_1, PATH_2, OUT_1, OUT_2)

if makeTarPatches:
	os.system("cd " + OUT_2 + "/ && tar -cf " + OUT_2 + ".tar * && mv " + OUT_2 + ".tar ..")
	os.system("cd " + OUT_1 + "/ && tar -cf " + OUT_1 + ".tar * && mv " + OUT_1 + ".tar ..")
