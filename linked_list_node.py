class Node:
    def __init__(self,init_data):
        self.data=init_data
        self.next=None

    def get_data(self):
        return self.data

    def set_data(self,new_data):
        self.data=new_data

    def get_next(self):
        return self.next

    def set_next(self,new_next):
        self.next=new_next
N1=Node(1)
N1.set_data(2)
N1.set_data(3)
N1.set_data(4)
N1.set_data(5)
N2=Node(10)
N1.get_next(N2)
print(N1.get_data())
