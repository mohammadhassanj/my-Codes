import sys
global who_is_first
global dic1
dic1={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","9":" ","7":" ","8":" "}
def start():
      who_is_first=raw_input("Who wants start first==>x/o\n")
      if who_is_first=="x":
         ask('x')
      elif who_is_first=='o':
         ask('o')
      else:
         print ("please Enter x or o MAN")
         start()

def print_board(dic):
   print 
   print 
   b="-----------"
   print " {} | {} | {}".format(dic1["1"],dic1["2"],dic1["3"])
   print b
   print " {} | {} | {}".format(dic1["4"],dic1["5"],dic1["6"])
   print b
   print " {} | {} | {}".format(dic1["7"],dic1["8"],dic1["9"])
def check(dic):
   list=dic_to_list(dic1)
   list_split=split_3(list)
   final_list=[]
   final_list.append(convert_list_str(list_split+zip(list_split[0],list_split[1],list_split[2])))
   final_list.append((list_split[0][0]+list_split[1][1]+list_split[2][2]))
   final_list.append((list_split[0][2]+list_split[1][1]+list_split[2][0]))
   if str(final_list).find("xxx")!=-1:
      return "xxx"
   elif str(final_list).find("ooo")!=-1:
      return "ooo"
   else:
   	  pass
   
def ask(person):
	if ' ' in [i for i in dic1.values()]:
		print 
		num=raw_input("what is your choice {}".format(person))
		while dic1[num]!=' ':
			print "!!!!!!!oops!!!!!!!!"
			print
			num=raw_input("This place is fill please select another place Mr {}\n".format(person))
		dic1[num]=person
		print_board(dic1)
		if check(dic1)=="xxx":
			print "======congragulation======"
			print
			print "     The x is winnner"
		elif check(dic1)=="ooo":
			print "======congragulation======"
			print
			print "     The O is winner"
		else:
			if "x" in person:
				person="o"
				ask(person)
			else:
				person='x'
				ask(person)
	else:
		print
		print "THE match has not winner"
		print
		askk=raw_input("do you want play again?")
		if askk=="y" or "yes":
			start()
		else:
			print "BE HAPPy"
			sys.exit()
		

def dic_to_list(dic):
	lis=[]
	for i in sorted(dic.keys()):
		lis.append(dic[i])
	return lis

def split_3(lis,b=0):
	# split our list to a 3 items list
	spli_list=[[],[],[]]
	for i in lis:
		spli_list[b].append(i)
		if len(spli_list[b])==3:
			b+=1
	return spli_list

def convert_list_str(list):
	b='';s=0
	for item in list:
		for i in item:
			if s==2:
				b+=i
				b+=','
				s=0
			else:
				b+=i
				s+=1
	return b

start()
