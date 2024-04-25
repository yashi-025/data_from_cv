import pandas as pd
import re
import designation

def  extract_date(file):
    #print(doc)
    pos = []
    i = 0
    for line in file:
        date = re.findall(re.compile(r'(\d{4}[-/]\d{1,2})|((?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[,. ]*\d{4})|(\d{4}[-/]\d{4})'), line)
        #print ('line==',file[i])
        if len(date)>0 and len(line)<25:
            
            print(date, line)
            pos.append(i)
        i = i +1
    print(pos)

    index = 1
    if len(pos) >1:
        for x in pos:
            #check previous few
            print('-----------------------------------------------------------------')
            print(x, index, file[x])
            y, post = check_cur_post(file, x)
            if post != "":
                checkCompanyAroundDesignation(post, y)
            print(index, len(pos))
            check_cur_desc(file, x, pos[index])
            if index + 1 < len(pos):
                index = index + 1




def  check_cur_post(file, x):
    print("------------- POST-----------")
    desigHighlo = designation.loadDesigns()
    #desigHighlo = ["CTO","Director", "Principal","PMTS", "Architect", "Staff Software", "Full Stack", "LMTS", "Lead", "Product Owner", "SMTS", "Software","Technical", "Developer","Programmer", "Analyst", "Associate",  "Fresher", "Intern"]
    y = x-20
    while y < x:
        if len(file[y]) < 50:
            #print(file[y])
            for dgn in desigHighlo:
                if dgn.lower() in set(file[y].lower().split()):
                    #print( dgn.lower())
                    design = designation.checkAround(dgn, file[y])
                    return y, design
                    #break


            #print(file[y])
        y = y + 1
    return 0, ""




def  check_cur_desc(file, x, z):
    print("-----------Job Details------------------", x , z)
    if (x==z):
        z = len(file)
    flag = 0
    while x < z:
        if len(file[x]) > 50:
            print(file[x])
            flag = 1
        else: 
            if flag == 1:
                break
        x = x+1

def checkCompanyAroundDesignation(post, y):
    print(post,y)
        #doc.append(line)
    # with open(r'C:\Personal\projects\learning\data\Resume-Parser-Using-NLP\preData\dates.txt') as file:
    #     print('file:', file)
    #     for line in file:
    #         doc.append(line)
    #     print(doc)
    # ori_df = pd.Series(doc)
    # ori_df.head(10)
    # #Applying Regex with pandas
    # ori_df = ori_df.str.extract('(\d{2,4}[-/]\d{1,2})|(\d{1,2}[-/]\d{1,2}[/-]\d{2,4})|(\d{1,2}/\d{4})|((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[ -.]*\d{2}[thsdn, .-]*\d{4})|((?:\d{1,2} )?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[,. ]*\d{4})|(\d{4})')
    
    # print(ori_df)
    # ori_df.iloc[271,4] = ""
    # ori_df.iloc[271,3] = "August 2008"
    # df = ori_df
    # print(df.head(5))
    # print(df.tail(5))
    # df = df.fillna('')
    # print(df.head(5))
    # print(df.tail(5))
    # df['dates'] = df[[0,1,2,3,4]].apply(lambda x: ''.join(x), axis=1)
    # df['dates']