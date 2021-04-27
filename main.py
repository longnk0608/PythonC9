# from tkinter import *
#
# window = Tk()
#
# btn_add = Button(text = 'Add two Number')
# btn_add.pack()
#
#
#
# window.mainloop()
#gán thong tin doi tuong
from NVdemo import Nhan_vien

# nv1 = Nhan_vien()
# nv1.ma_nhan_vien = "NV01"
# nv1.ten_nhan_vien = "Hoàng"
# nv1.luong_nhan_vien = 2000
nv1 = Nhan_vien( ma_nv="NV1", ten_nv= "Nguyen Thi 1", luong_nv=2000)

nv2 = Nhan_vien()
nv2.ma_nhan_vien = "NV02"
nv2.ten_nhan_vien = "Tran Van 2"
nv2.luong_nhan_vien = 1000

nv3=Nhan_vien(ma_nv="NV03", ten_nv="Nguyen Van 3", luong_nv=4000)

#truy xuất thông tin của dt
print (nv1.ten_nhan_vien,",", nv2.ten_nhan_vien)
# nv1.xoa_mot_nhan_vien()
nv1.xoa_mot_nhan_vien()
print(nv1.ma_nhan_vien,nv1.ten_nhan_vien,nv1.luong_nhan_vien)

ds_nv =[nv1,nv2,nv3]
for i in range (0,len(ds_nv)):
    print (ds_nv[i].ten_nhan_vien)

def xoa_nhan_vien():
ten = input("Vui long nhap ten muon tim: ")
flag = 0
dsconlai = []
for i in range(0, len(ds_nv)):
    if ten not in ds_nv[i].ten_nhan_vien :
        dsconlai.append(ds_nv[i])
    else:
        flag = 1

if flag ==0:
    Print("Khong tim thay ten xoa")
return dsconlai



for i in range(0,len(ds_con_lai)):
    print("Nhan vien con lai")
    print(ds_con_lai[i].ten_nhan_vien)














