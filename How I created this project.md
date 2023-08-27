<h1><strong>Creating your first project?</strong></h1>

<p>This was the first time that I had attempted to create a script like this, so I wanted to share with any beginners in Cybersecurity how to start
first project and how to be successful in doing so. </p>

<h3>Find something that interests you</h3>

<p>In this case I was given a tedious task and thought that there must be a quicker way to get the information from the National
Vulnerability Database (NVD) rather than to manually searching for each relevant CVE. So I conducted this browser search:</p>

<p><i>"NVD" + "Python" + "library"</i></p>

<p> which led me to the <u><a href='https://nvdlib.com/en/latest/index.html'>nvdlib</u></a> Python library</p>
<p> created by <a href='https://github.com/vehemont/nvdlib'>vehemont</a>.
<p> there were examples provided in the library, so I reverse engineered how these examples were grabbing the information from NVD.</p>

<h4> Steps that I needed to take to understand the library</h4>

<ul>
  <li>First I needed to grab information from NVD without pulling any specific parameter such as '<i>published</i>'</li>
  <li>Next I needed to compare the parameters such as 'published' to the code provided to see how the information was parsed</li>
  <li>Time to test it! Grab something from the big block of JSON text using your own code to see if you are able to grab new information</li>
</ul>

<p>The first matter of buisness is to request a CVE to see how the information outputs to the screen.</p>

<p><i>r = nvdlib.searchCVE(cveId='CVE-2023-38403')</i></p>
<p><i>print(r)</i></p>

<p>Which shows us this:</p>

![image](https://github.com/theCyberLeech/Web-Scraper-Tools/assets/102625690/4896004a-72b9-42db-9461-3325f7d86015)

<p>If we use the example that was given to us, then we should try to understand how <i>r[0].id</i> gives us the CVEID printed to the screen</p>
<p>By looking at the image above, we can see that the CVEID is the first thing printed to the block of text and the parameter name is '<i>id</i>!</p>

<p>Some of the more skilled programmers are probably asking why I didn't just parse the JSON and upload it to Excel like that. The answer here is that I tried doing that.</p>

<p>The first issue I had when I was trying to parse the JSON file was that the TRUE and FALSE Boolean values were not enclosed in quotation marks. Which meant that I would first need to write the block of code to a file, replace all TRUE and FALSE values to "TRUE" and "FALSE", then I would need to parse it.</p>

<p>The second issue I ran into was that there were subsections within this JSON file that were not parsing when uploaded after being formatted.</p>

<p>Thirdly, that felt like it was a little out of my comfort zone for the time being.</p>

<p>So I decided to just grab information that was relevant from those subsections and decided to write to an output file with a delimter of ";;" for the Options that will write links to a column, and ";" for the option that does not output links to a column.</p>

<p>I wanted to make the data workable and managable, which is, in my opinion, equally as important as having the data. If you have data that is not workable (not able to organize it) it creates a whole other job to sort the data. amiright?</p>
