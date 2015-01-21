from bs4 import BeautifulSoup
import re

inputFile = open("output.txt")
outputClearFile = open("outputClearFile.txt", "w")
output2 = open("output2.txt","w")

soup = BeautifulSoup(inputFile)
table = soup.find("table", attrs={"id": "ctl00_PageBody_tblBodyShow1"})

# The first tr contains the date when searched, the next few are search critera '
# counting on the format to remain the same (i.e i correspondong to the correct number), needs to be changed, elec has 1 extra td vs comp
i = 1
for tr in table.find_all("tr"):
    for td in tr.find_all("td"):
        outputClearFile.write(str(i) + ": ")
        outputClearFile.write((td.get_text()) + "\n")
        if i is 8:
            department = (td.get_text())[:4]
            number = (td.get_text())[-3:]
            output2.write(("Department: "+department + "\n" +"Course Number: "+number + "\n"))
        if i is 9:
            name = (td.get_text())
            output2.write(("Course Name: "+name + "\n"))
        if i is 10:
            Credits = (td.get_text())[:1]
            output2.write(("Credits: "+Credits + "\n"))
        if i is 13:
            text = (td.get_text())
            try:
                prereq = re.findall('[A-Z]{4} \d{3}',text)
                output2.write(("Prerequisites: "+str(prereq) + "\n"))
            except AttributeError:
                output2.write(("Prerequisites: NONE \n"))

        i= i+1


