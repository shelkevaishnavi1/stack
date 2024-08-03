#multi stack example

#stacksize = the size of each stack
#numstack = how many stack
#array = to keep all records of all stacks
#


class multi:

    def __init__(self,stacksize):
        self.numstacks=3
        self.array=[0] *(stacksize*self.numstacks)
        self.sizes=[0]*self.numstacks   #initialize to the [0,0,0]
        self.stacksize=stacksize

    def push(self,item,stacknum):
        if self.IsFull(stacknum):
            raise Exception("no space is there")
        self.sizes[stacknum]+=1
        self.array[self.IndexOfTop(stacknum)]=item

    def IndexOfTop(self,stacknum):
        offset=stacknum*self.stacksize
        return offset+self.sizes[stacknum]-1
    
    def IsEmpty(self,stacknum):
        return self.sizes[stacknum]==0
    
    def IsFull(self,stacknum):
        return self.sizes[stacknum]==self.stacksize
    
    def pop(self,stacknum):
        if self.IsEmpty(stacknum):
            raise Exception("the stack is empty")
        
        Value=self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)]=0
        return Value
    
    def peek(self,stacknum):

        if self.IsEmpty(stacknum):
            raise Exception("stack is empty")
        return self.array[self.IndexOfTop(stacknum)]
    


obj=multi(5)
print(obj.array)
obj.push(10,2)
print(obj.array)
obj.push(10,1)
print(obj.array)
obj.push(10,1)
obj.push(20,1)
obj.push(30,1)
obj.push(40,1)

print(obj.array)
print(obj.sizes)




        

    


