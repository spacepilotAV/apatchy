#!/usr/bin/python

import sys, os
import libapatchy

PATH_1 = sys.argv[1]
PATH_2 = sys.argv[2]

raw_input = input

print("would you like to use experimental pre-patches for speeding up the process and possibly more stability? (this is recommended on cellular devices)")
yon = raw_input("y/n? ")
print("would you like to enable debug output?")
dyon = raw_input("y/n? ")
if yon[0] == "y" or yon[0] == "Y":
    yon = True
else:
    yon = False
if dyon[0] == "y" or dyon[0] == "Y":
    dyon = True
else:
    dyon = False


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



if yon:
    prepatch(PATH_1)
    prepatch(PATH_2)

os.mkdir("enjb")
os.mkdir("dajb")


libapatchy.patch2d(PATH_1, PATH_2, "dajb", "enjb")

os.system("cd enjb/ && tar -cf enjb.tar * && mv enjb.tar ..")
os.system("cd dajb/ && tar -cf dajb.tar * && mv dajb.tar ..")
