

#creating astack using list


class stack:

    def __init__(self):
        self.list=[]

    def IsEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    def push(self,value):
        self.list.append(value)

        return True
    
    def pop(self):
        if self.IsEmpty():
            return "no element is there"
        else:
            self.list.pop()

    def display(self):
        self.list.reverse()
        value=[str(i) for i in self.list]
        print(value)


    def peek(self):
        return self.list[len(self.list)-1]
    


obj=stack()
obj.push(10)
obj.display()
obj.push(80)
obj.push(70)
obj.push(60)
obj.push(50)
obj.push(40)
obj.display()
print(obj.peek())
obj.pop()
obj.display()

