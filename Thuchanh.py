from nhanviendemoLong import Nhanviendemo

nv1 = Nhanviendemo(manv="NV1",tennv="Nguyen van Mot", luongnv = 2000)
nv2 = Nhanviendemo(manv="NV2",tennv="Nguyen van Hai", luongnv = 2000)
nv3 = Nhanviendemo(manv="NV3",tennv="Nguyen van Ba", luongnv = 2000)
nv4 = Nhanviendemo(manv="NV4",tennv="Nguyen thi Bon", luongnv = 2000)

# ripnt (nv1.ma_nhan_vien, nv2.ten_nhan_vien)

dsnhanvien = [nv1,nv2,nv3,nv4]
for i in range (0,len(dsnhanvien)):
    print (dsnhanvien[i].ten_nhan_vien)

def xoanhanvien():
    ten_can_xoa= input("Vui long nhap ten can xoa :")
    flag = 0
    dsconlai = []
    for i in range (0,len(dsnhanvien)):
        if ten_can_xoa not in dsnhanvien[i].ten_nhan_vien:
            dsconlai.append(dsnhanvien[i])

        else:
            flag = 1

    if flag == 0:
        print("Khong tim thay ten de xoa")
    return dsconlai

dsconlai = xoanhanvien()
print ("Danh sách còn lại bao gồm:")
for l in range (0,len(dsconlai)):
        print(dsconlai[l].ten_nhan_vien)



