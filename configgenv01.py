import os
import sys
import time
import re
import mactools


def splitcsvlist(*args):
    """ Summary: loads csv data from file and then converts it to a list of lists.

    Description:
    opens the file and read all the lines and stores it in a list.
    Returns csv rows in a list from the list of lists.
    Example:
    Input information: <input a file name>
    col1, col2, col3, col4
    col1, col2, col3, col4

    Output inforation: <list of lists>
    [['col1', 'col2', 'col3', 'col4'],
    ['col1', 'col2', 'col3', 'col4'],....]

    Syntax: splitcsvlist("filename.ext")

    """
    # Validation check if the filename was provided to function
    # print("lenght of function args is =",len(args),args)

    if len(args) <= 0:
        return("No input file provided")

    else:
        in_datafile = args[0]

    # print("Input file name --> ", in_datafile)

    outcsvlist = []  # Empty list to store the mac address list from the source.
    try:
        # gerr = load_datafile("README.md","-delcn")
        # print(in_datafile)
        gerr = mactools.load_datafile(in_datafile, "-delcn")
    except IndexError:
        print("Index error at end")
    else:
        cnt = 0
        # print("*** CSV List ***")
        for val in gerr:
            # print("line %d: " % cnt, val)
            outcsvlist.append(val.split(','))
            cnt = cnt + 1
    return outcsvlist
# end splitcsvlist()


def csvlisttodict(*args):
    """ Summary: loads csv list of lists and then converts it to a
    list of dictionaries with first row as the keys and rest as values.

    Description:
    opens the list of list and read all the rows and stores it in a list.
    The first row is converted to the keys of the resultant dictionary.
    The rest of the rows are added as list of key:value dictionary pairs.
    The function retunrs list of dictionaries.
    Example:
    Input information: <input a file name>
    [['Hcol1', 'Hcol2', 'Hcol3', 'Hcol4'],
    ['col1', 'col2', 'col3', 'col4'],
    ['col1', 'col2', 'col3', 'col4'],....]

    Output inforation: <list of lists>
    [{'Hcol1': 'col1', 'Hcol2': 'col2', 'Hcol3': 'col3', 'Hcol4': 'col4'},
    {'Hcol1': 'col1', 'Hcol2': 'col2', 'Hcol3': 'col3', 'Hcol4': 'col4'},....]

    Syntax: csvlistodict([csv listoflists])

    """
    # Validation check if the filename was provided to function
    # print("lenght of function args is =",len(args),args)

    if len(args) <= 0:
        return("No input file provided")

    else:
        srclistoflist = args[0]

    # print("Input file name --> ", srclistoflist)

    deslistoflist = []  # Empty list to store the mac address list from the source.

    listhead = srclistoflist.pop(0)   # store headings in the new list and remove the headings

    # listdata = []   # Empty list to cycle data in the input list

    # print(listhead)
    # print(srclistoflist)
    rowheadrange = range(0,len(listhead))

    for listline in srclistoflist:
        desdict = {} # Empty dictionary to dictonary
        for i in rowheadrange:
            desdict[listhead[i]]=listline[i]
            # print(listhead[i], listline[i])
        # print("dictrprint: ", desdict)
        deslistoflist.append(desdict)

    # print(deslistoflist)
    return deslistoflist
# end csvlisttodict()

def exectimer(runfun, *args):

    """ summary: this is a timer fuction to show the execution time of program.

    Call this function with the function name and arguments.
    The output will be a disctionary of start, end and total time.

    Syntax: exectimer(functionname, args)
    output: {'start':'start time', 'end':'end time', 'total':'total time'}

    """
    timerresulsts = {}  # Empty dictonary to work t
    debug = 'NO'  # debug settings
    timerresulsts['start'] = start = time.time()
    startft = time.strftime("%d-%m-%y %H:%M:%S %p", time.localtime())

    macadd = runfun( *args )
    timerresulsts['end'] = end = time.time()
    timerresulsts['total'] = totaltime = end - start
    # timerresulsts['start']=start

    if debug == "YES":
        print("Start time = ", startft)
        print("end time = ", time.strftime("%d-%m-%y %H:%M:%S %p", time.localtime()))
        print("Run time is ", start, end, totaltime)
    else:
        debug = "NO"
    return macadd, timerresulsts

# end exectimer()

def multireplace(string, replacements):
    """ summary: replace multiple patterns in a single pass.

    Given a string and a replacement map, it returns the replaced string.
    :param str string: string to execute replacements on
    :param dict replacements: replacement dictionary {'value to find': 'value to replace'}
    :rtype: str

    courtosey reference link: https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
    """
    # Place longer ones first to keep shorter substrings from matching where the longer ones should take place
    # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against the string 'hey abc', it should produce
    # 'hey ABC' and not 'hey ABc'
    # print(string, replacements)

    substrs = sorted(replacements, key=len, reverse=True)

    # Create a big OR regex that matches any of the substrings to replace
    regexp = re.compile('|'.join(map(re.escape, substrs)))

    # For each match, look up the new string in the replacements
    return regexp.sub(lambda match: replacements[match.group(0)], string)


def main_run():
    try:
        funcexec, timers = exectimer(csvlisttodict, a)
    except NameError:
        print("function name error: Function does not exist or name is wrong")
    else:
        print(funcexec, timers)
# end main_run()


# main_run()
# print(len(sys.argv))
if len(sys.argv) < 3:
    print("Error: Insuffient arguments")
    print("usage syntax: %s <configuration_template.file> <value_csv.file>" % sys.argv[0])
else:
    templatefilename = sys.argv[1]
    csvfilename = sys.argv[2]
    # print(templatefilename)
    a = splitcsvlist(templatefilename)
    # print(templatefilename,a)
    b = csvlisttodict(splitcsvlist(csvfilename))
    # print(a)
    # print(b)

    csvlength = len(b)
    for val in range(0, csvlength):
        # print(val,"=",b[val])
        # for i in range(0, len(a)):
        print("\n*** CSV line %d ***" % val)
        print("<----------------------->\n")

        for templateline in a:
                # print(templateline[0])
                out = multireplace(templateline[0], b[val])  # templateline is a 'list of list' hence index is used to extract the string
                print(out)

        print("\n!-----------------------!\n\n")
        # print("\n*** CSV line %d - END ***" % val)
