import threading
import numpy
import self
import json
import funcion
from threading import Thread
from selenium.webdriver.common.by import By
import var
from selenium import webdriver
import time
import action
import threaded
import decode
from seleniumwire.utils import decode as sw_decode



# file_name = 'emso.text'
# with open(file_name, 'r', encoding='utf-8') as f:
#     data = json.load(f, strict = False)
#     converted_file = data.decode('utf-8')
#     print(converted_file)









#
# with open('emso.log','rb') as f:
#     for ln in f:
#         decoded=False
#         data1 = ln.decode("utf-8")
#         if data1 != "@":
#             print("aaaa")


        # print(data1)




# with open('emso.log','rb') as f:
#     for ln in f:
#         decoded=False
#         line=''
#         # print(ln)
#         # for cp in ('cp1252', 'cp850','utf-8','utf8'):
#         #     try:
#         #         line = ln.decode(cp)
#         #         decoded=True
#         #         break
#         #     except UnicodeDecodeError:
#         #         pass
#         data1 = ln.decode("utf-8")





def dang_nhap(self):
    funcion.login.khong_thanh_cong_tk_emso1(self)
    funcion.login.khong_thanh_cong_tk_emso2(self)
    funcion.login.thanh_cong_tk_emso(self)
    funcion.login.chon_tk_dang_nhap_gan_day_khong_nhap_pass(self)
    funcion.login.chon_tk_dang_nhap_gan_day_nhap_sai_pass(self)
    funcion.login.chon_tk_dang_nhap_gan_day_chua_luu_mk(self)
    funcion.login.chon_tk_dang_nhap_gan_day_da_luu_mk(self)

    funcion.login.thanh_cong_tk_google1(self)
    # funcion.login.thanh_cong_tk_google2(self) #để chạy cuối, đang lỗi



def trangcanhan(self):
    action.login.login3(self, "truongvck33@gmail.com", "atgmj123456")
    funcion.thongtincanhan_anhdaidien(self)
    funcion.thongtincanhan_anhbia(self)
    funcion.gioithieu.gioithieu_tongquan(self)
    funcion.gioithieu.congviec_vahocvan(self)
    funcion.gioithieu.xemsukientrongdoi_congviecvahocvan(self)
    funcion.gioithieu.trangcanhan_gioithieu_congviecvahocvan_addthem(self)
    funcion.gioithieu.trangcanhan_gioithieu_thongtincoban(self)
    funcion.gioithieu.trangcanhan_gioithieu_gd_va_mqh(self)
    funcion.gioithieu.trangcanhan_gioithieu_sukientrongdoi(self)
    funcion.gioithieu.trangcanhan_gioithieu_noitungsong(self)
    funcion.anh_video.anh_video(self)
    funcion.check_thongtin_trangcanhan.check_thongtin_trangcanhan(self)
    funcion.banbe.banbe_tatcabanbe(self)


def trangchu(self):
    action.login.login4(self, "truongvck33@gmail.com", "atgmj123456")
    funcion.trangchu.taobaiviet_khoangkhac(self)
    funcion.trangchu.menu(self)
    funcion.trangchu.tinnhanmoi(self)
    funcion.trangchu.chat(self)
    funcion.trangchu.chat_xemtatca(self)
    funcion.trangchu.caidatcanhan_chuyentaikhoan(self)
    funcion.trangchu.canhan_caidatvaquyenriengtu(self)
    funcion.trangchu.trogiupvahotro(self)




