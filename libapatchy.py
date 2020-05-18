# libapatchy
# light speed directory patchfinder
import os, sys

def patch2d(d1, d2, o1, o2):
    os.system("diff -rq " + d1 + " " + d2 + " > .tmpout")
    text = open(".tmpout", "r").read()
    for i in text.split("\n"):
        try:
            fn_e = i.split(" ")[3]
            fn_o = i.split(" ")[1]
            print("en " + fn_e)
            print("da " + fn_o)
            print("en " + "/".join(fn_e.split("/")[1:-1]))
            print("da " + "/".join(fn_o.split("/")[1:-1]))
            os.system("mkdir -p " + o2 + "/".join(fn_e.split("/")[1:-1]))
            os.system("cp " + fn_e + " " + o2 + "/" + "/".join(fn_e.split("/")[1:-1]))
            os.system("mkdir -p " + o1 + "/" + "/".join(fn_o.split("/")[1:-1]))
            os.system("cp " + fn_o + " " + o1 + "/".join(fn_o.split("/")[1:-1]))
        except:
            print(sys.exc_info())

