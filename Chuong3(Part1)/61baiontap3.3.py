
x=int(input("Tieu thu="))
gia1=550
gia2=750
gia3=950
gia4=1350
if x<=100:
    x=tieuthu*gia1
elif x<=150:
    x=100*gia1+(x-100)*gia2
elif x<=200:
    x=100*gia1+50*gia2+(x-150)*gia3
else:
    x=100*gia1+50*gia2+50*gia3+(x-200)*gia4
phaitra=x*1.1 or x+x*0.1
print("Phai tra=",phaitra,sep="")


