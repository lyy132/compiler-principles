import sys

import termtables as tt
def adddot(s):   #加点，若右边不是#就在箭头后面加，否则去掉#
    if(s.split("->")[1]=="#"):
        new_s=s.replace("#",".")
        return new_s
    new_s=s.replace("->","->.")
    return new_s
def add_new_exps(ch,states):   #求闭包的函数，返回值是一个状态
    history=[]      #已经拓展过的非终结符
    history.append(ch)
    for i in range(len(final_lex)):
        if(final_lex[i].split("->")[0]==ch):
            new_s=adddot(final_lex[i])
            states.append(new_s)
            #如果新表达式还能拓展
            if(new_s.find(".")!=len(new_s)-1 and new_s[new_s.find(".")+1] in non_end_toks and new_s[new_s.find(".")+1] not in history):
                add_new_exps(new_s[new_s.find(".")+1],states)
    return states
def shift_to_states(state,k):
    k1 = len(states)
    chars = {}  # 所有.后面的元素
    for it in state:
        if (it.find(".") != len(it) - 1):
            if (it[it.find(".") + 1] not in chars.keys()):
                chars[it[it.find(".") + 1]] = []
            chars[it[it.find(".") + 1]].append(state.index(it))
    for item in chars:
        state2 = []
        seq = []  # 初始未扩展的表达式
        flag1 = False
        for l in chars[item]:
            n1 = state[l]
            loc_d = n1.find(".")
            n1 = list(state[l])
            n1.remove(".")
            n1.insert(loc_d + 1, '.')
            n1 = ''.join(n1)
            state2.append(n1)
            seq.append(n1)
            hist = []
        for item_1 in seq:
            if (item_1.find(".") != len(item_1) - 1):
                if (item_1[item_1.find(".") + 1] in non_end_toks and (
                        item_1[item_1.find(".") + 1] not in hist or hist == [])):
                    hist.append(item_1[item_1.find(".") + 1])
                    state2 = add_new_exps(item_1[loc_d + 2], state2)
        if (seq not in origin.values()):
            states.append(state2)
            shifts.append([k, item_1[item_1.find(".") - 1], states.index(state2)])
            origin[states.index(state2)] = seq
        else:
            for ii in origin.keys():
                if (origin[ii] == seq):
                    inde = ii
            shifts.append([k, item_1[item_1.find(".") - 1], inde])
'''k1=len(states)   #状态集合的长度
    chars={}         #所有.后面的元素及其对应的状态中生成式的序号
    for it in state:
        if(it.find(".")!=len(it)-1):
            if(it[it.find(".")+1] not in chars.keys()):
                chars[it[it.find(".")+1]]=[]
            chars[it[it.find(".")+1]].append(state.index(it))
    for item in chars:
        state2=[]
        flag1=False
        for l in chars[item]:
            n1=state[l]
            loc_d = n1.find(".")
            n1=list(state[l])
            n1.remove(".")    #去掉点，往后移一位
            n1.insert(loc_d + 1, '.')
            n1=''.join(n1)   #list转字符串
            state2.append(n1)
            if (n1.find(".") != len(n1) - 1): #点不在末尾，判断能不能拓展
                if (n1[n1.find(".") + 1] in non_end_toks):
                    state2 = add_new_exps(n1[loc_d + 2], state2)
                if (state2[0] not in state_first):
                    states.append(state2)
                    state_first.append(state2[0])
            else:
                if (state2[0] not in state_first):
                    states.append(state2)
                    state_first.append(state2[0])
                else:
                    ind = state_first.index(state2[0])
                    shifts.append([k, item, ind])
                    flag1=True
                    continue
        if(flag1==False):  #
            k1+=1
            shifts.append([k,item,states.index(state2)])'''

class ana_stack:
    def __init__(self):
        self.ana=[]
        self.top=-1
    def push(self,s):
        self.ana.append(s)
        self.top+=1
    def pop(self):
        self.ana.pop()
        self.top-=1
    def get_top(self):
        return self.ana[self.top]
    def printt(self):
        print(self.ana)
states=[]     #状态集合
shifts=[]     #转换集合
state_first=[]#每个state的第一个元素
origin={}
gen=[]
final_lex=[]
print("请输入产生式个数：")
n=int(input())
for i in range(n):
    str1=input()
    gen.append(str1)
start=gen[0].split("->")[0] #开始符号
final_lex.append(start+"'"+"->"+start)#拓广文法
non_end_toks=set()
end_toks=set()
non_end_toks.add(start+"'")
new_start=start+"'"
for i in range(n):
    non_end_toks.add(gen[i].split("->")[0])   #等式左边的都是非终结符
for i in range(0,n):
    left=gen[i].split("->")[0]
    right=gen[i].split("->")[1]
    right_eles=right.split("|")
    for k in range(len(right_eles)):
        final_lex.append(left + "->"+right_eles[k])       #求最终分析用的产生式
        sim=right_eles[k]
        for l in range(len(sim)):
            if(sim[l] not in non_end_toks):
                end_toks.add(sim[l])
print("============终结符==============")
print(end_toks)
print("============非终结符==============")
print(non_end_toks)
print("=============最终产生式=================")
print(final_lex)
#开始构造dfa状态
state1=[]
s1=adddot(final_lex[0])
state_first.append(s1)
state1.append(s1)
l=len(state1)
loc=s1.find(".")
if(s1[loc+1] in non_end_toks):
    state1=add_new_exps(s1[loc+1],state1)   #求闭包
origin[0]=[s1]
states.append(state1)
k=0
print(states[0])
print("==============求DFA===================")
global ll
ll=len(states)
while(True):   #状态数不再增加就结束构建
    if(k>=ll):
        break
    shift_to_states(states[k],k)
    k+=1
    ll=len(states)
print("================状态表===================")
print(states)
print("=================转换表=====================")
print(shifts)
#构造lr0分析表
table=[]
new_shifts=sorted(shifts,key=lambda book: book[0])
print(new_shifts)

for i in range(0,len(states)):
    table.append({})#构建一行
    temp2=states[i]
    cnt=[]#规约项的序号
    for j in range(len(temp2)):
        if(temp2[j].find('.')==len(temp2[j])-1):
            cnt.append(j)
    if(len(cnt)>0):#reduce项
        if(len(cnt)!=len(temp2)):
            print("不是lr0文法")
            sys.exit()
        for subs in cnt:
            temp_str=temp2[subs]
            temp_str=temp_str.replace(".","")
            if(temp_str.split("->")[1]==''):
                temp_str+="#"
            index1=final_lex.index(temp_str)
            if(temp_str.split("->")[0].strip(" ")!=new_start):
                for items in end_toks:
                    if (items in table[i].keys()):
                        print("不是lr0文法")
                        sys.exit()
                    if(items!='#'):
                        table[i][items]='r'+str(index1)
            if(temp_str.split('->')[0].strip(" ")==new_start):
                table[i]['$'] = "acc"
            else:
                table[i]['$']='r'+str(index1)
    else:#shift项
        for ob in new_shifts:
            if(ob[0]==i):
                if(ob[0] in table[i].keys()):
                    print("不是lr0文法")
                    break
                if(ob[1] in non_end_toks):
                    table[i][ob[1]]=str(ob[2])
                elif ob[1] in end_toks:
                    table[i][ob[1]]='s'+str(ob[2])
'''k=-1
for i in range(0,len(new_shifts)):
    if(i==0):
        table.append({})
        k+=1
    elif(new_shifts[i][0]!=new_shifts[i-1][0]):
        table.append({})
        k+=1
    if(new_shifts[i][1] in end_toks):
        table[k][new_shifts[i][1]]="s"+str(new_shifts[i][2])
    elif(new_shifts[i][1]=='$'):
        table[k][new_shifts[i][1]] = "acc"
    else:
        table[k][new_shifts[i][1]]=str(new_shifts[i][2])
'''
'''final_table = tt.to_string(data=table[0],header=['action','goto'] ,style=tt.styles.ascii_thin_double,
                           padding=(0, 1))
print(final_table)
'''
print(table)
print("请输入需要分析的串:")
undef=input()
undef=undef+'$'
stack=ana_stack()#分析栈
stack.push('$0')
top_ele=stack.get_top()
cur_state=top_ele.replace('\[a\-z\]\|\[A\-Z\]\|\$','')
print(cur_state)
loc=0
while(cur_state[1]!='1'):
    stack.printt()
    char=undef[loc]
    top_ele = stack.get_top()
    string1 = ''
    for i in range(0,len(top_ele)):
        if(top_ele[i]>='0' and top_ele[i]<='9'):
            string1=string1+top_ele[i]
    ss=int(string1)#得到后面的数字(状态号)
    if(char not in table[ss].keys()):
        print("不符合文法")
        break
    next_ele=table[ss][char]
    if(next_ele[0]=='r'):
        going_to_push=""
        exp_num =''
        kk=1
        while(kk<len(next_ele)):
            exp_num+=next_ele[kk]
            kk+=1
        exp_num=int(exp_num)#表达式编号
        print('reduce ',final_lex[exp_num])
        exp_char_ri=final_lex[exp_num].split("->")[1][0]#右侧第一个符号
        exp_char_le=final_lex[exp_num].split("->")[0]#右侧第一个符号
        going_to_push+=exp_char_le

        while(stack.get_top()[0]!=exp_char_ri):
            stack.pop()
        stack.pop()#pop掉栈顶
        cur_top=stack.get_top()
        top_num=''
        kk=1
        while(kk<len(next_ele)):#获得当前栈顶的状态号
            top_num+=cur_top[kk]
            kk+=1
        top_num=int(top_num)
        for it in shifts:
            if(it[0]==top_num and it[1]==exp_char_le):
                push_num=it[2]
                break
        going_to_push+=str(push_num)
        stack.push(going_to_push)#入栈新状态
    elif(next_ele[0]=='s'):

        print('shift')
        going_to_push=char
        kk=1
        top_num=''
        cur_top=stack.get_top()
        while(kk<len(next_ele)):#获得当前栈顶的状态号
            top_num+=cur_top[kk]
            kk+=1
        top_num=int(top_num)
        for it in shifts:
            if(it[0]==top_num and it[1]==char):
                push_num=it[2]
                break
        going_to_push+=str(push_num)
        stack.push(going_to_push)#入栈新状态
        loc+=1

    elif(next_ele[0]=='a'):
        print("acc")
        break
