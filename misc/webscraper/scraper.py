import urllib.request
import urllib.parse
import urllib.error
import re
import extract

concordiaSite = urllib.request.urlopen("http://fcms.concordia.ca/fcms/asc002_stud_all.aspx")
#print (concordiaSite.read())

#open list of courses to scrape, and put into list
coursedept = ""
coursenum = ""
courselist = []
unfilteredcourselist = open("ListOfCourseToScrape.txt", "r").readlines()

#to debug courses not  offered, timeconsuming to go through whole list
#unfilteredcourselist = open("debugcourselist.txt").readlines()

debugcourselist = open("debugcourselist.txt","w")

for lines in unfilteredcourselist:
        coursedeptnum = re.search('[A-Z]{4} \d{3}', lines)
        try:
            coursedeptnum = coursedeptnum.group(0)
            coursedept = coursedeptnum[:4]
            coursenum = coursedeptnum[-3:]
            courselist.append([coursedept, coursenum])
        except:
            coursedeptnum = ""

for i in courselist:
    debugcourselist.write( i[0]+ " "+ i[1]+ '\n')

#Make new Request
HardcodedParamsFiles = open("hardcodedParams.txt")
HardcodedParams = str(HardcodedParamsFiles.readline())
print(HardcodedParams)

Params={}
Params["ctl00$PageBody$ddlYear"]="2014"
Params["ctl00$PageBody$ddlSess"]="A"
Params["ctl00$PageBody$ddlLevl"]="U"
Params["ctl00$PageBody$ddlDept"]="0403"
Params["ctl00$PageBody$txtKeyTtle"]=""
Params["ctl00$PageBody$ddlClaWeek"]="+"
Params["ctl00$PageBody$ddlClaDays"]="+"
Params["ctl00$PageBody$ddlTimeBtw"]="+"
Params["ctl00$PageBody$ddlCampus"]="+"

#You can modify the POST param data 

for course in courselist:
    Params["ctl00$PageBody$txtCournam"] = course[0]
    Params["ctl00$PageBody$txtCournum"] = course[1]


    #Send the huge string of bytes.
    data = (HardcodedParams+Params["ctl00$PageBody$ddlSess"]+\
           "&ctl00%24PageBody%24ddlLevl="+Params["ctl00$PageBody$ddlLevl"]+\
           "&ctl00%24PageBody%24ddlDept="+Params["ctl00$PageBody$ddlDept"]+\
           "&ctl00%24PageBody%24txtCournam="+Params["ctl00$PageBody$txtCournam"]+\
           "&ctl00%24PageBody%24txtCournum="+Params["ctl00$PageBody$txtCournum"]+\
           "&ctl00%24PageBody%24txtKeyTtle=&ctl00%24PageBody%24ddlClaWeek=+&ctl00%24PageBody%24ddlClaDays=+&ctl00%24PageBody%24ddlTimeBtw=+&ctl00%24PageBody%24ddlCampus=+").encode('utf-8')

    concordiaSite = urllib.request.urlopen("http://fcms.concordia.ca/fcms/asc002_stud_all.aspx",data)


    extract.extract(str(concordiaSite.read().decode('utf-8')))
