from state_class import CPU,State,BTB
from hdu_class import HDU

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

def printPipelineRegisters(states, Knob3,masterClock):
    if(Knob3 == False):
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

states=[None for i in range(5)] # don't change it
predictionEnabled=1
hduob = HDU()
prediction_enabled = 1
Knob1ForPipelining= True # don't change it
Knob2ForDataForwarding = True
Knob3PrintingPipelineRegisterValues = True
controlChange = False
cntBranchHazards = 0
cntBranchHazardStalls = 0
controlChange_pc = 0
controlHazard = False
controlHazard_pc = 0
btb = BTB()
cntDataHazards = 0
cntDataHazardsStalls = 0
ProcessingUnit = CPU(prediction_enabled)
ProcessingUnit.readFile()
master_PC=0
masterClock = 0
# states[0] - fetch
# states[1] - Decode
# states[2] - execute
# states[3] - MemoryAccess
# states[4] - writeback

while True:

    if Knob1ForPipelining:
        alreadyUpdatedPC = 0
        for i in reversed(range(5)):
            if(i==0):
                states[i] = State(master_PC)
                states[i] = ProcessingUnit.Fetch(states[i],btb)
                if(states[i] !=None and states[i].predictionPC!=-1):
                    master_PC = states[i].predictionPC
                    alreadyUpdatedPC = 1
                states[i+1]=states[i]
                states[i]=None
            if(i==1):
                if(states[i]==None):
                    continue
                if(stall == i):
                    break
                controlHazard,control_hazard_pc = ProcessingUnit.Decode(states[i],btb)
                if(controlHazard==1):
                    master_PC = states[i].PC + 4
                elif(controlHazard==-1):
                    master_PC = control_hazard_pc
                states[i+1] = states[i]
                states[i]=None         
            if(i==2):
                if(states[i]==None):
                    continue
                if(stall == i):
                    break
                ProcessingUnit.Execute(states[i])
                states[i+1]=states[i]
                states[i]=None                
            if(i==3):
                if(states[i]==None):
                    continue
                if(stall == i):
                    break
                ProcessingUnit.MemoryAccess(states[i])
                states[i+1]=states[i]
                states[i]=None
            if(i==4):
                if(states[i]==None):
                    continue
                if(stall == i):
                    break
                ProcessingUnit.RegisterUpdate(states[i])
                states[i]=None  
            isHazard, states, stall, stallparameters = checkHazardous(states,Knob2ForDataForwarding)
            if((isHazard == 1 and Knob2ForDataForwarding == False) or (stall != -1 and Knob2ForDataForwarding == False)):
                alreadyUpdatedPC = 1
                break
        if(alreadyUpdatedPC == 0):
            master_PC += 4
    else:
        state = State(0)
        while(state != None):
            state = ProcessingUnit.Fetch(state,btb)
            if(state == None):
                break
            ProcessingUnit.Decode(state,btb)
            ProcessingUnit.Execute(state)
            ProcessingUnit.MemoryAccess(state)
            master_PC = state.PC
            ProcessingUnit.RegisterUpdate(state)
            state = State(master_PC)

    printPipelineRegisters(states,Knob3PrintingPipelineRegisterValues,masterClock)
    masterClock +=1
    if states[0]==None and states[1]==None and states[2]==None and states[3]==None and states[4]==None:
        break
print(ProcessingUnit.reg)
print(ProcessingUnit.dataMemory)
print("Program Executed!!!")