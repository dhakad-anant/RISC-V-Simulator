# for i in range (16):
#     # self.reg1.setText('x0:' +str(ProcessingUnit.reg[0]))
#     print("self.reg"+str(i+1)+".setText('x"+str(i+16)+": ' + str(ProcessingUnit.reg["+str(i+16)+"]))")

a = input()
b = []
while(a!='$'):
    a = a.split()
    b.extend(a[:1])
    a = input()
for i in b:
    print(i,end=",")
print()