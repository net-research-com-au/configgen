import os, sys, time
import mactools

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
main_run()
end = time.time()
totaltime = end - start
print("Start time = ", startft)
print("end time = ", time.strftime("%d-%m-%y %H:%M:%S %p", time.localtime()))
print("Run time is ", start, end, totaltime)
