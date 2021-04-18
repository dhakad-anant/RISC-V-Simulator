# CS204 Project
from collections import defaultdict
import sys ,os
# File reading completed
#defining 

class CPU:

    reg = [0]*32
    reg[2] = int("0x7FFFFFF0",16) # sp - STACK POINTER
    reg[3] = int("0x10000000",16) # pointer to begining of data segment

    clk = 0

    RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_Write,immed,PC_Temp,Mem_Write,Mem_Read=[0]*31


    isStepClicked = 0

    run = 0


    def GenerateControlSignals(self,reg_write,MuxB,MuxY,MemRead,MemWrite,MuxMA,MuxPC,MuxINC,numB):
        

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


    #Auxilary function______
    def init(self):
        
        ALUOp = [0]*15
        RS1,RS2,RD,RM,RZ,RY,RA,RB,PC,IR,MuxB_select,MuxC_select,MuxINC_select,MuxY_select,MuxPC_select,MuxMA_select,RegFileAddrA,RegFileAddrB,RegFileAddrC,RegFileInp,RegFileAOut,RegFileBOut,MAR,MDR,opcode,numBytes,RF_Write,immed,PC_Temp,Mem_Write,Mem_Read=[0]*31
        reg = [0]*32
        reg[2] = int("0x7FFFFFF0",16) # sp - STACK POINTER
        reg[3] = int("0x10000000",16) # pointer to begining of data segment
        dataMemory = defaultdict(lambda : [0,0,0,0])
        instructionMemory = defaultdict(lambda: [0,0,0,0])

    def sra(self,number,times):     #correct function
        bx = bin(number)[2:]
        if len(bx)<32 or bx[0]=='0':
            return number>>times
        else:
            ans = '1'*times + bx[:32-times]
            twosCompli = [str(1-int(i)) for i in ans[1:]]
            twosCompli = (''.join(twosCompli))
            twosCompli = - (int(twosCompli,2) + 1)
            return twosCompli


    #________

    dataMemory = defaultdict(lambda : [0,0,0,0])
    instructionMemory = defaultdict(lambda: [0,0,0,0])

    def ProcessorMemoryInterface(self):
        # Set MAR in Fetch
        if MuxMA_select == 0:
            if Mem_Read == 1:
                temp = dataMemory[MAR][:numBytes]
                temp.reverse()
                ans = '0x'
                for i in temp:
                    curr =  hex(i)[2:]
                    ans += '0'*(2-len(curr)) + curr
                    
                return ans
            elif Mem_Write == 1:
                for i in range (numBytes):
                    dataMemory[MAR][i] = (MDR & int('0xFF'+'0'*(2*i),16))>>(8*i)
                return '0x1'
        else:
            ans = instructionMemory[MAR]
            newans = ""
            x=len(ans)
            for i in range(len(ans)):
                newans += ans[x-1-i]
            newans = '0x'+newans
            return newans

    def Fetch(self):
        #Pc, ir
    
        # print("Fetching the instruction")
        self.MAR = hex(self.PC)
        self.MuxMA_select = 1    
        self.IR = self.ProcessorMemoryInterface()
        self.PC_Temp = self.PC + 4
        

    def decimalToBinary(self,num, length):
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

    def Decode(self):
        # print("Decoding the instruction")
        #getting the opcode
        
        ALUOp = [0]*15
        opcode = int(str(IR),16) & int("0x7f",16)
        fun3 = (int(str(IR),16) & int("0x7000",16)) >> 12
        
        # R format - (add,srl,sll,sub,slt,xor,sra,and,or,mul, div, rem)
        # R format - (0110011)  
        # I format - (lb-0,lh-1,lw-2)(addi-0, andi-7, ori-6,)(jalr-0)
        # I format - (0000011)(0010011)(1100111)
        # S format - (sb, sw, sh)
        # S format - (0100011) f3 - sb - 000, sh - 001, sw - 010
        # SB format - beq, bne, bge, blt
        # SB format - (1100011) f3 - beq - 000, bne - 001, blt - 100, bge - 101
        # U format - a
        # UJ format - jal-1101111
        message = ""
        if opcode==int("0110011",2): # R format
            GenerateControlSignals(1, 0, 0, 0, 0, 0, 1, 0, 4)
            RD = (int(IR,16) & int('0xF80',16)) >> 7 # setting destination register
            RS1 = (int(IR,16) & int('0xF8000',16)) >> 15 # setting rs1 register
            RS2 = (int(IR,16) & int('0x1F00000',16)) >> 20 # setting rs2 register
            fun7 = (int(IR,16) & int('0xFE000000',16)) >> 25
            if fun3 == 0:  # add/sub/mul
                if fun7 == 0: 
                    # add 
                    ALUOp[0]=1
                    message = "This is ADD instruction."
                elif fun7 == 32: # subtract
                    ALUOp[1]=1
                    message = "This is SUB instruction."
                elif fun7==1: # mul
                    ALUOp[3]=1 
                    message = "This is MUL instruction."
                else:
                    print("Invalid Func7 for Add/Sub")
                    
                    exit(1)
            elif fun3==7: # and
                message = "This is AND instruction."
                if fun7==0:
                    ALUOp[10]=1
                else:
                    print("Invalid Fun7 for AND")
                    
                    exit(1)
            elif fun3 == 6: # or/remainder
                if fun7==0: # or
                    message = "This is OR instruction."
                    ALUOp[9]=1
                elif fun7==1: # remainder
                    ALUOp[4]=1
                    message = "This is REMAINDER instruction."
                else:
                    print("Invalid Func7 for OR/REM")
                    
                    exit(1)
            elif fun3 == 1: # sll - shift_left
                if fun7==0:
                    ALUOp[6]=1
                    message = "This is SLL instruction."
                else:
                    print("Invalid Func7 for SLL")
                    
                    exit(1)
            elif fun3 == 2: # slt - set_if_less_than
                message = "This is SLT instruction."
                if fun7==0:
                    ALUOp[11]=1
                else:
                    print("Invalid Func7 for SLT")
                    
                    exit(1)
            elif fun3 == 5: # srl/sra
                if fun7==32: # shift_ri_ari
                    message = "This is SRA instruction."
                    ALUOp[7]=1
                elif fun7==0: #shift_ri_lo
                    message = "This is SRL instruction."
                    ALUOp[8]=1
                else:
                    print("Invalid Func7 for SRA/SRL")
                    
                    exit(1)
            elif fun3 == 4: #xor/div
                if fun7==0: # xor
                    message = "This is XOR instruction."
                    ALUOp[5]=1
                elif fun7==1: #div
                    message = "This is DIV instruction."
                    ALUOp[2]=1
                else:
                    
                    exit(1)
            else:
                
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

            #  ADDING CONSTRAINTS ON IMMEDIATE
            if immed>2047:
                immed -= 4096
            
            if opcode==int("0000011",2): # lb/lh/lw
                ALUOp[0]=1
                if fun3 == 0: #lb
                    message = "This is LB instruction."
                    GenerateControlSignals(1,1,1,1,0,0,1,0,1)
                elif fun3 == 1: #lh
                    message = "This is LH instruction."
                    GenerateControlSignals(1,1,1,1,0,0,1,0,2)
                elif fun3 == 2: #lw
                    message = "This is LW instruction."
                    GenerateControlSignals(1,1,1,1,0,0,1,0,4)
                else:
                    
                    exit(1)
                #setting ra rb rm -------------------------------------------------
                RA = reg[RS1]
                # RB = reg[RS2]   ---- DON'T CARES
                # RM = RB         ---- DON'T CARES
                # -----------------------------------------------------------------
            elif opcode==int("0010011",2): #addi/andi/ori
                GenerateControlSignals(1,1,0,0,0,0,1,0,4)
                if fun3==0:#addi
                    message = "This is ADDI instruction."
                    ALUOp[0]=1
                elif fun3==7:#andi
                    message = "This is ANDI instruction."
                    ALUOp[10]=1
                elif fun3==6:#ori
                    message = "This is ORI instruction."
                    ALUOp[9]=1
                else:
                    
                    exit(1)
                #setting ra rb rm -------------------------------------------------
                RA = reg[RS1]
                # RB = reg[RS2]   ---- DON'T CARES
                # RM = RB         ---- DON'T CARES
                # -----------------------------------------------------------------
            elif opcode==int("1100111",2): #jalr *ERROR(CHECK IT)*
                message = "This is JALR instruction."
                GenerateControlSignals(1,0,2,0,0,0,0,1,4)
                if fun3==0:
                    ALUOp[0]=1
                else:
                    
                    exit(1)
                #setting ra rb rm -------------------------------------------------
                RA = reg[RS1]
                # RB = reg[RS2]   ---- DON'T CARES
                # RM = RB         ---- DON'T CARES
                # -----------------------------------------------------------------

        elif opcode==int("0100011",2): # S format
            RS2 = (int(str(IR),16) & int("0xF8000",16)) >> 15
            RS1 = (int(str(IR),16) & int("0x1F00000",16)) >> 20
            immed4to0 = (int(str(IR),16) & int("0xF80",16)) >> 7
            immed11to5 = (int(str(IR),16) & int("0xFE000000",16)) >> 25
            immed = immed4to0 | immed11to5
            ImmediateSign(12)
            ALUOp[0]=1
            if fun3 == int("000",2): # sb
                message = "This is SB instruction."
                GenerateControlSignals(0,1,1,0,1,0,1,0,1)
            elif fun3 == int("001",2): # sh
                message = "This is SH instruction."
                GenerateControlSignals(0,1,1,0,1,0,1,0,2)
            elif fun3 == int("010",2): # sw
                message = "This is SW instruction."
                GenerateControlSignals(0,1,1,0,1,0,1,0,4)
            else:
                
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
            # Setting control Signals
            if(fun3 == 0):
                message = "This is BEQ instruction."
                ALUOp[12] = 1
            elif(fun3 == 1):
                message = "This is BNE instruction."
                ALUOp[13] = 1
            elif(fun3 == 4):
                message = "This is BLT instruction."
                ALUOp[11] = 1
            elif(fun3 == 5):
                message = "This is BGE instruction."
                ALUOp[14] = 1
            else:
                
                exit(1)
            GenerateControlSignals(0,0,0,0,0,0,1,1,0)

        elif opcode==int("0010111",2) or opcode==int("0110111",2): # U type
            RD = (int(IR, 16) & int("0xF80", 16)) >> 7
            immed = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
            ImmediateSign(20)
            if(opcode == int("0010111", 2)): # A
                
                ALUOp[0] = 1
                RA = PC
                immed = immed << 12
            else: #L
                
                ALUOp[6] = 1
                RA = immed
                immed = 12
            GenerateControlSignals(1,1,0,0,0,0,1,0,0)

        elif opcode==int("1101111",2): # UJ format
            message = "This is JALR instruction."
            RD = (int(IR, 16) & int("0xF80", 16)) >> 7
            immed_tmp = (int(IR, 16) & int("0xFFFFF000", 16)) >> 12
            immed = 0
            immed = immed | ((immed_tmp & int("0x7FE00", 16)) >> 9)
            immed = immed | ((immed_tmp & int("0x100", 16)) << 2)
            immed = immed | ((immed_tmp & int("0xFF", 16)) << 11)
            immed = immed | (immed_tmp & int("0x80000", 16))
            ImmediateSign(20)
            immed *= 2
            ALUOp[12] = 1
            RA = 0
            RB = 0
            # print("Immediate field : " + str(immed))
            GenerateControlSignals(1,0,2,0,0,0,1,1,0)

        else:
            print("invalid opcode")

        print(message)
        

    def ImmediateSign(self,num):
        
        if(immed & 2**(num-1) == 0):
            return
        immed = immed ^ (2**num-1)
        immed += 1
        immed *= (-1)

    def Execute(self):
        
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
                
                exit(1)
            RZ = int(InA/InB)
        elif(operation == 3): #mul
            RZ = InA*InB
        elif(operation == 4): #remainder
            if(InB == 0):
                
                exit(1)
            RZ = InA%InB
        elif(operation == 5): #xor
            RZ = InA^InB
        elif(operation == 6): #shift_left
            if (InB<0):
                
                exit(1)
            RZ = InA<<InB
        elif(operation == 7): #shift_right_ari 
            # *******ERROR****** WRITE SRA
            pass
        elif(operation == 8): #shift_ri_lo  
            if (InB<0):
                
                exit(1)
            RZ = InA>>InB
        elif(operation == 9): #or  
            RZ = (InA|InB)
        elif(operation == 10): #and  
            RZ = (InA&InB)
        elif(operation == 11): #less_than 
            RZ = int(InA<InB)
            MuxINC_select = RZ
        elif(operation == 12): #equal  
            RZ = int(InA==InB)
            MuxINC_select = RZ
        elif(operation == 13): #not_equal  
            RZ = int(InA!=InB)
            MuxINC_select = RZ
        elif(operation == 14): #greater_than_equal_to  
            RZ = int(InA>=InB)
            MuxINC_select = RZ
        # return RZ

    def IAG(self):
        
        if(MuxPC_select == 0):
            PC = RA
        else:
            if(MuxINC_select == 0):
                PC = PC + 4
            else:
                PC = PC + immed
        
    def MemoryAccess(self):
        # =========== CHECK =============

        # PC update (IAG module)    
        # if(MuxPC_select == 0):
        #     PC = RA
        # else:
        #     if(MuxINC_select == 0):
        #         PC = PC + 4
        #     else:
        #         PC = PC + immed
        IAG()

        if MuxY_select == 0:
            RY = RZ
        elif MuxY_select == 1:
            MAR = str(hex(RZ)).lower()
            MDR = RM
            RY = int(ProcessorMemoryInterface(),16)
            if RY > 2**31 - 1:
                RY = -(2**32 - RY)
        elif MuxY_select == 2:
            RY = PC_Temp


    def RegisterUpdate(self):
        if RF_Write == 1 and RD != 0:
            reg[RD] = RY

    def validateDataSegment(self,y):
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

    def validateInstruction(self,y):
        if len(y)!=2:
            return False
        addr,data = y[0],y[1]
        if addr[:2]!='0x' or data[:2]!='0x':
            return False
        try:
            temp = int(addr,16)
            temp1 = int(data,16)
        except:
            return False
        return True
    # 

    def main(self):

        # Read the .mc file as input
        mcFile = open("input.mc","r")
        # load the data segment
        flag = 0
        for x in mcFile:
            #creating a hashmap, data segment stored
            y = x.split('\n')[0].split()
            y[1] = y[1].lower()
            if flag==1:
                if validateDataSegment(y)==False:
                    print("ERROR : INVALID DATA SEGMENT")
                    
                    exit(1)
                dataMemory[y[0]][0] = (int(y[1],16) & int('0xFF',16))
                dataMemory[y[0]][1] = (int(y[1],16) & int('0xFF00',16))>>8
                dataMemory[y[0]][2] = (int(y[1],16) & int('0xFF0000',16))>>16
                dataMemory[y[0]][3] = (int(y[1],16) & int('0xFF000000',16))>>24

            if '$' in y:
                flag = 1    
            if flag==0:
                #TODO : Add Validation____
                y = x.split('\n')[0].split()
                if validateInstruction(y)== False:
                    print("ERROR : INVALID INSTRUCTION")
                    
                    exit(1)
                y[1] = y[1].lower() 
                for i in range (4):
                    instructionMemory[y[0]][i] = hex((int(y[1],16) & int('0xFF'+'0'*(2*i),16))>>(8*i))[2:]
                    instructionMemory[y[0]][i] = '0'*(2-len(instructionMemory[y[0]][i])) + instructionMemory[y[0]][i]
                    instructionMemory[y[0]][i] = instructionMemory[y[0]][i].lower()

        
        
        


    def UpdateFile(self,filename):
        mcFile = open(filename,"w")
        i = '0x0'
        for i in instructionMemory:
            curr = '0x' + (''.join(instructionMemory[i][::-1]))
            mcFile.write (i+' '+curr+"\n")
        i = hex(int(i,16) + 4)
        mcFile.write(i+' $\n')
        for i in dataMemory:
            if i== '0x7fffffec':
                break
            curr = '0x'
            for j in dataMemory[i][::-1]:
                curr += '0'*(2-len(hex(j)[2:])) + hex(j)[2:]
            mcFile.write(i+' '+curr+'\n')
        

    def run_RISC_simulator(self):
        
        flag=1
        while (hex(PC) in instructionMemory) and flag==1:
            Fetch()
            Decode()
            Execute()
            MemoryAccess()
            RegisterUpdate()
            clk+=1
            

        UpdateFile("output.mc")
        outFile = open("output.txt",'w')
        print("============= REGISTERS =============")
        outFile.write("============= REGISTERS =============\n")
        for i in range (len(reg)):
            print('x'+str(i)+' =',reg[i])
            outFile.write('x'+str(i)+' = '+str(reg[i])+'\n')
        print()
        outFile.write('\n')
        print("============= DATA MEMORY =============")
        outFile.write("============= DATA MEMORY =============\n")

        for i in dataMemory:
            print(i+' =',dataMemory[i])
            currStr = i + " = "
            for j in dataMemory[i]:
                currStr += hex(j)+' '
            outFile.write(currStr+ '\n')
        print()
        outFile.write('\n')
        print("PC = ",hex(PC))
        outFile.write("PC = "+hex(PC))
        print()
        outFile.write('\n')
        UpdateFile("output.mc")
        if hex(PC) not in instructionMemory:
            print("PROGRAM EXECUTED SUCCESSFULLY")