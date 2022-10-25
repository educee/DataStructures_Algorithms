class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        else: return -1        

    def increment(self, k: int, val: int) -> None:
        curLen = len(self.stack)
        
        tmpstack = [] 
        
        for i in range(curLen):
            tmpstack.append(self.stack.pop())
        if k > curLen: k = curLen
        for i in range(k):
            
            newval = tmpstack.pop() + val
            self.stack.append(newval)
            
        for i in range(len(tmpstack)):
            self.stack.append(tmpstack.pop())
            
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
