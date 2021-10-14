'''
Describe problem in
https://contest.yandex.ru/contest/29188/problems/A/
https://contest.yandex.ru/contest/29188/problems/B/
'''
class desicion_A:
    def __init__(self):
        self.n = int(input())
        self.lst = list(map(int,input().split()))
        self.lst.append(-1)
        #self.lst.sort()
        self.dict_={}
        ch = self.lst[0]
        index=0
        for ind,i in enumerate(self.lst):
            if i!=ch:
                self.dict_[ch] = (index,ind-1)
                index = ind
                ch = i
        print(self.dict_)
        
    def func_find(self,l,r,m,t)->int:
        m = (l+r)//2
        while len(self.lst[l:r+1])>1:
            
            if self.lst[m]>t:
                r = m-1
            elif self.lst[m]<t:
                l=m+1
            elif self.lst[m]==t:
                break
            m = (l+r)//2
        return m
        
    def left_right_border2(self):
        k = int(input())
        ans=[]
        arr = list(map(int,input().split()))
        for index in range(k):
            m = arr[index]
            if m in self.dict_:
                a,b = self.dict_[m]
                ans.append((a+1,b+1))
            else:
                ans.append((0,0))
        for i,j in ans:
            print('{} {}'.format(i,j))

    def how_many_numbers(self):
        k = int(input())
        ans=[]
        for _ in range(k):
            l,r = map(int,input().split())
            l1 = self.func_find(0,self.n-1,0,l)
            r1 = self.func_find(0,self.n-1,0,r)
            #print(self.lst[l1],self.lst[r1])
            if self.lst[l1]<l or self.lst[r1]>r:
                ans.append(0)
                continue
            if l1>0:
                s = self.lst[l1-1]
                while s==self.lst[l1]:
                    l1-=1
                    if l1==0:
                        break
            if r1<self.n-1:
                s = self.lst[r1+1]
                while s==self.lst[r1]:
                    r1+=1
                    if r1==self.n-1:
                        break
            size=len(self.lst[l1:r1+1])
            ans.append(size)
        print(' '.join(map(str,ans)))
    def left_right_border(self):
        k = int(input())
        ans=[]
        arr = list(map(int,input().split()))
        for index in range(k):
            m = arr[index]
            l1 = self.func_find(0,self.n-1,0,m)
            #print(self.lst[l1],self.lst[r1])
            if self.lst[l1]!=m:
                ans.append((0,0))
                continue
            #print(m,l1)
            a,b=l1-1,l1+1
            if m>0:
                while True:
                    if m!=self.lst[a] or a==0:
                        a+=1
                        break
                    a-=1
                    
            if l1<self.n:
                while True:
                    if b==self.n or m!=self.lst[b]:
                        b-=1
                        break
                    b+=1
            ans.append((a+1,b+1))
        for i,j in ans:
            print('{} {}'.format(i,j))
#desicion = desicion_A()
#desicion.left_right_border2()

'''
Describe problem:
https://contest.yandex.ru/contest/29188/problems/C/
'''
def get_squere_expression(a,b,c):
    if a*b*c==0:
        D = b**2-4*a*c
        if D>0:
            return ((-b+D**0.5)//(2*a),(-b-D**0.5)//(2*a))
        elif D==0:
            return (-b//(2*a))
        else:
            None
    else:
        if a==0:
            return get_cube_with_b(b,c)
        if b==0:
            return get_cube_with_c(a,c)

def get_cube_with_b(a,b):
    if a!=0:
        return -b/a
    elif a==0:
        return None
    else:
        return 0

def get_cube_with_c(a,b):
    if b<0:
        if a!=0:
            return ((-b/a)**0.5, -(-b/a)**0.5)
        else:
            return 0
    elif b==0:
        return 0
    else:
        return None

def get_desicion_square(a,b,c,d):
    answer=[]
    if a == 0:
        ans = get_squere_expression(b,c,d)
        if ans != None:
            answer.append(ans)
    elif d ==0:
        ans = get_squere_expression(a,b,c)
        if ans != None:
            answer.append(ans)
    elif b==0:
        ans = get_cube_with_c(a,b)
        if ans != None:
            answer.append(ans)
            answer.append(0)
    elif c==0:
        ans = get_cube_with_b(a,c)
        if ans != None:
            answer.append(ans)
            answer.append(0)


def get_decision_cube(a,b,c,d):
    answer = []
    if a+b+c+d==0:
        return 1
    elif b+d==a+c:
        return -1
    else:
        pass

def get_definite_null(a,b,c,d):
    if a*b*c*d==0:
        get_desicion_square(a,b,c,d)
    else:
        get_decision_cube(a,b,c,d)

def get_decision_exercise():
    a,b,c,d = map(int, input().split())
    if a*b*c*d==0:
        get_definite_null(a,b,c,d)
