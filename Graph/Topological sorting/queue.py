from node import Node 
class Queue:
    __head=None 
    __tail=None 
    __count=0 

    def add(self,element):
        if self.__head==None:
            self.__head=Node(element,None,None)
            self.__tail=self.__head 
        else:
            new_node=Node
            self.__tail.next=new_node 
            new_node.prev=self.__tail
            self.__tail=new_node 
            self.__count+=1
    def poll(self):
        p=self.__head 
        self.__head=self.__head.next 
        p.next=None 
        p.prev=None 

        self.__count-=1 
        return p.data 
    def peek(self):
        return self.__head.data 
    def size(self):
        return self.__count 
    def isempty(self):
        if self.__count==0:
            return True 
        else:
            return False 
    