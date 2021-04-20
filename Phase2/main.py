from state_class import CPU, State

states=[None for i in range(5)]
prediction_enabled=1
ProcessingUnit = CPU(prediction_enabled)
ProcessingUnit.readFile()
master_PC=0
master_cycle=0
while True:
    master_cycle+=1
    for i in reversed(range(5)):
        if(i==0):
            states[i]=State(master_PC)
            ProcessingUnit.Fetch(states[i])
            states[i+1]=states[i]
            states[i]=None
        if(i==1):
            if(states[i]==None):
                continue
            ProcessingUnit.Decode(states[i])
            states[i+1]=states[i]
        if(i==2):
            if(states[i]==None):
                continue
            ProcessingUnit.Execute(states[i])
            states[i+1]=states[i]
        if(i==3):
            if(states[i]==None):
                continue
            ProcessingUnit.MemoryAccess(states[i])
            states[i+1]=states[i]
        if(i==4):
            if(states[i]==None):
                continue
            ProcessingUnit.RegisterUpdate(states[i])
    master_PC += 4