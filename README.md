# Web-Scraper-Tools
Web Scraper that will automate vulnerability assessement tasks

Usage: python3 NewNVDNistScraper.py

NOTE: under construction due to updates made to the nvdlib library. 8/7/2023
NOTE: I have updated the script to align with the updates made to the nvdlib Python library.
      Results now are outputted to a text file that is formatted in a way that it can be 
      uploaded to an Excel spreadsheet. The data is now workable and managable. 





Screenshot of Menu: (Randomized ASCII font)

![image](https://user-images.githubusercontent.com/102625690/160985225-90e53470-f35c-4e3c-b0d0-a977b2babbc5.png)



<h2>(1) Search by CVE:</h2>
If you know the CVE ID that you want to search for, you can just type them in individually spaced.
Example:

![image](https://user-images.githubusercontent.com/102625690/160985481-0256cb99-8203-45db-8943-5b7166035e88.png)

The results will then output to a file in the same directory named 'CVESearchYYYY_MM_DD-hh:mm:ss_AM|PM.txt'
each column is delimited by 2 semi-colons (;;) due to some of the links containing semi-colons, two are used to resolve
the issue of links showing up in separate columns.

Screenshot of output:

![image](https://user-images.githubusercontent.com/102625690/160985948-833bff9e-1fb4-47c3-b2ee-e4580d5488d9.png)



<h2>(2) Search for CPE by Keyword:</h2>

If you're uncertain of the CPE Name (Affected Software), you can search for the name of the service or software and this will output to a file that is named after the search you conducted Ex. 'Microsoft Windows Server 2008YYYY_MM_DD-hh:mm:ss_AM|PM.txt'.txt'. You can utilize this to find the cpe: that you'll need to use option (3). After you know 
which cpeName is needed for your particiular software, you can use the 'search by CPE' option which will then give you all the vulnerabilities related to that software.

Ex.

![image](https://user-images.githubusercontent.com/102625690/160989150-b5e22992-83b6-40b2-b1b9-77d7158ffd20.png)


Sreenshot of Output:


![image](https://user-images.githubusercontent.com/102625690/160987465-281e1875-8583-4bef-b7c9-171feefd91a1.png)

<p>Copy the most relevant CPE Name and then move to step (3).</p>

<h2>(3) Search by CPE:</h2>

Paste the CPE Name starting with cpe:
![image](https://user-images.githubusercontent.com/102625690/160988054-d5d4c06e-578f-4d3f-8976-c1066d300a89.png)

All the vulnerabilities found for that specific CPE Name will be listed and the file will be named after the CPE Name that you searched for.
Screenshot of the Output:

![image](https://github.com/theCyberLeech/Web-Scraper-Tools/assets/102625690/b1adbcac-f50d-4e82-8ac9-e3bb563e55f6)


NOTE: Data can now be uploaded to an Excel spreadsheet for ease of use.

<h2>(4) Exit program:</h2>

Good-bye...



