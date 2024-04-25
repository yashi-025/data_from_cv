import os
import json
from pdfminer.high_level import extract_text
import docx2txt
from source import mobile, skills
from source import designation
from source import edu
from source import awards
from source import project
#from source import extract_dates;

import re


def extract_exp(lines):
    exp = 'years'
    for line in lines:
        #print(line.lower())
        if  exp in line.lower():
             res = int(re.search(r'\d+', line).group())
             #print(res)
             if res>0:
                 return res


def extract_name(lines):
    nn = lines[0]
    # if 'mobile' in nn.lower():
    #     i = nn.index('mobile')
    #     nn = nn[:i]

    # if 'email' in nn.lower():
    #     i = nn.index('email')
    #     nn = nn[:i]

    return nn



def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)[0]
 
def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None
 
def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def loadAllCV():
    dir_list = os.listdir('./cv')
    print(dir_list)
    resumes = []
    #rr=loadSingleCV('pankajvgosavi.pdf')
    #resumes.append(rr)
    for cv in dir_list:
        rr = loadSingleCV(cv)
        resumes.append(rr)
    print((resumes))

def loadSingleCV(file):
    #print(extract_text_from_pdf('./resume.pdf'))  # noqa: T001
    #data = extract_text_from_pdf('./MANISH KUMAR.pdf')
    #data = extract_text_from_pdf('./resume.pdf')
    data = extract_text_from_pdf('./cv/'+ file)
    #print(data)
    print('-------------------------------' + file + ' -----------------------------------' )
    if len(data) == 0:
        print('No data for: ', file)
        print('###################### END ##########################################' )
        return 
    #print(data)
    lines = data.splitlines()
    #print(lines[3])

    #extract_dates.extract_date(lines)
    name = extract_name(lines)
    mob = mobile.extract_mobile_number(data, lines)
    email = extract_email_addresses(data)
    coreSkills = skills.extract_coreSkills(lines)
    techSkills = skills.extract_techSkills(lines)
    experience = extract_exp(lines)
    design = designation.extract_designation(lines)
    

    #print('Name: ', name)
    #print('Designation: ',  design)
    #print('Mobile: ', mob)
    #print('Mail id: ', email)
    #print('Core Skills: ',  coreSkills)
    #print('Technical Skills: ',  techSkills)
    #print('Experience: ',  experience)

    #print("EDUCATION")
    edu.extract_education(data)
    


    #print("Awards")
    #award=awards.extract_awards_and_achievements(data)
    #for p in award:
    #    print(p)


    #print("Project")
    #project.extract_project(data)


    print('----------------------------------------------END---------------------------------------------------------\n\n' )

    # resumeInfo = {"name": name , 
    #               "designation":design, 
    #               "mobile": mob, 
    #               "email":email, 
    #               "coreSkills":coreSkills, 
    #               "techSkills": techSkills, 
    #               "experience": experience }
    # resumeData = json.dumps(resumeInfo, default = lambda x: x.__dict__)
    # print('resumeData:', resumeData)
    # return (resumeData)

if __name__ == '__main__':

    #loadSingleCV('AMIT KUMAR Hirehunch.pdf')
    #loadSingleCV('AJIT HEGDE.pdf')
    loadAllCV()
    
    
    #print(data)