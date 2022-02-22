print("****************************    Methods for List     ****************************************") 


l1 = ["Audi","B.M.W","Tesla","jaguar"]

l2 = ["Tony","captain"]


l1.append("MG")
print(l1)


o=l1.copy()
print(o)


t = l1.count("Tesla")
print(t)


l1.extend(l2)
print("new list ",l1)


r=l1.index("Tony")
print(r)


l1.insert(2, "Volvo")
print(l1)


l1.pop()
print(l1)


l1.remove("MG")
print(l1)


l1.reverse()
print(l1)


l1.sort()
print(l1)


l1.clear()
print(l1)






print("**************************   Methods for dictionary    ***********************************")
print("  ")


d1={"gujarat":"gujju","punjab":"punjabi","maharastra":"marathi"}

x=d1.copy()
print(x)


w =("ktm","cbr","ninja")
e =("bike")
dict = dict.fromkeys(w,e)
print(dict)


s=d1.get("gujarat")
print(s)


j=d1.items()
print(j)


v=d1.keys()
print(v)


d1.pop("maharastra")
print(d1)


d1.popitem()
print(d1)


q=d1.setdefault("punjab","sardarji")
print(q)


d1.update({"kerela":"maliyali"})
print(d1)


b=d1.values()
print(b)


d1.clear()
print(d1)


print("  ")
print("**************************    Methods for Strings    ******************************************")

st1 = "hello,i am jil."


sw=st1.splitlines()
print(sw)


mydict = {83:  80}
BN=st1.translate(mydict)
print(BN)


t45="567"
yu=t45.zfill(17)
print(yu)


sd=st1.upper()
print(sd)



hte=st1.partition("i")
print(hte)

io=st1.replace("jil","jack")
print(io)

		
ty=st1.rfind("i")
print(ty)


ri=st1.rindex("am")
print(ri)


cv=st1.rjust(10)
print(cv,"hope u r all nice")



fg=st1.rsplit(",")
print(fg)


ni=st1.startswith("hello")
print(ni)


st=st1.swapcase()
print(st)


y=st1.capitalize()
print(y)

d=st1.casefold()
print(d)

c=st1.center(20)
print(c)

n=st1.count("i")
print(n)

k=st1.encode()
print(k)


l=st1.endswith(".")
print(l)


st2="c\th\t\a\tn\tg\te\t"
e=st2.expandtabs(3)
print(e)


x=st1.find("am")
print(x)


txt="movie will start at {time:.2f}"
print(txt.format(time = 2.30))


I=st1.index("jil")
print(I)


hi=st1.isalnum()
print(hi)


RT=st1.isalpha()
print(RT)


er=st1.isascii()
print(er)


df=st1.isspace()
print(df)


pr=st1.isprintable()
print(pr)


ti=st1.istitle()
print(ti)


turple = ("bishop","ryan","dwayne")
qw="#".join(turple)
print(qw)


su=st1.isupper()
print(su)


te=st1.ljust(10)
print(te,"nice to meet u")


op=st1.lstrip()
print(op)


txt2="pain is temp"
mytable=txt2.maketrans("p","g")
print(txt2.translate(mytable))
