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
	print dict1
	for each_key in dict1:
		print "\n"
		sys.stdout.write(each_key+" ")
		for each_item in dict1[each_key]:
			sys.stdout.write(each_item+" ")

			

if __name__ == "__main__":
	input_str=sys.argv[1]
	mylist=input_str.split(",")
	anagramfinder(mylist)
