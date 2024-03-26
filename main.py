import emso
import action
import var
import threading
from threading import Thread
import time
import unittest
import multiprocessing
from selenium.webdriver.common.by import By
import asyncio



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
        action.runtest()


if __name__ == "__main__":
    unittest.main()


















from selenium.webdriver.chrome.options import Options
from selenium import webdriver







# soluong = 4
# threads= []
#
# for x in range(soluong):
#     threads += [threading.Thread(target=action.runtest, args={x}, )]
# for t in threads:
#     t.start()
# # for t in threads:
# #     t.join()
# #     print("t2:", t)
# print("Kết thúc số luồng")









