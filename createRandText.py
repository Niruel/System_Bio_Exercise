import random
orginalFile = "AISdisease_4.txt"
filecontent = []
for i in range(5):
    i += 1
    ran = random.choice(list(open(orginalFile)))
    filecontent.append(ran)

    #contentres = filecontent

print(*filecontent, sep='')
file1 = open('AISvaccines.txt', 'w')
file1.writelines(filecontent)
file1.close()