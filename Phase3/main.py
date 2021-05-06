from state_class import CPU,State,BTB,MainMemory,DataCacheMemory,InstrCacheMemory
from hdu_class import HDU
import math

def checkHazardous(states,isDataForwardingEnabled):
    isHazard, stallparameters, newState, forwardPaths = hduob.isDataHazard(states,isDataForwardingEnabled)
    # print('============> ',forwardPaths)
    states = []
    stall = -1
    for i in newState:
        if i.opcode == 0:
            states.append(None)
            continue
        states.append(i)
    if stallparameters[0]==1:
        stall = stallparameters[1]
    return [isHazard, states, stall, stallparameters]

def printPipelineRegisters(states, Knob3,masterClock,Knob4,ProcessingUnit):
    if(Knob4 == False):
        if(Knob3 == False):
            return
        else:
            print(ProcessingUnit.reg)
        return
    print("Cycle number -> ", masterClock)
    print("Content of First Pipeline Register -------------------------------------- ")
    if(states[1]!=None):
        print("IR -> ",states[1].IR)
    else: print("EMPTY")
    print("Content of Second Pipeline Register -------------------------------------")
    if(states[2]!=None):
        print("Opcode -> ", states[2].opcode)
        if(states[2].RS1 != -1):
            print("RS1 -> ",states[2].RS1)
        if(states[2].RS2 != -1):
            print("RS2 -> ",states[2].RS2)
        if(states[2].RD != 0):
            print("RD -> ", states[2].RD)
        print("Immediate -> ", states[2].immed)
        if(states[2].fun3 != -1):
            print("Funct3 -> ", states[2].fun3)
        if(states[2].fun7 != -1):
            print("Funct7 -> ", states[2].fun7)
    else: print("EMPTY")
    print("Content of Third Pipeline Register ---------------------------------------")
    if(states[3]!=None):
        print("RZ -> ", states[3].RZ)
    else: print("EMPTY")
    print("Content of Fourth Pipeline Register ---------------------------------------")
    if(states[4]!=None):
        print("RY -> ", states[4].RY)
    else: print("EMPTY")
    if(Knob3 == True):
        print("Content of Register File ------------------------------------------------------------------")
        print(ProcessingUnit.reg)

def check(num, states):
    dont = True
    for i in states:
        if(i == None): continue
        if(i.PC == num):
            dont=False
    if(dont==False):
        print("Cycle number -> ", masterClock)
        print("Content of First Pipeline Register -------------------------------------- ")
        if(states[1]!=None):
            print("IR -> ",states[1].IR)
        else: print("EMPTY")
        print("Content of Second Pipeline Register -------------------------------------")
        if(states[2]!=None):
            print("Opcode -> ", states[2].opcode)
            if(states[2].RS1 != -1):
                print("RS1 -> ",states[2].RS1)
            if(states[2].RS2 != -1):
                print("RS2 -> ",states[2].RS2)
            if(states[2].RD != 0):
                print("RD -> ", states[2].RD)
            print("Immediate -> ", states[2].immed)
            if(states[2].fun3 != -1):
                print("Funct3 -> ", states[2].fun3)
            if(states[2].fun7 != -1):
                print("Funct7 -> ", states[2].fun7)
        else: print("EMPTY")
        print("Content of Third Pipeline Register ---------------------------------------")
        if(states[3]!=None):
            print("RZ -> ", states[3].RZ)
        else: print("EMPTY")
        print("Content of Fourth Pipeline Register ---------------------------------------")
        if(states[4]!=None):
            print("RY -> ", states[4].RY)
        else: print("EMPTY")

states =[None for i in range(5)] # don't change it
predictionEnabled =1
hduob = HDU()
prediction_enabled = 1
Knob1ForPipelining= True # don't change it
Knob2ForDataForwarding = True
Knob3PrintingRegFile = False
Knob4PrintingPipelineRegister = False
Knob5PrintingPipelineRegForSpecificInst = False
num = -4
if(Knob5PrintingPipelineRegForSpecificInst == True):
    num = int(input("Enter the instruction number which you want to observe : "))
    num = num*4

controlChange = False
cntBranchHazards = 0
cntBranchHazardStalls = 0
controlChange_pc = 0
controlHazard = False
controlHazard_pc = 0
btb = BTB()
cntDataHazards = 0
cntDataHazardsStalls = 0


#______________________________________________________________________inputs_____________________________________________________

cacheSize = int(input("Please Enter the cacheSize : "))
blockSize = int(input("Please Enter the blockSize : "))
cacheAssociativity = int(input("Please Enter the cacheAssociativity : "))



dataCacheMemory = DataCacheMemory(cacheSize,blockSize,cacheAssociativity)
instrCacheMemory = InstrCacheMemory(cacheSize,blockSize,cacheAssociativity)
mainMemory = MainMemory(blockSize//4)




ProcessingUnit = CPU(Knob1ForPipelining, prediction_enabled)
numberOfBitsinBO = math.log2(blockSize)
if(numberOfBitsinBO-int(numberOfBitsinBO)!=0): numberOfBitsinBO+=1
numberOfBitsinBO = int(numberOfBitsinBO)
mainMemory.readFile(numberOfBitsinBO)
# stats to be printed variables
master_PC=0
masterClock = 0
CPI = 0
LoadAndStoreInstructions = 0
ALUInst = 0
ControlInst = 0
stallsCount = 0
DataHazardCount = 0
ControlHazardCount = 0
BranchMisprediction = 0
StallsDuetoDataHazards = 0
StallsDuetoControlHazards = 0
InstCount = 0
stall = -1
programExecuted = 0
clockNonPipeline = 0
numAccesses = 0
numHits = [0]
numMisses = [0]

# states[0] - fetch
# states[1] - Decode
# states[2] - execute
# states[3] - MemoryAccess
# states[4] - writeback

while True:

    if Knob1ForPipelining:
        alreadyUpdatedPC = 0
        for i in reversed(range(5)):
            if(Knob5PrintingPipelineRegForSpecificInst ==True):
                check(num,states)
            if(i==0):
                states[i] = State(master_PC)
                states[i] = ProcessingUnit.Fetch(states[i],btb,mainMemory,instrCacheMemory,numMisses,numHits)
                if(states[i] !=None and states[i].predictionPC!=-1):
                    master_PC = states[i].predictionPC
                    ControlHazardCount += 1
                    alreadyUpdatedPC = 1
                states[i+1]=states[i]
                states[i]=None
            if(i==1):
                if(states[i]==None):
                    continue
                if(stall == i):
                    StallsDuetoDataHazards += 1
                    stallsCount += 1
                    break
                controlHazard,control_hazard_pc = ProcessingUnit.Decode(states[i],btb)
                if(controlHazard==1):
                    BranchMisprediction += 1
                    StallsDuetoControlHazards += 1
                    master_PC = states[i].PC + 4
                elif(controlHazard==-1):
                    StallsDuetoControlHazards += 1
                    master_PC = control_hazard_pc
                states[i+1] = states[i]
                states[i]=None         
            if(i==2):
                if(states[i]==None):
                    continue
                if(stall == i):
                    StallsDuetoDataHazards += 1
                    stallsCount += 1
                    break
                ProcessingUnit.Execute(states[i])
                states[i+1]=states[i]
                states[i]=None                
            if(i==3):
                if(states[i]==None):
                    continue
                if(stall == i):
                    StallsDuetoDataHazards += 1
                    stallsCount += 1
                    break
                ProcessingUnit.MemoryAccess(states[i],dataCacheMemory,mainMemory,numMisses,numHits)
                states[i+1]=states[i]
                states[i]=None
            if(i==4):
                if(states[i]==None):
                    continue
                if(stall == i):
                    StallsDuetoDataHazards += 1
                    stallsCount += 1
                    break
                if(states[i].opcode == 3 or states[i].opcode == 35):
                    LoadAndStoreInstructions += 1
                elif(states[i].opcode in [51,19,23,55]):
                    ALUInst += 1
                elif(states[i].opcode in [99, 103,111]):
                    ControlInst += 1
                InstCount += 1
                ProcessingUnit.RegisterUpdate(states[i])
                states[i]=None  
            isHazard, states, stall, stallparameters = checkHazardous(states,Knob2ForDataForwarding)
            if((isHazard == 1 and Knob2ForDataForwarding == False) or (stall != -1 and Knob2ForDataForwarding == False)):
                alreadyUpdatedPC = 1
                break
            if(isHazard == 1):
                DataHazardCount += 1
        if(alreadyUpdatedPC == 0):
            master_PC += 4
    else:
        state = State(0)
        while(state != None):
            state = ProcessingUnit.Fetch(state,btb,mainMemory,instrCacheMemory,numMisses,numHits)
            if(state == None):
                break
            ProcessingUnit.Decode(state,btb)
            ProcessingUnit.Execute(state)
            ProcessingUnit.MemoryAccess(state,dataCacheMemory,mainMemory,numMisses,numHits)
            master_PC = state.PC1
            ProcessingUnit.RegisterUpdate(state)
            state = State(master_PC)
        print("check here")
    printPipelineRegisters(states,Knob3PrintingRegFile,masterClock,Knob4PrintingPipelineRegister,ProcessingUnit)
    masterClock +=1
    if states[0]==None and states[1]==None and states[2]==None and states[3]==None and states[4]==None:
        break
if InstCount!=0:
    CPI = masterClock/InstCount
else:
    CPI = 0
if(Knob4PrintingPipelineRegister == False):
    print(ProcessingUnit.reg)
numAccesses = numMisses[0] + numHits[0]
print(numMisses[0], numHits[0])
print("Program Executed!!!")
