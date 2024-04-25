import re
from tkinter import END

def extract_education(data):





    head_not_req = re.compile(r'Hobbies|Personal|Project|Experience|Award|Activities|Technical|Language|Skill|Company|Job|Role|Responsibi|Employ|Profile|Contact|EXTRACURRICULAR|Current',re.IGNORECASE)
    year_pattern = re.compile(r'\d{4}')
    edu_pattern = re.compile(r'Education|Academic|EDUCATION|ACADEMIC')
    in_edu_pattern = re.compile(r'College|University|Bachelor|master|degree|Graguate|((B|M).?(Tech|E|S|Com).?)|(M.?BA.?)|CBSE|ICSE|Board|(s.?s.?e.?)|(h.?s.?e.?)|(s.?s.?c.?)|(h.?s.?c.?)|CGPA|GPA|%|X|XII|10|12|(ph.?d.?)|(%$)',re.IGNORECASE)



    is_edu=False
    lines=data.split('\n')
    
    for line_number, line in enumerate(lines):
       
       if edu_pattern.match(line):
           is_edu = True
       elif head_not_req.match(line):
            is_edu = False

       if is_edu:
           print(line)
           lines[line_number]=" "
       
       

    return