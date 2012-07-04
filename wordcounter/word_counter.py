import sys

index=0
def counter(mystr):
	my_list=mystr.split()
	ans=dict([x,0] for x in my_list)
	for index in range(len(my_list)):
		if ans.has_key(my_list[index]):
			ans[my_list[index]]+=1
			print ans



if __name__ == "__main__":
	counter(sys.argv[1])
