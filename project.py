# CS204 Project
# Read the .mc file as input
mcFile = open("input.mc","r+")
# File reading completed

#defining global variables________________________________________________________________________________
reg = [0]*32
RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_write,immed=[0]*27

ALUOp = [0]*29 
#instructions
#add 0, and 1, or 2, sll 3, slt 4, sra 5, srl 6, sub 7, xor 8, mul 9, div 10, rem   11
#addi 12, andi 13, ori 14 , lb 15, lh 16, lw 17, jalr 18
#sb 19, sw 20, sh 21
# beq 22, bne 23, bge 24, blt 25
# auipc 26, lui 27
# jal 28


#Auxilary function________________________________________
def sra(x,n,m):     #to change the function
    if x & 2**(n-1) != 0:  # MSB is 1, i.e. x is negative
        filler = int('1'*m + '0'*(n-m),2)
        x = (x >> m) | filler  # fill in 0's with 1's
        return x
    else:
        return x >> m
#______________________________________________________________________

dataMemory = {}
instructionMemory = {}

def Fetch():
    #Pc, ir
    global IR
    print("Fetching the instruction")
    IR = instructionMemory[hex(PC)]
    print(IR)

def decimalToBinary(num, length):
    ans=""
    while(num>0):
        if(num&1):
            ans+='1'
        else:
            ans+='0'
        num = num//2
    for i in range(length-len(ans)):
        ans+='0'
    return ans[::-1]   

def Decode():
    print("Decoding the instruction")
    #getting the opcode
    global opcode
    print(int("0x7f", 16))
    opcode = int(str(IR),16) & int("7f",16)
    fun3 = (int(str(IR),16) & int("0x7000",16)) >> 12
    instruction = [0]*32
    print("Decoding Results :-")
    print("Opcode : "+decimalToBinary(opcode, 7))
    # R format - (add,srl,sll,sub,slt,xor,sra,and,or,) ( mul, div, rem)
    # R format - (0110011)(?)
    
    # I format - (lb,lh,lw,)(addi, andi, ori,)(jalr)
    # I format - (0000011)(0010011)(1100111)
    
    # S format - (sb, sw, sh)
    # S format - (0100011) f3 - sb - 000, sh - 001, sw - 010
    
    # SB format - beq, bne, bge, blt
    # SB format - (1100011) f3 - beq - 000, bne - 001, blt - 100, bge - 101
    
    # U format - auipc-0010111, lui-0110111
    
    # UJ format - jal-1101111


    if opcode==int("0110011",2): # r format
        pass
    elif opcode==int("0000011",2) or opcode==int("0010011",2) or opcode==int("1100111",2): # i format

        RD = (int(IR,16) & '0xF80') >> 7
        RS1 = (int(IR,16) & '0xF8000') >> 15
        immed = (int(IR,16) & '0xFFF00000') >> 20
        #to make error check

    elif opcode==int("0100011",2): # S format
        RS1 = (int(str(IR),16) & int("0xF8000",16)) >> 15
        RS2 = (int(str(IR),16) & int("0x1F00000",16)) >> 20
        immed4to0 = (int(str(IR),16) & int("0xF80",16)) >> 7
        immed11to5 = (int(str(IR),16) & int("0xFE000000",16)) >> 20
        immed = immed4to0 | immed11to5
        print("rs1 : ",RS1)
        print("rs2 : ",RS2)
        print("Immediate field : ",immed)

        #sb 19, sw 20, sh 21

        if fun3 != int("000",2):
            ALUOp[19]=1
        elif fun3 != int("010",2):
            ALUOp[20]=1
        elif fun3 != int("001",2):
            ALUOp[21]=1
        else:
            print("invalid fun3 => S format")
            exit(1)
            return
    elif opcode==int("1100011",2): # SB format
        pass
    elif opcode==int("0010111",2) or opcode==int("0110111",2): # U type
        RD = (int(IR, 16) & int("0xF80", 16)) >> 7
        print("rd : " + str(RD))
        immed = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
        print("Immediate field : " + str(immed))
    elif opcode==int("1101111",2): # UJ format
        RD = (int(IR, 16) & int("0xF80", 16)) >> 7
        print("rd : " + str(RD))
        immed_tmp = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
        immed = 0
        immed = immed | ((immed_tmp & int("0x7FE00", 16)) >> 9)
        immed = immed | ((immed_tmp & int("0x100", 16)) << 2)
        immed = immed | ((immed_tmp & int("0xFF", 16)) << 11)
        immed = immed | (immed_tmp & int("0x80000", 16))
        immed *= 2
        print("Immediate field : " + str(immed))
    else:
        print("invalid opcode")


# make the control signals global   
def Execute():
    if 1 not in ALUOp:
        print("ERROR")
        exit(1)  
    global immed, numBytes      
    instructionType = ALUOp.index(1)
    #instructions
    #add 0, and 1, or 2, sll 3, slt 4, sra 5, srl 6, sub 7, xor 8, mul 9, div 10, rem 11
    #addi 12, andi 13, ori 14 , lb 15, lh 16, lw 17, jalr 18
    #sb 19, sw 20, sh 21
    # beq 22, bne 23, bge 24, blt 25
    # auipc 26, lui 27
    # jal 28
    InA = RA
    InB = (RB if MuxB_select==0 else immed)
    if instructionType==0 or instructionType==12 or instructionType==18: # add, addi, jalr
        RZ = InA + InB
    elif instructionType==1 or instructionType==13: # and, andi
        RZ = InA & InB
    elif instructionType==2 or instructionType==14: # or,ori
        RZ = InA|InB
    elif instructionType==3: # left shift
        if (InB<0):
            print("Cannot left shift a number negative times")
            exit(1)
        RZ = InA << InB
    elif instructionType==4: # slt
        RZ = 1 if InA<InB else 0
    elif instructionType==5: # sra
        if (InB<0):
            print("Cannot right shift a number negative times")
            exit(1)
        RZ = sra(InA,32,InB) #to change the function
    elif instructionType==6: # srl
        if (InB<0):
            print("Cannot right shift a number negative times")
            exit(1)
        RZ = InA >> InB
    elif instructionType==7: #sub
        RZ = InA - InB
    elif instructionType==8: #xor
        RZ = InA ^ InB
    elif instructionType==9: # mul
        RZ = InA*InB
    elif instructionType==10: # div
        if(InB==0):
            print("Error... Cannot divide by zero exception")
            exit(1)
        RZ = InA/InB
    elif instructionType==11: # rem
        if(InB==0):
            print("Error... Cannot modulo number by zero exception")
            exit(1)
        RZ = InA % InB
    elif instructionType==15:  #lb
        RZ = InA+InB
        numBytes = 1
    elif instructionType==16: #lh
        RZ = InA + InB 
        numBytes = 2
    elif instructionType==17: #lw
        RZ = InA + InB
        numBytes = 4   
    elif instructionType==19: # sb
        RZ = InA + InB
        numBytes = 1
    elif instructionType==20: # sw
        RZ = InA + InB
        numBytes = 4
    elif instructionType==21: # sh
        RZ = InA + InB
        numBytes = 2
    elif instructionType==22: # beq
        if InA == InB:
            equal = 1         # control signal for branch; IAG      
    elif instructionType==23: # bne
        if InA != InB:
            notEqual = 1       # control signal for branch
    elif instructionType==24: # bge
        if InA >= InB:
            gequal = 1         # control signal for branch
    elif instructionType==25: # blt
        if InA < InB:
            less = 1           # control signal for branch
    elif instructionType==26: # auipc
        #todo
        pass
    elif instructionType==27: # lui  eg  lui x5, 0x2
        RZ = InB<<12
    elif instructionType==28: # jal jal x0, label
        RZ = PC + 4
        # add a control signal
        pass   # PC = label  # x0 = PC + 4
    
# def ALUControl():
#     InA = RA
#     if(operation == 0): #add
#         RY = InA + InB
#     elif(operation == 1): #sub
#         RY = InA - InB
#     elif(operation == 2): #div
#         if(InB == 0):
#             print("Error : Division by zero")
#             exit(1)
#         RY = InA/InB
#     elif(operation == 3): #mul
#         RY = InA*InB
#     elif(operation == 4): #remainder
#         if(InB == 0):
#             print("Error : Remainder by zero")
#             exit(1)
#         RY = InA%InB
#     elif(operation == 5): #or
#         RY = InA|InB
#     elif(operation == 6): #xor
#         RY = InA^InB
#     elif(operation == 7): #shift left
#         if (InB<0):
#             print("Cannot  left shift a number negative times")
#             exit(1)
#         RY = InA<<InB
#     elif(operation == 8): #shift right
#         if (InB<0):
#             print("Cannot  right shift a number negative times")
#             exit(1)
#         RY = InA>>InB
#     elif(operation == 9): #and
#         RY = InA&InB
#     elif(operation == 10): #less than
#         RY = (InA < InB)
#     elif(operation == 11): #comparator
#         RY = (InA == InB)
#     elif(operation == 12): #greater than equal to
#         RY = (InA >= InB)
#     return RY

def MemoryAccess():
    pass

def RegisterUpdate():
    if RF_write==1: 
        reg[RegFileAddrC] = RY


def validateDataSegment(y):
    if len(y)!=2:
        return False
    addr,data = y[0],y[1]
    if addr[:2]!='0x' or data[:2]!='0x':
        return False
    try:
        if int(addr,16)<int("0x10000000",16):
            return False
        int(data,16)
    except:
        return False 
    return True

def main():
    # load the data segment
    flag = 0
    for x in mcFile:
        #creating a hashmap, data segment stored
        y = x.split('\n')[0].split()
        if flag==1:
            if validateDataSegment(y)==False:
                print("ERROR")
                exit(1)
            dataMemory[y[0]] = y[1]
        if '$' in y:
            flag = 1
        if flag==0:
            #TODO : Add Validation______________
            y = x.split('\n')[0].split()
            instructionMemory[y[0]] = y[1]            
    # run simulator 
    run_RISC_simulator()
    # exit from the code

def run_RISC_simulator():
    Fetch()
    Decode()
    Execute()
    MemoryAccess()
    RegisterUpdate()

main()
