##############33 Get all query from controller
import scan
#def get_query_from_controller_and_function(url,controller,function):
#    files="/root/laravel-ecommerce/app/Http/Controllers/" + controller
#    controller_file = open(files,"r") 
def get_function(string):
    result = ""
    if ( "public function" in string ):
        result = string
    return result

def get_query(string):
    result=""
    model_file = open("sub_folder/model_files.txt","r")
    model_file = model_file.readlines()
    for i in range(0,len(model_file)):
        model_file[i]=model_file[i].replace("\n","")
    for i in model_file:
        tmp= i+"::"
        if (tmp in string):
            result= string
        tmp= "new "+i
        if (tmp in string):
            result= string
    return result




#def get_query(file_directory):
#    count_total=0
#    model_file = open("sub_folder/model_files.txt","r")
#    model_file = model_file.readlines()
#    for i in range(0,len(model_file)):
#        model_file[i]=model_file[i].replace("\n","")
#    controller_file = open(file_directory,"r")
#    lines = controller_file.readlines()
#    for i in lines:
#        for j in model_file:
#            tmp=j+"::"
#            if (tmp in i):
#                print i.strip()
#            tmp="new "+j
#            if (tmp in i):
#                print i.strip()

file_directory="/root/laravel-ecommerce/app/Http/Controllers/Shop.php"
controller_file = open(file_directory,"r")
lines = controller_file.readlines()
string=""
for i in lines:
    if (scan.Del_space(i) ==""):
        continue
    #print scan.Del_kep(i)
    if (scan.Del_kep(i) == "1"):
        continue
##### Remove all comment
    tmp=scan.Del_comment(i)
    if (tmp == ""):
        continue
    else:
        i=tmp
##### Remove all HTML line
    tmp=scan.Del_html(i)
    if (tmp == ""):
        continue
    else:
        i=tmp

            ############# Check ";" ###########
    if (scan.check_sub_comma(i)==1):
        string=string + " " +scan.Del_space(i).replace("\n"," ")
        continue
    else:
        string=string + " " +scan.Del_space(i).replace("\n"," ")
        
##### Remove Block comment 
#    tmp=scan.Del_block_comment(string)
#    print tmp
#    if (tmp == ""):
#        continue
#    else:
#        string=tmp
#            #############
    result=""
    result=get_function(string)
    if (result != ""):
        print result
       # continue
    result=get_query(string)
    if (result != ""):
        print result
       # continue
    string = ""
