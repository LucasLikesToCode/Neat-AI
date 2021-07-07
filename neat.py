import random as rand
class neat:
    def __init__(self, inNodes, outNodes, layers):
        self.nodes = []
        for a in range(inNodes): self.nodes.append([0, 'in', 0])
        for a in range(outNodes): self.nodes.append([layers+1, 'out', 0])
        self.connections = []
        self.layers = layers+1
        self.inNodes = inNodes
        self.outNodes = outNodes
    def dupe(self):
        a = neat(self.inNodes, self.outNodes, self.layers-1)
        a.nodes = self.nodes
        a.connections = self.connections
        return a
    def inputNodes(self, *values):
        for a in range(len(values)):
            self.nodes[a] = [0, 'in', values[a]]
    def outputNodes(self):
        out = []
        for a in self.nodes:
            if a[1] == 'out':
                out.append(a[2])
        return out
    def mutate(self, times):
        for b in range(times):
            if len(self.connections) == 0:
                self.addConnection()
            else:
                a = rand.randrange(0, 100)
                if a < 25:
                    self.tweakConnection()
                elif a < 50:
                    self.addConnection()
                elif a < 75:
                    self.changeEnable()
                elif a < 90:
                    self.changeNode()
                else:
                    self.addNode()
    def compute(self):
        for a in range(self.layers): # get layers
            for b in range(len(self.nodes)): # get nodes in layer
                if self.nodes[b][0] == a+1:
                    connections = []
                    for c in range(len(self.connections)): # get connections to node
                        if self.connections[c][1] == b and self.connections[c][3]:
                            connections.append(self.connections[c])
                    if len(connections) != 0:
                        inputTotal = 0
                        for c in connections: # get inputs
                            inputTotal += (self.nodes[c[0]][2]/len(connections))*c[2]
                        self.nodes[b] = [a+1, self.nodes[b][1], self.activation(inputTotal, self.nodes[b][1])]
    def addConnection(self):
        loops = 0
        while loops < 10:
            a, b = rand.randrange(0, len(self.nodes)), rand.randrange(0, len(self.nodes))
            if a is not b and self.nodes[a][0] < self.nodes[b][0]:
                copy = False
                for c in self.connections:
                    if c[0] == a and c[1] == b:
                        copy = True
                if copy == False:
                    self.connections.append([a, b, round(rand.randint(-200, 200)/100, 2), True])
                    loops = 10
            loops += 1
    def addNode(self):
        if len(self.connections) > 0:
            a = rand.randrange(0, len(self.connections))
            b, c, d = self.connections[a][0], self.connections[a][1], self.connections[a][2]
            if self.nodes[b][0] < self.nodes[c][0]-1:
                self.connections[a][3] = False
                self.nodes.append([self.nodes[b][0]+1, {0:'sig', 1:'lin', 2:'exp', 3:'abs', 4:'rel', 5:'neg'}[rand.randrange(0,6)], 0])
                self.connections.append([b, len(self.nodes)-1, 1, True])
                self.connections.append([len(self.nodes)-1, c, d, True])
    def tweakConnection(self):
        if len(self.connections) > 0:
            b = rand.randrange(0,len(self.connections))
            a = self.connections[b]
            self.connections[b][2] = round(a[2] + rand.randrange(-100, 100)/100, 2)
    def changeEnable(self):
         if len(self.connections) > 0:
              a = rand.randrange(0, len(self.connections))
              self.connections[a][3] = not self.connections[a][3]
    def changeNode(self):
        loops = 0
        while loops<10:
            a = rand.randrange(0, len(self.nodes))
            if self.nodes[a][1] != 'in' and self.nodes[a][1] != 'out':
                self.nodes[a][1] = {0:'sig', 1:'lin', 2:'exp', 3:'abs', 4:'rel', 5:'neg'}[rand.randrange(0,6)]
                loops = 10
            loops += 1
    @staticmethod
    def activation(num, nodeType):
        if nodeType == 'sig' or nodeType == 'out':
            return 1/(1+3**-num)
        elif nodeType == 'lin':
            return num
        elif nodeType == 'exp':
            return num**2
        elif nodeType == 'abs':
            return abs(num)
        elif nodeType == 'rel':
            return num>0
        elif nodeType == 'neg':
            return -num


