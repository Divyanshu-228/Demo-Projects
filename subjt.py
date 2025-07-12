#Stack Implementatipn using Python
stack=[]
l=0
'''
push implementatṇion 
for push implementation we use append function that adds an element from the last
pop 
peek
'''
def empt(a):
    if len(a)==0:
        print("Stack is empty!!")
        l=1
    
def push():
    # empt(stack)
    # if l!=1:
    elt= input("Enter a element here: ")
    stack.append(elt)
        
def pop(a):
    empt(stack)
    if l!=1:
        print(stack[-1],"has been removed")
        stack.pop()

def peek(a):
    empt(a)
    if l!=1:
        print(a[-1])
        
print('''Choose a opreation to perform !!
1=push
2=pop
3=peek
''')
choise = int(input("Enter your choise : "))

if choise == 1:
    push()
elif choise ==2:
    pop()
elif choise ==3:
    peek()