""" MAC address tools.

Information: python script to provide mac address tools for network egineers
Author: Dheep Balaraman
Language: python 3.x

features:-
    - Compare mac address to OUI vendor list and list mac-address and respective vendor
"""


#!/usr/bin

import sys
import re
import os

# Global function Definistions


def load_datafile(*args):
    """ Summary: loads data from file to a list.

    Description:
    opens the file and read all the lines and stores it in a list returns list
    Syntax: load_datafile("filename.ext","Options")
    Options:
    -delcn --> removes new line character or carriage return
    """
    # Validation check if the filename was provided to function
    # print("lenght of function args is =",len(args),args)

    if len(args) <= 0:
        return("No input file provided")

    else:
        in_datafile = args[0]

    print("Input file name --> ", in_datafile)

    # File validation
    try:
        out_linelist = open(in_datafile, "r")
    except FileNotFoundError:
        return in_datafile + " --> file not found"
    except IOError:
        return in_datafile + " --> unable to open file"

    print("Importing lines from --> ", in_datafile)
    out_linelist.seek(0)

    var_out_rawlist = out_linelist.readlines()
    out_linelist.close()

    # create a dummy list for nomalised output
    var_out_normlist = list(range(0, len(var_out_rawlist)))

    # print(type(var_out_normlist))

    try:
        if args[1] == "-delcn":
            print("Option: Remove new line/carriage return")
            for i in range(0, len(var_out_rawlist)):
                var_out_normlist[i] = var_out_rawlist[i].rstrip("\n|\r")

            var_outlist = var_out_normlist

    except IndexError:
        print("No options provided")
        var_outlist = var_out_rawlist

    print("....*** DONE ***\nLine count = ", len(var_outlist), "\n\n")
    # Return the mac address table list
    return var_outlist

# end load_datafile()

def loadoui_file(*args):
    """ Summary: loads mac oui list from file to a dictionary.

    Description:
    import oui csv to dictionary (instead of comma '=' is used as separator
    due to conflict with comma in vendor names)

    Syntax: loadoui_file("filename.ext","Options")
    Defaults:
    if no file name is given then default file is oui_base16_eqseperator.dat

    """

    #
    # print "lenght of function args is =",len(args)

    if len(args) <=0 :
        oui_base16_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "oui_base16_eqseperator.dat") # default file is oui_base16_eqseperator.dat
    else:
        oui_base16_file = args[0]

    print("Importing OUI list from --> ",oui_base16_file)

    file_oui16 = open(oui_base16_file, "r", encoding='utf8')
    file_oui16.seek(0)

    oui16 = file_oui16.readlines()
    # oui16 = load_datafile(oui_base16_file.join("encoding='utf8'"))
    file_oui16.close()

    mac_oui_dict = {}   # creat dummy dictonary to store OUI vendor list

    ouiprefix = list(range(0, len(oui16)))
    ouivendor = list(range(0, len(oui16)))

    for i in list(range(0, len(oui16))):
        ouiprefix[i], ouivendor[i] = (oui16[i].rstrip("\n")).split("=")
        mac_oui_dict[ouiprefix[i].lower()] = ouivendor[i]  # Normalising the oui names to lowercase

    print("....*** DONE ***\nMAC vendor count = ", len(mac_oui_dict), "\n\n")

    # Return the OUI vendor dictonary
    return mac_oui_dict

# end loadout_file()

class mactools:
    """ mactools class.

    summary:  to provide tools to deal with mac addresses from cisco switch
    """

    oui_source_file = "oui_base16_eqseperator.dat"

    def __init__(self):
        self.mac_oui_db = loadoui_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.oui_source_file))
    # end constructor __init__()

    def mac_add_list(self, *args):
        """ Summary: loads mac address from file to a list.

        Description:
        opens the file and read all the lines and stores it in a list
        and returns below details in a list from the file
        [['vlan', 'mac address', 'type', 'switch port'],
        ['vlan', 'mac address', 'type', 'switch port'],....]

        Syntax: mac_add_list("filename.ext")

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
            gerr = load_datafile(in_datafile, "-delcn")
        except IndexError:
            print("Index error at end")
        else:
            cnt = 0
            for val in gerr:
                # print(val)
                if re.search(r"(([0-9]|[a-o]|[A-O]){4}\.([0-9]|[a-o]|[A-O]){4}\.([0-9]|[a-o]|[A-O]){4})", val):
                    # print(val, " --> processed <-- ")
                    stripval = val.strip().split()
                    maclist.append(stripval)
                    # print(stripval, "-->", type(stripval))
                    cnt = cnt+1
            print("Mac count is ", cnt)
        # print full mac address table as a list of lists
        # print(maclist)
        return maclist
    # end mac_add_list()

    def mac_add_list_web(self, *args):
        """ Summary: loads mac address from web form to a list.

        Description:
        This is similar to mac_add_list() except the input would be a list from
        textarea of a HTML form. Reads all the lines and stores it in a list
        and returns below details in a list from the from's textarea.
        [['vlan', 'mac address', 'type', 'switch port'],
        ['vlan', 'mac address', 'type', 'switch port'],....]

        Syntax: mac_add_list(list of mac-address table)

        """
        # Validation check if the filename was provided to function
        # print("lenght of function args is =",len(args),args)

        if len(args) <= 0:
            return("No input list")

        else:
            in_datafrom = args[0]

        # print("Input file name --> ", in_datafile)

        maclist = []  # Empty list to store the mac address list from the source.
        try:
            # gerr = load_datafile("README.md","-delcn")
            gerr = in_datafrom
        except IndexError:
            print("Index error at end")
        else:
            cnt = 0
            for val in gerr:
                # print(val)
                if re.search(r"(([0-9]|[a-o]|[A-O]){4}\.([0-9]|[a-o]|[A-O]){4}\.([0-9]|[a-o]|[A-O]){4})", val):
                    # print(val, " --> processed <-- ")
                    stripval = val.strip().split()
                    maclist.append(stripval)
                    # print(stripval, "-->", type(stripval))
                    cnt = cnt+1
            print("Mac count is ", cnt)
        # print full mac address table as a list of lists
        # print(maclist)
        return maclist
    # end mac_add_list_web()

    def mac_oui_get(self, mac_add):
        """ Summary: retruns vendor name for the mac address.

        Description:
        Retruns the OUI vendor name for the given mac address
        NOTE: mac address should be input without any dots or hypens.
        example: 0ab10ab10ab1 (not as 0ab1.0ab1.0ab1)


        Syntax: mac_oui_get("mac address")
            eg. mac_oui_get("0ab10ab10ab1")

        """
        first6digit = re.findall(r"^[0-9a-oA-O]{6}",mac_add.rstrip("\n"))
        # print(first6digit)

        # load mac address OUI data base
        # macouidb_def = loadoui_file(oui_db_file)

        try:
            a = self.mac_oui_db[first6digit[0].lower()]
        except KeyError:
            a = "UNKNOWN VENDOR/VIRTUAL MAC"
            # print re.sub(","," = ",i.rstrip("\n"))
            # print(c,"=",re.sub(","," = ",i.rstrip("\n|\r")),"=",a)  # remove 'new line' or 'carriage return'
            return a
        else:
            # print i.rstrip("\n")
            # print(c,"=",re.sub(","," = ",i.rstrip("\n|\r")),"=",a)
            return a
    # end mac_oui_get()

    def mac_oui_get_list(self, mac_add):
        """ Summary: retruns vendor name for the mac address in a list.

        Description:
        Retruns the OUI vendor name for the given list of mac addresses
        NOTE: mac address should be input without any dots or hypens.
        example: 0ab10ab10ab1 (not as 0ab1.0ab1.0ab1)


        Syntax: mac_oui_get("mac address")
            eg. mac_oui_get("0ab10ab10ab1")

        """

        # load mac address OUI data base
        # macouidb_def = loadoui_file(oui_db_file)
        # print(oui_db_file)
        mac_add_out = []  # dummy list with title for storing output of the oui search
        for i in mac_add:
            # print(i)
            first6digit = re.findall(r"^[0-9a-oA-O]{6}", (i[1].replace(".", "")).rstrip("\n"))
            # print(first6digit)
            try:
                a = self.mac_oui_db[first6digit[0].lower()]
            except KeyError:
                a = "UNKNOWN VENDOR/VIRTUAL MAC"
                # print re.sub(","," = ",i.rstrip("\n"))
                # print(c,"=",re.sub(","," = ",i.rstrip("\n|\r")),"=",a)  # remove 'new line' or 'carriage return'
                i.append(a)
                # print(i)
            else:
                # print i.rstrip("\n")
                # print(c,"=",re.sub(","," = ",i.rstrip("\n|\r")),"=",a)
                i.append(a)
                # print(i)
            mac_add_out.append(i)
        # print(mac_add_out)
        return mac_add_out
    # end mac_oui_get()

# end class mactools
