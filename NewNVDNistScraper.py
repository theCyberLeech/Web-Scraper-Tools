# Copyright (C) 2022 Creator: Ana De Jesus
# Created and intended for learning purposes
# Helps aid in vulnerability assessment by pulling relevant software or services
# from the NVD Nist Framework
# Creator is not responsible for the actions that you as the user does with this script.
# Note: I know this code could have been implemented better and intend on updating it with classes,
# however, it works well enough for now :)

import nvdlib
import requests
import zulu
import sys
from datetime import datetime
from art import *
import re

date = datetime.now().strftime('%Y_%m_%d-%I:%M:%S_%p')
original_stdout = sys.stdout

def searchByCVE():
        input_string = input('Which CVE IDs do you want to look up?\n')
        CVEID = input_string.split()
        with open('CVESearch' + date + '.txt', 'w') as f:
                sys.stdout = f
                print('CVE ID;; Date Published;; CWE ID;; Affected CPE IDs;;V31 Severity;; Description;; References') 
                for i in CVEID:
                    pattern = '^(cve|CVE)-[0-9]{4}-[0-9]{4,}$'
                    result = re.match(pattern, i)
                    if result:
                        try:
#                               r = nvdlib.searchCVE(cveId=i, key='XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX') # << Place your API key here
                                r = nvdlib.searchCVE(cveId=i)
                        except LookupError:
                                print(i + ' ;;does not exist.;;n/a;;n/a;;n/a;;n/a;;n/a', end='\n')
                                continue
                        print(i + ';;', end=' ')
                        print(r[0].published + ';;', end=' ')
                        print(str(r[0].weaknesses[0].description[0].value) + ';;', end=' ')
                        count = 0
                        cpeAffected = r[0].cpe
                        for e in cpeAffected:
                                length = range(len(cpeAffected))
                                cpes = r[0].cpe[count].criteria
                                print(cpes, end=', ')
                                count += 1
                        print(end=';; ')
                        print(str(r[0].score[1]) + ' ' + r[0].score[2], end=';; ')
                        print(r[0].descriptions[0].value, end=';; ')
                        count = 0
                        print(str(r[0].url), end=', ')
                        References = r[0].references
                        for eachURL in References:
                                length = range(len(References))
                                Refs = r[0].references[count].url
                                print(Refs, end=', ')
                                count += 1
                        print(end='\n')

                    else:
                        print(i + ';; CVE IDs need to be in the format of CVE-YYYY-NNNNNNN;;', end='')
                        print('Please try again.;;n/a ;;n/a ;;n/a ;;n/a')
                        continue
                sys.stdout = original_stdout
        f.close()
        whatNext()
        Menu()




def searchByKeyword():
        inputString = input('What service || Software do you want to search for? \n')
#       r = nvdlib.searchCPE(keywordSearch=inputString, key='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx') # << Place your API key here
        r = nvdlib.searchCPE(keywordSearch=inputString)
        with open(inputString + date + '.txt', 'w') as f:
                sys.stdout = f
                print('Keyword Search; Published; Title; Deprecated?; CPE Name; CPE ID', end='\n')
                for i in r:
                        print(inputString, end='; ')
                        print(i.created, end='; ')
                        print(str(i.titles[0].title), end='; ')
                        print(i.deprecated, end='; ')
                        print(i.cpeName, end='; ')
                        print(i.cpeNameId, end='\n')
                sys.stdout = original_stdout
        f.close()
        whatNext()
        Menu()



def searchByCPE():
        CPE = input(''' 
                                           _____
                                            | |
        What is the cpe that you you seek? <0.o>

        Starting with "cpe:" enter the cpe that you wish to conduct your search with:
        Example: cpe:2.3:a:openbsd:openssh:7.2:p2:*:*:*:*:*:*\n
''')
        try:
#               vulns = nvdlib.searchCVE(cpeName=CPE, key='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx') # << Place your API key here
                vulns = nvdlib.searchCVE(cpeName=CPE)
                with open(CPE + '.txt', 'w') as f:
                        sys.stdout = f
                        print('CVE ID;; Published;; Severity;; CWE ID;; Description;; NVD URL;; References', end='\n')
                        for i in vulns:
                                print(i.id + ';;', end=' ')
                                print(i.published + ';;', end=' ')
                                print(str(i.score[1]) + ' - ' + str(i.score[2]) + ';;', end=' ')
                                print(i.cwe[0].value + ';;', end=' ')
                                print(i.descriptions[0].value + ';;', end=' ')
                                count = 0
                                References = i.references
                                print(i.url, end=';; ')
                                for URL in References:
                                        length = range(len(References))
                                        Refs = i.references[count].url
                                        print(Refs, end=', ')
                                        count += 1
                                print(end='\n')
                        sys.stdout = original_stdout
                f.close()
        except LookupError:
                print(CPE + ' does not exist. Double-check your input.')
        whatNext()



def whatNext():
        print('''\n\n

        _______________
       Done! What's next?
         ------------ \|   /-|-|-\\
                         <|(O) (o)|>
                          |   -   |
                           \|___|/
                           |-----|
 \n\n''')
        Menu()


def Banner():
        NVDNistBanner = text2art('NVDNISTSCRAPEr.py', font='rnd-small')
        print(NVDNistBanner)




def Menu():
        print('''
        \n\n
                                Welcome to the NewNVDNistScrapper.py!
        This tool can be used to grab information on known vulnerabilities inside the NVD framework.

                                        Created By Ana De Jesus
\n\n''')
        menuInput = input('''
        (1) Search by CVE
        (2) Search for CPE by Keyword
        (3) Search by CPE Name
        (4) Exit Program

Make your selection: \n''')
        if menuInput == '1':
                searchByCVE()
        elif menuInput == '2':
                searchByKeyword()
        elif menuInput =='3':
                searchByCPE()
        elif menuInput == '4':
                print('Good-bye.....')
                sys.exit()
        elif menuInput == '5':
                Banner()
        else:
                print('Bad input, try again. Do not use spaces. Enter 1, 2, 3 or 4.')
        Menu()

Banner()
Menu()
