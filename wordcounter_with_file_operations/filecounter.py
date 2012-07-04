import sys

index=0
def counter(mystr):
	my_list=mystr.split()
	ans=dict([x,0] for x in my_list)
	for index in range(len(my_list)):
		if ans.has_key(my_list[index]):
			ans[my_list[index]]+=1
	newstr=""
	for each_key in ans:	
		intr_str=str(ans[each_key])
		newstr=newstr+each_key+" "+intr_str+"\n"

	return newstr


if __name__ == "__main__":
	inp_file=sys.argv[1]
	indata=open(inp_file,'r')
	mystring=indata.readline()
	counter(mystring)
	indata.close()
	opt_file=sys.argv[2]
	outdata=open(opt_file,'w')
	outdata.write(counter(mystring))
	outdata.close()
