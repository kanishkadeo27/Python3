class Node:
    data = None
    next = None 
    def __init__(self,data):
        self.data = data
class LinkedList:
    #characteristics
    head = None
    tail = None
    length = 0
    limit = 0
    #behaviour
    #inserting in the end
    def my_append(self,val):
        #create a node
        newNode = Node(val)
        self.length += 1
        if(self.head==None): #to check if list is empty list
            #list is empty
            self.head= newNode
            self.tail=newNode
        else:
            self.tail.next = newNode
            self.tail=newNode
            #inserting in end
    def my_append(self,val):
        #create a node
        newNode = Node(val)
        self.length += 1
        if(self.head==None): #to check if list is empty list
            #list is empty
            self.head= newNode
            self.tail=newNode
        else:
            self.tail.next = newNode
            self.tail=newNode

    #inserting in begin
    def beg_ins(self,val):
        #create a node
        LinkedList.length+=1
        newNode = Node(val)
        if(self.head==None): 
            self.head= newNode
            self.tail=newNode
        else:
            newNode.next = self.head
            self.head=newNode

    #inserting in between
    def ins (self,pos,val):
        newNode = Node(val)
        if(pos==1):
            self.beg_ins(val)
        elif(pos>self.length):
            self.my_append(val)
        else:
            #get address of pos 1
            #pos = 6 el = 3
            befadd=self.head #a1
            cnt=1
            while(cnt!=pos-1):
                befadd = befadd.next #a2
                cnt+=1
            #create a node
            newNode = Node(val)

            nextadd = befadd.next #a3

            newNode.next = nextadd #a6 will have address a3
            befadd.next = newNode

            self.length+=1 

    #deleting a node from start
    def delbeg(self):
        if(self.head==None):
            print("No elements!!")
            return None
        elif(self.head==self.tail):
            r=self.head
            self.head=self.tail=None
            return r
        else:
            t=self.head
            self.head=self.head.next
            t.next=None
            self.length-=1
            return t
        
    #deleting a node from end --> empty pop
    def pop(self):
        if(self.head==None):
            print("No elements!!")
            return None
        elif(self.head==self.tail): #if there ios only one element in list
            r=self.head
            self.head=self.tail=None
            return r

        else:
            t=self.tail
            tem = self.head #A1
            while(tem.next.next!=None):
                tem = tem.next
            tem.next=None
            self.tail=tem
            self.length-=1
            return t
        
    #deleting a node from between
    def popbtn(self,pos): #pos=1
        if(self.head==None):  #to check when to delete or not delete
            print("No elements!!")
            return None
        elif(pos==1): 
            return self.delbeg()
        elif(pos>=5): 
            self.pop()
        else:
            #pos=4
            cnt=1
            tem = self.head #A1
            while(cnt!=pos-1):
                tem = tem.next
                cnt+=1
            nextposadd = tem.next.next
            posadd=tem.next
            tem.next=nextposadd
            posadd.next=None
            self.length-=1
            return posadd
        
    #swapping two nodes
    #swap fisrt and last
    def swapfstlst(self):
        pos1add=self.delbeg() #a1
        pos2add=self.pop() #a5
        pos2add.next=self.head
        self.head = pos2add
        self.tail.next = pos1add
        self.tail = pos1add
    #swap in between
    def swap(self,pos1,pos2): #pos1=2,pos2=4
        if(pos1==1 and pos2 == self.length):
            self.swapfstlst()
        elif(pos1>1 and pos1+1==pos2):
            if(pos1==1):
                t=self.delbeg()
                t.next=self.head.next
                self.head.next=t
            else:
                pass
        else:
            befaddpos_1=None #a1
            befaddpos_2=None #a3
            temp=self.head #a1
            cnt=1
            while(temp!=None):
                if(cnt==pos1-1):
                    befaddpos_1=temp
                if(cnt==pos2-1):
                    befaddpos_2=temp
                temp = temp.next #a2 #a3
                cnt+=1 #2 #3

            #deletion
            posadd1=befaddpos_1.next #posadd1=a2
            posadd2=befaddpos_2.next #posadd2=a4
            #1-->3
            befaddpos_1.next=posadd1.next #a1.next=a3
            posadd1.next=None
            #3-->5
            befaddpos_2.next=posadd2.next #a3.next=a5
            posadd2.next=None
            #insertion
            #posadd2(4) after the befaddpos_1(1)
            posadd2.next=befaddpos_1.next #4-->3
            befaddpos_1.next=posadd2 #1-->4
            #posadd1(2) after the befaddpos_2(3)
            posadd1.next=befaddpos_2.next #2-->5
            befaddpos_2.next=posadd1 #3-->2

    #printing the linked list
    def printlist(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ") 
            temp = temp.next  
        print()

class StackLL:
    head = None
    top = None
    length = 0
    def push(self,val):
        newNode = Node(val)
        self.length += 1
        if(self.head==None): #to check if list is empty list
            #list is empty
            self.head= newNode
            self.top=newNode
        else:
            self.top.next = newNode
            self.top=newNode
    
    def pop(self):
        if(self.head==None):
            print("No elements!!")
            return None
        elif(self.head==self.top): #if there ios only one element in list
            r=self.head
            self.head=self.top=None
            return r.data

        else:
            t=self.top
            tem = self.head #A1
            while(tem.next.next!=None):
                tem = tem.next
            tem.next=None
            self.top=tem
            self.length-=1
            return t.data

    def peek(self):
        if(self.head==None):
            return None
        else:
            return self.top.data
    #display stack with LL
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end=" ") 
            temp = temp.next  
    def isempty(self):
        if(self.head==None):
            return True
        return False

st=StackLL()
st.push(78)
st.push(25)
st.push(20)
st.push(290)
st.push(30)
print(st.peek())
print(st.isempty())
st.display()


    
    