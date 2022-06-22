import sys
def find_longest_prefix(str1,str2):   #求最长公共前缀
    str1=str1.strip(" ")
    str2=str2.strip(" ")
    shortest_str=str1
    max_prefix=len(shortest_str)
    flag=0
    i1=0
    while(i1<max_prefix):
        if str2[i1]!=shortest_str[i1]:
            break
        i1+=1
    if(i1==0):
        return ""
    else:
        ss=shortest_str[:i1]
        return ss
def fir_str(str):              #求string的first集合
    vocabs=str.strip(" ").split(" ")
    f_alp=set()
    f_alp.update(set_inf[vocabs[0].strip(" ")]-empty_set)
    i=0
    j=0
    for i in range(1,len(vocabs)): #对于字符串中的每个元素
        flag=True
        for j in range(0,i):
            if("#" not in set_inf[vocabs[j].strip(" ")]):
                flag=False
                break
        if(flag==True):
            for k in range(0,i):
                f_alp.update(set_inf[vocabs[k].strip(" ")]-empty_set)
    flag1=True
    for i in range(0,len(vocabs)):
        if("#" not in set_inf[vocabs[i].strip(" ")]):
            flag1=False
            break
    if(flag1==True):   #若每个字符串的first集合都有#
        f_alp.add("#")
    return f_alp
class ana_stack:
    def __init__(self):
        self.container = []
        self.top = 0
    def push(self,str):
        self.container.append(str)
        self.top+=1
    def pop(self):
        self.container.pop()
        self.top-=1
    def get_top(self):
        return self.container[self.top-1]
n=int(input('请输入文法产生式个数：'))
gen=[]  # 产生式列表
end_toks = set()  # 终结符
non_end_toks = set()  # 非终结符
for i in range(0,n):
    x = input()
    gen.append(x)
for i in range(0,len(gen)):
    y = gen[i].split('->')[0].strip(" ")
    non_end_toks.add(y)
for i in range(0,len(gen)):
    y = gen[i].split('->')[1]
    z = y.split('|')
    for j in range(0,len(z)):
        r1=z[j].split(' ')
        for k in range(0,len(r1)):
            if(r1[k].strip(" ") not in non_end_toks and r1[k].strip(" ")!=""):
                end_toks.add(r1[k])
print(non_end_toks)#非终结符集合
print(end_toks)#终结符
start=gen[0].split("->")[0]
print(start)#开始符号

#消除左递归
final1_gen=[]
for i in range(0,len(gen)):
    lefts=gen[i].split("->")[0].strip(" ")
    right=gen[i].split("->")[1].split("|")
    #rights=set()
    s1=set()#有左递归的右半部分
    s2=set()#无左递归部分
    for j in range(0,len(right)):
        temp1=right[j].strip(" ")
        a=temp1.find(" ")
        if(temp1.find(" ")!=-1):
            temp=temp1[:temp1.find(" ")]
        else :
            temp=""
        if(temp==lefts):
            s1.add(temp1[temp1.find(" ")+1:])
        else:
            s2.add(right[j].strip(" "))
    ss1=list(s1)
    ss2=list(s2)
    if(len(s1)==0):
        final1_gen.append(gen[i])
        continue
    else:
        str1=lefts+" "+"->"+" "
        for k in range(0,len(ss2)-1):
            str1=str1+ss2[k]+" "+lefts+"'"+" "+"|"
        str1=str1+ss2[len(ss2)-1]+" "+lefts+"'"
        final1_gen.append(str1)
        str2=lefts+"'"+" "+"->"+" "
        non_end_toks.add(lefts+"'")
        for k1 in range(0,len(s1)):
            str2=str2+ss1[k1]+" "+lefts+"'"+" "+"|"
        str2=str2+"#"
        final1_gen.append(str2)
print(final1_gen)
sfinal=set(final1_gen)
#提取左因子
final_gen=[]
for i in  range(0,len(final1_gen)):                         #对于每个表达式
    left=final1_gen[i].split("->")[0].strip(" ")
    right=final1_gen[i].split("->")[1].split("|")
    for al in right:
        al=al.strip(" ")
    length=[]   #公共子串 长度
    s=""   #s是左因子
    for l in range(1,len(right)):                   #对于右边的项
        stemp=find_longest_prefix(right[0],right[l])
        if(stemp!=""):
            stemp=stemp.strip(" ")
        if(len(stemp)!=0):
            s=stemp
        length.append(len(stemp))
    if(length!=[]):
        length.insert(0,length[0])
    else:
        length.append(0)
    if(length[0]==0):                        #没有左因子就直接插入原式
        final_gen.append(final1_gen[i])
    else:
        str1=left+" "+"->"+" "+s.strip(" ")+" "+left+"'"
        non_end_toks.add(left+"'")
        final_gen.append(str1)             #加入新的非终结符S‘
        for k in range(0,len(right)):
            str2 = left + "'" + " " + "->"
            if(length[k]!=0):          #有左因子项的
                if (length[k] != len(right[k].strip(" "))):
                    str2 = str2 + " " + (right[k].strip(" "))[length[k]:].strip(" ")
                    final_gen.append(str2)
                else:
                    str2 = str2 + " " + "#"
                    final_gen.append(str2)
            else:              #无左因子的项
                str2 = left + " " + "->"
                str2=str2+" "+right[k].strip(" ")
                final_gen.append(str2)
print(final_gen)
simplest=[]
for i in range(0,len(final_gen)):
    right=final_gen[i].split("->")[1].split("|")
    if(len(right)==1):
        simplest.append(final_gen[i])
    else:
        left=final_gen[i].split("->")[0]+"->"
        for j in range(0,len(right)):
            simplest.append(left+right[j])
print(simplest)                #最终分析用的产生式
for it in simplest:
    left=it.split("->")[0].strip(" ")
    non_end_toks.add(left)
print("start to get first set...")
#求first集合
set_inf={}
for items in non_end_toks:
    set_inf[items]=set()
for items in end_toks:
    set_inf[items]=set()
for items in end_toks:
    set_inf[items].add(items)
set_inf["#"]=set()
set_inf["#"].add("#")
empty_set=set()
empty_set.add("#")
chan_fl=True

while(chan_fl==True):         #集合有变化，就继续循环，否则退出
    chan_fl=False
    for gener in simplest:
        k=0
        continue_=True
        right=gener.split("->")[1].split(" ")
        ff=True
        while(ff==True):
            ff=False
            if('' in right):
                ff=True
                right.remove('')
        n=len(right)               #表达式右边的所有符号
        while ( continue_ == True and k < n ):    #遍历右侧的符号
            if(right[k]!='#'):                    #右侧不是#
                current_set=set_inf[gener.split("->")[0].strip(" ")].copy()
                set_inf[gener.split("->")[0].strip(" ")].update(set_inf[right[k]]-empty_set)
                if(current_set!=set_inf[gener.split("->")[0].strip(" ")]):
                    chan_fl=True
            else:
                current_set=set_inf[gener.split("->")[0].strip(" ")].copy()
                set_inf[gener.split("->")[0].strip(" ")].add("#")
                if(current_set!=set_inf[gener.split("->")[0].strip(" ")]):
                    chan_fl=True
            if("#" not in set_inf[right[k]]):        #如果当前右侧符号的first集合不含#就结束
                continue_=False
            k=k+1
        if(continue_==True):      #所有元素的first集合都含#
            current_set=set_inf[gener.split("->")[0].strip(" ")].copy()
            set_inf[gener.split("->")[0].strip(" ")].add("#")
            if (current_set != set_inf[gener.split("->")[0].strip(" ")]):
                chan_fl=True
print("first set:")
print(set_inf)

#求follow集合
fol_set_inf={}
for lab in non_end_toks:
    fol_set_inf[lab]=set()
fol_set_inf[start.strip(" ")].add("$")#开始符号加入$
flag=True
while(flag==True):
    flag=False
    for gener in simplest:
        right=gener.split("->")[1].split(" ")
        left=gener.split("->")[0].strip(" ")
        ff=True
        while(ff==True):
            ff=False
            if('' in right):
                ff=True
                right.remove('')
        n=len(right)
        for k in range(0,n):
            if(right[k].strip(" ") in non_end_toks):   #右侧的非终结符
                if(k==n-1):
                    current_set=fol_set_inf[right[k].strip(" ")].copy()
                    fol_set_inf[right[k].strip(" ")].update(fol_set_inf[left])
                    if(current_set!=fol_set_inf[right[k].strip(" ")]):
                        flag=True
                elif(k<n-1):
                    r=gener.split("->")[1]
                    tempstr=r[r.find(right[k])+len(right[k]):]
                    f_alp=fir_str(tempstr)       #求后面串的first集合
                    current_set=fol_set_inf[right[k].strip(" ")].copy()
                    fol_set_inf[right[k].strip(" ")].update(f_alp-empty_set)
                    if("#" in f_alp):
                        fol_set_inf[right[k].strip(" ")].update(fol_set_inf[left])       #后面串有first集合就把左边符号的follow集合加进去
                    if(current_set!=fol_set_inf[right[k].strip(" ")]):
                        flag=True

print("follow set:")
print(fol_set_inf)
print("==============改写后的文法===============")
for k in range(0,len(simplest)):
    print(k,end=" ")
    print(simplest[k])
#构建分析表
table={}
for item in non_end_toks:
    table.update({item:{}})
for k in range(0,len(simplest)):
    right_str=simplest[k].split("->")[1]
    left_str=simplest[k].split("->")[0].strip(" ")
    ffir=fir_str(right_str)                 #得到右边字符串的first集合
    for item in ffir:
        if(item!='#'):
            if(item in table[left_str].keys()):
                print("不是ll1文法")
                sys.exit()
            table[left_str][item]=simplest[k]
    if("#" in ffir):          #如果右边first集合有#，就往左边集合的follow元素中填表
        for item in fol_set_inf[left_str]:
            if(item in table[left_str].keys()):
                print("不是ll1文法")
                sys.exit()
            table[left_str][item]=simplest[k]
print("============ll1分析表================")
for item in table.keys():
    for v in table[item].keys():
        print(item,end=" ")
        print(v,end=" ")
        print(table[item][v])
print("输入待分析的串：")
uncertain=input()
stack=ana_stack()
stack.push("$")
stack.push(start.strip(" "))
tokens=uncertain.split(" ")
tokens.append("$")
k=0
while(k<len(tokens)):
    s11=stack.get_top()
    print(s11)
    if(s11 in non_end_toks and tokens[k].strip(" ") not in table[s11]):      #表中没这项
        print("匹配失败")
        break
    elif(s11 in non_end_toks and tokens[k].strip(" ") in table[s11]):       #替换
        stack.pop()
        expr=table[s11][tokens[k].strip(" ")]
        exp_right=expr.split("->")[1].split(" ")
        ff=True
        while(ff==True):
            ff=False
            if('' in exp_right):
                ff=True
                exp_right.remove('')
        num=len(exp_right)-1
        print("替换 ",expr)
        if(exp_right[0]!='#'):
            while num>=0:
                stack.push(exp_right[num])
                num-=1
    elif(s11 == tokens[k].strip(" ")):         #匹配
        print("匹配")
        k+=1
        stack.pop()
if(k==len(tokens)):    #若匹配到了最后一个字符位
    print("匹配成功")