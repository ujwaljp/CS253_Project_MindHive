from bs4 import BeautifulSoup
import re
import requests


s = requests.Session()
s.get("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITK_Srch.jsp?typ=stud")

payload = {
    'k4': 'oa',
    'numtxt': '',
    'recpos': 0,
    'str': '',
    'selstudrol': '',
    'selstuddep': '',
    'selstudnam': '',
    'txrollno': '',
    'Dept_Stud': '',
    'selnam1': '',
    'mail': ''
}

payload1 = {
    'typ': ['stud'],
    'numtxt': '',
    'sbm': ['Y']
}

r = s.post("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITK_Srch.jsp?typ=stud", data=payload)

def process_response_soup(soup):
    for link in soup.select('.TableText a'):
        roll = link.get_text().strip()
        payload1['numtxt'] = roll
        r1 = s.post("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchRes_new.jsp", headers=headers1, data=payload1)
        soup1 = BeautifulSoup(r1.text, 'html.parser')

        name = ''
        program = ''
        dept = ''
        hall = ''
        room = ''
        username = ''
        blood_group = ''
        gender = ''
        hometown = ''

        for para in soup1.select('.TableContent p'):
            body = para.get_text().strip()
            field = body.split(':')
            key = field[0].strip()
            value = field[1].strip()
            if key == 'Name':
                name = value.lower().title()
            elif key == 'Program':
                program = value
            elif key == 'Department':
                dept = value.lower().title()
            elif key == 'Hostel Info':
                if len(value.split(',')) > 1:
                    hall = value.split(',')[0].strip()
                    room = value.split(',')[1].strip()
            elif key == 'E-Mail':
                if len(value.split('@')) > 1:
                    username = value.split('@')[0].strip()
            elif key == 'Blood Group':
                blood_group = value
            elif key == 'Gender':
                if len(value.split('\t')) > 1:
                    gender = value.split('\t')[0].strip()
            else:
                print("{} {}".format(key, value))

        body = soup1.prettify()
        if len(body.split('Permanent Address :')) > 1:
            address = body.split('Permanent Address :')[1].split(',')
            if len(address) > 2:
                address = address[len(address) - 3: len(address) - 1]
                hometown = "{}, {}".format(address[0], address[1])

        print(roll) 
        print(username)
        print(name) 
        print(program)
        print(dept) 
        print(hall) 
        print(room)
        print(blood_group)
        print(gender)
        print(hometown)


payload['mail'] = user.email
r = s.post("https://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchStudRoll_new.jsp", headers=headers, data=payload)
soup = BeautifulSoup(r.text, 'html.parser')
