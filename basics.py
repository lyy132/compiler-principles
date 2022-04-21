from inspect import stack
from lib2to3.pgen2.pgen import NFAState
from logging import StringTemplateStyle
from ntpath import join
import string
from tracemalloc import start
from typing import final
import numpy as np
from tkinter import *
from tkinter import ttk
from graphviz import Digraph
from queue import Queue
from pip import main
class Stack:
     def __init__(self):
         self.items = []

     def empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def top(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
postack=Stack()
a=[] #状态表
b=[] #状态转换表
final_dfastate=[]
final_transition=[]
mappings={} #新旧标号之间的映射
def priority(c):
    c1=postack.top()
    priorities={'*':3,'.':2,'|':1,'(':0}#优先级表
    if(priorities[c]<=priorities[c1]):#c是当前元素 c1是栈顶元素
        return True
    else:
        return False
        
def algorithm(*args):
    try:
        #chars={0:'a',1:'b',2:'c',1:'b',1:'b'}
        #s2.set(reg.get())
        s=""
        s=reg.get()
        s1=list(s) #s1是list类型
        print(len(s1))
        nn=len(s1)
        i=0
        while(i<nn):
            #print(i)
            #print(nn)
            #print('\n')
            if(i<nn-1):
                if(s1[i]>='a' and s1[i]<='z'):
                    if(s1[i+1]>='a' and s1[i+1]<='z'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1
                    elif(s1[i+1]=='#'):
                        s1.insert(i+1,'.')
                        i=i+1 
                        nn=nn+1                       
                    elif(s1[i+1]=='('):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1 
                if(s1[i]=='#'):
                    if(s1[i+1]>='a' and s1[i+1]<='z'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1
                    elif(s1[i+1]=='#'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1                        
                    elif(s1[i+1]=='('):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1                     
                if(s1[i]==')'):
                    if(s1[i+1]>='a' and s1[i+1]<='z'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1
                    elif(s1[i+1]=='#'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1                        
                    elif(s1[i+1]=='('):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1    
                if(s1[i]=='*'):
                    if(s1[i+1]>='a' and s1[i+1]<='z'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1
                    elif(s1[i+1]=='#'):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1                        
                    elif(s1[i+1]=='('):
                        s1.insert(i+1,'.')
                        i=i+1
                        nn=nn+1  
            i=i+1                                                          
        s=''.join(s1)
        print(s)                  
        #s2.set(s)
        #逆波兰表达式
        res=list()
        i=0
        while(i<nn):
            #print(i)
            #print(s1[i])
            #print(postack.size())
            if(s1[i]>='a' and s1[i]<='z' or s1[i]=='#'):
                res.append(s1[i])
            elif(s1[i]=='('):
                postack.push(s1[i])
            elif(s1[i]==')'):
                while not postack.top()=='(':
                    res.append(postack.top())
                    postack.pop()
                postack.pop()
            elif(s1[i]=='*'or s1[i]=='|' or s1[i]=='.'):
                if(postack.empty()):
                    postack.push(s1[i])                
                elif(postack.top()=='('):
                    postack.push(s1[i])
                elif(priority(s1[i])==True):
                    while(postack.size()>0 and priority(s1[i])==True):
                        res.append(postack.top())
                        postack.pop()
                    postack.push(s1[i])
                else:
                    postack.push(s1[i])
            i=i+1
        while not postack.empty():
            res.append(postack.top())
            postack.pop()
        s2.set(''.join(res))
        '''g = Digraph('测试图片')
        g.node(name='a',color='red')
        g.node(name='b',color='blue')
        g.edge('a','b',color='green')
        g.view()
        print("heeee")'''

    except ValueError:
        pass
class NFA:
    def __init__(self):               
        self.state1=state()
        self.state2=state()
        self.tran=[transition() for i in range (10)]
class state:
    def __init__(self):
        self.ID=0
        self.start=0
        self.accept=0 
class transition:
    def __init__(self):
        self.sourcestate=state()
        self.targetstate=state()
        self.ways=''        

def createNFA(*args):
    s22=s2.get()
    s3=list(s22)
    nfastack=Stack()#存放nfa的栈

    i=0
    k=0
    while(i<len(s3)):
        #print(nfastack.size())
        if(s3[i]>='a' and s3[i]<='z' or s3[i]=='#'):
            N1=NFA()
            N1.state1.ID=k
            N1.state1.start=1
            N1.state1.accept=0
            k=k+1
            N1.state2.ID=k
            N1.state2.start=0
            N1.state2.accept=1   
            k=k+1        
            N1.tran[0].sourcestate=N1.state1
            N1.tran[0].targetstate=N1.state2
            N1.tran[0].ways=s3[i]
            nfastack.push(N1)
            a.append(N1.state1)
            a.append(N1.state2)
            b.append(N1.tran[0])
        elif(s3[i]=='|'):
            t1=nfastack.top()
            nfastack.pop()
            t2=nfastack.top()
            nfastack.pop()
            N3=NFA()
            num=0            
            N3.state1.ID=k
            N3.state1.start=1
            N3.state1.accept=0
            t1.state1.start=0
            t1.state2.accept=0
            k=k+1
            N3.state2.ID=k
            N3.state2.start=0
            N3.state2.accept=1  
            t2.state1.start=0         
            t2.state2.accept=0
            k=k+1
            N3.tran[num].sourcestate=N3.state1
            N3.tran[num].targetstate=t1.state1
            N3.tran[num].ways='#'              
            num=num+1  
            N3.tran[num].sourcestate=N3.state1
            N3.tran[num].targetstate=t2.state1
            N3.tran[num].ways='#'      
            num=num+1
            N3.tran[num].sourcestate=t1.state2
            N3.tran[num].targetstate=N3.state2
            N3.tran[num].ways='#'  
            num=num+1
            N3.tran[num].sourcestate=t2.state2
            N3.tran[num].targetstate=N3.state2
            N3.tran[num].ways='#' 
            num=num+1
             
            nfastack.push(N3)         
            a.append(N3.state1)
            a.append(N3.state2)
            for ii in range(0,num):
                b.append(N3.tran[ii])
            #print("finish")             
        elif(s3[i]=='.'):
            t1=nfastack.top()
            nfastack.pop()
            t2=nfastack.top()
            nfastack.pop()
            N3=NFA()
            N3.state1.ID=k
            N3.state1.start=1
            N3.state1.accept=0
            k=k+1
            N3.state2.ID=k
            N3.state2.start=0
            N3.state2.accept=1
            k=k+1
            t1.state1.start=0
            t1.state2.accept=0
            t2.state1.start=0
            t2.state2.accept=0
            num=0
            N3.tran[num].sourcestate=N3.state1
            N3.tran[num].targetstate=t2.state1
            N3.tran[num].ways='#'   
            num=num+1
            N3.tran[num].sourcestate=t2.state2
            N3.tran[num].targetstate=t1.state1
            N3.tran[num].ways='#'  
            num=num+1
            N3.tran[num].sourcestate=t1.state2
            N3.tran[num].targetstate=N3.state2
            N3.tran[num].ways='#'    
            nfastack.push(N3)
            a.append(N3.state1)
            a.append(N3.state2)
            for ii in range(0,3):
                b.append(N3.tran[ii])            
        elif(s3[i]=='*'):
            t1=nfastack.top()
            nfastack.pop()
            N3=NFA()
            N3.state1.ID=k
            N3.state1.start=1
            N3.state1.accept=0
            k=k+1
            N3.state2.ID=k
            N3.state2.start=0
            N3.state2.accept=1
            k=k+1
            t1.state1.start=0
            t1.state2.accept=0
            num=0
            N3.tran[num].sourcestate=N3.state1
            N3.tran[num].targetstate=t1.state1
            N3.tran[num].ways='#'   
            num=num+1
            N3.tran[num].sourcestate=N3.state1
            N3.tran[num].targetstate=N3.state2
            N3.tran[num].ways='#'   
            num=num+1
            N3.tran[num].sourcestate=t1.state2
            N3.tran[num].targetstate=t1.state1
            N3.tran[num].ways='#'   
            num=num+1
            N3.tran[num].sourcestate=t1.state2
            N3.tran[num].targetstate=N3.state2
            N3.tran[num].ways='#'
            num=num+1 
            nfastack.push(N3)  
            a.append(N3.state1)
            a.append(N3.state2)
            for ii in range(0,num):
                b.append(N3.tran[ii])
        i=i+1
    g = Digraph('测试图片')
    #print("a="+str(len(a)))
    #print(len(b))
    for i in  range(0,len(a)):
        if(a[i].start==1):
            g.edge('start',str(a[i].ID),color='blue')
            g.node(name=str(a[i].ID),color='red',shape='circle')
        elif(a[i].accept==1):
            g.node(name=str(a[i].ID),color='red',shape='doublecircle')
        else:
            g.node(name=str(a[i].ID),color='red',shape='circle')            
    for j in range(0,len(b)):
        g.edge(str(b[j].sourcestate.ID),str(b[j].targetstate.ID),str(b[j].ways),color='green')
    g.view()
    #print("heeee")
def combine(startstate):# #合并
    fstate=[]
    while not startstate.empty():
        t=startstate.get()
        fstate.append(t)
        for j in range(0,len(b)):
            if b[j].sourcestate.ID==t and b[j].ways=='#':
                startstate.put(b[j].targetstate.ID) 
    return fstate       
def createDFA(*args):
    startstate=Queue(maxsize=500) #NFA开始状态
    fstate=[]
    for i in range(0,len(a)):
        if(a[i].start==1):
            startstate.put(a[i].ID)
            break
    fstate=combine(startstate)
    #print(fstate)
    statetrans=[]
    dfastate=[]
    dfastate.append(fstate)
     #list的大小
    j=0
    nn=0
    sizee=1
    print(dfastate[nn])
    while(nn<sizee):
        print(dfastate[nn])
        for c in range(0,26):#假设字母表有ab
            print("chahrew")
            char=chr(c+97) 
            temp=Queue(maxsize=2000)                              
            for j in range (0,len(dfastate[nn])):
                #print(len(b))
                for k1 in range(0,len(b)):
                    #print(b[k1].sourcestate.ID)
                    #print(b[k1].ways)
                    #print(char)
                    #print(dfastate[nn][j])
                    if(b[k1].sourcestate.ID==dfastate[nn][j] and b[k1].ways==str(char)):#条件判断没进去
                        #print(b[k1].targetstate.ID)
                        temp.put(b[k1].targetstate.ID)
                
            temp1=[]
            temp1=combine(temp)
            temp1_set=set(temp1)
            temp1=list(temp1_set)#去重            
            #print(temp1)
            if temp1 not in dfastate:
                dfastate.append(temp1)
                sizee=sizee+1
            statetrans.append([dfastate[nn],char,temp1])
        nn=nn+1
    print(dfastate)
    print(statetrans)
    cnt=0

    startnum=0
    endnum=0
    for i in range(0,len(a)):
        if(a[i].start==1):
            startnum=a[i].ID
        if(a[i].accept==1):
            endnum=a[i].ID
    for i in range(0,len(dfastate)):
        #print(dfastate[i])
        flag=0
        for j in range(0,len(dfastate[i])):
            if(endnum in dfastate[i]):
                    s=state()
                    s.start=0
                    s.accept=1
                    s.ID=cnt
                    mappings[cnt]=dfastate[i]
                    cnt=cnt+1
                    final_dfastate.append(s)
                    flag=1
                    break
            elif startnum in dfastate[i]:
                    s=state()
                    s.start=1
                    s.accept=0
                    s.ID=cnt
                    mappings[cnt]=dfastate[i]
                    cnt=cnt+1
                    final_dfastate.append(s)
                    flag=1 
                    break                               
        print(i)
        print(j)
        if(flag==0):#既不是开始也不是结束
            s=state()
            s.start=0
            s.accept=0
            s.ID=cnt
            mappings[cnt]=dfastate[i]
            cnt=cnt+1
            final_dfastate.append(s)  
    print(mappings) 
    for i in range(0,len(statetrans)):
        ttr=transition()
        if(statetrans[i][0]!=[]):#只存了头非空的转换
            
            ttr.sourcestate=list(mappings.keys())[list(mappings.values()).index(statetrans[i][0])]
            ttr.targetstate=list(mappings.keys())[list(mappings.values()).index(statetrans[i][2])]
            ttr.ways=statetrans[i][1]
            final_transition.append(ttr)
    for i in range(0,len(final_transition)):
        print(final_transition[i].sourcestate,end="")
        print(final_transition[i].targetstate,end="")
        print(final_transition[i].ways)
    g = Digraph('测试dfa')
    #print("a="+str(len(a)))
    #print(len(b))
    for i in  range(0,len(final_dfastate)):
        if(mappings[final_dfastate[i].ID]!=[]):
            if(final_dfastate[i].start==1):
                g.edge('start',str(final_dfastate[i].ID),color='blue')
                g.node(name=str(final_dfastate[i].ID),color='red',shape='circle')
            elif(final_dfastate[i].accept==1):
                g.node(name=str(final_dfastate[i].ID),color='red',shape='doublecircle')
            else:
                g.node(name=str(final_dfastate[i].ID),color='red',shape='circle')            
    for j in range(0,len(final_transition)):
        if(mappings[final_transition[j].sourcestate]!=[] and mappings[final_transition[j].targetstate]!=[]):
            g.edge(str(final_transition[j].sourcestate),str(final_transition[j].targetstate),str(final_transition[j].ways),color='green')
    g.view()    
    return 0
def createminimizedDFA(*args):
    ori_cata={}
    for i in range(len(final_dfastate)):
        if(mappings[final_dfastate[i].ID]!=[]):
            if(final_dfastate[i].accept==1):
                ori_cata[final_dfastate[i].ID]=2;
            else:
                ori_cata[final_dfastate[i].ID]=1;
    kinds=2
    previous=1
    mata= {}
    ll=0
    for i in range(len(final_transition)):
        '''if(mappings[final_transition[i].sourcestate]!=[] and final_transition[i].sourcestate not in mata.keys()):
            mata[final_transition[i].sourcestate]={ord(final_transition[i].ways):final_transition[i].targetstate}
            ll=ll+1            
        elif(mappings[final_transition[i].sourcestate]!=[] and final_transition[i].sourcestate in mata.keys()):
            mata[final_transition[i].sourcestate].update({ord(final_transition[i].ways):final_transition[i].targetstate})
        '''
        if(final_transition[i].sourcestate not in mata.keys()):
            mata[final_transition[i].sourcestate]={ord(final_transition[i].ways):final_transition[i].targetstate}
            ll=ll+1            
        elif(final_transition[i].sourcestate in mata.keys()):
            mata[final_transition[i].sourcestate].update({ord(final_transition[i].ways):final_transition[i].targetstate})
    for key,value in mata.items():
        value=sorted(value.items(),key=lambda k:k[0])
    print(mata)
    print(ori_cata)
    maps={} #更新后节点的类号   
    while not kinds==previous:
        cnt=1
        if(len(maps) is not 0):
            for key,value in maps.items():
                ori_cata[key]=value
        maps={}
        set1={}
        previous=kinds
        for key,value in mata.items():
            state1=[]
            state1.append(ori_cata[key])
            for key1,value1 in value.items():
                if(mappings[value1]!=[]):
                    state1.append(ori_cata[value1])
                else:
                    state1.append(-1)
            if(tuple(state1) not in set1.keys()):
                maps[key]=cnt
                set1[tuple(state1)]=cnt
                cnt=cnt+1
            else:
                maps[key]=set1[tuple(state1)]
        print(maps)
        kinds=cnt-1
    print(ori_cata)# 新的编号
    new_states1=[] #新的状态表
    new_transition=[]
    for i in range(len(final_dfastate)):
        ss1=state()
        if(mappings[final_dfastate[i].ID]!=[]):
            ss1.ID=ori_cata[final_dfastate[i].ID]
            if(final_dfastate[i].accept==1):
                ss1.accept=1
                ss1.start=0
            elif final_dfastate[i].start==1:
                ss1.start=1
                ss1.accept=0
            else:
                ss1.start=0
                ss1.accept=0
            if ss1 not in new_states1:
                new_states1.append(ss1)
    for i in range(len(final_transition)):
        if(mappings[final_transition[i].sourcestate]!=[] and mappings[final_transition[i].targetstate]!=[]):
            '''tran=transition()
            tran.sourcestate=ori_cata[final_transition[i].sourcestate]
            tran.targetstate=ori_cata[final_transition[i].targetstate]
            tran.ways=final_transition[i].ways'''
            tran=[ori_cata[final_transition[i].sourcestate],ori_cata[final_transition[i].targetstate],final_transition[i].ways]
            if tran not in new_transition:
                new_transition.append(tran)
    
    for i in range(0,len(new_transition)):
        print(new_transition[i])
    g = Digraph('测试最小化dfa')
    #print("a="+str(len(a)))
    #print(len(b))
    for i in  range(0,len(new_states1)):
        if(new_states1[i].start==1):
            g.edge('start',str(new_states1[i].ID),color='blue')
            g.node(name=str(new_states1[i].ID),color='red',shape='circle')
        elif(new_states1[i].accept==1):
            g.node(name=str(new_states1[i].ID),color='red',shape='doublecircle')
        else:
            g.node(name=str(new_states1[i].ID),color='red',shape='circle')            
    for j in range(0,len(new_transition)):
        g.edge(str(new_transition[j][0]),str(new_transition[j][1]),str(new_transition[j][2]),color='green')
    g.view()    
    return 0
root=Tk()
root.title("Regex to NFA and DFA")
mainframe=ttk.Frame(root,padding="5 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
label1=Label(mainframe,text="请输入正则表达式（epsilon用#代替）：")
label1.grid(row=1,column=1)
reg=StringVar()
reg_entry=ttk.Entry(mainframe,width=15,textvariable=reg)
reg_entry.grid(row=1,column=2,rowspan=1,columnspan=2)
button1=Button(mainframe,text="提交",command=algorithm).grid(row=1,column=6)
s2=StringVar()
ttk.Label(mainframe,text="逆波兰表达式为：").grid(row=2,column=1)
ttk.Label(mainframe, textvariable=s2).grid(row=2,column=2)
#s3=s2
button2=Button(mainframe,text="generate NFA",command=createNFA).grid(row=3,column=1)
button3=Button(mainframe,text="generate DFA",command=createDFA).grid(row=3,column=3)
button4=Button(mainframe,text="generate minimized DFA",command=createminimizedDFA).grid(row=3,column=6)
root.bind("<Return>", algorithm)
root.mainloop()