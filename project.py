# CS204 Project
# Read the .mc file as input
mcFile = open("input.mc","r+")
# File reading completed

#defining global variables________________________________________________________________________________
reg = [0]*32
RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,immed=[0]*25

ALUOp = [0]*29 
#instructions
#add 0, and 1, or 2, sll 3, slt 4, sra 5, srl 6, sub 7, xor 8, mul 9, div 10, rem   11
#addi 12, andi 13, ori 14 , lb 15, lh 16, lw 17, jalr 18
#sb 19, sw 20, sh 21
# beq 22, bne 23, bge 24, blt 25
# auipc 26, lui 27
# jal 28

dataMemory = {}
instructionMemory = {}

def Fetch():
    #Pc, ir
    global IR
    print("Fetching the instruction")
    IR = instructionMemory[hex(PC)]
    print(IR)

def Decode():
    print("Decoding the instruction")
    #getting the opcode
    global opcode
    opcode = int(str(IR),16) & int("0x7f",16)
    fun3 = (int(str(IR),16) & int("0x7000",16)) >> 12
    instruction = [0]*32
    print(opcode)
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
        immed40 = (int(str(IR),16) & int("0xF80",16)) >> 7
        print("immed40 : ",immed40)
        immed11to5 = (int(str(IR),16) & int("0xFE000000",16)) >> 20
        print("immed11to5 : ",immed11to5)
        immed = immed40 | immed11to5
        print("rs1 : ",RS1)
        print("rs2 : ",RS2)
        print("immed : ",immed)

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
        pass
    elif opcode==int("1101111",2): # UJ format
        pass
    else:
        print("invalid opcode")
        
def Execute():

    if 1 not in ALUOp:
        print("ERROR")
        exit(1)
        
    instructionType = ALUOp.index(1)
    #instructions
    #add 0, and 1, or 2, sll 3, slt 4, sra 5, srl 6, sub 7, xor 8, mul 9, div 10, rem   11
    #addi 12, andi 13, ori 14 , lb 15, lh 16, lw 17, jalr 18
    #sb 19, sw 20, sh 21
    # beq 22, bne 23, bge 24, blt 25
    # auipc 26, lui 27
    # jal 28
    InA = RA
    InB = (RB if MuxB_select==0 else immed)
    if instructionType==0:
        RY = InA+InB
    elif instructionType==1:
        RY = InA&InB
    elif instructionType==2:
        RY = InA|InB
    elif instructionType==3:
        RY = InA<<InB
    elif instructionType==4:
        RY = 1 if InA<InB else 0
    elif instructionType==5:
    elif instructionType==6:
    elif instructionType==7:
    elif instructionType==8:
    elif instructionType==9:
    elif instructionType==10:
    elif instructionType==11:
    elif instructionType==12:
    elif instructionType==13:
    elif instructionType==14:
    elif instructionType==15:
    elif instructionType==16:



    elif instructionType==17:
        RY = reg[RS1] + immed
    elif instructionType==18:
        EffAddress = reg[RS1] + immed

    elif instructionType==19:
        RY = reg[RS1] + immed
    elif instructionType==20:
        RY = reg[RS1] + immed
    elif instructionType==21:
        RY = reg[RS1] + immed
    elif instructionType==22:
        RY = 0
        if reg[RS1] == reg[RS2]:
            RY = 1
            PC = PC + immed
    elif instructionType==23:
        RY = 0
        if reg[RS1] != reg[RS2]:
            RY = 1
            PC = PC + immed
    elif instructionType==24:
        RY = 0
        if reg[RS1] >= reg[RS2]:
            RY = 1
            PC = PC + immed
    elif instructionType==25:
        RY = 0
        if reg[RS1] < reg[RS2]:
            RY = 1
            PC = PC + immed
    elif instructionType==26:
        reg[rd] = immed<<12 + PC
    elif instructionType==27:
        reg[rd] = immed<<12
    elif instructionType==28:
        

def MemoryAccess():
    pass

def RegisterUpdate():
    pass

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
