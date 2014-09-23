"""
Author : Bhavul Gauri

Modify! Make it better, and add your name above!
"""

import csv

p_id = []
cpu_time = []
start_time = []

def read_problem(file_name):
	global p_id,cpu_time,start_time
	with open(file_name,'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			#print row
			p_id.append(row[0])
			cpu_time.append(row[1])
			start_time.append(row[2])


def fcfs():
	"""
	first come first server
	"""
	dict = {}	#start time will be the key.
	for i in range(0,len(start_time)):
		dict[int(start_time[i])] = [p_id[i],cpu_time[i]]		#If I don't convert to int, it takes 11 as a string and puts it after 1 an before 2. :P
	t = 0 #time
	w = 0
	for key in sorted(dict):
		a = dict[key]
		w += t;
		print "from t = %-5s to t = %-5s => P%-5s   " % (int(t),int(t)+int(a[1]),int(a[0]))
		t += int(a[1])
	w = w/float(len(dict))
	print "\n Average waiting time : %-2.2f" % (w)

def sjf():
	"""
	Shortest job first
	
	here, you'll first give priority to time and then the cpu burst time. See, how many processes have really arrived. 
	If something has arrived, then check it's cpu burst time.

	need : 3 original arrays, 1 rdy queue, tempExecEnd, tempExecEnd2, arrayForIndices

	algo : 
	> Put the arrival times and cpu burst times and pids in three arrays with corresponding indexes - call 'em original arrays
	> Find the smallest arrival time. Check how many processes are coming then.
	
	"""
	




file_name = raw_input("Enter the file name : ")
read_problem(file_name)
print "=====FCFS======"
fcfs()
print "\n=====SJF======"
#sjf()

