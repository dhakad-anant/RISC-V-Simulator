# CS204 Project

# TODO - 
# Instruction memory should be byte addressable
# Store dhange se karo

from collections import defaultdict

# Read the .mc file as input
mcFile = open("input.mc","r+")
# File reading completed

#defining global variables________________________________________________________________________________
reg = [0]*32
RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_write,immed,PC_Temp,Mem_Write,Mem_Read=[0]*29

def GenerateControlSignals(reg_write,MuxB,MuxY,MemRead,MemWrite,MuxMA,MuxPC,MuxINC,numB):
    global RF_write, MuxB_select, MuxY_select, MuxMA_select, MuxINC_select, MuxPC_select, Mem_Read, Mem_Write,numBytes

    RF_Write = reg_write
    MuxB_select = MuxB
    MuxY_select = MuxY
    Mem_Write = MemWrite
    Mem_Read = MemRead
    MuxMA_select = MuxMA
    MuxPC_select = MuxPC
    MuxINC_select = MuxINC
    numBytes = numB

ALUOp = [0]*28
#instructions
# add 0, sub 1, div 2, mul 3, remainder 4, xor 5,
# shift_left 6, shift_right_ari 7,shift_ri_lo 8, or 9,
# and 10, less_than 11, equal 12, not_equal 13, 
# greater_than_equal_to 14,


#Auxilary function________________________________________
def sra(x,m):     #to change the function
    bx = bin(x)[2:]
    if len(bx)<32 or bx[0]=='0':
        return x>>m
    else:
        ans = '1'*m + bx[:32-m]
        twosCompli = [str(1-int(i)) for i in ans[1:]]
        twosCompli = (''.join(twosCompli))
        twosCompli = - (int(twosCompli,2) + 1)
        return twosCompli

    # if x & 2**(n-1) != 0:  # MSB is 1, i.e. x is negative
    #     filler = int('1'*m + '0'*(n-m),2)
    #     x = (x >> m) | filler  # fill in 0's with 1's
    #     return x
    # else:
    #     return x >> m
#______________________________________________________________________

dataMemory = defaultdict(lambda : [0,0,0,0])
instructionMemory = {}

def ProcessorMemoryInterface():
    # Set MAR in Fetch

    if MuxMA_select == 0:
        temp = dataMemory[MAR][:numBytes]
        temp.reverse()
        ans = '0x'
        for i in temp:
            curr =  hex(i)[2:]
            ans += '0'*(2-len(curr)) + curr
        return ans

    else:
        ans = instructionMemory[MAR]
        return ans
    

def Fetch():
    #Pc, ir
    global IR,MAR,MuxMA_select, PC_Temp

    print("Fetching the instruction")
    MAR = hex(PC)
    MuxMA_select = 1
    IR = ProcessorMemoryInterface()
    PC_Temp = PC + 4
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
    global opcode,immed,RS1,RS2,RD,RF_write,MuxB_select,numBytes
    global ALUOp
    ALUOp = [0]*28
    opcode = int(str(IR),16) & int("0x7f",16)
    fun3 = (int(str(IR),16) & int("0x7000",16)) >> 12
    instruction = [0]*32
    print("Decoding Results :-")
    print("Opcode : "+decimalToBinary(opcode, 7))
    # R format - (add,srl,sll,sub,slt,xor,sra,and,or,mul, div, rem)
    # R format - (0110011)
    # I format - (lb-0,lh-1,lw-2)(addi-0, andi-7, ori-6,)(jalr-0)
    # I format - (0000011)(0010011)(1100111)
    # S format - (sb, sw, sh)
    # S format - (0100011) f3 - sb - 000, sh - 001, sw - 010
    # SB format - beq, bne, bge, blt
    # SB format - (1100011) f3 - beq - 000, bne - 001, blt - 100, bge - 101
    # U format - auipc-0010111, lui-0110111
    # UJ format - jal-1101111

    if opcode==int("0110011",2): # R format
        # setting control signals ------------------------
        MuxB_select =  0 # i.e choose RB
        MuxY_select = 0 # i.e choose output from RZ
        RF_write = 1 # i.e can write at register file
        numBytes = 4
        # ------------------------
        RD = (int(IR,16) & int('0xF80',16)) >> 7 # setting destination register
        RS1 = (int(IR,16) & int('0xF8000',16)) >> 15 # setting rs1 register
        RS2 = (int(IR,16) & int('0x1F00000',16)) >> 20 # setting rs2 register
        fun7 = (int(IR,16) & int('0xFE000000',16)) >> 25
        if fun3 == 0:  # add/sub/mul
            if fun7 == 0: # add 
                ALUOp[0]=1
            elif fun7 == 32: # subtract
                ALUOp[1]=1
            elif fun7==1: # mul
                ALUOp[3]=1 
            else:
                print("Invalid Func7 for Add/Sub")
                exit(1)
        elif fun3==7: # and
            if fun7==0:
                ALUOp[10]=1
            else:
                print("Invalid Fun7 for AND")
                exit(1)
        elif fun3 == 6: # or/remainder
            if fun7==0: # or
                ALUOp[9]=1
            elif fun7==1: # remainder
                ALUOp[4]=1
            else:
                print("Invalid Func7 for OR/REM")
                exit(1)
        elif fun3 == 1: # sll - shift_left
            if fun7==0:
                ALUOp[6]=1
            else:
                print("Invalid Func7 for SLL")
                exit(1)
        elif fun3 == 2: # slt - set_if_less_than
            if fun7==0:
                ALUOp[11]=1
            else:
                print("Invalid Func7 for SLT")
                exit(1)
        elif fun3 == 5: # srl/sra
            if fun7==32: # shift_ri_ari
                ALUOp[7]=1
            elif fun7==0: #shift_ri_lo
                ALUOp[8]=1
            else:
                print("Invalid Func7 for SRA/SRL")
                exit(1)
        elif fun3 == 4: #xor/div
            if fun7==0: # xor
                ALUOp[5]=1
            elif fun7==1: #div
                ALUOp[2]=1
            else:
                print("Invalid Func7 for XOR/div")
                exit(1)
        else:
            print("fun3 not matching in R format")
            exit(1)

    elif opcode==int("0000011",2) or opcode==int("0010011",2) or opcode==int("1100111",2): # I format
        RD = (int(IR,16) & int('0xF80',16)) >> 7 # setting destination register
        RS1 = (int(IR,16) & int('0xF8000',16)) >> 15 # setting rs1 register
        immed = (int(IR,16) & int('0xFFF00000',16)) >> 20
        ImmediateSign(12)

        if opcode==int("0000011",2): # lb/lh/lw
            # setting control signals ------------------------
            MuxB_select =  1 # i.e choose Immediate
            MuxY_select = 1 # i.e choose output from MDR
            RF_write = 1 # i.e can write at register file
            # ------------------------
            ALUOp[0]=1
            if fun3 == 0: #lb
                numBytes = 1
            elif fun3 == 1: #lh
                numBytes = 2
            elif fun3 == 2: #lw
                numBytes = 4
            else:
                print("Wrong fun3 for lb/lh/lw")
                exit(1)
        elif opcode==int("0010011",2): #addi/andi/ori
            # setting control signals ------------------------
            numBytes = 4
            MuxB_select =  1 # i.e choose Immediate
            MuxY_select = 0 # i.e choose output from MDR
            RF_write = 1 # i.e can write at register file
            # ------------------------
            if fun3==0:#addi
                ALUOp[0]=1
            elif fun3==7:#andi
                ALUOp[10]=1
            elif fun3==6:#ori
                ALUOp[9]=1
            else:
                print("Error fun3 not matching for addi/andi/ori")
                exit(1)
        elif opcode==int("1100111",2): #jalr ****************ERROR(CHECK IT)**************************
            # setting control signals ------------------------
            MuxB_select =  1 # i.e choose Immediate
            MuxY_select = 2 # i.e choose output from link register
            RF_write = 1 # i.e can write at register file
            # ------------------------
            if fun3==0:
                ALUOp[0]=1
            else:
                print("Error wrong fun3 for jalr")
                exit(1)

    elif opcode==int("0100011",2): # S format
        RS1 = (int(str(IR),16) & int("0xF8000",16)) >> 15
        RS2 = (int(str(IR),16) & int("0x1F00000",16)) >> 20
        immed4to0 = (int(str(IR),16) & int("0xF80",16)) >> 7
        immed11to5 = (int(str(IR),16) & int("0xFE000000",16)) >> 25
        immed = immed4to0 | immed11to5
        print("rs1 : ",RS1)
        print("rs2 : ",RS2)
        # setting control signals ------------------------
        MuxB_select =  1 # i.e choose Immediate
        MuxY_select = 0 # i.e choose output from RY(BUT IT IS A DON'T CARE BCZ YOU CAN WRITE TO RF FILE)
        RF_write = 0 # i.e can't write at register file
        # ------------------------
        ImmediateSign(12)
        ALUOp[0]=1
        print("Immediate field : ",immed)
        if fun3 != int("000",2): # sb
            numBytes = 1
        elif fun3 != int("010",2): # sw
            numBytes = 4
        elif fun3 != int("001",2): # sh
            numBytes = 2
        else:
            print("invalid fun3 => S format")
            exit(1)
            return

    elif opcode==int("1100011",2): # SB format
        RS1 = (int(IR, 16) & int("0xF8000", 16)) >> 15
        RS2 = (int(IR, 16) & int("0x1F00000", 16)) >> 20
        imm1 = (int(IR, 16) & int("0xF80", 16)) >> 7
        imm2 = (int(IR, 16) & int("0xFE000000", 16)) >> 25
        immed = 0
        immed = immed | ((imm1 & int("0x1E", 16)) >> 1)
        immed = immed | ((imm2 & int("0x3F", 16)) << 4)
        immed = immed | ((imm1 & 1) << 10)
        immed = immed | (((imm2 & int("0x40", 16)) >> 6) << 11)
        ImmediateSign(12)
        immed *= 2
        print("Immediate field : ", immed)
        # Setting control Signals
        if(fun3 == 0):
            ALUOp[22] = 1
        elif(fun3 == 1):
            ALUOp[23] = 1
        elif(fun3 == 4):
            ALUOp[25] = 1
        elif(fun3 == 5):
            ALUOp[24] = 1
        else:
            print("Invalid fun3 for SB Format instruction. Terminating the program.")
            exit(1)
        GenerateControlSignals(0,0,0,0,0,0,0,1,0)

    elif opcode==int("0010111",2) or opcode==int("0110111",2): # U type
        RD = (int(IR, 16) & int("0xF80", 16)) >> 7
        print("rd : " + str(RD))
        immed = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
        ImmediateSign(20)
        print("Immediate field : " + str(immed))
        if(opcode == int("0010111", 2)):
            ALUOp[26] = 1
            GenerateControlSignals(0,1,0,0,0,0,0,1,0)
        else:
            ALUOp[27] = 1
            GenerateControlSignals(1,1,0,0,0,0,0,0,0)
    elif opcode==int("1101111",2): # UJ format
        RD = (int(IR, 16) & int("0xF80", 16)) >> 7
        print("rd : " + str(RD))
        immed_tmp = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
        immed = 0
        immed = immed | ((immed_tmp & int("0x7FE00", 16)) >> 9)
        immed = immed | ((immed_tmp & int("0x100", 16)) << 2)
        immed = immed | ((immed_tmp & int("0xFF", 16)) << 11)
        immed = immed | (immed_tmp & int("0x80000", 16))
        ImmediateSign(20)
        immed *= 2
        print("Immediate field : " + str(immed))
        GenerateControlSignals(1,1,2,0,0,0,0,1,0)
    else:
        print("invalid opcode")

def ImmediateSign(num):
    global immed
    if(immed & 2**(num-1) == 0):
        return
    immed = immed ^ (2**num-1)
    immed += 1
    immed *= (-1)


# make the control signals global   
def Execute():
    if 1 not in ALUOp:
        print("ERROR")
        exit(1)  
    global immed    
    instructionType = ALUOp.index(1)
    #instructions
    #add 0, and 1, or 2, sll 3, slt 4, sra 5, srl 6, sub 7, xor 8, mul 9, div 10, rem 11
    #addi 12, andi 13, ori 14 , lb 15, lh 16, lw 17, jalr 18
    #sb 19, sw 20, sh 21
    # beq 22, bne 23, bge 24, blt 25
    # auipc 26, lui 27
    InA = RA
    InB = (RB if MuxB_select==0 else immed)
    if instructionType==0 or instructionType==12 or instructionType==15 or instructionType==16 or instructionType==17 or instructionType==18 or instructionType==19 or instructionType==20 or instructionType==21: # add, addi, jalr sb sw lb lh lw sh
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
        RZ = sra(InA,InB) #to change the function
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
    elif instructionType==22: # beq
        if InA == InB:
            RZ = 1         # control signal for branch; IAG  
        else:
            RZ = 0    
    elif instructionType==23: # bne
        if InA != InB:
            RZ = 1       # control signal for branch
        else:
            RZ = 0
    elif instructionType==24: # bge
        if InA >= InB:
            RZ = 1       # control signal for branch
        else:
            RZ = 0
    elif instructionType==25: # blt
        if InA < InB:
            RZ = 1      # control signal for branch
        else:
            RZ = 0
    elif instructionType==26 or instructionType==27: # auipc
        RZ = InB<<12

def MemoryAccess():
    # =========== CHECK =============
    global MAR,RY

    if MuxY_select == 0:
        RY = RZ
    elif MuxY_select == 1:
        MAR = RZ
        RY = ProcessorMemoryInterface()
    elif MuxY_select == 2:
        RY = PC_Temp
    

    # if instructionType == 15:
    #     MDR = int(dataMemory[MAR],16) & (int('0xFF',16))
    # elif instructionType == 16:
    #     MDR = int(dataMemory[MAR],16) & (int('0xFFFF',16))
    # elif instructionType == 17:
    #     MDR = int(dataMemory[MAR],16)
    # elif instructionType == 19:
    #     dataMemory[MAR] = hex(MDR & int('0xFF',16))
    # elif instructionType == 20:
    #     dataMemory[MAR] = hex(MDR)
    # elif instructionType == 21:
    #     dataMemory[MAR] = hex(MDR & int('0xFFFF',16))
    # pass

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
            dataMemory[y[0]][0] = int(y[1],16) & int('0xFF',16)
            dataMemory[y[0]][1] = int(y[1],16) & int('0xFF00',16)
            dataMemory[y[0]][2] = int(y[1],16) & int('0xFF0000',16)
            dataMemory[y[0]][3] = int(y[1],16) & int('0xFF000000',16)

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
