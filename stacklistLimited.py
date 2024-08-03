# stack eith the limited size


class stack:

    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.list=[]


    def IsEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def IsFull(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False
        

    def push(self,value):
        if self.IsFull():
            return "the stack is full"
        else:
            self.list.append(value)
        return True
    

    def pop(self):
        if self.IsEmpty():
            return False
        else:
            value= self.list.pop()

        return value
    

    def peek(self):
        if self.IsEmpty:
            return "empty"
        else:
            return self.list[len(self.list)-1]
        
    def display(self):
        
        value=self.list.reverse()
        value=[str(i) for i in self.list]
        print(value)
    


obj=stack(5)

obj.push(10)
obj.push(30)
obj.push(40)
obj.push(50)
obj.push(60)
print(obj.display())
obj.pop()
print(obj.display())
obj.push(60)
print(obj.push(60))
print(obj.display())
            