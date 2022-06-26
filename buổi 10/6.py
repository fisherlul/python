def ky_tu_khong_trung_lap(s):
   chuoiKetQua = ""
   for kyTu in s:
       if kyTu not in chuoiKetQua:
           chuoiKetQua += kyTu
   return chuoiKetQua

def dem_ky_tu(s):
   chuoiKyTu = ky_tu_khong_trung_lap(s)
   for kyTu in chuoiKyTu:
       dem = s.count(kyTu)
       #Hien thi ra man hinh
       print("'{}': {}; ".format(kyTu, dem), end='')

s = input()
dem_ky_tu(dict(s))    