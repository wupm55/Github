import json
import pprint

a="""A	B	C	D	E	F
123	3	125	126	127	12
298	24	25	26	23 	28"""

def toNumber(data):
    if data.isnumeric():
        return float(data)
    else:
        return data    


def str2DList(tableString):
# table string is string delimted by \n, and \t   like 
# a="""A	B	C	D	E	F
#      123	12	125	126	127	128
#     298	24	25	26	27	28"""
# to list [['123', '124', '125', '126', '127', '128'], ['298', '24', '25', '26', '27', '28']]
    lineStr = tableString.split('\n') 
    lines=[]   # lines is a 2D array ,fully delimited
    for item in lineStr:
        i = item.split('\t')
        lines += [i]   
    title = lines.pop(0)
    return (title,lines)        

def line2Ditc(title,line):
    # line is 1D list of data only,like[1,2,3]
    # title is 1D list of keys
    # d is dict which is "title[1]":line[1]
    # this functiion is to convert to {'a':1,'b':2,'c':3}
    d={}
    i=0 #i is index for title
    for item in line:
        d[title[i]]= toNumber(item)
        i+=1
    return d

def lines2Dicts(title,lines):
# lines is 2D list like [[1,2,3],[4,5,6]]    
# title is 1D keys [a,b,c]
# this function to convert 2D list with a title to a list of dict [{'a':1,'b':2,'c':3},
# {'a':4,'b':5,'c':6}]
    x=[]
    for i in lines:
        x+=[line2Ditc(title,i)]
    return x

def table2Dicts(tableString):
    (title,lines)=str2DList(tableString)
    return lines2Dicts(title,lines)

def table2Json(tableString):
    data=table2Dicts(tableString)
    return json.dumps(data)

jj=table2Json(a)
pprint.pprint(jj)

def json2Dicts(jsonString):
    dicts=eval(jsonString)
    return dicts

def dicts2List(dicts):
    # dicts are the list of dict [{"a":1,"b":2},{"a":21,"b":22}]
    # this function is covert dicts to table ["a","b"],and [[1,2],[21,22]]
    title=list(dicts[0].keys())
    data=[]
    for l in dicts:
        data += [list(l.values())]
    return (title,data)

def lists2Table(title,data):
    # this function is covert list ["a","b","c"],and [[1,2,3],[4,5,6]]] to table string 
    # "a b c
    #  1 2 3
    #  4 5 6"
    table=""
    for t in title:
        table += (t + "\t")
    table += "\n"
    for dl in data:
        for d in dl:
            table += (str(d) + "\t")
        table +="\n"    
    return table    

def json2Table(jsonString):
    dicts=json2Dicts(jsonString)
    (title,data)=dicts2List(dicts)
    table=lists2Table(title,data)
    return table       


table=json2Table(jj)
print(table)
print(a)

