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
	bug : you can't provide same arrival times for two processes. They have to differ by a second at least! cuz keys can't be same.

	here, you'll first give priority to time and then the cpu burst time. See, how many processes have really arrived. 
	If something has arrived, then check it's cpu burst time.

	> make a list of processes that are there at t.
	> sort them according to their cpu_time.
	> print and stuff.
	"""
	dicto = {}	#start time will be the key.
	current = {}
	for i in range(0,len(start_time)):
		dicto[int(start_time[i])] = [p_id[i],cpu_time[i]]
	length = len(dicto)
	t = 0 #time
	w = 0	#for average waiting time.	
	for key in sorted(dicto):
		current = {}
		if(int(key) <= int(t)):
			current[int(key)] = dicto[key]

	for key1 in sorted(current):
		a = current[key1]
		w += t
		print "from t = %-5s to t = %-5s => P%-5s	" % (int(t),int(t)+int(a[1]),int(a[0]))
		t += int(a[1])
		del dicto[int(key1)]		
		break

		"""
		a = dict[key]	#gets an array of pid (0th index) and start_time (1st index).
		w += t;
		print "from t = %-5s to t = %-5s => P%-5s   " % (int(t),int(t)+int(key),int(a[0]))
		t += int(key)
		"""
	w = w/float(length)
	print "\n Average waiting time : %-2.2f" % (w)




file_name = raw_input("Enter the file name : ")
read_problem(file_name)
print "=====FCFS======"
fcfs()
print "\n=====SJF======"
#sjf()

