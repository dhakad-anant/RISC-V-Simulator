from state_class import CPU,State,BTB
from hdu_class import HDU

def checkHazardous(states):
    isHazard, stallparameters, newState, forwardPaths = hduob.isDataHazard(states)
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
    return [states, stall, stallparameters]

states=[None for i in range(5)] # don't change it
predictionEnabled=1
hduob = HDU()
prediction_enabled = 1
knob2_stallingEnabled= True # don't change it
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
master_cycle=0
masterClock = 0
# states[0] - fetch
# states[1] - Decode
# states[2] - execute
# states[3] - MemoryAccess
# states[4] - writeback

while True:

    if knob2_stallingEnabled:
        # states[0] = State(master_PC)

        # [state1,state2,state3,state4,state5]  
        # stalling will occcue when data hazard
        # control hazard means stalling
        alreadyUpdatedPC = 0
        # print("states : ",states)
        # print("registers : ",ProcessingUnit.reg)
        # print("===> ", hex(master_PC))
        for i in reversed(range(5)):
            states, stall, stallparameters = checkHazardous(states)
            if(i==0):
                states[i] = State(master_PC)
                states[i] = ProcessingUnit.Fetch(states[i],btb)
                if(states[i] !=None and states[i].predictionPC!=-1):
                    master_PC = states[i].predictionPC
                    alreadyUpdatedPC = 1
                states[i+1]=states[i]
                states[i]=None
            if(i==1):
                if(states[i]==None or stall==i):
                    continue
                controlHazard,control_hazard_pc = ProcessingUnit.Decode(states[i],btb)
                if(controlHazard==1):
                    master_PC = states[i].PC + 4
                elif(controlHazard==-1):
                    master_PC = control_hazard_pc
                states[i+1] = states[i]
                states[i]=None         
            if(i==2):
                if(states[i]==None or stall==i):
                    continue
                ProcessingUnit.Execute(states[i])
                states[i+1]=states[i]
                states[i]=None                
            if(i==3):
                if(states[i]==None):
                    continue
                ProcessingUnit.MemoryAccess(states[i])
                states[i+1]=states[i]
                states[i]=None
            if(i==4):
                if(states[i]==None):
                    continue
                if(states[4].IR == "0x00412083" and states[3].IR == "0x00810113" and states[2].IR == "0x03450533" and states[1].IR == "0x00008067" and (states[2].RA == 3 or states[2].RB == 3)):
                    print("Check Here")
                ProcessingUnit.RegisterUpdate(states[i])
                states[i]=None  
        if(alreadyUpdatedPC == 0):
            master_PC += 4
    else:
        pass

    masterClock +=1
    if states[0]==None and states[1]==None and states[2]==None and states[3]==None and states[4]==None:
        break
print(ProcessingUnit.reg)
print(ProcessingUnit.dataMemory)
print("Program Executed!!!")