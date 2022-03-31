# Web-Scraper-Tools
Web Scraper that will automate vulnerability assessement tasks

Usage: python3 NewNVDNistScraper.py






Screenshot of Menu: (Randomized ASCII font)

![image](https://user-images.githubusercontent.com/102625690/160985225-90e53470-f35c-4e3c-b0d0-a977b2babbc5.png)



(1) Search by CVE:
If you know the CVE ID that you want to search for, you can just type them in individually spaced.
Example:

![image](https://user-images.githubusercontent.com/102625690/160985481-0256cb99-8203-45db-8943-5b7166035e88.png)

The results will then output to a file in the same directory named 'CVESearchYYYY_MM_DD-hh:mm:ss_AM|PM.txt'

Screenshot of output:

![image](https://user-images.githubusercontent.com/102625690/160985948-833bff9e-1fb4-47c3-b2ee-e4580d5488d9.png)

((NOTE: Currently working on organizing the output better so that grepping would be more efficient)
Example:
**cat 'CVESearchYYYY_MM_DD-hh:mm:ss_AM|PM.txt' | grep 'Privileges Required: NONE' -B 5**
would ouptut the CVE ID of a vulnerability that did not require the attacker to have previous authentication.)

(2) Search for CPE by Keyword:
If you're uncertain of the CPE Name (Affected Software), you can search for the name of the service or software and this will output to a file that is named after the search you conducted Ex. 'Microsoft Windows Server 2008YYYY_MM_DD-hh:mm:ss_AM|PM.txt'.txt'. You can utilize this to find the cpe: that you'll need to use option (3).
Ex.

![image](https://user-images.githubusercontent.com/102625690/160989150-b5e22992-83b6-40b2-b1b9-77d7158ffd20.png)


Sreenshot of Output:


![image](https://user-images.githubusercontent.com/102625690/160987465-281e1875-8583-4bef-b7c9-171feefd91a1.png)

Copy the most relevant CPE Name and then move to step (3).
Ex. cpe:2.3:o:microsoft:windows_server_2008:-:-:*:*:enterprise:*:x64:*

(3) Search by CPE:
Paste the CPE Name starting with cpe:
![image](https://user-images.githubusercontent.com/102625690/160988054-d5d4c06e-578f-4d3f-8976-c1066d300a89.png)

All the vulnerabilities found for that specific CPE Name will be listed and the file will be named after the CPE Name that you searched for.
Screenshot of the Output:

![image](https://user-images.githubusercontent.com/102625690/160988298-be069588-b3ba-4b48-9914-05ce7d29aa2e.png)

NOTE: Again, working on reorganizing this to be more efficient for grepping :)

(4) Exit program:
Good-bye...



