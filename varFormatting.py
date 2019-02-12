file = open("statsStuff.txt")
file2 = open("newStatsStuff.txt","w")

for line in file:
    temp = line.split()
    file2.write("        self." +temp[0] +" = data['"+temp[0] +"']\n")
file.close()
file2.close()
