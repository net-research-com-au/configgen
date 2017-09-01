# README #
Generic configuration generator

### Repository Details ###

* Summary
This program is generic configuration generator for any device with command line configuration.

* Version: 0.01
* Usage
    syntax: configgenv01.py <configuration_template.file> <value_csv.file>


### EXAMPLE USAGE ###

Some example templates are included in this repository

Generic Example: Create a list of real server configuration for the Radware Aleon Loadbalancer

    python configgenv01.py testtemplate.cfg testcsv.csv

    Parameters:
        <configuration_template.file>: testtemplate.cfg
        <value_csv.file>: testcsv.csv

Cisco Example: Create a list cisco deivce configurations based on input template
    python configgenv01.py ciscotemplate.cfg cisco.csv

    Parameters:
        <configuration_template.file>: testtemplate.cfg
        <value_csv.file>: testcsv.csv


### Who do I talk to? ###

* Repo owner or admin
    Contact: dheep@net-research.com.au

* Other community or team contact
    None
