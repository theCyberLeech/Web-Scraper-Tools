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

date = datetime.now().strftime('%Y_%m_%d-%I:%M:%S_%p')
original_stdout = sys.stdout



def searchByCVE():
	input_string = input('Which CVE IDs do you want to look up?\n')
	CVEID = input_string.split()
	with open('CVESearch' + date + '.txt', 'w') as f:
		sys.stdout = f
		for i in CVEID:
			try:
				r = nvdlib.getCVE(i)
			except LookupError:
				print(i + ' does not exist.')
				continue
			print('\nCVE ID: ' + i)
			PubDate = r.publishedDate
			timeParsed = zulu.parse(PubDate)
			print('Published Date: ', end='')
			print(timeParsed)
			print('\nDescription: ' + r.cve.description.description_data[0].value + '\n')
			try:
				print('v3 Vector: ' + r.v3vector)
			except AttributeError:
				print('v3 Vector Score not available')
			print('CWE ID: ' + r.cve.problemtype.problemtype_data[0].description[0].value)
			print('Nist URL: ' + str(r.url))
			print('Exploitability: ', end='')
			try:
				print(r.v3exploitability)
			except AttributeError:
				print('Not available')
			print('V3 Score: ', end='')
			print(r.score[1], end=' - ')
			print(r.score[2])
			print('\nReferences: ')
			count = 0
			References = r.cve.references.reference_data
			for eachURL in References:
				length = range(len(References))
				Refs = r.cve.references.reference_data[count].url
				print(Refs)
				count += 1
			print('------------------------------------------------------------\n')
		sys.stdout = original_stdout
	f.close()
	whatNext()
	Menu()




def searchByKeyword():
	inputString = input('What service || Software do you want to search for? \n')
	r = nvdlib.searchCPE(keyword = inputString , limit = 100)
	with open(inputString + date + '.txt', 'w') as f:
		sys.stdout = f
		for eachCPE in r:
			print('\nTitle: ', end=eachCPE.title)
			print('\nCPE Name: ' + eachCPE.name)
			References = eachCPE.refs
			count = 0
			print('\n\nReferences:')
			for eachURL in References:
				print(References[count].ref, end=' Type: ')
				print(References[count].type)
				count += 1
			print('-------------------------------------------------------\n')
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
#       CPERegEx()
	try:
		vulns = nvdlib.searchCVE(cpeName=CPE, exactMatch=True)
		with open(CPE + '.txt', 'w') as f:
			sys.stdout = f
			for i in vulns:
				print('CVE ID: ' + i.id)
				print('Severity: ' +  str(i.score[1]) + ' - ' + str(i.score[2]))
				print('NVD URL: ' +  i.url)
				print('\nDescription: ' + i.cve.description.description_data[0].value + '\n')
				try:
        	        	        print('v3 Vector: ' + i.v3vector)
				except AttributeError:
					print('v3 Vector Score not available')
				print('CWE ID: ' + i.cve.problemtype.problemtype_data[0].description[0].value)
				print('Nist URL: ' + str(i.url))
				print('Exploitability: ', end='')
				try:
					print(i.v3exploitability)
				except AttributeError:
					print('Not available')
				print('V3 Score: ', end='')
				print(i.score[1], end=' - ')
				print(i.score[2])
				print('\nReferences: ')
				count = 0
				References = i.cve.references.reference_data
				for eachURL in References:
					Refs = i.cve.references.reference_data[count].url
					print(Refs)
					count += 1
				print('---------------------------------------\n')
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
	else:
		print('Bad input, try again. Do not use spaces. Enter 1, 2, 3 or 4.')
	Menu()

NVDNistBanner = text2art('NVDNISTSCRAPER.py', font='rnd-small')


print(NVDNistBanner)
Menu()

