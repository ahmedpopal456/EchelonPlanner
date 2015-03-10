import urllib.request
import urllib.parse
import urllib.error

concordiaSite = urllib.request.urlopen("http://fcms.concordia.ca/fcms/asc002_stud_all.aspx")
#print (concordiaSite.read())

#Make new Request
HardcodedParamsFiles = open("hardcodedParams.txt")
HardcodedParams = str(HardcodedParamsFiles.readline())
print(HardcodedParams)

Params={}
Params["ctl00$PageBody$ddlYear"]="2014"
Params["ctl00$PageBody$ddlSess"]="A"
Params["ctl00$PageBody$ddlLevl"]="U"
Params["ctl00$PageBody$ddlDept"]="0403"
Params["ctl00$PageBody$txtCournam"]="comp"
Params["ctl00$PageBody$txtCournum"]="352"
Params["ctl00$PageBody$txtKeyTtle"]=""
Params["ctl00$PageBody$ddlClaWeek"]="+"
Params["ctl00$PageBody$ddlClaDays"]="+"
Params["ctl00$PageBody$ddlTimeBtw"]="+"
Params["ctl00$PageBody$ddlCampus"]="+"

#You can modify the POST param data 


#Send the huge string of bytes.
data = (HardcodedParams+Params["ctl00$PageBody$ddlSess"]+\
       "&ctl00%24PageBody%24ddlLevl="+Params["ctl00$PageBody$ddlLevl"]+\
       "&ctl00%24PageBody%24ddlDept="+Params["ctl00$PageBody$ddlDept"]+\
       "&ctl00%24PageBody%24txtCournam="+Params["ctl00$PageBody$txtCournam"]+\
       "&ctl00%24PageBody%24txtCournum="+Params["ctl00$PageBody$txtCournum"]+\
       "&ctl00%24PageBody%24txtKeyTtle=&ctl00%24PageBody%24ddlClaWeek=+&ctl00%24PageBody%24ddlClaDays=+&ctl00%24PageBody%24ddlTimeBtw=+&ctl00%24PageBody%24ddlCampus=+").encode('utf-8')

concordiaSite = urllib.request.urlopen("http://fcms.concordia.ca/fcms/asc002_stud_all.aspx",data)
#print(concordiaSite.read().decode('utf-8'))
output = open("output.txt","w")
output.write(str(concordiaSite.read().decode('utf-8')))
output.close()