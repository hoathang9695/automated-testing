import threading
import numpy
import self

import funcion
from threading import Thread
from selenium.webdriver.common.by import By
import var
from selenium import webdriver
import time
import threaded





#
#
# @threaded.Threaded
# def dang_nhap(self):
#     print("so luong", self)
#     Options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=Options)
#     driver.get("https://docs.python.org/3.8/library/threading.html#threading.target")
#
#     funcion.login.khong_thanh_cong_tk_emso1(self)
#     funcion.login.khong_thanh_cong_tk_emso2(self)
#     funcion.login.thanh_cong_tk_emso(self)
#
#     funcion.login.chon_tk_dang_nhap_gan_day_khong_nhap_pass(self)
#     funcion.login.chon_tk_dang_nhap_gan_day_nhap_sai_pass(self)
#     funcion.login.chon_tk_dang_nhap_gan_day_chua_luu_mk(self)
#     funcion.login.chon_tk_dang_nhap_gan_day_da_luu_mk(self)
#
#     funcion.login.thanh_cong_tk_google1(self)
#     # funcion.login.thanh_cong_tk_google2(self) #để chạy cuối, đang lỗi
#
#
# @threaded.Threaded
# def trangcanhan(self):
#     print("so luong", self)
#     Options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=Options)
#     driver.get("https://docs.python.org/3.8/library/threading.html#threading.target")
#     # funcion.thongtincanhan_anhdaidien(self)
#     # funcion.thongtincanhan_anhbia(self)
#     funcion.gioithieu.gioithieu_tongquan(self)
#     funcion.gioithieu.congviec_vahocvan(self)
#     funcion.gioithieu.xemsukientrongdoi_congviecvahocvan(self)
#     funcion.gioithieu.trangcanhan_gioithieu_congviecvahocvan_addthem(self)
#     funcion.gioithieu.trangcanhan_gioithieu_thongtincoban(self)
#     funcion.gioithieu.trangcanhan_gioithieu_gd_va_mqh(self)
#     funcion.gioithieu.trangcanhan_gioithieu_sukientrongdoi(self)
#     funcion.gioithieu.trangcanhan_gioithieu_noitungsong(self)
#
#     funcion.banbe.banbe_tatcabanbe(self)
#     funcion.anh_video.anh_video(self)
#     funcion.check_thongtin_trangcanhan.check_thongtin_trangcanhan(self)
#
#
#
# thread = dang_nhap(self)
# thread.start()
# thread.join()
#
# thread1 = trangcanhan(self)
# thread1.start()
# thread1.join()






# soluong = 6
# barrier = Barrier(soluong)
#
# for i in range(6):








# luong1 = Thread(target= dang_nhap(self=""))
# luong2 = Thread(target= trangcanhan(self=""))
# luong2.start()
# luong1.start()








# def runtest(self):
#     print("đang chạy luồng", self)
#     Options = webdriver.ChromeOptions()
#     # Options.add_argument("https://www.youtube.com/watch?v=VN3-VkM7SqY&t=1464s")
#     driver = webdriver.Chrome(options=Options)
#     driver.get("https://www.youtube.com/watch?v=VN3-VkM7SqY&t=1464s"
#     funcion.gioithieu.gioithieu_tongquan(self="")
#     driver.set_window_size(400, 600)
#     time.sleep(1000)



# def login3(self):
#     print("đang chạy luồng", self)
#     Options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=Options)
#     driver.implicitly_wait(15)
#     driver.get(var.url)
#     driver.maximize_window()
#     driver.find_element(By.XPATH, var.login_user).send_keys("truongvck33@gmail.com")
#     driver.find_element(By.XPATH, var.login_password).send_keys("atgmj123456")
#     driver.find_element(By.XPATH, var.login_submit).click()
#     time.sleep(3.5)
#     driver.find_element(By.XPATH, var.trangcanhan).click()
#     time.sleep(1000)









# soluong =4
# threads = []
# for x in range(soluong):
#     threads += [threading.Thread(target= dang_nhap, args={x}, )]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("het rui")





# threads = []
# for x in range(4):
#     threads += [threading.Thread(target=dang_nhap, args= {x}).start()]
#     threads += [threading.Thread(target=trangcanhan, args={x}).start()]
#     # threading.Thread(target=trangcanhan(self=""), args= {x}).start()
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("het rui")






# def checkout():
#   browser.get("https//:google.com")


# for i in range(5):
#     browserThread = threading.Thread(target = trangcanhan(self=""), args = "")
#     browserThread.start()




# soluong =4
# threads = []
# for i in range(soluong):
#     threads += [threading.Thread(target= trangcanhan(self=""), args={i}, )]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("het rui")







# luong1 = Thread(target= dang_nhap(self=""))
# luong1.start()
#
# luong2 = Thread(target= trangcanhan(self=""))
# luong2.start()


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
    funcion.banbe.banbe_tatcabanbe(self)
    # funcion.anh_video.anh_video(self)
    funcion.check_thongtin_trangcanhan.check_thongtin_trangcanhan(self)


def trangchu(self):
    funcion.trangchu_taobaiviet.taobaiviet_congkhai(self)


