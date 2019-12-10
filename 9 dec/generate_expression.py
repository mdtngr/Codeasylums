#Generate the mathematical expression from the given expression

#{
#    "op": "equal",
#    "lhs": {
#        "op": "add",
#        "lhs": 1,
#        "rhs": {
#            "op": "multiply",
#            "lhs": "x",
#            "rhs": 10
#        }
#    },
#    "rhs": 21
#}

import json
n=[]

def cal(n):
#    print(type(n))
    str2=""
    for x in n.keys():
        
        if x=='op':                
            if(n[x]=='add'):
                    str2=str2+"+"
            if(n[x]=='subtract'):
                    str2=str2+"-"
            if(n[x]=='multiply'):
                    str2=str2+"*"
            if(n[x]=='divide'):
                    str2=str2+"/"
            if(n[x]=='equal'):
                    str2=str2+"="
                    
			
            
        elif x=='lhs':
            if type(n[x])==type(4):
#                print("here bro")
                str2= str(n[x]) + str2
           
            elif type(n[x])==type(n):
                str2= cal(n[x]) + str2
            elif type(n[x])==type("l"):
                str2=n[x]+str2
            

        elif x=='rhs':
            if type(n[x])==type(4):
                str2= str2 + str(n[x]);
            
            elif type(n[x])==type(n):
                str2= str2 + cal(n[x])
            elif type(n[x])==type("l"):
                str2=str2+n[x]
                
        
#        print(type(n[x]))
    return str2
             
            

with open('./data.txt') as file:
     data=json.load(file)
        

cal(data)

    
