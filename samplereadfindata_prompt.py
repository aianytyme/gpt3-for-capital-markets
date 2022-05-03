import os
import re
import json

path = "C:\\GPT3-Project-Python\\openai-quickstart-python\\data\\archive\\extracted\\"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
mainfile=open("C:\\GPT3-Project-Python\\openai-quickstart-python\\alldata_prompt_completion.jsonl","w")
for x in dir_list:
    print(x)
    f=open(path+x, "r")
    data=f.read()
    
    ##data=data.replace("\r"," ")
    ##data=data.replace("\n"," ")
    jdata=json.loads(data)
    length=len(jdata['item_1'])
    if length != None:
        print("Length of the item_1 is {0}".format(length))                    
    item_1=jdata['item_1'][0:3000]
    #item_1=jdata['item_1']
    item_1=item_1.replace("\r"," ")
    item_1=item_1.replace("\n","||")
    item_1=item_1.replace("\""," ")
    item_1=item_1.replace("	"," ")
    item_1=item_1.replace("Overview","Overview:")
    company_name=jdata['company']
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(special_char.search(item_1) == None):
        print('String does not contain any special characters.')
    else:
        print('The string contains special characters.')
        item_1=re.sub('[@_!#$%^&*()<>?/\|}{~:]'," ",item_1)
    
    #print(jdata['item_1'])
    #print(jdata['company'])
    str="{\"prompt\": \"\", \"completion\": \""+company_name+":"+item_1.replace("Overview","Overview:")+"\"}"
    try:        
        mainfile.write(str)
        mainfile.write("\n")
    except:
        print("Error")
    
    ##For Item_10
    item_10=jdata['item_10'][0:3000]
    #item_10=jdata['item_1']
    item_10=item_10.replace("\r"," ")
    item_10=item_10.replace("\n","||")
    item_10=item_10.replace("\""," ")
    item_10=item_10.replace("	"," ")
    item_10=item_10.replace("Overview","Overview:")
    company_name=jdata['company']
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(special_char.search(item_10) == None):
        print('String does not contain any special characters.')
    else:
        print('The string contains special characters.')
        item_10=re.sub('[@_!#$%^&*()<>?/\|}{~:]'," ",item_10)
    
    #print(jdata['item_1'])
    #print(jdata['company'])
    str_10="{\"prompt\": \"\", \"completion\": \""+company_name+":"+item_10.replace("Overview","Overview:")+"\"}"
    try:        
        mainfile.write(str_10)
        mainfile.write("\n")
    except:
        print("Error")


