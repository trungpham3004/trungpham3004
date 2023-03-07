

Hoten=(input("Ho ten="))
Songaycong=int(input("So ngay cong="))
Dongiangaycong=int(input("Don gia ngay cong="))
Hesophucap=float(input("He so phu cap="))
Tamung=int(input("Tam ung="))
luong=round(Dongiangaycong*Songaycong*Hesophucap,2)
thuclinh=round(luong-Tamung,2)
print("Nhan vien ", Hoten,"co tien luong=",luong,"tam ung=", Tamung, "va thuc linh=", thuclinh )
