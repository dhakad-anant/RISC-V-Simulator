from state_class import CPU, State,BTB
from hdu_class import HDU
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
        checkDataHazard = hduob.checkDataHazardStalling(states)
        copyOfStates = states[:] 
        state[0] = ProcessingUnit.Fetch(State(0),btb)

        # [state1,state2,state3,state4,state5]
        # stalling will occcue when data hazard
        # control hazard means stalling

        for i in reversed(range(5)):
            print("states : ",states)
            if(i==0):
                states[i+1] = ProcessingUnit.Fetch(states[i],btb)
                controlChange = states[i+1].predictionOutcome
                controlChange_pc= states[i+1].predictionPC
                # states[i]=None  
            if(i==1):
                if(states[i]==None):
                    continue
                controlHazard,control_hazard_pc,states[i+1] = ProcessingUnit.Decode(states[i],btb)
                states[i]=None         
            if(i==2):
                if(states[i]==None):
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
                ProcessingUnit.RegisterUpdate(states[i])
                states[i]=None        
        if states[1].IR != 0 and (not checkDataHazard):
            #aagle instr pe jaana he
            master_PC+=4
        if(controlChange == True and checkDataHazard == False):
            #if we predicted in fetch state
            master_PC = controlChange_pc        
        vis = False
        if(controlHazard == True and checkDataHazard == False):
            cntBranchHazards+=1
            cntBranchHazardStalls+=1
            master_PC = controlHazard_pc
            # out_states[0] = State(0)
            states[0]=None
            vis = True
        if (not vis) and controlHazard and checkDataHazard and predictionEnabled:
            #doubt condition
            btb.updateState(states[1].PC)
        if checkDataHazard==1:
            tempState = copyOfStates[1]          +    [None]      +    states[2:4]
            # decode put in feteh a stall
            states = tempState[:]
            cntDataHazardsStalls+=1
            cntDataHazards+=1
            # states = tempState.copy()
        
    else:
        pass

    masterClock +=1
    if set([states[0] , states[1] , states[2] , states[3] , states[4]]) == set([None, None]):
        break
    states = [State(master_PC)]+states
    # master_cycle+=1
    # for i in reversed(range(5)):
    #     if(i==0):
    #         states[i]=State(master_PC)
    #         states[i]=ProcessingUnit.Fetch(states[i])
    #         if(states[i]==None):
    #             continue
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==1):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.Decode(states[i])
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==2):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.Execute(states[i])
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==3):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.MemoryAccess(states[i])
    #         states[i+1]=states[i]
    #         states[i]=None
    #     if(i==4):
    #         if(states[i]==None):
    #             continue
    #         ProcessingUnit.RegisterUpdate(states[i])
    #         states[i]=None
    # if(states[0]==None and states[1]==None and states[2]==None and states[3]==None and states[4]==None):
    #     break
    # master_PC += 4
print(ProcessingUnit.reg)
print("Program Executed!!!")