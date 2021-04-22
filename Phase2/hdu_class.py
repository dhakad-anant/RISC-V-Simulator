
class HDU:
    def __init__(self):
        self.E_to_E = 0   # 0
        self.M_to_M = 0   # 1
        self.E_to_D = 0   # 2
        self.M_to_D = 0   # 3
        self.M_to_E = 0   # 4

    # ind1 => Fetch, Decode, Exe, Ma, WB
    # para => RA, RB, RD
    def evaluate(ind1, ind2,forwardPaths, prevStates):
        isHazard = 0

        if ind1== 3 and ind2 == 4:
            if prevStates[4].RD == prevStates[3].RS2:
                prevStates[3].RB = prevStates[4].RY
                isHazard = 1
                self.M_to_M = prevStates[4].RY
                forwardPaths.append(1)
        if ind1==2 and ind2 == 4:
            temp = 0
            if prevStates[2].RS1 == prevStates[4].RD:
                temp = 1
                prevStates[2].RA = prevStates[4].RY
            if prevStates[2].RS2 == prevStates[4].RY:
                temp = 1
                prevStates[2].RB = prevStates[4].RY
            if temp==1:
                self.M_to_E = prevStates[4].RY
                isHazard = 1
                forwardPaths.append(4)

        if ind1 == 2 and ind2 == 3:
            temp = 0
            if prevStates[2].RS1 == prevStates[3].RD:
                temp = 1
                prevStates[2].RA = self.E_to_E = prevStates[3].RZ
            if prevStates[2].RS2 == prevStates[3].RD:
                temp = 1
                prevStates[2].RB = self.E_to_E = prevStates[3].RZ
            if temp:
                isHazard = 1
                forwardPaths.append(0)
        
        if ind1 == 1 and ind2 == 4:
            temp = 0
            if prevStates[1].RS1 == prevStates[4].RD:
                prevStates[1].RS1Branch = self.M_to_D = prevStates[4].RY
                temp = 1
            if prevStates[1].RS2 == prevStates[4].RD:
                prevStates[1].RS2Branch = self.M_to_D = prevStates[4].RY
                temp = 1
            if temp:
                isHazard = 1
                forwardPaths.append(3)

        if ind1 == 1 and ind2 == 3:
            temp = 0
            if prevStates[1].RS1 == prevStates[3].RD:
                prevStates[1].RS1Branch = self.E_to_D = prevStates[3].RZ
                temp = 1
            if prevStates[1].RS2 == prevStates[3].RD:
                prevStates[1].RS2Branch = self.E_to_D = prevStates[3].RZ
                temp = 1
            if temp:
                isHazard = 1
                forwardPaths.append(2)
            
        
        return [forwardPaths, prevStates, isHazard]

    
    def isDataHazard(self, states):
        forwardPaths = []
        newState = [states[0]]
        prevStates = states[:]
        # isHazard, toStall, whereToStall = [0,0,3]
        isHazard = 0
        stallParameters = [0,3]

        prevStatesOpcode = [0]
        for i in range (1,5):
            prevStatesOpcode.append(int(str(prevStates[i].IR),16) & int("0x7f",16))
        # fetch, decode, exe, MA, WB
        if prevStatesOpcode[4]==int('11',2) and prevStatesOpcode[3]==35 and prevStates[4].RD >=1:
            forwardPaths, prevStates, isHazard = evaluate(3,4,forwardPaths, prevStates)
        
        if prevStates[4].RD >= 1:
            forwardPaths, prevStates, isHazard = evaluate(2,4,forwardPaths, prevStates)
        
        if prevStates[3].RD >= 1:
            if (prevStatesOpcode[3] == 3) and ((prevStatesOpcode[2] == 35 and prevStates[2].RS1 == prevStates[3].RD) or (prevStatesOpcode[2]!=35)):
                isHazard = 1
                stallParameters = [1, min(stallParameters[1],1)]
            if prevStatesOpcode[3]!=3:
                forwardPaths, prevStates, isHazard = evaluate(2,3, forwardPaths, prevStates)
        
        if prevStatesOpcode[1] in [99, 103]:
            # M to D forwarding
            if prevStates[4].RD >= 1:
                forwardPaths, prevStates, isHazard = evaluate(1,4, forwardPaths, prevStates)
            # E to D forwarding
            if prevStates[3].RD >=1:
                if prevStatesOpcode[3] in [3]:
                    isHazard = 1
                    stallParameters = [1, min(stallParameters[1], 2)]
                else:
                    forwardPaths, prevStates, isHazard = evaluate(1,3,forwardPaths, prevStates)
            
            if prevStates[2].RD >=1:
                if (prevStates[2].RD in [prevStates[1].RS1, prevStates[1].RS2]):
                    isHazard = 1
                    stallParameters = [1, min(stallParameters[1], 2)]

        newState.extend(prevStates[1:])
        forwardPaths = list(set(forwardPaths))
        return [isHazard, stallParameters, newState, forwardPaths]
    