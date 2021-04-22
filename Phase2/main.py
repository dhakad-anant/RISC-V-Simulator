from state_class import CPU, State

states=[None for i in range(5)]
prediction_enabled=1
ProcessingUnit = CPU(prediction_enabled)
ProcessingUnit.readFile()
master_PC=0
master_cycle=0
# states[0] - fetch
# states[1] - Decode
# states[2] - execute
# states[3] - MemoryAccess
# states[4] - writeback
while True:
    master_cycle+=1
    for i in reversed(range(5)):
        if(i==0):
            states[i]=State(master_PC)
            states[i]=ProcessingUnit.Fetch(states[i])
            if(states[i]==None):
                continue
            states[i+1]=states[i]
            states[i]=None
        if(i==1):
            if(states[i]==None):
                continue
            ProcessingUnit.Decode(states[i])
            states[i+1]=states[i]
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
    if(states[0]==None and states[1]==None and states[2]==None and states[3]==None and states[4]==None):
        break
    master_PC += 4
print("Program Executed!!!")