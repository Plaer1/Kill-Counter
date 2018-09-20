import fileinput

total = open("totalkills", "r")
tmp = int(total.read().rstrip())
tmp +=1
total.close()
total = open("totalkills", "w")
total.write(str(tmp))
total.close()

total = open("tmpkills", "r")
tmp = int(total.read().rstrip())
tmp +=1
total.close()
total = open("tmpkills", "w")
total.write(str(tmp))
total.close()
