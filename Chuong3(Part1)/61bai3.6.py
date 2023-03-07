


a=int(input(""))
b=int(input(""))
c=int(input(""))

if (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0):
    print("Tam giac vuong",(a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==a*a+b*b))
if (a+b>c) and (a+c>b) and (b+c>a) and (a>0) and (b>0) and (c>0):
        print("Tam giac deu",(a==b) and (b==c) and (c==a))
else:
    print("Tam giac loai khac")
elif (a+b<c) or (a+c<b) or (b+c<a) or (a>0) or (b>0) or (c>0):
    print("Khong hop le")