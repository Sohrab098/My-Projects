class Node:
    def __init__(self, symbol, leftChild=None, rightChild=None):
        self.symbol = symbol
        self.leftChild = leftChild
        self.rightChild = rightChild
#Setting global variables
next_token= '%'
length=0
error=False
n9=1
# a function that merges all lines in file and gibes it as a single line
#This is fulfilling the requirment of skipping splitted expressions in multiple line
def merge():
    with open("d://lab3decoy.txt", "r") as f:
        contents = f.read()
    contents = contents.replace("\n", "")
    global lenght 
    lenght=len(contents)
    print(lenght)
    with open("d://lab3decoy.txt", "w") as f:
        f.write(contents)
#reading the line in decoy file and appending them to an array except for "\n" and " "(white space) 
def lexres():
    x=[]
    with open("d://lab3decoy.txt", "r") as k:
        k=k.readline()
        for b in k:
            if b in [" ","\n"]:
                continue
            else:
                x.append(b)
        with open("d://lab3decoy.txt","w") as d:
            if x==[]:
                return
            else:
                global next_token
                next_token= x[0]
                x=x[1:]
                d.write("".join(x))
#this returns unconsumed inputs 
def unconsumed_input():
    with open("d://lab3decoy.txt", "r") as d:
        c=d.readline()
        c=next_token+c[0:]
        return c
#lex function made out of 2 other functions which reads the expression even whit space and line between them
def lex():
    merge()
    lexres()
    global next_token
#parser formulas
#G -> E
def G():
    lex()
    print ("G -> E");
    tree = E()
    if next_token=='$' and not error:
        print( "success")
        return tree
 
    else:
        print ("failure: unconsumed input=", unconsumed_input())
#E -> T R
def E():
    if error:
        return
    print ("E -> T R")
    temp=T()
    return R(temp)
# R -> + T R | - T R | e 
def R(tree):
    if error:
        return;
    if next_token== '+':
        print ("R -> + T R");
        lex()
        temp1=T()
        temp2=R(temp1)
        return Node('+', tree, temp2)
    elif next_token== '-':
        print ("R -> - T R");
        lex()
        temp1=T()
        temp2=R(temp1)
        return Node('-', tree, temp2)
    else:
        print ("R->e")
        return tree
# T -> F S 
def T():
     if error: 
        return
     print ("T -> F S")
     temp= F()
     return S(temp)
# S -> * F S | / F S | e 
def S(tree):
    if error: 
        return
    if next_token=='*':
        print ("S -> * F S")
        lex()
        temp1=F()
        temp2=S(temp1)
        return Node('*', tree, temp2)
    elif next_token=='/':
         print ("S -> / F S")
         lex()
         temp1=F()
         temp2=S(temp1)
         return Node('/', tree, temp2)
    else:
        print ("S -> e") 
        return(tree)
#F -> ( E ) | M | N
def F():
     global error
     if error:
         return
     if next_token=='(':
         print ("F->( E )")
         lex()
         temp=E()
         if next_token == ')':
            lex();
            return temp
     
         else: 
             error=True
             print(f"error: unexptected token {next_token}")
             print("unconsumed_input= ", unconsumed_input());
             return;
     elif next_token in ['a','b','c','d']:
         print ("F->M")
         return M()
     elif next_token in ['0','1','2','3']:
         print ("F->N")
         return N()
     else:
         error=True;
         print(f"error: unexptected token {next_token}")
         print("unconsumed_input= ", unconsumed_input())
         return
#M -> a | b | c | d 
def M():
    global error
    prev_token=next_token
    if error:
        return
    if next_token in ['a','b','c','d']:
        print ("M->", next_token)
        lex() 
        return Node(prev_token, None, None)

    else:
        error=True;
        print(f"error: unexptected token {next_token}")
        print("unconsumed_input= ", unconsumed_input());
        return
# N -> 0 | 1 | 2 | 3 
def N():
    global error
    prev_token=next_token
    if error:
        return;
    if next_token in ['0','1','2','3']:
        print ("N->", next_token)
        lex()
        return Node(prev_token, None, None)

    else:
        error=True;
        print(f"error: unexptected token {next_token}")
        print("unconsumed_input= ", unconsumed_input());
        return
def printTree(tree):
    if tree is None:
        return
    printTree(tree.leftChild)
    printTree(tree.rightChild)
    print(tree.symbol)
def evaluate(tree):
    if tree is None:
        return -1
    if tree.symbol == 'a':
        return 10
    if tree.symbol == 'b':
        return 20
    if tree.symbol == 'c':
        return 30
    if tree.symbol == 'd':
        return 40
    if tree.symbol in ['0', '1', '2', '3']:
        return int(tree.symbol)
    if tree.symbol == '+':
        return evaluate(tree.leftChild) + evaluate(tree.rightChild)
    if tree.symbol == '-':
        return evaluate(tree.leftChild) - evaluate(tree.rightChild)
    if tree.symbol == '*':
        return evaluate(tree.leftChild) * evaluate(tree.rightChild)
    if tree.symbol == '/':
        return evaluate(tree.leftChild) / evaluate(tree.rightChild)

def draw(tree, indent='', is_last=True):
    if tree is None:
        return
    symbol = tree.symbol
    marker = "└── " if is_last else "├──"
    print(indent + marker + symbol)

    child_indent = indent + ("    " if is_last else "│   ")

    if tree.leftChild is not None:
        draw(tree.leftChild, child_indent, is_last=False)

    if tree.rightChild is not None:
        draw(tree.rightChild, child_indent, is_last=True)
#main program allows user to choose between expressions given in main file after choosing expression
#program runs if 1 u can chose if 2 break if 3 or any number u got a function in decoy file already itruns it 
#if u choose any of expressions u will fill up decoy file
mm=0
while mm<2:
    z=int(input("write statuse if u wanna chose 1 wanna leave 2 already have press any: "))
    if z==1:
        with open("d://lab3.txt","r") as s:
            with open("d://lab3decoy.txt","w") as l:
                p=s.readline()

                p=p.split("@")
                i=0
                while i<len(p):
                    print(i+1,end=".")
                    print(p[i])
                    i=i+1
                s=len(p)
                n=str(s)
                print("We have number of "+n+" expressions in file which one u want to parse??")
                num=int(input())
                num=num-1
                if num>=s:
                    print("Out of bound")
                else:
                    x=p[num]
                    x1=x[:len(x)//2]
                    x2=x[len(x)//2:]
                    l.write(x1+'\n'+x2)
                    mm=mm+1
    elif z==2:
        break
    else:
        theTree=G()
        if not error:
             printTree(theTree);
             value = evaluate(theTree); 
             print("The value is",value)
             draw(theTree)
        else:
             print("There was an error")
        mm=mm+2
            

