import sys
from copy import deepcopy
mydict={}
dict1={}
def anagramfinder(alist):
	index=0
	cmp_wrd=0
	for index in range(len(alist)):
		mydict[alist[index]]=[ ]
		for cmp_wrd in range(index+1,len(alist)):
			if cmp(sorted(alist[index]),sorted(alist[cmp_wrd])) == 0:
				mydict[alist[index]].append(alist[cmp_wrd])
	dict1 = deepcopy(mydict)
	for each_key in mydict:
		for each_item in mydict[each_key]:
			if dict1.has_key(each_item):
				del dict1[each_item]
	returnstr=" "
	for each_key in dict1:
		returnstr=returnstr+"\n"
		returnstr=returnstr+(each_key)+" "
		for each_item in dict1[each_key]:
			returnstr=returnstr+(each_item)+" "

	return returnstr		

if __name__ == "__main__":
	inp_file=sys.argv[1]
	indata=open(inp_file,'r')
	input_str=indata.readline()
	newlist=input_str.split(",")
	anagramfinder(newlist)
	indata.close()
	opt_file=sys.argv[2]
	outdata=open(opt_file,'w')
	outdata.write(anagramfinder(newlist))
	outdata.close()
	
