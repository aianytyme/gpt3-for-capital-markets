import os
import re
import json

path = "C:\\GPT3-Project-Python\\openai-quickstart-python\\data\\archive\\extracted\\"
dir_list = os.listdir(path)
 
#List of 30 companies to consider
lst=[]
mainfile=open("C:\\GPT3-Project-Python\\openai-quickstart-python\\alldata_prompt_completion.jsonl","w")
for x in dir_list:    
    f=open(path+x, "r")
    data=f.read()
    jdata=json.loads(data)
    company_name=jdata['company']
    #print(company_name)
    lst.append(company_name)

#print(lst)
lst_to_consider=lst[0:30]
print(lst_to_consider)


print("Files and directories in '", path, "' :")

def getCleanString(str):
    str=str.replace("\r"," ")
    str=str.replace("\n","||")
    str=str.replace("\""," ")
    str=str.replace("	"," ")
    str=str.replace("Overview","Overview:")
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(special_char.search(str) == None):
        print('String does not contain any special characters.')
    else:
        print('The string contains special characters.')
        str=re.sub('[@_!#$%^&*()<>?/\|}{~:]'," ",str)
    return str
def getFormattedString(companyname,texttoadd):
    return "{\"prompt\":\"\",\"completion\":\""+companyname+":"+texttoadd+"\"}"

# prints all files
mainfile=open("C:\\GPT3-Project-Python\\openai-quickstart-python\\alldata_prompt_completion.jsonl","w")
for x in dir_list:
    #print(x)
    f=open(path+x, "r")
    data=f.read()
    jdata=json.loads(data)
    company_name=jdata['company']
    if company_name in lst_to_consider :
        length=len(jdata['item_1'])
        if length != None:
            print("Length of the item_1 is {0}".format(length))                    
        item_1=jdata['item_1'][0:3000]
        item_1=getCleanString(item_1);        
        str_1=getFormattedString(company_name,item_1)
        try:        
            mainfile.write(str_1)
            mainfile.write("\n")
        except:
            print("Error")
        
        #Item1, Item1A, Item_7

        ##For Item_10
        item_1A=jdata['item_1A'][0:3000]
        item_1A=getCleanString(item_1A);
        str_1A=getFormattedString(company_name,item_1A)
        try:        
            mainfile.write(str_1A)
            mainfile.write("\n")
        except:
            print("Error")

        ##For item  Item_7
        item_7=jdata['item_7'][0:3000]
        item_7=getCleanString(item_7);
        str_7=getFormattedString(company_name,item_7)
        try:        
            mainfile.write(str_7)
            mainfile.write("\n")
        except:
            print("Error")
