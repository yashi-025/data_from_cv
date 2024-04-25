def loadDesigns():
    return ["CTO","Director", "Principal","PMTS", "Architect", "Manager", "Head", "Staff Software", "Full Stack", "LMTS", "Lead", "Product Owner", "Consultant", "SMTS","Member", " Software Engineer","Software","Technical", "Developer","Programmer", "Analyst", "Associate",  "Fresher", "Intern"]
def extract_designation(data):
    #designations = set(open('./preData/designation.txt').read().splitlines())
    desigHighlo = loadDesigns()
    default = "Software Engineer"
    for dgn in desigHighlo:
        for line in data:
            if dgn.lower() in set(line.lower().split()):
                #print( dgn.lower(), line)
                return checkAround(dgn, line)

    return default

def checkAround(dgn, line):
    aroundLeft = {"Delivery Project","Sr. Engineering","Project", "Engineering", "Bussiness", "Lead", "Team", "Sr.", "Senior", "Technical", "Associate"}
    aroundRight = {"Engineer", "Software Engineer", "Lead", "Analyst", "Software Developer"}

    for pre in aroundLeft:
        dgnPlus = pre + " " + dgn
        if dgnPlus.lower() in line.lower() :
            #print(dgnPlus, line)
            return dgnPlus
        
    for post in aroundRight:
        dgnPlus = dgn + " " + post
        if dgnPlus.lower() in line.lower() :
            #print(dgnPlus, line)
            return dgnPlus

    return dgn