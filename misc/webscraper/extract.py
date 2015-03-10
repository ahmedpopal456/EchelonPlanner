from bs4 import BeautifulSoup
import re

def extractSemester(text):
    semesterlist = []
    position = []
    index = 0
    for i in text:
        if i == "Summer\n" or i == "Fall\n" or i == "Winter\n" or i=="Fall&Winter\n":
            position.append(index)
        index+=1

    j=0
    while j < len(position)-1:
        semesterlist.append(text[position[j]:position[j+1]])
        j+=1
    semesterlist.append(text[position[j]:])

    for semester in semesterlist:
        extractLecture(semester)

    return semesterlist


def extractLecture(semester):
    lecturelist = []
    position = []
    index = 0

    for i in semester:
        if "Lect" in i:
            position.append(index)
        index+=1
    j=0

    while j < len(position)-1:
        lecturelist.append(semester[position[j]:position[j+1]])
        j+=1
    lecturelist.append(semester[position[j]:])

    return lecturelist



#def extractTutorial(lecture):

#def extractLab(tutorial):


inputFile = open("output.txt")
outputClearFile = open("outputClearFile.txt", "w")
output2 = open("output2.txt","w")
output3 = open("output3.txt", "w")

soup = BeautifulSoup(inputFile)
table = soup.find("table", attrs={"id": "ctl00_PageBody_tblBodyShow1"})

# The first tr contains the date when searched, the next few are search critera '
# counting on the format to remain the same (i.e i correspondong to the correct number), needs to be changed, elec has 1 extra td vs comp
i = 1
for tr in table.find_all("tr"):
    for td in tr.find_all("td"):
        text = (td.get_text())
        outputClearFile.write(text + "\n")

outputClearFile.close()

file_content = open("outputClearFile.txt")
file_content = file_content.readlines()
course_info  = extractSemester(file_content)
for semester in course_info:
    for lines in semester:
        output3.write(lines)
    output3.write("----------------------------\n")


with open("outputClearFile.txt", "r") as lines:
    for text in lines:
        # Find the Course, then extract Dept, Num, Name and Credits
        if (len(text))is 9 and re.match('[A-Z]{4} \d{3}', text):
            department = text[:4]
            number = text[-4:-1]
            output2.write(("Department: "+department + "\n" +"Course Number: "+number + "\n"))
            text = next(lines,0)
            name = text
            output2.write(("Course Name: "+name))
            text = next(lines,0)
            Credits = text[:1]
            output2.write(("Credits: "+Credits + "\n"))
        #Extract Preq
        if text.find("Prerequisite") is not -1:
            text = next(lines,0)
            try:
                prereq = re.findall('[A-Z]{4} \d{3}',text)
                output2.write(("Prerequisites: "+str(prereq) + "\n"))
            except AttributeError:
                output2.write(("Prerequisites: NONE \n"))
        #Extract  Semester Summer class
        if text == "Summer\n":
            text = next(lines,0)
            output2.write("Semester: Summer"+ "\n")
            output2.write(str(text))

            #Skip lines under Summer term until it hits line with LECT XX
            while "Lect" not in text:
                text = next(lines,0)

            #Type Lect plus section
            output2.write(text)
            # Under Lect get days/time

            text = next(lines,0)
            days = text[:7]
            matchtime = re.findall('[0-9]{2}:[0-9]{2}-',text)
            starttime = matchtime[0][:-1]
            matchtime = re.findall('[0-9]{2}:[0-9]{2}[)]{1}',text)
            endtime = matchtime[0][:-1]
            output2.write("Days: "+days+ "\n" )
            output2.write("Start Time: "+str(starttime)+ "\n" )
            output2.write("End Time: "+str(endtime)+ "\n" )

            #Location
            text = next(lines,0)
            location = text
            output2.write("Location: "+location )

            #Prof
            text = next(lines,0)
            prof = text
            output2.write("Prof: "+prof )

            while "Tut" not in text:
                text = next(lines,0)

            #Type Tut plus section
            output2.write(text)
            text = next(lines,0)
            days = text[:7]
            matchtime = re.findall('[0-9]{2}:[0-9]{2}-',text)
            starttime = matchtime[0][:-1]
            matchtime = re.findall('[0-9]{2}:[0-9]{2}[)]{1}',text)
            endtime = matchtime[0][:-1]
            output2.write("Days: "+days+ "\n" )
            output2.write("Start Time: "+str(starttime)+ "\n" )
            output2.write("End Time: "+str(endtime)+ "\n" )

            #Location
            text = next(lines,0)
            location = text
            output2.write("Location: "+location)

            #TODO seperate into different functions, i.e Extractlect, extractTut.