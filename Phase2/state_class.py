from collections import defaultdict

class State:
    def __init__(self, pc=0):
        self.reset()
        self.PC = pc
    
    def reset(self):
        self.RS1 = -1
        self.RS2 = -1
        self.RD = 0
        self.RM = 0
        self.RZ = 0
        self.RY = 0
        self.RA = 0
        self.RB = 0
        self.IR = 0
        self.MAR = 0
        self.MDR = 0
        self.opcode = 0
        self.PC_temp = 0
        self.predictionOutcome = 0
        self.predictionPC = 0


class BTB:
    Btb_table = defaultdict(lambda: -1)
    P_state = 0

    def isPresent(self, PC):   # isEntered
        if Btb_table[PC] == -1:
            return False
        else:
            return True
    
    def store(self, PC, targetAddress):
        self.Btb_talbe[PC] = [0, targetAddress]
    
    def prediction(self, PC):
        if self.Btb_table[PC][0] == 0:
            return False
        else:
            return True
    
    def getTarget(self, PC):
        if self.Btb_table[PC][0]!=-1:
            return self.Btb_table[PC][1]
        else:
            return 0
    
    def updateState(self, PC):
        if self.Btb_table[PC][0] == 1:
            self.Btb_table[PC][0] = 0
        else:
            self.Btb_table[PC][0] = 1


class CPU:
    def __init__(self, predictionEnabled = 1):
        self.dataMemory = defaultdict(lambda : [0,0,0,0])
        self.instructionMemory = defaultdict(lambda: [0,0,0,0])
        self.reg = [0]*32
        self.reg[2] = int("0x7FFFFFF0",16) # sp - STACK POINTER
        self.reg[3] = int("0x10000000",16) # pointer to begining of data segment
        
    
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

    def readFile(self):
        try:
            mcFile = open("input.mc","r")
        except:
            print("File Not Found!")
            return
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

    def ProcessorMemoryInterface(self, MAR, numBytes, MDR, MuxMA_select, Mem_Read, Mem_Write):
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

    def extendSign(self,num, numBits):
        if(num & 2**(numBits-1) == 0):
            return num
        num = num ^ (2**numBits-1)
        num += 1
        num *= (-1)
        return num
    

    # def _get_opcode(self, IR): === SKIPPED FOR NOW

    def getOpcode(self, IR):
        opcode = int(str(IR),16) & int("0x7f",16)
        return opcode
        

    def getFunc3(self, IR):
        fun3 = (int(str(IR),16) & int("0x7000",16)) >> 12
        return fun3
    
    # def _getImmediate(self, IR):

    # 	def ALU(self, A, B, ALU_control):

    # 	def IAG(self, state):

    # 	def fetch(self, state, btb):

    