def load_skills():
    skillSets =  set(open('./coreSkills.txt').read().splitlines())
    #print(skillSets)
    # for item in skillSets:
    #     print(item)


    return skillSets


def extract_techSkills(data):
    skillSets = set(open('./preData/techSkills.txt').read().splitlines())
    skills = []
    #print(data)
    for skillLine in data:
        temp = skillLine.lower()
        for skill in skillSets:
            if ((' '+ skill.lower()) or (skill.lower() + ' ')) in temp:
                if skill not in skills:
                    skills.append(skill)
    #print(skills)
    return skills

def extract_coreSkills(data):
    skillSets = set(open('./preData/coreSkills.txt').read().splitlines())
    skills = []
    #print(data)
    for skillLine in data:
        temp = skillLine.lower()
        for skill in skillSets:
            if ((' '+ skill.lower()) or (skill.lower() + ' ')) in temp:
                if skill not in skills:
                    skills.append(skill)
    #print(skills)
    return skills