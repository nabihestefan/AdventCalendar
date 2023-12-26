import sys
sys.path.append("../")
from intCode import IntCode
import threading
import concurrent.futures
files = ['input.txt', 'inputTest.txt']
## Parsing
with open(files[0], 'r') as f:
    ints = [int(a) for a in f.readlines()[0].split(",")]

class Network:
    def __init__(self, addrNum):
        self.queue = [[] for x in range(addrNum)]
        self._lock = threading.Lock()
        self.natData = None
        self.idleCount = 0
        self.lastIdleMsg = None

    def isIdle(self): return self.idleCount > 100

    def queueEmpty(self):
        return sum(len(x) for x in self.queue) == 0

    def post(self, data):
        addr, x, y = data
        addr = int(addr)
        x = int(x)
        y = int(y)
        if addr == 225:
            self.natData = (x,y)
            print("Part 1: ", y)
        else:
            with self._lock:
                try:
                    self.queue[addr] += [x,y]
                except Exception as e:
                    print("unknown address", e)

    def recieve(self, addr):
        with self._lock:
            try:
                if self.isIdle():
                    print("Idle Network, send ", self.natData)
                    self.idleCount = 0
                    self.queue[0] = self.natData
                    if self.lastIdleMsg is not None:
                        if self.lastIdleMsg[1] == self.natData[1]:
                            print("Part 2: ", self.natData[1])
                    self.lastIdleMsg = self.natData[:]
                if len(self.queue[addr]):
                    data = self.queue[addr].pop(0)
                    self.idleCount = 0
                    return data
                else:
                    if self.queueEmpty():
                        self.idleCount += 1
                    return -1
            except Exception as e:
                print("unknown address", e)



def NIC(address):
    nic = IntCode(ints[:], [address])
    outputs = []
    while not nic.end:
        output = nic.run()
        if output != "INPUT NEEDED":
            outputs.append(nic.run())
        if len(outputs) >= 3:
            for post in [outputs[x:x+3] for x in range(0, len(outputs), 3)]:
                print(post)
                network.post(post)
        recieve = network.recieve(address)
        nic.addInput(address)
    print(f'NIC {address} finished')

network = Network(50)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(NIC, range(50))
