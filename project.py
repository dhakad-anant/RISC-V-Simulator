# CS204 Project

# TODO - 
# Instruction memory should be byte addressable
# Store dhange se karo

from collections import defaultdict

# Read the .mc file as input
mcFile = open("input.mc","r+")
# File reading completed

#defining global variables____________________________
reg = [0]*32
RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_Write,immed,PC_Temp,Mem_Write,Mem_Read=[0]*31

def GenerateControlSignals(reg_write,MuxB,MuxY,MemRead,MemWrite,MuxMA,MuxPC,MuxINC,numB):
    global RF_Write, MuxB_select, MuxY_select, MuxMA_select, MuxINC_select, MuxPC_select, Mem_Read, Mem_Write,numBytes

    RF_Write = reg_write
    MuxB_select = MuxB
    MuxY_select = MuxY
    Mem_Write = MemWrite
    Mem_Read = MemRead
    MuxMA_select = MuxMA
    MuxPC_select = MuxPC
    MuxINC_select = MuxINC
    numBytes = numB

ALUOp = [0]*15
#instructions
# add 0, sub 1, div 2, mul 3, remainder 4, xor 5,
# shift_left 6, shift_right_ari 7,shift_ri_lo 8, or 9,
# and 10, less_than 11, equal 12, not_equal 13, 
# greater_than_equal_to 14,


#Auxilary function______________
def sra(number,times):     #to change the function
    bx = bin(number)[2:]
    if len(bx)<32 or bx[0]=='0':
        return number>>times
    else:
        ans = '1'*times + bx[:32-times]
        twosCompli = [str(1-int(i)) for i in ans[1:]]
        twosCompli = (''.join(twosCompli))
        twosCompli = - (int(twosCompli,2) + 1)
        return twosCompli

#________________________

dataMemory = defaultdict(lambda : [0,0,0,0])
instructionMemory = defaultdict(lambda: [0,0,0,0])

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
        ans.reverse()
        ans = (''.join(ans))
        ans = '0x'+ans
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
    global opcode,immed,RS1,RS2,RD,RF_Write,MuxB_select,numBytes,RM,RA,RB, reg
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
        # # setting control signals ------------------------
        # MuxB_select =  0 # i.e choose RB
        # MuxY_select = 0 # i.e choose output from RZ
        # RF_write = 1 # i.e can write at register file
        # numBytes = 4
        # # ------------------------
        GenerateControlSignals(1, 0, 0, 0, 0, 0, 1, 0, 4)
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
        #setting ra rb rm -------------------------------------------------
        RA = reg[RS1]
        RB = reg[RS2] 
        RM = RB        # ---- DON'T CARES
        # -----------------------------------------------------------------
   
    elif opcode==int("0000011",2) or opcode==int("0010011",2) or opcode==int("1100111",2): # I format
        RD = (int(IR,16) & int('0xF80',16)) >> 7 # setting destination register
        RS1 = (int(IR,16) & int('0xF8000',16)) >> 15 # setting rs1 register
        immed = (int(IR,16) & int('0xFFF00000',16)) >> 20

        if opcode==int("0000011",2): # lb/lh/lw
            # # setting control signals ------------------------
            # MuxB_select =  1 # i.e choose Immediate
            # MuxY_select = 1 # i.e choose output from MDR
            # RF_write = 1 # i.e can write at register file
            # # ------------------------
            ALUOp[0]=1
            if fun3 == 0: #lb
                GenerateControlSignals(1,1,1,1,0,0,1,0,1)
            elif fun3 == 1: #lh
                GenerateControlSignals(1,1,1,1,0,0,1,0,2)
            elif fun3 == 2: #lw
                GenerateControlSignals(1,1,1,1,0,0,1,0,4)
            else:
                print("Wrong fun3 for lb/lh/lw")
                exit(1)
            #setting ra rb rm -------------------------------------------------
            RA = reg[RS1]
            # RB = reg[RS2]   ---- DON'T CARES
            # RM = RB         ---- DON'T CARES
            # -----------------------------------------------------------------
        elif opcode==int("0010011",2): #addi/andi/ori
            # # setting control signals ------------------------
            # numBytes = 4
            # MuxB_select =  1 # i.e choose Immediate
            # MuxY_select = 0 # i.e choose output from MDR
            # RF_write = 1 # i.e can write at register file
            # # ------------------------
            GenerateControlSignals(1,1,0,0,0,0,1,0,4)
            if fun3==0:#addi
                ALUOp[0]=1
            elif fun3==7:#andi
                ALUOp[10]=1
            elif fun3==6:#ori
                ALUOp[9]=1
            else:
                print("Error fun3 not matching for addi/andi/ori")
                exit(1)
            #setting ra rb rm -------------------------------------------------
            RA = reg[RS1]
            # RB = reg[RS2]   ---- DON'T CARES
            # RM = RB         ---- DON'T CARES
            # -----------------------------------------------------------------
        elif opcode==int("1100111",2): #jalr **ERROR(CHECK IT)****
            # # setting control signals ------------------------
            # MuxB_select =  1 # i.e choose Immediate
            # MuxY_select = 2 # i.e choose output from link register
            # RF_write = 1 # i.e can write at register file
            # # ------------------------
            GenerateControlSignals(1,0,2,0,0,0,0,1,4)
            if fun3==0:
                ALUOp[0]=1
            else:
                print("Error wrong fun3 for jalr")
                exit(1)
            #setting ra rb rm -------------------------------------------------
            RA = reg[RS1]
            # RB = reg[RS2]   ---- DON'T CARES
            # RM = RB         ---- DON'T CARES
            # -----------------------------------------------------------------

    elif opcode==int("0100011",2): # S format
        RS1 = (int(str(IR),16) & int("0xF8000",16)) >> 15
        RS2 = (int(str(IR),16) & int("0x1F00000",16)) >> 20
        immed4to0 = (int(str(IR),16) & int("0xF80",16)) >> 7
        immed11to5 = (int(str(IR),16) & int("0xFE000000",16)) >> 25
        immed = immed4to0 | immed11to5
        print("rs1 : ",RS1)
        print("rs2 : ",RS2)
        # # setting control signals ------------------------
        # MuxB_select =  1 # i.e choose Immediate
        # MuxY_select = 0 # i.e choose output from RY(BUT IT IS A DON'T CARE BCZ YOU CAN WRITE TO RF FILE)
        # RF_write = 0 # i.e can't write at register file
        # # ------------------------
        ImmediateSign(12)
        ALUOp[0]=1
        print("Immediate field : ",immed)
        if fun3 != int("000",2): # sb
            GenerateControlSignals(0,1,0,0,1,0,1,0,1)
        elif fun3 != int("001",2): # sh
            GenerateControlSignals(0,1,0,0,1,0,1,0,2)
        elif fun3 != int("010",2): # sw
            GenerateControlSignals(0,1,0,0,1,0,1,0,4)
        else:
            print("invalid fun3 => S format")
            exit(1)
            return
        #setting ra rb rm -------------------------------------------------
        RA = reg[RS2]
        RB = reg[RS1]
        RM = RB
        # -----------------------------------------------------------------
    elif opcode==int("1100011",2): # SB format
        RS1 = (int(IR, 16) & int("0xF8000", 16)) >> 15
        RS2 = (int(IR, 16) & int("0x1F00000", 16)) >> 20
        RA = reg[RS1]
        RB = reg[RS2]
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
            ALUOp[12] = 1
        elif(fun3 == 1):
            ALUOp[13] = 1
        elif(fun3 == 4):
            ALUOp[11] = 1
        elif(fun3 == 5):
            ALUOp[14] = 1
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
            ALUOp[0] = 1
            RA = PC
            immed = immed << 12
        else:
            ALUOp[6] = 1
            RA = immed
            immed = 12
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
        ALUOp[0] = 1
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

def Execute():
    global immed,ALUOp,RZ, reg
    operation = ALUOp.index(1)
    ALUOp = [0]*15
    InA = RA
    if(MuxB_select == 1):
        InB = immed
    else:
        InB = RB
    if(operation == 0): #add
        RZ = InA + InB
    elif(operation == 1): #sub
        RZ = InA - InB
    elif(operation == 2): #div
        if(InB == 0):
            print("Error : Division by zero")
            exit(1)
        RZ = InA/InB
    elif(operation == 3): #mul
        RZ = InA*InB
    elif(operation == 4): #remainder
        if(InB == 0):
            print("Error : Remainder by zero")
            exit(1)
        RZ = InA%InB
    elif(operation == 5): #xor
        RZ = InA^InB
    elif(operation == 6): #shift_left
        if (InB<0):
            print("Cannot  left shift a number negative times")
            exit(1)
        RZ = InA<<InB
    elif(operation == 7): #shift_right_ari 
        # ********************ERROR***************** WRITE SRA
        pass
    elif(operation == 8): #shift_ri_lo  
        RZ = InA>>InB
    elif(operation == 9): #or  
        RZ = (InA|InB)
    elif(operation == 10): #and  
        RZ = (InA&InB)
    elif(operation == 11): #less_than  
        RZ = (InA<InB)
    elif(operation == 12): #equal  
        RZ = (InA==InB)
    elif(operation == 13): #not_equal  
        RZ = (InA!=InB)
    elif(operation == 14): #greater_than_equal_to  
        RZ = (InA>=InB)
    # return RZ

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


def RegisterUpdate():
    global reg,RD
    print('register mein',RF_Write, RD)
    if RF_Write == 1:
        reg[RD] = RY

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
            #TODO : Add Validation______
            y = x.split('\n')[0].split()
            instructionMemory[y[0]][0] = hex(int(y[1],16) & int('0xFF',16))[2:]
            instructionMemory[y[0]][1] = hex((int(y[1],16) & int('0xFF00',16))>>8)[2:]
            instructionMemory[y[0]][2] = hex((int(y[1],16) & int('0xFF0000',16))>>16)[2:]
            instructionMemory[y[0]][3] = hex((int(y[1],16) & int('0xFF000000',16))>>24)[2:] 
            for i in range (4):
                instructionMemory[y[0]][i] = '0'*(2-len(instructionMemory[y[0]][i])) + instructionMemory[y[0]][i]
                instructionMemory[y[0]][i] = instructionMemory[y[0]][i].upper()
    # run simulator 
    run_RISC_simulator()
    # exit from the code

def run_RISC_simulator():
    Fetch()
    Decode()
    Execute()
    MemoryAccess()
    RegisterUpdate()
    print(reg)
main()
