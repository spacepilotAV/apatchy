#!/usr/bin/python

import sys, os
import libapatchy

PATH_1 = sys.argv[1]
PATH_2 = sys.argv[2]

if sys.version_info[0] == 3:
	raw_input = input

print("would you like to use experimental pre-patches for speeding up the process and possibly more stability? (this is recommended on cellular devices)")
exp_pre = raw_input("y/n? ")
print("would you like to enable debug output?")
debug = raw_input("y/n? ")
if exp_pre[0] == "y" or exp_pre[0] == "Y":
    exp_pre = True
else:
    exp_pre = False
if debug[0] == "y" or debug[0] == "Y":
    debug = True
else:
    debug = False


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



if exp_pre:
    prepatch(PATH_1)
    prepatch(PATH_2)

try:
	os.mkdir("enjb")
	os.mkdir("dajb")
except FileExistsError:
	pass
except:
	print("error")


libapatchy.patch(PATH_1, PATH_2, "dajb", "enjb")

os.system("cd enjb/ && tar -cf enjb.tar * && mv enjb.tar ..")
os.system("cd dajb/ && tar -cf dajb.tar * && mv dajb.tar ..")
