#Stack implementation using list in Python 

stack = []
def ask():
    global imp
    print('''Which opreation you want to perform:
    1 --> Push
    2 --> Pop
    3 --> Peek
    4 --> Display
    5 --> size
    ''')
    global l
    l=0
    imp = int(input("Enter no to choose: "))
    chk()    
    
def isEmpty():
    if len(stack) == 0:
        l=1
        print("Stack is Empty!!")
def ret():
     ak = print("Do you want to Enter more!!")
     aa = input("'Y/N' :")
     if aa in "Yy":
        push()
     elif aa in "Nn":
        ask()
     else:
        Print("invalid")
        chk()    

def push():
    if l==0:
        choi = int(input(''' what data-type to enter:
        1 --> intiger
        2 --> float
        3 --> string

        Enter your choise here: 

        '''))

        if choi == 1:
            elt = int(input("Enter here: "))
        elif choi == 2:
            elt = float(input("Enter here: "))
        elif choi == 3:
            elt = input("Enter here: ")

        stack.append(elt)
        ret() 

def pop():
    isEmpty()
    if l == 0:
        stack.pop()
        ret()

def peek():
    isEmpty()
    if l == 0:
        print(stack[-1])
        ret()

def display():
    isEmpty()
    if l == 0:
        print(stack[::-1])
        ret()

def size():
    isEmpty()
    if l==0:
        print("Size of stack is ",len(stack))
        ret()



def chk():
    if imp == 1:
        push()
    elif imp ==2:
        pop()
    elif imp == 3:
        peek()
    elif imp == 4:
        display()
    elif imp == 5:
        size()
    else :
        print("Invalaid input..!! TRY AGAIN")
        ask()


ask()
