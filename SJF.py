readyq=[]
no=input("Enter number of processes ")
#print "Total processes: ", no

for i in range(no):	#inputting processes
	process=[]
	pname=raw_input("Process name: ")
	process.append(pname)
	atime=input("Arrival time: ")
	process.append(atime)
	btime=input("Burst time  : ")
	process.append(btime)
	readyq.append(process)
print("Before: ")
print readyq

#sorting the readyq
for i in range(no):	#outer loop executing for all processes
	j=i+1
	while j<no:	#inner loop going from j till last process
		if readyq[i][2]>readyq[j][2]:	#sort in increasing order of btime. swap if true
			readyq[i], readyq[j]=readyq[j], readyq[i]
		j+=1

print("After: ")
print readyq

delcount=0
i=0
while len(readyq)>0:
	i+=1
	if i==readyq[0][1]+readyq[0][2] :	#check finish time: if timer= atime+btime 
		delcount=delcount+1
		print "..Process ", readyq[0][0], " executed"
		del readyq[0]
					
print readyq
print delcount, "processes executed" 


						

