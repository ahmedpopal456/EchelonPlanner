from bs4 import BeautifulSoup
import re

# Master DB file
outputDB = open("outputDB.txt", "w")


def extractSemester(text):

    department = ""
    number = ""
    name = ""
    Credits = ""
    prereq = []

    for index, line in enumerate(text):
        # Find the Course, then extract Dept, Num, Name and Credits
        if (len(line))is 9 and re.match('[A-Z]{4} \d{3}', line):
            department = line[:4]
            number = line[-4:-1]
            name = text[index+1][:-1]  #remove trailing newline from name
            Credits = text[index+2][:1]

        #Extract Preq
        if line.find("Prerequisite") is not -1:
            line = text[index+1]
            try:
                prereq = re.findall('[A-Z]{4} \d{3}',line)
            except AttributeError:
                prereq = ["NONE"]

    print('Course: {}, {}, {}, {} Credits, {}\n'.format(department, number, name, Credits, prereq)) # goes into DB course table
    outputDB.write('Course: {}, {}, {}, {} Credits, {}\n'.format(department, number, name, Credits, prereq))

    semesterlist = []
    position = []
    index = 0
    for i in text:
        if i == "Summer\n" or i == "Fall\n" or i == "Winter\n" or i=="Fall&Winter;\n":
            position.append(index)
        index+=1

    j=0
    while j < len(position)-1:
        semesterlist.append(text[position[j]:position[j+1]])
        j+=1
    semesterlist.append(text[position[j]:])

    for semester in semesterlist:
        extractLecture(semester, department, number)

    return semesterlist


def extractLecture(semester, department, number):

    semestername = "" #winter, fall, summer, further processing if summer
    section = ""
    prof =""
    starttime = ""
    endtime = ""
    days = ""
    location =""

    lecturelist = []
    position = []
    index = 0

    for i, line in enumerate(semester):
        if i == 0:
            semestername = line.strip()
            if semestername == "Summer":
                if "May" in semester[i+1]:
                    semestername = "Summer1"
                else:
                    semestername = "Summer2"

        if "Lect" in line or "OnLine" in line and "NOTE" not in line:
            position.append(index)
        index+=1
    j=0

    while j < len(position)-1:
        lecturelist.append(semester[position[j]:position[j+1]])
        j+=1
    lecturelist.append(semester[position[j]:])

    for lecture in lecturelist:
        location = lecture[2].strip() # strip new line and spaces
        enumerate(lecture)
        sectionline = lecture[0].split()
        for i in sectionline:
            if "Lect" or "OnLine" not in i:
                section = i
            if "OnLine" == i:
                location = location+"(Online)"
        section = section.strip()
        days = lecture[1][:7]
        matchtime = re.findall('[0-9]{2}:[0-9]{2}-', lecture[1])
        starttime = matchtime[0][:-1]
        matchtime = re.findall('[0-9]{2}:[0-9]{2}[)]{1}', lecture[1])
        endtime = matchtime[0][:-1]
        prof = lecture[3]

        # ignore cancelled sections
        if section != "*Canceled*":
            print("Lecture : {} {}, {}, {}, {}, {}, {}, {}, {}".format
                  (department, number, semestername, section, days, starttime, endtime, location, prof))
                  # would be sent to DB Lectures, with key section, and links to courses with dept+num
            outputDB.write("Lecture : {} {}, {}, {}, {}, {}, {}, {}, {}".format
                  (department, number, semestername, section, days, starttime, endtime, location, prof))
            extractTutorial(lecture, section, department, number)
    outputDB.write("\n")

    return lecturelist



def extractTutorial(lecture, lecturesection, department, number):
    section = ""
    days = ""
    starttime = ""
    endtime = ""
    location = ""
    tutorialList = []
    position = []
    index = 0

    for i in lecture:
        if "Tut" in i and "NOTE" not in i:
            position.append(index)
        index+=1

    if position.__len__() == 0:
        #no tutorial for this section, see if there are labs
        extractLab(lecture, lecturesection, department, number)
        return 0

    j = 0

    while j < len(position)-1:
        tutorialList.append(lecture[position[j]:position[j+1]])
        j += 1
    tutorialList.append(lecture[position[j]:])

    for tutorial in tutorialList:
        enumerate(tutorial)
        sectionline = tutorial[0].split()
        for i in sectionline:
            if "Tut" is not i:
                section = i
        section = section.strip()
        days = tutorial[1][:7]
        matchtime = re.findall('[0-9]{2}:[0-9]{2}-', tutorial[1])
        starttime = matchtime[0][:-1]
        matchtime = re.findall('[0-9]{2}:[0-9]{2}[)]{1}', tutorial[1])
        endtime = matchtime[0][:-1]
        location = tutorial[2].strip() # strip new line and spaces
        print("Tutorial {} {} {} : {}, {}, {}, {}, {}".format
              (department, number, lecturesection, section, days, starttime, endtime, location))
              # would be sent to DB Tutorials, with key section, and links to Lectures with lecturesection and dept+num
        outputDB.write("Tutorial {} {} {} : {}, {}, {}, {}, {}\n".format
              (department, number, lecturesection, section, days, starttime, endtime, location))
        extractLab(tutorial, section, department, number)
    outputDB.write("\n")
    print("\n")
    return tutorialList


def extractLab(tutorial, tutorialsection, dept, num):

    labList = []
    section = ""
    days = ""
    starttime = ""
    endtime = ""
    location = ""

    position = []
    index = 0

    for i in tutorial:
        if "Lab" in i:
            position.append(index)
        index+=1

    if position.__len__() == 0:
        return 0

    j=0

    while j < len(position)-1:
        labList.append(tutorial[position[j]:position[j+1]])
        j+=1
    labList.append(tutorial[position[j]:])

    for lab in labList:
        enumerate(lab)
        sectionline = lab[0].split()
        for i in sectionline:
            if "Lab" is not i:
                section = i
        section = section.strip()
        days = lab[1][:7]
        matchtime = re.findall('[0-9]{2}:[0-9]{2}-', lab[1])
        starttime = matchtime[0][:-1]
        matchtime = re.findall('[0-9]{2}:[0-9]{2}[)]{1}', lab[1])
        endtime = matchtime[0][:-1]
        location = lab[2].strip() # strip new line and spaces
        print("Lab {} {} {} : {}, {}, {}, {}, {}".format
              (dept, num, tutorialsection, section, days, starttime, endtime, location))
              # would be sent to DB Lab, with key section, and links to tutorials with tutorialsection and dept+num
        outputDB.write("Lab {} {} {} : {}, {}, {}, {}, {}".format
              (dept, num, tutorialsection, section, days, starttime, endtime, location))
        outputDB.write("\n")
    print("\n")



    return labList


def extract(inputFile):
    #used as intermediary file to extract each course
    outputClearFile = open("outputClearFile.txt", "w")

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
    extractSemester(file_content)


