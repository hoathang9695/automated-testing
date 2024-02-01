import emso
import action
import var
import threading
from threading import Thread
import time
import unittest
import multiprocessing




class Test(unittest.TestCase):
    def test_run(self):
        #Emso
        # emso.dang_nhap(self="")
        emso.trangcanhan(self="")
        # emso.trangchu(self="")
        # emso.chat(self="")
        # emso.khoanhkhac(self="")
        # emso.watch(self="")
        # emso.trang(self="")
        # emso.nhom(self="")

        #Người mua
        # emso.muahangthanhcong(self="")
        # emso.muahangthatbai(self="")

        #Người bán
        # emso.quanlysanpham(self="")
        # emso.kenhmarketing(self="")

        #Add dữ liệu
        # emso.add_dulieuemso(self="")


if __name__ == "__main__":
    unittest.main()





from selenium.webdriver.chrome.options import Options
from selenium import webdriver
#
# def runtest(x):
#     print("đang chạy luồng", x)
#     chrome_options = Options()
#     driver = webdriver.Chrome(var.PATH, chrome_options=chrome_options)
#     driver.get("https://cmc-fe.emso.vn")
#     driver.set_window_size(400, 600)
#     time.sleep(10)
# soluong = 4
# threads1= [
#         emso.trangcanhan(self=""),
#         emso.muahangthanhcong(self=""),
#         emso.quanlysanpham(self=""),
#         emso.add_dulieuemso(self="")
# ]
# threads= []
#
# for x in range(soluong):
#     threads += [threading.Thread(target=runtest, args={x}, )]
# for t in threads:
#     t.start()
# for t in threads:
#     t.join()
# print("Kết thúc số luồng")

