#!/usr/bin/python
# apatchy frontend
# (c) spv 2020
# gpl v2

import sys, os
import libapatchy

PATH_1 = sys.argv[1]
PATH_2 = sys.argv[2]

if sys.version_info[0] == 3:
	raw_input = input

print("would you like to use experimental pre-patches for speeding up the process and possibly more stability? (this is recommended on cellular devices)")
willUsePrePatches = raw_input("y/n? ")
print("would you like to enable debug output?")
debugOutput = raw_input("y/n? ")
if willUsePrePatches[0] == "y" or willUsePrePatches[0] == "Y":
    willUsePrePatches = True
else:
    willUsePrePatches = False
if debugOutput[0] == "y" or debugOutput[0] == "Y":
    debugOutput = True
else:
    debugOutput = False


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
	os.mkdir("enjb")
	os.mkdir("dajb")
except FileExistsError:
	pass
except:
	print("error")


libapatchy.patch(PATH_1, PATH_2, "dajb/", "enjb/")

os.system("cd enjb/ && tar -cf enjb.tar * && mv enjb.tar ..")
os.system("cd dajb/ && tar -cf dajb.tar * && mv dajb.tar ..")
