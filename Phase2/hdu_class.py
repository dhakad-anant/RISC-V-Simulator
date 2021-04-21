class HDU:
    def __init__(self):
        self.E_to_E = 0
        self.M_to_M = 0
        self.E_to_D = 0
        self.M_to_D = 0
        self.M_to_E = 0
    
    
    def checkDataHazardStalling(self,states):
        # states = states[1:]
        if len(states)==2:
            return False
        elif len(states)>=3:
            ExecuteState = states[2]
            DecodeState = states[1]
            negOne = -1
            if ExecuteState.RD != negOne and DecodeState.RS1 != negOne:
                if ExecuteState.RD == DecodeState.RS1 or ExecuteState.RD == DecodeState.RS2:
                    if ExecuteState.RD != 0:
                        return True
                
            if len(states)>=4:
                MemoryState = states[3]
                if MemoryState.RD != negOne and DecodeState.RS1 != negOne:
                    if MemoryState.RD == DecodeState.RS1 or MemoryState.RD == DecodeState.RS2:
                        if MemoryState.RD != 0:
                            return True
        return False
        
