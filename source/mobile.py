import re

def extract_mobile_number(resume_text, lines):
    phone = re.findall(re.compile(r'(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), resume_text)
    #phone = re.findall(re.compile(r'(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?'), resume_text)

    if phone:
        number = ''.join(phone[0])
        #print('resex:', number)
        # if len(number) >= 10:
        #     return number
        # else:
        #     return number
        #verify number
        num = number
        if len(number)>5 :
            num = number[5:]
            for line in lines:
                #print(line)
                ll = line.replace('-','')
                if num in ll:
                    return checkAround(num, ll)


        return num
    
def  checkAround(num, line):
    index = line.index(num)
    #print('line:', line)
    s = index
    e = index
    while (s>0 and (line[s-1] == ' ' or  (line[s-1]>='0' and line[s-1]<='9'))):
        s = s-1
    while ( e < len(line) - 1 and (line[e+1] == ' ' or (line[e+1]>='0' and line[e+1]<='9'))):
        e = e+1

    num = line[s:e+1].replace(' ','').replace('-','').replace('.','')
    #print('correct Mobile', num, s, e)
    return num
# print('Mobile Number: ',extract_mobile_number(textinput))