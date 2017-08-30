import os, sys, time
import mactools


def splitcsvlist(self, *args):
    """ Summary: loads csv data from file to a list.

    Description:
    opens the file and read all the lines and stores it in a list
    and returns below details in a list from the file
    [['vlan', 'mac address', 'type', 'switch port'],
    ['vlan', 'mac address', 'type', 'switch port'],....]

    Syntax: splitcsvlist("filename.ext")

    """
    # Validation check if the filename was provided to function
    # print("lenght of function args is =",len(args),args)

    if len(args) <= 0:
        return("No input file provided")

    else:
        in_datafile = args[0]

    # print("Input file name --> ", in_datafile)

    maclist = []  # Empty list to store the mac address list from the source.
    try:
        # gerr = load_datafile("README.md","-delcn")
        print(in_datafile)
        gerr = mactools.load_datafile(in_datafile, "-delcn")
    except IndexError:
        print("Index error at end")
    else:
        cnt = 0
        for val in gerr:
            print(val)
            # maclist.append(val.split(',')

    #return maclist
# end mac_add_list()


def main_run():
    """ summary: this is the main function

    call this from the program

    """

    try:
        # gerr = load_datafile("README.md","-delcn")
        macadd = mactools.load_datafile(sys.argv[1],"-delcn")
    except IndexError:
        print("Index error at end: No argument provided")
    else:
        print(macadd)
        print("Vlan\tMac Address\tType\tPorts\tVendor Oui")
        for macl in macadd:
            # print(macl[1].replace(".", ""))  # remove the . in mac address abcd.abcd.abcd
            # print("\t".join(macl), "\t", mac_oui_get(macl[1].replace(".", "")))
            print("line: ", macl)
        print("mac count is ", len(macadd))
# end main_run()

start = time.time()
startft = time.strftime("%d-%m-%y %H:%M:%S %p", time.localtime())

#totaltime = timeit.timeit("main_run()",setup="main_run", number=1)
#main_run()
a = splitcsvlist(sys.argv[1])
print(sys.argv[1],a)
end = time.time()
totaltime = end - start
print("Start time = ", startft)
print("end time = ", time.strftime("%d-%m-%y %H:%M:%S %p", time.localtime()))
print("Run time is ", start, end, totaltime)
