# libapatchy
# light speed directory patchfinder
# this needs to be cleaned up
import os, sys

def patch(dir1, dir2, out1, out2):
    os.system("diff -rq " + dir1 + " " + dir2 + " > .tmpout")
    output = open(".tmpout", "r").read()
    for i in output.split("\n"):
        try:
            fn_dir2 = i.split(" ")[3]
            fn_dir1 = i.split(" ")[1]
            print("dir2 " + fn_dir2)
            print("dir1 " + fn_dir1)
            print("dir2 " + "/".join(fn_dir2.split("/")[1:-1]))
            print("dir1 " + "/".join(fn_dir1.split("/")[1:-1]))
            os.system("mkdir -p " + out2 + "/".join(fn_dir2.split("/")[1:-1]))
            os.system("cp " + fn_dir2 + " " + out2 + "/" + "/".join(fn_dir2.split("/")[1:-1]))
            os.system("mkdir -p " + out1 + "/" + "/".join(fn_dir1.split("/")[1:-1]))
            os.system("cp " + fn_dir1 + " " + out1 + "/".join(fn_dir1.split("/")[1:-1]))
        except:
            print(sys.exc_info())
