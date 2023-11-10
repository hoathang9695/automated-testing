from urllib import response

import openpyxl
import asyncio
import requests
# from pytz import unicode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
options = Options()
from seleniumwire.utils import decode as sw_decode
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import Select
import csv
import json
import var
from retry import retry
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import urllib.request as request
import subprocess
import urllib.error as error

import datetime as dt
from seleniumwire import webdriver
from seleniumwire.utils import decode


driver = webdriver.Chrome(var.PATH)


import pandas as pd
import codecs
import decode
from selenium.common.exceptions import InvalidSessionIdException
import unittest
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#read wrirte csv
def getRowCount(file, sheetName):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return (sheet.max_row)

def getColumnCount(file, sheetName):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return (sheet.max_column)

def readData(file,sheetName,rownum,columnno):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    return sheet.cell(row=rownum,column=columnno).value

def writeData(file,sheetName,rowum,columnno,data):
    wordbook = openpyxl.load_workbook(file)
    sheet = wordbook.get_sheet_by_name(sheetName)
    sheet.cell(row=rowum,column=columnno).value = data
    wordbook.save(file)


rows = getRowCount(var.path_baocao,'Sheet1')


file_name = 'data_emso.json'
with open(file_name, 'r', encoding='utf-8') as f:
    data = json.load(f, strict = False)




logging.basicConfig(handlers=[logging.FileHandler(filename="C:/Users/Admin/PycharmProjects/pythonProject/emso.log",
                                                 encoding='utf-8', mode='a+')],
                    format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%F %A %T",
                    level=logging.INFO)



logging.debug("đây là debug")
logging.info("đây là info")
logging.warning("đây là warning")
logging.error("đây là error")
logging.critical("đây là critical")

@retry(tries=3, delay=2, backoff=1, jitter=5, )
def logout():
    driver.implicitly_wait(15)
    time.sleep(2)
    driver.set_window_size(1024, 768)
    driver.find_element(By.XPATH, var.logout_chontaikhoan1).click()
    driver.find_element(By.XPATH, var.logout_dangxuat).click()
    writeData(var.path_baocao, "Sheet1", 31, 2, "x")
    time.sleep(2)


class login():
    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login1(self, user, password):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_user).send_keys(user)
        driver.find_element(By.XPATH, var.login_password).send_keys(password)
        driver.find_element(By.XPATH, var.login_submit).click()
        time.sleep(1)
        message_sai_tk_mk = driver.find_element(By.XPATH, var.message_sai_tk_mk1).text
        print(message_sai_tk_mk)
        logging.info("Đăng nhập bằng tài khoản emso-(Đăng nhập không thành công/Chuyển tài khoản không thành công): Nhập sai tài khoản/mật khẩu")
        logging.info("Message: Tài khoản hoặc mật khẩu không đúng, vui lòng kiểm tra lại.")
        logging.info( message_sai_tk_mk == "Tài khoản hoặc mật khẩu không đúng, vui lòng kiểm tra lại.")
        print("tên tài khoản login:", user)
        print("mật khẩu login:", password)
        print("login vào phần mềm emso khong thành công")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login2(self, user, password):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_user).send_keys(user)
        driver.find_element(By.XPATH, var.login_password).send_keys(password)
        driver.find_element(By.XPATH, var.login_submit).click()
        time.sleep(1)
        # bỏ trống tài khoản
        message_bo_trong_tk = driver.find_element(By.XPATH, var.message_bo_trong_tk1).text
        print(message_bo_trong_tk)
        logging.info("Đăng nhập bằng tài khoản emso-(Đăng nhập không thành công/Chuyển tài khoản không thành công): Không nhập tài khoản/mật khẩu")
        logging.info("Message Email, Số điện thoại:Email hoặc số điện thoại không được để trống ")
        logging.info(message_bo_trong_tk == "Email hoặc số điện thoại không được để trống")
        # bỏ trống mật khẩu
        message_bo_trong_mk = driver.find_element(By.XPATH, var.message_bo_trong_mk1).text
        print(message_bo_trong_mk)
        logging.info("Đăng nhập bằng tài khoản emso-(Đăng nhập không thành công/Chuyển tài khoản không thành công): Không nhập tài khoản/mật khẩu")
        logging.info("Message Mật khẩu: Mật khẩu không được để trống")
        logging.info(message_bo_trong_mk == "Mật khẩu không được để trống")

        print("tên tài khoản login:", user)
        print("mật khẩu login:", password)
        print("login vào phần mềm emso khong thành công")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login3(self, user, password):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        # driver.set_window_size(400, 600)

        driver.find_element(By.XPATH, var.login_user).send_keys(user)
        driver.find_element(By.XPATH, var.login_password).send_keys(password)
        driver.find_element(By.XPATH, var.login_submit).click()
        time.sleep(3.5)
        login_thanh_cong = driver.find_element(By.XPATH, var.login_thanhcong_khoanh_khac).text
        print(login_thanh_cong)
        logging.info("Đăng nhập bằng tài khoản emso/Gmail")
        logging.info( login_thanh_cong == "Khoảnh khắc")
        print("tên tài khoản login:", user)
        print("mật khẩu login:", password)
        print("login vào phần mềm emso thành công")
        driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1)

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login4(self, user, password):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_user).send_keys(user)
        driver.find_element(By.XPATH, var.login_password).send_keys(password)
        driver.find_element(By.XPATH, var.login_submit).click()
        time.sleep(3.5)
        login_thanh_cong = driver.find_element(By.XPATH, var.login_thanhcong_khoanh_khac).text
        print(login_thanh_cong)
        logging.info("Đăng nhập bằng tài khoản google - Đăng nhập thành công - tài khoản đã có sẵn và đã được đồng bộ")
        logging.info( login_thanh_cong == "Khoảnh khắc")
        print("tên tài khoản login:", user)
        print("mật khẩu login:", password)
        print("login vào phần mềm emso thành công")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_google(self, user, passsword):
        driver.implicitly_wait(20)
        driver.get(var.url)
        # driver.maximize_window()
        driver.find_element(By.XPATH, var.login_google).click()
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.title)
        time.sleep(1)
        driver.find_element(By.XPATH, var.login_google_nhap_gmail).send_keys(user)
        driver.find_element(By.XPATH, var.login_google_tiep).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.login_google_nhap_password).send_keys(passsword)
        time.sleep(1)
        driver.find_element(By.XPATH, var.login_google_tiep).click()
        time.sleep(15)
        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.title)
            if driver.title =="Mạng xã hội Emso":
                login_thanh_cong = driver.find_element(By.XPATH, var.login_thanhcong_khoanh_khac).text
                print(login_thanh_cong)
                logging.info("Đăng nhập bằng tài khoản google - Đăng nhập thành công - tài khoản chưa có sẵn và đã được đồng bộ")
                logging.info(login_thanh_cong == "Khoảnh khắc")

                logout()
                writeData(var.path_baocao, "Sheet1", 16, 2, "x")
                print("Current session is {}".format(driver.session_id))
                driver.close()
                # try:
                #     driver.get("https://sn.emso.vn/login")
                # except Exception as e:
                #     print("ko vao duoc emso")
                #     # print(e.message)

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_chon_tk_dang_nhap_gan_day_nhap_sai_pass(self, password):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_password).send_keys(password)
        driver.find_element(By.XPATH, var.login_nho_mat_khau).click()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_dang_nhap).click()
        time.sleep(1)
        message_ganday_sai_mk = driver.find_element(By.XPATH, var.message_sai_tk_mk1).text
        print(message_ganday_sai_mk)
        logging.info("Chọn tài khoản đăng nhập gần đây - (Đăng nhập không thành công/Chuyển tài khoan không thành công) - Nhập sai pass")
        logging.info("Message: Tài khoản hoặc mật khẩu không đúng, vui lòng kiểm tra lại.")
        logging.info( message_ganday_sai_mk == "Tài khoản hoặc mật khẩu không đúng, vui lòng kiểm tra lại.")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_chon_tk_dang_nhap_gan_day_khong_nhap_pass(self):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_password).clear()
        driver.find_element(By.XPATH, var.login_nho_mat_khau).click()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_dang_nhap).click()
        time.sleep(1)
        message_ganday_khong_nhap_mk = driver.find_element(By.XPATH, var.message_ganday_khong_nhap_mk1).text
        print(message_ganday_khong_nhap_mk)
        logging.info("Chọn tài khoản đăng nhập gần đây - (Đăng nhập không thành công/Chuyển tài khoan không thành công) - Không nhập pass")
        logging.info("Message: Mật khẩu không được để trống")
        logging.info( message_ganday_khong_nhap_mk == "Mật khẩu không được để trống")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_chon_tk_dang_nhap_gan_day_chua_luu_mk(self, password):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_password).send_keys(password)
        driver.find_element(By.XPATH, var.login_nho_mat_khau).click()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_dang_nhap).click()
        time.sleep(3.5)
        login_thanh_cong = driver.find_element(By.XPATH, var.login_thanhcong_khoanh_khac).text
        print(login_thanh_cong)
        logging.info("Chọn tài khoản đăng nhập gần đây - (login thành công/Chuyển tài khoản thành công) - chưa lưu mật khẩu")
        logging.info( login_thanh_cong == "Khoảnh khắc")

    @retry(tries=3, delay=2, backoff=1, jitter=5, )
    def login_chon_tk_dang_nhap_gan_day_da_luu_mk(self):
        driver.implicitly_wait(15)
        driver.get(var.url)
        driver.maximize_window()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day).click()
        time.sleep(3.5)
        login_thanh_cong = driver.find_element(By.XPATH, var.login_thanhcong_khoanh_khac).text
        print(login_thanh_cong)
        logging.info("Chọn tài khoản đăng nhập gần đây - (login thành công/Chuyển tài khoản thành công) - đã lưu mật khẩu")
        logging.info( login_thanh_cong == "Khoảnh khắc")



class anhdaidien():
    def anhdaidien_themmoi(self):
        driver.implicitly_wait(15)
        #thêm ảnh đại diện mới
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_iconmayanh).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_taianhlen).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_icon_taianhlen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        del driver.requests
        driver.find_element(By.XPATH, var.capnhatanhdaidien_mota).send_keys(data['trangcanhan_anhdaidien_anhbia']['anhdaidien_mota'])
        driver.find_element(By.XPATH, var.capnhatanhdaidien_luu).click()
        writeData(var.path_baocao, "Sheet1", 52, 2, "x")
        time.sleep(7)

    def anhdaidien_khac(self):
        driver.implicitly_wait(15)
        #tải lên ảnh đại diện khác
        driver.find_element(By.XPATH, var.trangcanhan_iconmayanh).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_taianhlen).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_icon_taianhlen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien3.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_mota).send_keys(data['trangcanhan_anhdaidien_anhbia']['anhdaidienkhac_mota'])
        driver.find_element(By.XPATH, var.capnhatanhdaidien_luu).click()
        writeData(var.path_baocao, "Sheet1", 53, 2, "x")
        time.sleep(7)


    def anhdaidien_tuanhcosan(self):
        driver.implicitly_wait(15)
        # Chọn từ 1 ảnh có sẵn
        # huỷ
        driver.find_element(By.XPATH, var.trangcanhan_iconmayanh).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonanhthu2).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonanhcosan_luu).click()
        time.sleep(7)
        writeData(var.path_baocao, "Sheet1", 54, 2, "x")

    def anhdaidien_themkhung(self):
        driver.implicitly_wait(15)
        #Thêm khung
        driver.find_element(By.XPATH, var.trangcanhan_iconmayanh).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_themkhung).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_dangquauday).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_dangbuonday).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_yeuthuongvn).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_wowvn).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_tuhaovn).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_trungthu).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_rangrovietnam).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_quockhanhvietnam).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_phunuvietnam).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_noel).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_nhagiaovietnam).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_lacquanvietnam).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_cmsn).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_vulanbaohieu).click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_x).click()
        time.sleep(1)
        #chọn khung yeu thuong vn
        driver.find_element(By.XPATH, var.trangcanhan_iconmayanh).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_themkhung).click()
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_yeuthuongvn).click()
        del driver.requests
        time.sleep(1)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonkhung_luu2).click()
        writeData(var.path_baocao, "Sheet1", 55, 2, "x")
        time.sleep(3.5)

class anhbia():
    def anhbia_tailen(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1.5)
        #tải lên ảnh bìa từ thiết bị
        driver.execute_script("window.scrollBy(0,-100)", "")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_iconchinhsua_anhbia).click()
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_taianhlen).click()
        time.sleep(1)
        del driver.requests
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia1.exe")
        time.sleep(1)
        cap_nhat = driver.find_element(By.XPATH, var.trangcanhan_anhbia_capnhat)
        cap_nhat.click()
        writeData(var.path_baocao, "Sheet1", 57, 2, "x")
        time.sleep(2.5)

    def anhbia_thayanh(self):
        driver.implicitly_wait(15)
        #thay ảnh bìa từ thiết bị
        driver.find_element(By.XPATH, var.trangcanhan_iconchinhsua_anhbia).click()
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_taianhlen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia2.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_capnhat).click()
        time.sleep(2.5)
        writeData(var.path_baocao, "Sheet1", 58, 2, "x")
    def anhbia_chonanh(self):
        driver.implicitly_wait(15)
        #cập nhật ảnh bìa từ ảnh của bạn
        driver.find_element(By.XPATH, var.trangcanhan_iconchinhsua_anhbia).click()
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_chontuanhcuaban).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_chonanhthu2).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_capnhat).click()
        time.sleep(2.5)
        writeData(var.path_baocao, "Sheet1", 59, 2, "x")

    def anhbia_chinhsuavitri(self):
        driver.implicitly_wait(15)
        # chỉnh sửa vị tri ảnh bìa
        driver.find_element(By.XPATH, var.trangcanhan_iconchinhsua_anhbia).click()
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_datlaivitri).click()
        time.sleep(1)
        anh_bia = driver.find_element(By.XPATH, var.trangcanhan_anhbia)
        button_themmoi = driver.find_element(By.XPATH, var.trangcanhan_button_themmoi)
        action1 = ActionChains(driver)
        action1.drag_and_drop(anh_bia, button_themmoi).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_anhbia_capnhat).click()
        time.sleep(2.5)
        writeData(var.path_baocao, "Sheet1", 60, 2, "x")



class checkdata_be():
    def trangcanhan_thongtincanhan_anhdaidien_themmoi(self):
        driver.implicitly_wait(10)
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/me":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: có file ảnh đại diện to không?")
                logging.info(res['avatar_media']['url'] != None)
                logging.info((res['avatar_media']['url']))

                logging.info("check back-end: có file ảnh đại diện nhỏ không?")
                logging.info(res['avatar_media']['preview_url'] != None)
                logging.info((res['avatar_media']['preview_url']))

                logging.info("check back-end: Mô tả ảnh đại diện")
                logging.info("Ảnh đại diện - Mô tả - " + data['trangcanhan_anhdaidien_anhbia']['anhdaidien_mota'])
                logging.info(res['avatar_media']['description'] == data['trangcanhan_anhdaidien_anhbia']['anhdaidien_mota'])
                break
            else:
                print("không có  response")
    def trangcanhan_thongtincanhan_anhdaidien_themkhung(self):
        driver.implicitly_wait(10)
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/me":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                logging.info("check back-end: Chọn khung cho avatar")
                logging.info("Khung ảnh đại diện - " + data['trangcanhan_anhdaidien_anhbia']['khung_anhdaidien'])
                logging.info(res['avatar_media']['frame']['name'] == data['trangcanhan_anhdaidien_anhbia']['khung_anhdaidien'])
                logging.info((res['avatar_media']['frame']['url']))
                break
            else:
                print("không có  response")
    def trangcanhan_thongtincanhan_anhbia_tailen(self):
        driver.implicitly_wait(15)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/me":
                data = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data = data.decode("utf8")
                res = json.loads(data)

                logging.info("check back-end: có file ảnh bìa không?")
                logging.info(res['banner']['show_url'] != None)
                logging.info(res['banner']['show_url'])

                logging.info("check back-end: có file ảnh bìa trên dòng thời gian không?")
                logging.info(res['banner']['url'] != None)
                logging.info(res['banner']['url'])

                logging.info("check back-end: có file ảnh bìa trong danh mục ảnh không?")
                logging.info(res['banner']['preview_url'] != None)
                logging.info(res['banner']['preview_url'])

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_tongquan(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/abouts":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Tổng quan")
                logging.info("check back-end: Sống tại - " + data['trangcanhan_gioithieu_tongquan']['songtai'])
                logging.info((res['general_information']['place_live']['title']) == data['trangcanhan_gioithieu_tongquan']['songtai'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Tổng quan")
                logging.info("check back-end: Đến từ - " + data['trangcanhan_gioithieu_tongquan']['dentu'])
                logging.info((res['general_information']['hometown']['title']) == data['trangcanhan_gioithieu_tongquan']['dentu'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Tổng quan")
                logging.info("check back-end: Tình trạng mqh/Ngày bắt đầu - Ly Thân/2022-01-01")
                logging.info("Mối quan hệ - Ly thân")

                #123
                logging.info(res['account_relationship']['relationship_category']['name'])
                logging.info((res['account_relationship']['relationship_category']['name']) == "Ly Thân")
                logging.info("Mối quan hệ - Ngày bắt đầu")
                logging.info((res['account_relationship']['start_date']) == "2022-01-01")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Tổng quan")
                logging.info("check back-end: Số điện thoại - " + data['trangcanhan_gioithieu_tongquan']['sodienthoai'])
                logging.info(res['general_information']['phone_number'])
                logging.info((res['general_information']['phone_number']) == data['trangcanhan_gioithieu_tongquan']['sodienthoai'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Tổng quan")
                logging.info("check back-end: Biệt danh - " + data['trangcanhan_gioithieu_tongquan']['bietdanh'])
                logging.info((res['general_information']['other_name']))
                logging.info((res['general_information']['other_name']) == data['trangcanhan_gioithieu_tongquan']['bietdanh'])

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_cvvahocvan_congviec(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url[0:70] == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/life_events":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Công ty - " + data['trangcanhan_gioithieu_congviecvahocvan']['congty'])
                logging.info((res['company']) == data['trangcanhan_gioithieu_congviecvahocvan']['congty'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Chức vụ - " + data['trangcanhan_gioithieu_congviecvahocvan']['chucvu'])
                logging.info((res['position']) == data['trangcanhan_gioithieu_congviecvahocvan']['chucvu'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Ngày bắt đầu - " + data['trangcanhan_gioithieu_congviecvahocvan']['ngaybatdau'])
                logging.info((res['start_date']) == "2021-10-03")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['ngayketthuc'])
                logging.info((res['end_date']) == "2022-10-09T00:00:00.000+07:00")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Thành phố/Thị xã - " + data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])
                logging.info((res['city']) == data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Mô tả - " + data['trangcanhan_gioithieu_congviecvahocvan']['mota'])
                logging.info((res['description']) == data['trangcanhan_gioithieu_congviecvahocvan']['mota'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc")
                logging.info("check back-end: Trạng thái - Công khai")
                logging.info((res['visibility']) == "public")

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_cvvahocvan_daihoc(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url[0:70] == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/life_events":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Chuyên nghành - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_chuyennghanh1'])
                logging.info((res['concentration1']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_chuyennghanh1'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Tên đại học - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_truonghoc'])
                logging.info((res['company']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_truonghoc'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Bằng cấp - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_bangcap'])
                logging.info((res['degree']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_bangcap'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Ngày bắt đầu - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_ngaybatdau'])
                logging.info((res['start_date']) == "2019-11-16")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_ngayketthuc'])
                logging.info((res['end_date']) == "2023-11-08T00:00:00.000+07:00")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Mô tả - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_mota'])
                logging.info((res['description']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_mota'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Loại trường = Đại học")
                logging.info((res['school_type']) == "UNIVERSITY")

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_cvvahocvan_trunghoc(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url[0:70] == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/life_events":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học")
                logging.info("check back-end: Tên trung học - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_truonghoc'])
                logging.info((res['company']) == data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_truonghoc'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học")
                logging.info("check back-end: Ngày bắt đầu - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_ngaybatdau'])
                logging.info((res['start_date']) == "2017-10-13")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học")
                logging.info("check back-end: Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_ngayketthuc'])
                logging.info((res['end_date']) == "2020-10-24T00:00:00.000+07:00")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học")
                logging.info("check back-end: Mô tả - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghochoc_mota'])
                logging.info((res['description']) == data['trangcanhan_gioithieu_congviecvahocvan']['trunghochoc_mota'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học")
                logging.info("check back-end: Loại trường - Trung học")
                logging.info((res['school_type']) == "HIGH_SCHOOL")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học")
                logging.info("check back-end: Trạng thái - Công khai")
                logging.info((res['visibility']) == "public")
                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_cvvahocvan_xemsukientrongdoi_congviec(self):
        driver.implicitly_wait(10)
        time.sleep(2)
        for request in driver.requests:
            if request.url[0:39] == "https://snapi.emso.asia/api/v1/statuses":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Công ty - " + data['trangcanhan_gioithieu_congviecvahocvan']['congty'])
                logging.info((res['life_event']['company']) == data['trangcanhan_gioithieu_congviecvahocvan']['congty'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Công ty - Ngày bắt đầu - " + data['trangcanhan_gioithieu_congviecvahocvan']['ngaybatdau'])
                logging.info((res['life_event']['start_date']) == "2021-10-03")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Công ty - Chức vụ - " + data['trangcanhan_gioithieu_congviecvahocvan']['chucvu'])
                logging.info((res['life_event']['position']) == data['trangcanhan_gioithieu_congviecvahocvan']['chucvu'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Công ty - Thành phố/Thị xã - " + data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])
                logging.info((res['life_event']['city']) == data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Công ty - Mô tả - " + data['trangcanhan_gioithieu_congviecvahocvan']['mota'])
                logging.info((res['life_event']['description']) == data['trangcanhan_gioithieu_congviecvahocvan']['mota'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Công ty - Trạng thái - Công khai")
                logging.info((res['life_event']['visibility']) == "public")

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_cvvahocvan_xemsukientrongdoi_daihoc(self):
        driver.implicitly_wait(10)
        time.sleep(2)
        for request in driver.requests:
            if request.url[0:39] == "https://snapi.emso.asia/api/v1/statuses":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Tên đại học - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_truonghoc'])
                logging.info((res['life_event']['company']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_truonghoc'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Ngày bắt đầu - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_ngaybatdau'])
                logging.info((res['life_event']['start_date']) == "2019-11-16")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_ngayketthuc'])
                logging.info((res['life_event']['end_date']) == "2023-11-08T00:00:00.000+07:00")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - loại trường - Đại học")
                logging.info((res['life_event']['school_type']) == "UNIVERSITY")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Chuyên nghành - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_chuyennghanh1'])
                logging.info((res['life_event']['concentration1']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_chuyennghanh1'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Bằng cấp - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_bangcap'])
                logging.info((res['life_event']['degree']) == data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_bangcap'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Công việc - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Trạng thái - Công khai")
                logging.info((res['life_event']['visibility']) == "public")


                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_cvvahocvan_xemsukientrongdoi_trunghoc(self):
        driver.implicitly_wait(10)
        time.sleep(2)
        for request in driver.requests:
            if request.url[0:39] == "https://snapi.emso.asia/api/v1/statuses":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học - Xem sự kiện trong đời")
                logging.info("check back-end: Trung học - Tên Trung học - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_truonghoc'])
                logging.info((res['life_event']['company']) == data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_truonghoc'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học - Xem sự kiện trong đời")
                logging.info("check back-end: Trung học - Ngày bắt đầu - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_ngaybatdau'])
                logging.info((res['life_event']['start_date']) == "2017-10-13")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học - Xem sự kiện trong đời")
                logging.info("check back-end: Trung học - Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_ngayketthuc'])
                logging.info((res['life_event']['end_date']) == "2020-10-24T00:00:00.000+07:00")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học - Xem sự kiện trong đời")
                logging.info("check back-end: Trung học - loại trường - Trung học")
                logging.info((res['life_event']['school_type']) == "HIGH_SCHOOL")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học - Xem sự kiện trong đời")
                logging.info("check back-end: Trung học - Mô tả - " + data['trangcanhan_gioithieu_congviecvahocvan']['trunghochoc_mota'])
                logging.info((res['life_event']['description']) == data['trangcanhan_gioithieu_congviecvahocvan']['trunghochoc_mota'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Trung học - Xem sự kiện trong đời")
                logging.info("check back-end: Trung học - Trạng thái - Công khai")
                logging.info((res['life_event']['visibility']) == "public")

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_thongtincoban(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/account_general_infomation":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin liên hệ(Số điện thoại)")
                logging.info("check back-end: Số điện thoại - " + data['trangcanhan_gioithieu_thongtincoban']['sodienthoai'])
                logging.info((res['phone_number']) == data['trangcanhan_gioithieu_thongtincoban']['sodienthoai'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Liên kết và xã hội")
                logging.info("check back-end: Web - " + data['trangcanhan_gioithieu_thongtincoban']['web'])
                logging.info((res['account_web_link'][0]['url']) == data['trangcanhan_gioithieu_thongtincoban']['web'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Liên kết và xã hội")
                logging.info("check back-end: Liên kết - " + data['trangcanhan_gioithieu_thongtincoban']['lienket'])
                logging.info((res['account_social'][0]['text']) == data['trangcanhan_gioithieu_thongtincoban']['lienket'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
                logging.info("check back-end: Tiểu sử - " + data['trangcanhan_gioithieu_thongtincoban']['tieusu'])
                logging.info((res['description']) == data['trangcanhan_gioithieu_thongtincoban']['tieusu'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
                logging.info("check back-end: Giới tinh - female")
                logging.info((res['gender']) == "female")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
                logging.info("check back-end: Ngày sinh - 3 tháng 10, 2000")
                logging.info("Ngày 3")
                logging.info((res['birth_date']) == 3)

                logging.info("Tháng 10")
                logging.info((res['birth_month']) == 10)

                logging.info("Năm 2000")
                logging.info((res['birth_year']) == 2000)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
                logging.info("check back-end: Biệt danh - " + data['trangcanhan_gioithieu_thongtincoban']['bietdanh'])
                logging.info((res['other_name']) == data['trangcanhan_gioithieu_thongtincoban']['bietdanh'])

                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_giadinh_va_cacmqh(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/abouts":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Mối quan hệ")
                logging.info("check back-end: Mối quan hệ name - " + data['trangcanhan_gd_va_mqh']['name'])
                logging.info((res['account_relationship']['partner']['display_name']) == data['trangcanhan_gd_va_mqh']['name'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Mối quan hệ")
                logging.info("check back-end: Tình trạng mqh/Ngày bắt đầu - Hẹn hò/2022-01-01")
                logging.info("Mối quan hệ - Hẹn hò")
                logging.info(res['account_relationship']['relationship_category']['name'])
                logging.info((res['account_relationship']['relationship_category']['name']) == "Hẹn hò")
                logging.info("Mối quan hệ - Ngày bắt đầu")
                logging.info((res['account_relationship']['start_date']) == "2022-01-01")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Gia đình")
                logging.info("check back-end: Gia đình name - " + data['trangcanhan_gd_va_mqh']['name1'])
                logging.info((res['family_members'][0]['partner']['display_name']) == data['trangcanhan_gd_va_mqh']['name1'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Gia đình")
                logging.info("check back-end: Mối quan hệ - Gia đình")
                logging.info((res['family_members'][0]['family_relationship_category']['name']) =="Gia đình")
                break
            else:
                print("không có  response")
    def trangcanhan_gioithieu_sukientrongdoi(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/statuses?exclude_replies=true&limit=3":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Sự kiện trong đời - Thêm mới sự kiện lên dòng thời gian")
                logging.info("check back-end: Mô tả - " + data['trangcanhan_sukientrongdoi']['dulich_mota'])
                logging.info((res[0]['content']) == data['trangcanhan_sukientrongdoi']['dulich_mota'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Sự kiện trong đời - Thêm mới sự kiện lên dòng thời gian")
                logging.info("check back-end: Tiêu đề - " + data['trangcanhan_sukientrongdoi']['dulich_tieude'])
                logging.info((res[0]['life_event']['name']) == data['trangcanhan_sukientrongdoi']['dulich_tieude'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Sự kiện trong đời - Thêm mới sự kiện lên dòng thời gian")
                logging.info("check back-end: Địa điểm - " + data['trangcanhan_sukientrongdoi']['dulich_diachi'])
                logging.info((res[0]['life_event']['place']['title']) == data['trangcanhan_sukientrongdoi']['dulich_diachi'])

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Sự kiện trong đời - Thêm mới sự kiện lên dòng thời gian")
                logging.info("check back-end: Thời gian - 2023-09-01")
                logging.info((res[0]['life_event']['start_date']) == "2023-09-01")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Sự kiện trong đời - Thêm mới sự kiện lên dòng thời gian")
                logging.info("check back-end:Có ảnh sự kiện trên dòng thời gian không? ")
                logging.info(res[0]['media_attachments'][0]['url'])
                logging.info((res[0]['media_attachments'][0]['url']) != None)
                logging.info(res[0]['media_attachments'][0]['preview_url'])
                logging.info((res[0]['media_attachments'][0]['preview_url']) != None)

                break
            else:
                print("không có  response")



class tongquan():
    def tongquan(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1.5)
        # Trang cá nhân - Giới thiệu tổng quan
        #Sống tại
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_chinhsua).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['songtai'])

        wait = WebDriverWait(driver, 10)
        chon_hanoi = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hanoi)))

        try:
            chon_hanoi.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,700)", "")
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_chinhsua).click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['songtai'])
            chon_hanoi.click()

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_luu).click()
        time.sleep(1.5)
        writeData(var.path_baocao, "Sheet1", 62, 2, "x")
        check_trangcanhan_gioithieu_songtai = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai1).text
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Sống tại")
        logging.info("check font-end: Sống tại - " + data['trangcanhan_gioithieu_tongquan']['songtai'])
        logging.info(check_trangcanhan_gioithieu_songtai == data['trangcanhan_gioithieu_tongquan']['songtai'])

        # Đến từ
        driver.execute_script("window.scrollBy(0,500)", "")
        # time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).send_keys(data['trangcanhan_gioithieu_tongquan']['dentu'])
        wait = WebDriverWait(driver, 10)
        dentu_langson = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_dentu_langson)))

        try:
            dentu_langson.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,700)", "")
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_chinhsua).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).send_keys(data['trangcanhan_gioithieu_tongquan']['dentu'])
            dentu_langson.click()

        # time.sleep(1)
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_langson).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 63, 2, "x")
        check_gioithieu_dentu = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_dentu1).text
        print(check_gioithieu_dentu)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Đến từ")
        logging.info("check font-end: Đến từ - " + data['trangcanhan_gioithieu_tongquan']['dentu'])
        logging.info(check_gioithieu_dentu == data['trangcanhan_gioithieu_tongquan']['dentu'])

        # Mối quan hệ
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_icon_chonmqh).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_lythan).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_nam).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_nam_2022).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_thang).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_thang_1).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_ngay).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_ngay_1).click()

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 64, 2, "x")
        # check_gioithieu_mqh = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh1).text
        # logging.info("Trang cá nhân - Giới thiệu tổng quan - Mối quan hệ")
        # logging.info("check font-end: Ly Thân started 2022-01-01")
        # logging.info(check_gioithieu_mqh == "Ly Thân started 2022-01-01")



        # Số điện thoại
        try:
            check_gioithieu_mqh = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh1).text
            logging.info("Trang cá nhân - Giới thiệu tổng quan - Mối quan hệ")
            logging.info("check font-end: Ly Thân(Đang chờ) started 2022-01-01")
            logging.info(check_gioithieu_mqh == "Ly Thân(Đang chờ) started 2022-01-01")
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai).click()   #mqh_loi
        except:
            driver.find_element(By.XPATH, var.trangcanhan_gioithieuhuy).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_chinhsua).click()
        time.sleep(1)
        sdt1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input)
        sdt1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['sodienthoai'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 65, 2, "x")
        check_gioithieu_sodienthoai = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_sodienthoai1).text
        print(check_gioithieu_sodienthoai)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Số điện thoại")
        logging.info("check font-end: Số điện thoại - " + data['trangcanhan_gioithieu_tongquan']['sodienthoai'])
        logging.info(check_gioithieu_sodienthoai == data['trangcanhan_gioithieu_tongquan']['sodienthoai'])

        # Biệt danh
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_chinhsua).click()
        time.sleep(1)
        bietdanh1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_input)
        bietdanh1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_input).send_keys(data['trangcanhan_gioithieu_tongquan']['bietdanh'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 66, 2, "x")
        check_gioithieu_bietdanh = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_bietdanh1).text
        print(check_gioithieu_bietdanh)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Biệt danh")
        logging.info("check font-end: Biệt danh - " + data['trangcanhan_gioithieu_tongquan']['bietdanh'])
        logging.info(check_gioithieu_bietdanh == data['trangcanhan_gioithieu_tongquan']['bietdanh'])
        time.sleep(1)
        del driver.requests
        driver.refresh()
        time.sleep(1)

    def tongquan_dulieusai(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        # Trang cá nhân - Giới thiệu tổng quan
        # Sống tại
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['songtai_dulieusai'])
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_luu).click()
        time.sleep(1)

        check_gioithieu_songtai_dulieusai = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_songtai_dulieusai1).text
        print(check_gioithieu_songtai_dulieusai)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Sống tại - nhập địa điểm không tồn tại")
        logging.info("check font-end: Chúng tôi không thể nhận dạng vị tri bạn đã chỉ định.")
        logging.info(check_gioithieu_songtai_dulieusai == "Chúng tôi không thể nhận dạng vị trí bạn đã chỉ định.")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_ok).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_huy).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 67, 2, "x")
        writeData(var.path_baocao, "Sheet1", 67, 3, "đã pass: Thành phố hiện tại")
        # Đến từ
        driver.execute_script("window.scrollBy(0,500)", "")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).send_keys(data['trangcanhan_gioithieu_tongquan']['dentu_dulieusai'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_luu).click()
        time.sleep(2)
        check_gioithieu_dentu_dulieusai = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_dentu_dulieusai1).text
        print(check_gioithieu_dentu_dulieusai)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Đến từ - nhập địa điểm không tồn tại")
        logging.info("check font-end: Chúng tôi không thể nhận dạng vị tri bạn đã chỉ định.")
        logging.info(check_gioithieu_dentu_dulieusai == "Chúng tôi không thể nhận dạng vị trí bạn đã chỉ định.")
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_ok).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_huy).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 67, 2, "x")
        writeData(var.path_baocao, "Sheet1", 67, 3, "đã pass: Thành phố hiện tại, quê quán")

        #mối quan hệ
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_icon_chonmqh).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_goa).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 68, 2, "x")
        driver.execute_script("window.scrollBy(0,500)", "")
        # check_gioithieu_mqh1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh4).text         #mqh_loi
        check_gioithieu_mqh1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh2).text
        print(check_gioithieu_mqh1)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Mối quan hệ")
        logging.info("check font-end: Góa(Đang chờ) started 2022-01-01")
        logging.info(check_gioithieu_mqh1 == "Góa(Đang chờ) started 2022-01-01")
        time.sleep(1)

        # Số điện thoại1
        # try:
        #     check_gioithieu_mqh1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_mqh2).text
        #     print(check_gioithieu_mqh1)
        #     logging.info("Trang cá nhân - Giới thiệu tổng quan - Mối quan hệ")
        #     logging.info("check font-end: Góa started 2022-01-01")
        #     logging.info(check_gioithieu_mqh1 == "Góa started 2022-01-01")
        #     time.sleep(1)
        #     driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai).click()
        # except:
        #     driver.find_element(By.XPATH, var.trangcanhan_gioithieuhuy).click()
        # # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai).click()
        #     driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_chinhsua2).click()
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_chinhsua).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_chinhsua).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input).click()
        time.sleep(1)
        sdt2 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input)
        sdt2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['sodienthoai_dai'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_luu).click()
        time.sleep(1)
        check_gioithieu_sodienthoai_dai = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_sodienthoai_dai1).text
        print(check_gioithieu_sodienthoai_dai)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Số điện thoại dài quá 10 ký tự")
        logging.info("check font-end: Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        logging.info(check_gioithieu_sodienthoai_dai == "Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_ok).click()
        writeData(var.path_baocao, "Sheet1", 70, 2, "x")
        writeData(var.path_baocao, "Sheet1", 70, 3, "đã pass: SĐT quá dài")
        sdt2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['sodienthoai_ngan'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_luu).click()
        time.sleep(1)
        check_gioithieu_sodienthoai_ngan = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_sodienthoai_ngan1).text
        print(check_gioithieu_sodienthoai_ngan)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Số điện thoại it hơn 10 ký tự")
        logging.info("check font-end: Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        logging.info(check_gioithieu_sodienthoai_ngan == "Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_ok).click()
        writeData(var.path_baocao, "Sheet1", 70, 2, "x")
        writeData(var.path_baocao, "Sheet1", 70, 3, "đã pass: SĐT quá dài, SĐT quá ngắn")
        sdt2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['sodienthoai_trung'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_luu).click()
        time.sleep(1)
        check_gioithieu_sodienthoai_trungso = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_sodienthoai_trungso1).text
        print(check_gioithieu_sodienthoai_trungso)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Số điện thoại bị trùng")
        logging.info("check font-end: Số điện thoại đã có, Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        logging.info(check_gioithieu_sodienthoai_trungso == "Số điện thoại đã có, Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_ok).click()
        writeData(var.path_baocao, "Sheet1", 70, 2, "x")
        writeData(var.path_baocao, "Sheet1", 70, 3, "đã pass: SĐT quá dài, SĐT quá ngắn, trùng SĐT")
        sdt2.send_keys(Keys.CONTROL, "a")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['sodienthoai2'])
        writeData(var.path_baocao, "Sheet1", 69, 2, "x")
        writeData(var.path_baocao, "Sheet1", 69, 3, "đã pass: số điện thoại")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_luu).click()
        time.sleep(1)

        # Biệt danh1
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_chinhsua).click()
        bietdanh2 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_input)
        bietdanh2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_input).send_keys(data['trangcanhan_gioithieu_tongquan']['bietdanh_dai'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_luu).click()
        time.sleep(1)
        check_gioithieu_bietdanh_quadai = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_bietdanh_quadai1).text
        print(check_gioithieu_bietdanh_quadai)
        logging.info("Trang cá nhân - Giới thiệu tổng quan - Biệt danh quá dài, quá 20 ký tự")
        logging.info("check font-end: Tên biệt danh không vượt quá 20 ký tự.Vui lòng điền lại thông tin!")
        logging.info(check_gioithieu_bietdanh_quadai == "Tên biệt danh không vượt quá 20 ký tự.Vui lòng điền lại thông tin!")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_ok).click()
        writeData(var.path_baocao, "Sheet1", 70, 2, "x")
        writeData(var.path_baocao, "Sheet1", 70, 3, "đã pass: SĐT quá dài, SĐT quá ngắn, trùng SĐT, biệt danh quá dài")
        time.sleep(1)
        bietdanh2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_input).send_keys(data['trangcanhan_gioithieu_tongquan']['bietdanh2'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_bietdanh_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 69, 2, "x")
        writeData(var.path_baocao, "Sheet1", 69, 3, "đã pass: số điện thoại, biệt danh")



class cong_viec_va_hoc_van():
    def congviecvahocvan_congviec(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_vahocvan).click()
        #Công việc và học vấn
        #Công việc-công ty
        driver.execute_script("window.scrollBy(0,700)", "")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_iconcongviec).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_chinhsuacongviec).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['congty'])
        wait = WebDriverWait(driver, 10)
        gioithieu_congty_quantrada = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_congty_input_quantrada)))

        try:
            gioithieu_congty_quantrada.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,700)", "")
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_iconcongviec).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_chinhsuacongviec).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['congty'])
            gioithieu_congty_quantrada.click()

        #Công việc-chức vụ
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_chucvu_input).click()
        chucvu1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_chucvu_input)
        chucvu1.send_keys(Keys.CONTROL, "a")
        # time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_chucvu_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['chucvu'])
        #Công việc-thành phố, thị xã
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_tp_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_tp_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_tp_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])

        wait = WebDriverWait(driver, 10)
        gioithieu_congty_tp_hanoi = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_cv_tp_hanoi)))
        gioithieu_congty_tp_hanoi.click()
        time.sleep(0.5)
        #Công việc-mô tả
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_mota_input).click()
        mota1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_mota_input)
        mota1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_mota_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['mota'])
        time.sleep(2)
        # Công việc-ngày bắt đầu, ngày kết thúc
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_iconchonnam_2021).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_chonngay_3).click()

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_iconchonnam_2022).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_chonngay_11).click()

        del driver.requests
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 71, 2, "x")
    def congviecvahocvan_daihoc(self):
        driver.implicitly_wait(15)
        # Đại học - trường học
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_icondaihoc).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_chinhsuadaihoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_truonghoc'])
        time.sleep(1.5)
        wait = WebDriverWait(driver, 10)
        gioithieu_daihoc_truonghoc_dhbachkhoa = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_dhbachkhoa)))

        try:
            gioithieu_daihoc_truonghoc_dhbachkhoa.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,700)", "")
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_icondaihoc).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_chinhsuadaihoc).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_truonghoc'])
            gioithieu_daihoc_truonghoc_dhbachkhoa.click()
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_datotnghiep).click()

        # #Đại học - khoang thời gian
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_iconchonnam_2019).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_chonngay_16).click()

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_iconchonnam_2023).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_chonngay_8).click()
        time.sleep(1)
        #Đại học - mô tả
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_mota_input).click()
        mota2 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_mota_input)
        mota2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_mota_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_mota'])
        #Đại học - chuyên nghành 1
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_chuyennghanh1_input).click()
        chuyennghanh1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_chuyennghanh1_input)
        chuyennghanh1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_chuyennghanh1_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_chuyennghanh1'])
        time.sleep(0.5)
        # Đại học - đã học tại
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_dahoctai_caodang).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_dahoctai_daihoc).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_bangcap_input).click()
        bangcap1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_bangcap_input)
        bangcap1.send_keys(Keys.CONTROL, "a")
        del driver.requests
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_bangcap_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_bangcap'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 72, 2, "x")

    def congviecvahocvan_trunghoc(self):
        driver.implicitly_wait(15)
        # Trung học - trường học
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_icontrunghoc).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_chinhsuatrunghoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_truonghoc_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_truonghoc'])

        wait = WebDriverWait(driver, 10)
        gioithieu_trunghoc_truonghoc_thptdinhlap = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_thpt_dinhlap)))

        try:
            gioithieu_trunghoc_truonghoc_thptdinhlap.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.execute_script("window.scrollBy(0,700)", "")
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_icontrunghoc).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_chinhsuatrunghoc).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_truonghoc_input_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['trunghoc_truonghoc'])
            gioithieu_trunghoc_truonghoc_thptdinhlap.click()
        # Trung học - mô tả
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_mota_input).click()
        mota_trunghoc = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_mota_input)
        mota_trunghoc.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_mota_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan']['trunghochoc_mota'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_datotnghiep).click()

        # Trung học - khoảng thời gian
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_iconchonnam_2017).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_chonngay_13).click()

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_iconchonnam_2020).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_chonngay_24).click()
        time.sleep(1)

        del driver.requests
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_luu).click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        writeData(var.path_baocao, "Sheet1", 73, 2, "x")

    def congviecvahocvan_addthem(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_vahocvan).click()
        driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_addthem_congviec).click()
        #Công việc và học vấn
        #Công việc-công ty
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congty_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['congty'])
        try:
            wait = WebDriverWait(driver, 10)
            gioithieu_congty_input_quancf = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_congty_input_quancf)))
            gioithieu_congty_input_quancf.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_vahocvan).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_addthem_congviec).click()
            wait = WebDriverWait(driver, 10)
            gioithieu_congty_input_quancf = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_congty_input_quancf)))
            gioithieu_congty_input_quancf.click()

        #Công việc-chức vụ
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_chucvu_input).click()
        chucvu1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_chucvu_input)
        chucvu1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_chucvu_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['chucvu'])
        #Công việc-thành phố, thị xã
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_tp_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_tp_input_x).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_tp_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['thanhpho'])

        wait = WebDriverWait(driver, 10)
        gioithieu_cv_tp_langson = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_cv_tp_langson)))
        gioithieu_cv_tp_langson.click()

        #Công việc-mô tả
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_mota_input).click()
        mota1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_mota_input)
        mota1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_mota_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['mota'])
        time.sleep(0.5)

        # Công việc-ngày bắt đầu, ngày kết thúc
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_toidanglamviecoday).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_iconchonnam_2021).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngaybatdau_chonngay_5).click()

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_iconchonnam_2022).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_ngayketthuc_chonngay_16).click()

        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_luu).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cvvahocvan_iconxoa).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cvvahocvan_xoa).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cvvahocvan_xoa1).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 74, 2, "x")

        # Đại học - trường học
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_addtruongdaihoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['daihoc_truonghoc1'])
        try:
            wait = WebDriverWait(driver, 10)
            gioithieu_daihoc_truonghoc_dhkingkong = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_dhkingkong)))
            gioithieu_daihoc_truonghoc_dhkingkong.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_addtruongdaihoc).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['daihoc_truonghoc1'])
            wait = WebDriverWait(driver, 10)
            gioithieu_daihoc_truonghoc_dhkingkong = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_dhkingkong)))
            gioithieu_daihoc_truonghoc_dhkingkong.click()


        #
        # time.sleep(2.5)
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_dhkingkong).click()
        # time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_truonghoc_datotnghiep).click()

        # Đại học - khoang thời gian
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_iconchonnam_2019).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngaybatdau_chonngay_9).click()

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_iconchonnam_2023).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dh_ngayketthuc_chonngay_18).click()
        time.sleep(1)



        time.sleep(0.5)
        # Đại học - mô tả
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_mota_input).click()
        mota2 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_mota_input)
        mota2.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_mota_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['daihoc_mota1'])
        # Đại học - chuyên nghành 1
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_chuyennghanh1_input).click()
        chuyennghanh1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_chuyennghanh1_input)
        chuyennghanh1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_chuyennghanh1_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['daihoc_chuyennghanh11'])
        time.sleep(0.5)
        # Đại học - đã học tại
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_dahoctai_caodang).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_dahoctai_daihoc).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_bangcap_input).click()
        bangcap1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_bangcap_input)
        bangcap1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_bangcap_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['daihoc_bangcap1'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_luu).click()
        time.sleep(2)
        writeData(var.path_baocao, "Sheet1", 75, 2, "x")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_iconxoa).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_xoa).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_xoa1).click()
        time.sleep(1)

    # Trung học - trường học
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_addthemtrunghoc).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_truonghoc_input_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['trunghoc_truonghoc1'])
        try:
            wait = WebDriverWait(driver, 10)
            gioithieu_trunghoc_truonghoc_thpt_phubinh = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_thpt_phubinh)))
            gioithieu_trunghoc_truonghoc_thpt_phubinh.click()
        except:
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_addthemtrunghoc).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_truonghoc_input_x).click()
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['trunghoc_truonghoc1'])
            wait = WebDriverWait(driver, 10)
            gioithieu_trunghoc_truonghoc_thpt_phubinh = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_thpt_phubinh)))
            gioithieu_trunghoc_truonghoc_thpt_phubinh.click()
        #
        # time.sleep(2.5)
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_truonghoc_thpt_phubinh).click()
        # time.sleep(1.5)
        # Trung học - mô tả
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_mota_input).click()
        mota_trunghoc = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_mota_input)
        mota_trunghoc.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghochoc_mota_input).send_keys(data['trangcanhan_gioithieu_congviecvahocvan_addthem']['trunghochoc_mota1'])
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_datotnghiep).click()

        # Trung học - khoảng thời gian
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_iconchonnam_2017).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngaybatdau_chonngay_16).click()

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_iconchon).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_iconchonnam).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_iconchonnam_2020).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_ngayketthuc_chonngay_22).click()
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_luu).click()
        time.sleep(2)
        writeData(var.path_baocao, "Sheet1", 76, 2, "x")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_iconxoa).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_xoa).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_xoa1).click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)




class xemkientrongdoi():
    def congviecvahocvan_congviec(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_cv_vahocvan).click()
        #Công việc
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_iconcongviec).click()
        del driver.requests
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_xemsukientrongdoi).click()
        time.sleep(2)
        check_congviec_congty = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_congviec_congty).text
        print(check_congviec_congty)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - công việc - công ty - xem sự kiện trong đời ")
        logging.info("check font-end: Bắt đầu công việc mới tại Quán trà đá")
        logging.info(check_congviec_congty == "Bắt đầu công việc mới tại Quán trà đá")

        check_congviec_ngaythangchucvu = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_congviec_ngaythangchucvu).text
        print(check_congviec_ngaythangchucvu)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - công việc - xem sự kiện trong đời")
        logging.info("check font-end: Ngày bắt đầu làm việc, chức vụ - 03 tháng 10, 2021 - Nhân Viên")
        logging.info(check_congviec_ngaythangchucvu == "03 tháng 10, 2021 - Nhân Viên")

        check_congviec_thanhpho = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_congviec_thanhpho).text
        print(check_congviec_thanhpho)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - công việc - xem sự kiện trong đời")
        logging.info("check font-end: Thành phố làm việc - " + data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])
        logging.info(check_congviec_thanhpho == data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])
        writeData(var.path_baocao, "Sheet1", 77, 2, "x")

    def congviecvahocvan_daihoc(self):
        driver.implicitly_wait(15)
        driver.back()
        time.sleep(2)
        #Đại học
        driver.execute_script("window.scrollBy(0,700)", "")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_icondaihoc).click()
        del driver.requests
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_daihoc_xemsukientrongdoi).click()
        time.sleep(2)
        check_daihoc_tentruong = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_daihoc_tentruong).text
        print(check_daihoc_tentruong)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - Đại học - tên trường - xem sự kiện trong đời ")
        logging.info("check font-end: Bắt đầu học tại Đại học bách khoa hà nội")
        logging.info(check_daihoc_tentruong == "Bắt đầu học tại Đại học bách khoa hà nội")

        check_daihoc_ngaythang = driver.find_element(By.XPATH,var.trangcanhan_xemsukientrongdoi_check_daihoc_ngaythang).text
        print(check_daihoc_ngaythang)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - đại học - thời gian bắt đầu - xem sự kiện trong đời")
        logging.info("check font-end: Ngày nhập học: 16 tháng 10, 2019")
        logging.info(check_daihoc_ngaythang == "16 tháng 11, 2019")

        check_daihoc_dahoctai_chuyennghanh = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_daihoc_dahoctai_chuyennghanh).text
        print(check_daihoc_dahoctai_chuyennghanh)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - đại học- đã học tại, chuyên nghành - xem sự kiện trong đời")
        logging.info("check font-end: đã học tại, chuyên nghành - Đại học - Kỹ thuật máy tinh")
        logging.info(check_daihoc_dahoctai_chuyennghanh)
        logging.info(check_daihoc_dahoctai_chuyennghanh == "Đại học - Kỹ thuật máy tính")
        writeData(var.path_baocao, "Sheet1", 78, 2, "x")

    def congviecvahocvan_trunghoc(self):
        driver.implicitly_wait(15)
        driver.back()
        time.sleep(2)
        #Trung học
        driver.execute_script("window.scrollBy(0,700)", "")
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_icontrunghoc).click()
        del driver.requests
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_trunghoc_xemsukientrongdoi).click()
        time.sleep(2)
        check_trunghoc_tentruong = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_trunghoc_tentruong).text
        print(check_trunghoc_tentruong)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - Trung học - tên trường - xem sự kiện trong đời ")
        logging.info("check font-end: Bắt đầu học tại Trường THPT Đình Lập")
        logging.info(check_trunghoc_tentruong == "Bắt đầu học tại Trường THPT Đình Lập")

        check_trunghoc_ngaythang = driver.find_element(By.XPATH,var.trangcanhan_xemsukientrongdoi_check_trunghoc_ngaythang).text
        print(check_trunghoc_ngaythang)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - trung học - thời gian bắt đầu - xem sự kiện trong đời")
        logging.info("check font-end: Ngày nhập học: 13 tháng 10, 2017")
        logging.info(check_trunghoc_ngaythang == "13 tháng 10, 2017")

        check_trunghoc_captruong = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_trunghoc_captruong).text
        print(check_trunghoc_captruong)
        logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - trung học- cấp trường - xem sự kiện trong đời")
        logging.info("check font-end: Trường trung học")
        logging.info(check_trunghoc_captruong == "Trường trung học")
        writeData(var.path_baocao, "Sheet1", 79, 2, "x")
        driver.back()
        time.sleep(2)


class thongtincoban():
    def thongtincoban(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.thongtincoban).click()

        #thông tin liên hệ
        driver.find_element(By.XPATH, var.thongtincoban_icon_sdt).click()
        driver.find_element(By.XPATH, var.thongtincoban_sdt_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).click()
        thongtincoban_sdt1 = driver.find_element(By.XPATH, var.thongtincoban_sdt_input)
        thongtincoban_sdt1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['sodienthoai'])
        driver.find_element(By.XPATH, var.thongtincoban_sdt_luu).click()
        time.sleep(1)
        thongtincoban_sodienthoai = driver.find_element(By.XPATH, var.thongtincoban_sdt_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin liên hệ(số điện thoại)")
        logging.info("check font-end: Số điện thoại - " + data['trangcanhan_gioithieu_thongtincoban']['sodienthoai'])
        logging.info(thongtincoban_sodienthoai == data['trangcanhan_gioithieu_thongtincoban']['sodienthoai'])

        # Các trang web và liên kết xã hội
        #web
        driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(1)
        driver.find_element(By.XPATH, var.thongtincoban_icon_web).click()
        driver.find_element(By.XPATH, var.thongtincoban_web_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_web_input).click()
        thongtincoban_web1 = driver.find_element(By.XPATH, var.thongtincoban_web_input)
        thongtincoban_web1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_web_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['web'])
        driver.find_element(By.XPATH, var.thongtincoban_web_luu).click()
        time.sleep(1)
        thongtincoban_web = driver.find_element(By.XPATH, var.thongtincoban_web_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Các trang web và liên kết xã hội")
        logging.info("check font-end: Web - " + data['trangcanhan_gioithieu_thongtincoban']['web'])
        logging.info(thongtincoban_web == data['trangcanhan_gioithieu_thongtincoban']['web'])

        #liên kết xã hội
        driver.find_element(By.XPATH, var.thongtincoban_icon_lienket).click()
        driver.find_element(By.XPATH, var.thongtincoban_lienket_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_lienket_input).click()
        thongtincoban_lienket1 = driver.find_element(By.XPATH, var.thongtincoban_lienket_input)
        thongtincoban_lienket1.send_keys(Keys.CONTROL, "a")
        del driver.requests
        driver.find_element(By.XPATH, var.thongtincoban_lienket_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['lienket'])
        driver.find_element(By.XPATH, var.thongtincoban_lienket_luu).click()
        time.sleep(1)
        thongtincoban_lienket = driver.find_element(By.XPATH, var.thongtincoban_lienket_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Các trang web và liên kết xã hội")
        print(thongtincoban_lienket)
        logging.info(thongtincoban_lienket)
        logging.info("check font-end: Liên kết - " + data['trangcanhan_gioithieu_thongtincoban']['lienket'])
        logging.info(thongtincoban_lienket == data['trangcanhan_gioithieu_thongtincoban']['lienket'])

        #thông tin cơ bản
        #tiểu sử
        driver.find_element(By.XPATH, var.thongtincoban_icon_tieusu).click()
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_input).click()
        thongtincoban_tieusu1 = driver.find_element(By.XPATH, var.thongtincoban_tieusu_input)
        thongtincoban_tieusu1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['tieusu'])
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_luu).click()
        time.sleep(1)
        thongtincoban_tieusu = driver.find_element(By.XPATH, var.thongtincoban_tieusu_fe).text
        print(thongtincoban_tieusu)
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Tiểu sử - " + data['trangcanhan_gioithieu_thongtincoban']['tieusu'])
        logging.info(thongtincoban_tieusu == data['trangcanhan_gioithieu_thongtincoban']['tieusu'])

        #Giới tinh
        driver.find_element(By.XPATH, var.thongtincoban_icon_gioitinh).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_iconchongioitinh).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_nu).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_luu).click()
        time.sleep(1)
        thongtincoban_gioitinh = driver.find_element(By.XPATH, var.thongtincoban_gioitinh_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Giới tinh - female")
        logging.info(thongtincoban_gioitinh == "female")

        #Ngày sinh
        driver.find_element(By.XPATH, var.thongtincoban_icon_ngaysinh).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_luu).click()
        time.sleep(1)
        thongtincoban_ngaysinh = driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Ngày sinh - 3 tháng 10, 2000")
        logging.info(thongtincoban_ngaysinh == "3 tháng 10, 2000")

        #biệt danh
        driver.find_element(By.XPATH, var.thongtincoban_icon_bietdanh).click()
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input).click()
        thongtincoban_bietdanh1 = driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input)
        thongtincoban_bietdanh1.send_keys(Keys.CONTROL, "a")
        del driver.requests
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['bietdanh'])
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_luu).click()
        time.sleep(1)
        thongtincoban_bietdanh = driver.find_element(By.XPATH, var.thongtincoban_bietdanh_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Biệt danh - " + data['trangcanhan_gioithieu_thongtincoban']['bietdanh'])
        logging.info(thongtincoban_bietdanh == data['trangcanhan_gioithieu_thongtincoban']['bietdanh'])
    def thongtincoban_dulieusai(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        driver.find_element(By.XPATH, var.thongtincoban).click()
        #thông tin liên hệ
        #số điện thoại
        driver.find_element(By.XPATH, var.thongtincoban_icon_sdt).click()
        driver.find_element(By.XPATH, var.thongtincoban_sdt_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).click()
        thongtincoban_sdt1 = driver.find_element(By.XPATH, var.thongtincoban_sdt_input)
        thongtincoban_sdt1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['sodienthoai_dai'])
        driver.find_element(By.XPATH, var.thongtincoban_sdt_luu).click()
        time.sleep(1)
        check_thongtincoban_sodienthoai_dai = driver.find_element(By.XPATH,var.trangcanhan_check_thongtincoban_sodienthoai_dai1).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin liên hệ - Số điện thoại dài quá 10 ký tự")
        logging.info("check font-end: Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        logging.info(check_thongtincoban_sodienthoai_dai == "Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_thongtincoban_sodienthoai_ok).click()

        thongtincoban_sdt1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['sodienthoai_ngan'])
        driver.find_element(By.XPATH, var.thongtincoban_sdt_luu).click()
        time.sleep(1)
        check_thongtincoban_sodienthoai_ngan = driver.find_element(By.XPATH,var.trangcanhan_check_thongtincoban_sodienthoai_ngan1).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin liên hệ - Số điện thoại it hơn 10 ký tự")
        logging.info("check font-end: Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        logging.info(check_thongtincoban_sodienthoai_ngan == "Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_thongtincoban_sodienthoai_ok).click()

        thongtincoban_sdt1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['sodienthoai_trung'])
        driver.find_element(By.XPATH, var.thongtincoban_sdt_luu).click()
        time.sleep(1)
        check_thongtincoban_sodienthoai_trungso = driver.find_element(By.XPATH,var.trangcanhan_check_thongtincoban_sodienthoai_trungso1).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin liên hệ - Số điện thoại bị trùng")
        logging.info("check font-end: Số điện thoại đã có, Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        logging.info(check_thongtincoban_sodienthoai_trungso == "Số điện thoại đã có, Số điện thoại độ dài không đúng (phải là 10 ký tự)")
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_thongtincoban_sodienthoai_ok).click()

        thongtincoban_sdt1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_sdt_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['sodienthoai2'])
        driver.find_element(By.XPATH, var.thongtincoban_sdt_luu).click()
        time.sleep(1)

        # Các trang web và liên kết xã hội
        #web
        driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(1)
        driver.find_element(By.XPATH, var.thongtincoban_icon_web).click()
        driver.find_element(By.XPATH, var.thongtincoban_web_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_web_input).click()
        thongtincoban_web1 = driver.find_element(By.XPATH, var.thongtincoban_web_input)
        thongtincoban_web1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_web_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['web_dulieusai'])
        driver.find_element(By.XPATH, var.thongtincoban_web_luu).click()
        time.sleep(1)
        thongtincoban_web_dulieusai = driver.find_element(By.XPATH, var.thongtincoban_web_fe_dulieusai).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Các trang web và liên kết xã hội")
        logging.info("check font-end: Web(nhập sai định dạng web) - message: URL You provided invalid URL")
        logging.info(thongtincoban_web_dulieusai == "URL You provided invalid URL")
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.thongtincoban_web_ok).click()
        thongtincoban_web1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_web_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['web1'])
        driver.find_element(By.XPATH, var.thongtincoban_web_luu).click()
        time.sleep(1)

        #liên kết xã hội
        try:
            driver.find_element(By.XPATH, var.thongtincoban_icon_lienket).click()
            driver.find_element(By.XPATH, var.thongtincoban_lienket_chinhsua).click()
            driver.find_element(By.XPATH, var.thongtincoban_lienket_input).click()
            thongtincoban_lienket1 = driver.find_element(By.XPATH, var.thongtincoban_lienket_input)
            thongtincoban_lienket1.send_keys(Keys.CONTROL, "a")
            driver.find_element(By.XPATH, var.thongtincoban_lienket_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['lienket_dulieusai'])
            driver.find_element(By.XPATH, var.thongtincoban_lienket_luu).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
            driver.find_element(By.XPATH, var.thongtincoban).click()
            driver.find_element(By.XPATH, var.thongtincoban_icon_lienket).click()
            driver.find_element(By.XPATH, var.thongtincoban_lienket_chinhsua).click()
            driver.find_element(By.XPATH, var.thongtincoban_lienket_input).click()
            thongtincoban_lienket1 = driver.find_element(By.XPATH, var.thongtincoban_lienket_input)
            thongtincoban_lienket1.send_keys(Keys.CONTROL, "a")
            driver.find_element(By.XPATH, var.thongtincoban_lienket_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['lienket_dulieusai'])
            driver.find_element(By.XPATH, var.thongtincoban_lienket_luu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.thongtincoban_icon_lienket).click()
        driver.find_element(By.XPATH, var.thongtincoban_lienket_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_lienket_input).click()
        thongtincoban_lienket1 = driver.find_element(By.XPATH, var.thongtincoban_lienket_input)
        thongtincoban_lienket1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_lienket_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['lienket1'])
        driver.find_element(By.XPATH, var.thongtincoban_lienket_luu).click()
        time.sleep(1)


        #thông tin cơ bản
        #tiểu sử
        driver.find_element(By.XPATH, var.thongtincoban_icon_tieusu).click()
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_input).click()
        thongtincoban_tieusu1 = driver.find_element(By.XPATH, var.thongtincoban_tieusu_input)
        thongtincoban_tieusu1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['tieusu_dai'])
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_luu).click()
        time.sleep(1)

        thongtincoban_tieusu_dulieusai = driver.find_element(By.XPATH, var.thongtincoban_tieusu_fe_dulieusai).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Các trang web và liên kết xã hội")
        logging.info("check font-end: Tiểu sử(Nhập quá 100 ký tự) - message: Tiểu sử chỉ được phép nhập tối đa 100 ký tự!")
        logging.info(thongtincoban_tieusu_dulieusai == "Tiểu sử chỉ được phép nhập tối đa 100 ký tự!")
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_x).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_huy).click()
        driver.find_element(By.XPATH, var.thongtincoban_icon_tieusu).click()
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_input).click()
        thongtincoban_tieusu1 = driver.find_element(By.XPATH, var.thongtincoban_tieusu_input)
        thongtincoban_tieusu1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['tieusu1'])
        driver.find_element(By.XPATH, var.thongtincoban_tieusu_luu).click()
        time.sleep(1)

        #Giới tinh
        driver.find_element(By.XPATH, var.thongtincoban_icon_gioitinh).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_iconchongioitinh).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_nam).click()
        driver.find_element(By.XPATH, var.thongtincoban_gioitinh_luu).click()
        time.sleep(1)
        thongtincoban_gioitinh = driver.find_element(By.XPATH, var.thongtincoban_gioitinh_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Giới tinh - male")
        logging.info(thongtincoban_gioitinh == "male")

        #Ngày sinh
        driver.find_element(By.XPATH, var.thongtincoban_icon_ngaysinh).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_iconchonnam).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_duoi14t_2022).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_luu).click()
        time.sleep(1)
        thongtincoban_ngaysinh_message = driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_fe_chuadu14t).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Ngày sinh - message: Tuổi của bạn không đủ 14 tuổi.Vui lòng điền lại thông tin!")
        logging.info(thongtincoban_ngaysinh_message == "Tuổi của bạn không đủ 14 tuổi.Vui lòng điền lại thông tin!")
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_ok).click()
        time.sleep(0.5)

        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_iconchonnam).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_tren14t_2000).click()
        driver.find_element(By.XPATH, var.thongtincoban_ngaysinh_luu).click()
        time.sleep(1)

        #biệt danh
        driver.find_element(By.XPATH, var.thongtincoban_icon_bietdanh).click()
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input).click()
        thongtincoban_bietdanh1 = driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input)
        thongtincoban_bietdanh1.send_keys(Keys.CONTROL, "a")

        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['bietdanh_dai'])
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_luu).click()
        time.sleep(1)
        thongtincoban_bietdanh_dai = driver.find_element(By.XPATH, var.thongtincoban_bietdanhdai_fe).text
        logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Thông tin cơ bản")
        logging.info("check font-end: Biệt danh(dài quá 100 ký tự) - message: Tiểu sử chỉ được phép nhập tối đa 100 ký tự!")
        logging.info(thongtincoban_bietdanh_dai)
        logging.info(thongtincoban_bietdanh_dai == "Tên biệt danh không vượt quá 20 ký tự.Vui lòng điền lại thông tin!")
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_ok).click()
        time.sleep(0.5)

        thongtincoban_bietdanh1 = driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input)
        thongtincoban_bietdanh1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['bietdanh1'])
        driver.find_element(By.XPATH, var.thongtincoban_bietdanh_luu).click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)


class giadinh_va_cacmoiquanhe():
    def gd_va_mqh_taikhoan1(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(1)
        #gia đình và các mối quan hệ
        #Mối quan hệ
        driver.find_element(By.XPATH, var.giadinhvamqh).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_icon_mqh).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_chinhsua).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_icon_chonmqh).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_henho).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.giadinhvamqh_chonnguoithan_input).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_chonnguoithan_input_x).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_chonnguoithan_input).send_keys(data['trangcanhan_gd_va_mqh']['name'])

        wait = WebDriverWait(driver, 10)
        giadinhvamqh_ngocmai1 = wait.until(EC.element_to_be_clickable((By.XPATH, var.giadinhvamqh_ngocmai)))
        giadinhvamqh_ngocmai1.click()
        driver.find_element(By.XPATH, var.giadinhvamqh_luu).click()
        time.sleep(1)

        # mqh_ngocmai = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_ngocmai1).text
        # logging.info("Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Mối quan hệ")
        # logging.info("check font-end: Người thân - " + data['trangcanhan_gd_va_mqh']['name'])
        # logging.info(mqh_ngocmai == data['trangcanhan_gd_va_mqh']['name'])
        #
        # # mqh_trangthai_thoigian = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_trangthai_thoigian4).text   #mqh_loi
        # mqh_trangthai_thoigian = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_trangthai_thoigian1).text
        # logging.info("Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Gia đình")
        # logging.info("check font-end: Gia đình - Trạng thái/Thời gian - Hẹn hò started 2022-01-01" )
        # logging.info(mqh_trangthai_thoigian == "Hẹn hò started 2022-01-01")

        #Gia đình
        try:
            mqh_ngocmai = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_ngocmai1).text
            logging.info("Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Mối quan hệ")
            logging.info("check font-end: Người thân - " + data['trangcanhan_gd_va_mqh']['name'])
            logging.info(mqh_ngocmai == data['trangcanhan_gd_va_mqh']['name'])

            # mqh_trangthai_thoigian = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_trangthai_thoigian4).text   #loi
            mqh_trangthai_thoigian = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_trangthai_thoigian1).text
            logging.info("Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Gia đình")
            logging.info("check font-end: Gia đình - Trạng thái/Thời gian - Hẹn hò(Đang chờ) started 2022-01-01")
            logging.info(mqh_trangthai_thoigian == "Hẹn hò(Đang chờ) started 2022-01-01")
            driver.find_element(By.XPATH, var.giadinhvamqh_icon_nguoithan).click()
            driver.find_element(By.XPATH, var.giadinhvamqh_sdt_chinhsua).click()
        except:
            driver.find_element(By.XPATH, var.trangcanhan_gioithieuhuy).click()
            driver.find_element(By.XPATH, var.giadinhvamqh_icon_nguoithan).click()
        # driver.find_element(By.XPATH, var.giadinhvamqh_icon_nguoithan).click()
            driver.find_element(By.XPATH, var.giadinhvamqh_sdt_chinhsua).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_nguoithan_input).click()
        # driver.find_element(By.XPATH, var.giadinhvamqh_nguoithan_input).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_nguoithan_input_x).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_nguoithan_input).send_keys(data['trangcanhan_gd_va_mqh']['name1'])

        wait = WebDriverWait(driver, 10)
        giadinhvamqh_manhcuong1 = wait.until(EC.element_to_be_clickable((By.XPATH, var.giadinhvamqh_manhcuong)))
        giadinhvamqh_manhcuong1.click()
        driver.find_element(By.XPATH, var.giadinhvamqh_nguoithan_chongiadinh).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_giadinh).click()
        driver.find_element(By.XPATH, var.giadinhvamqh_giadinh_luu).click()
        time.sleep(1)

        gd_manhcuong = driver.find_element(By.XPATH, var.giadinhvamqh_gd_manhcuong1).text
        logging.info("Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Mối quan hệ")
        logging.info("check font-end: Gia đình - " + data['trangcanhan_gd_va_mqh']['name1'])
        logging.info(gd_manhcuong == data['trangcanhan_gd_va_mqh']['name1'])

        gd_tinhtrang = driver.find_element(By.XPATH, var.giadinhvamqh_mqh_gd_tinhtrang1).text
        logging.info("Trang cá nhân - Giới thiệu - Gia đình và các mối quan hệ - Gia đình")
        logging.info("check font-end: Tình trạng - Gia đình(Đang chờ)" )
        logging.info(gd_tinhtrang == "Gia đình(Đang chờ)")
        del driver.requests
        driver.refresh()
        time.sleep(2)


class sukientrongdoi():
    def sukientrongdoi_xem(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sukientrongdoi).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        driver.find_element(By.XPATH, var.sukientrongdoi_trunghoc_icon).click()
        driver.find_element(By.XPATH, var.sukientrongdoi_trunghoc_xem).click()
        time.sleep(3)
        driver.back()
        time.sleep(2)
        driver.find_element(By.XPATH, var.sukientrongdoi_daihoc_icon).click()
        driver.find_element(By.XPATH, var.sukientrongdoi_daihoc_xem).click()
        time.sleep(3)
        driver.back()
        time.sleep(2)
        driver.find_element(By.XPATH, var.sukientrongdoi_congviec_icon).click()
        driver.find_element(By.XPATH, var.sukientrongdoi_congviec_xem).click()
        time.sleep(3)
        driver.back()
        time.sleep(2)
    def sukientrongdoi_themmoisukien_check(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sukientrongdoi).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        driver.find_element(By.XPATH, var.sukientrongdoi_iconthemmoi).click()
    def mau1(self, tieude):
        # Tạo sự kiện riêng
        driver.find_element(By.XPATH, var.taosukienrieng_tailenfile).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        sukientrongdoi_clear = driver.find_element(By.XPATH, var.taosukienrieng_input)
        sukientrongdoi_clear.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.taosukienrieng_input).send_keys(tieude)
        time.sleep(1)
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
        time.sleep(1)
    def mau2(self, tieude, diachi):
        driver.find_element(By.XPATH, var.nhacuavadoisong_tailenfile).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        sukientrongdoi_clear1 = driver.find_element(By.XPATH, var.nhacuavadoisong_tieude_input)
        sukientrongdoi_clear1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.nhacuavadoisong_tieude_input).send_keys(tieude)
        driver.find_element(By.XPATH, var.nhacuavadoisong_chondiachi_input).send_keys(diachi)
        wait = WebDriverWait(driver, 10)
        nhacuavadoisong_chondiachi = wait.until(EC.element_to_be_clickable((By.XPATH, var.nhacuavadoisong_chondiachi_thainguyen)))
        nhacuavadoisong_chondiachi.click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
        time.sleep(1)
    def taosukienrieng(self):
        try:
            wait = WebDriverWait(driver, 10)
            taosukienrieng = wait.until(EC.element_to_be_clickable((By.XPATH, var.taosukienrieng1)))
            taosukienrieng.click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.sukientrongdoi).click()
            driver.execute_script("window.scrollBy(0,400)", "")
            driver.find_element(By.XPATH, var.sukientrongdoi_iconthemmoi).click()
            wait = WebDriverWait(driver, 10)
            taosukienrieng = wait.until(EC.element_to_be_clickable((By.XPATH, var.taosukienrieng1)))
            taosukienrieng.click()
        sukientrongdoi.mau1(self, data['trangcanhan_sukientrongdoi']['taosukienrieng'])
    def nhacuavadoisong(self):
        driver.find_element(By.XPATH, var.nhacuavadoisong).click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_nhaptieude).click()
        sukientrongdoi.mau2(self, data['trangcanhan_sukientrongdoi']['nhacuavadoisong_quequan'], data['trangcanhan_sukientrongdoi']['nhacuavadoisong_diachi'])
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
    def moiquanhe(self):
        driver.find_element(By.XPATH, var.moiquanhe).click()
        driver.find_element(By.XPATH, var.moiquanhe_nhaptieude).click()
        sukientrongdoi.mau2(self, data['trangcanhan_sukientrongdoi']['moiquanhe_tieude'], data['trangcanhan_sukientrongdoi']['moiquanhe_diachi'])
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
    def work(self):
        driver.find_element(By.XPATH, var.work).click()
        driver.find_element(By.XPATH, var.work_nhaptieude).click()
        sukientrongdoi.mau2(self, data['trangcanhan_sukientrongdoi']['work_tieude'], data['trangcanhan_sukientrongdoi']['work_diachi'])
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
    def tuongnho(self):
        driver.find_element(By.XPATH, var.tuongnho).click()
        sukientrongdoi.mau1(self, data['trangcanhan_sukientrongdoi']['tuongnho_tieude'])
    def daumocvathanhtuu(self):
        driver.find_element(By.XPATH, var.daumocvathanhtuu).click()
        sukientrongdoi.mau1(self, data['trangcanhan_sukientrongdoi']['daumocvathanhtuu_tieude'])
    def suckhoethechatvatinhthan(self):
        driver.find_element(By.XPATH, var.suckhoethechatvatinhthan).click()
        sukientrongdoi.mau1(self, data['trangcanhan_sukientrongdoi']['suckhoethechatvatinhthan_tieude'])
    def sothichhoatdong(self):
        driver.find_element(By.XPATH, var.sothichhoatdong).click()
        sukientrongdoi.mau1(self, data['trangcanhan_sukientrongdoi']['sothichhoatdong_tieude'])
    def dulich(self):
        driver.find_element(By.XPATH, var.dulich).click()
        sukientrongdoi.mau2(self, data['trangcanhan_sukientrongdoi']['dulich_tieude'], data['trangcanhan_sukientrongdoi']['dulich_diachi'])
    def giadinh(self):
        driver.find_element(By.XPATH, var.giadinh).click()
        driver.find_element(By.XPATH, var.work_nhaptieude).click()
        sukientrongdoi.mau2(self, data['trangcanhan_sukientrongdoi']['giadinh_tieude'], data['trangcanhan_sukientrongdoi']['giadinh_diachi'])
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
    def hocvan(self):
        driver.find_element(By.XPATH, var.hocvan).click()
        driver.find_element(By.XPATH, var.work_nhaptieude).click()
        sukientrongdoi.mau2(self, data['trangcanhan_sukientrongdoi']['hocvan_tieude'], data['trangcanhan_sukientrongdoi']['hocvan_diachi'])
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
        driver.find_element(By.XPATH, var.taosukientrongdoi_x).click()
    def sukientrongdoi_themmoisukien(self):
        driver.implicitly_wait(15)
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sukientrongdoi).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        driver.find_element(By.XPATH, var.sukientrongdoi_iconthemmoi).click()
        wait = WebDriverWait(driver, 10)
        dulich_add = wait.until(EC.element_to_be_clickable((By.XPATH, var.dulich_add1)))
        dulich_add.click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_tailenfile).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        sukientrongdoi_clear1 = driver.find_element(By.XPATH, var.nhacuavadoisong_tieude_input)
        sukientrongdoi_clear1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.nhacuavadoisong_tieude_input).send_keys(data['trangcanhan_sukientrongdoi']['dulich_tieude'])
        driver.find_element(By.XPATH, var.nhacuavadoisong_chondiachi_input).send_keys(data['trangcanhan_sukientrongdoi']['dulich_diachi'])
        wait = WebDriverWait(driver, 10)
        nhacuavadoisong_chondiachi = wait.until(EC.element_to_be_clickable((By.XPATH, var.nhacuavadoisong_chondiachi_thainguyen)))
        nhacuavadoisong_chondiachi.click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian).click()
        # driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian_nam).click()
        # driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian_nam_2022).click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian_thang).click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian_thang_9).click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian_ngay).click()
        driver.find_element(By.XPATH, var.nhacuavadoisong_thoigian_ngay_1a).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.taosukientrongdoi_luu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.taosukientrongdoi_mota).send_keys(data['trangcanhan_sukientrongdoi']['dulich_mota'])
        driver.find_element(By.XPATH, var.taosukientrongdoi_dang).click()
        time.sleep(10)
        driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(2)
        del driver.requests
        driver.refresh()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,1100)", "")
        dongthoigian_sukien_mota = driver.find_element(By.XPATH, var.dongthoigian_sukienthemmoi1).text
        logging.info("Trang cá nhân - Giới thiệu - Thêm mới sự kiện trong đời lên trang cá nhân(du lịch)")
        logging.info("check font-end: Dòng thời gian - Mô tả - " + data['trangcanhan_sukientrongdoi']['dulich_mota'])
        logging.info(dongthoigian_sukien_mota == data['trangcanhan_sukientrongdoi']['dulich_mota'])

        dongthoigian_sukiendiadiem = driver.find_element(By.XPATH, var.dongthoigian_sukien_diadiem1).text
        logging.info("Trang cá nhân - Giới thiệu - Thêm mới sự kiện trong đời lên trang cá nhân(du lịch)")
        logging.info("check font-end: Dòng thời gian - Sự kiện, địa điểm - Du lịch, Trường test tại Thái Nguyên")
        logging.info(dongthoigian_sukiendiadiem == "Du lịch, Trường test tại Thái Nguyên")

        dongthoigian_sukien_thoigian = driver.find_element(By.XPATH, var.dongthoigian_sukien_thoigian1).text
        logging.info("Trang cá nhân - Giới thiệu - Thêm mới sự kiện trong đời lên trang cá nhân(du lịch)")
        logging.info("check font-end: Dòng thời gian - Thời gian - 01 tháng 09, 2023")
        logging.info(dongthoigian_sukien_thoigian == "01 tháng 09, 2023")

        dongthoigian_sukien_mota = driver.find_element(By.XPATH, var.dongthoigian_sukien_mota).text
        logging.info("Trang cá nhân - Giới thiệu - Thêm mới sự kiện trong đời lên trang cá nhân(du lịch)")
        logging.info("check font-end: Dòng thời gian - Mô tả - " + data['trangcanhan_sukientrongdoi']['dulich_mota'])
        logging.info(dongthoigian_sukien_mota == data['trangcanhan_sukientrongdoi']['dulich_mota'])

        #chỉnh sửa dữ liệu thêm mới sự kiên
        dongthoigian_sukien_diadiem = driver.find_element(By.XPATH, var.dongthoigian_sukien_diadiem).text
        print(dongthoigian_sukien_diadiem)
        logging.info("Trang cá nhân - Giới thiệu - Thêm mới sự kiện trong đời lên trang cá nhân(du lịch)")
        logging.info("check font-end: Dòng thời gian - Địa điểm - " + data['trangcanhan_sukientrongdoi']['dulich_diachi'])
        logging.info(dongthoigian_sukien_diadiem == data['trangcanhan_sukientrongdoi']['dulich_diachi'])
        time.sleep(1)
    def sukientrongdoi_themmoisukien_chinhsua_xoa(self):
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, var.icon_chinhsuabaiviet).click()
        driver.find_element(By.XPATH, var.chinhsuabaiviet).click()
        driver.find_element(By.XPATH, var.chinhsuabaiviet_mota_input).send_keys("123")
        driver.find_element(By.XPATH, var.chinhsuabaiviet_luu).click()
        time.sleep(5)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_chinhsuabaiviet).click()
        driver.find_element(By.XPATH, var.icon_chinhsuabaiviet_xoabaiviet).click()
        driver.find_element(By.XPATH, var.xoa).click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)


class noitungsong():
    def noitungsong(self):
        driver.implicitly_wait(15)
        # driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(2)
        # Trang cá nhân - Giới thiệu - Nơi từng sống
        #Sống tại
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        driver.find_element(By.XPATH, var.trangcanhan_noitungsong).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_chinhsua).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).send_keys(data['trangcanhan_noitungsong']['noitungsong_songtai'])

        wait = WebDriverWait(driver, 10)
        chon_hungyen = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hungyen)))
        chon_hungyen.click()

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 62, 2, "x")
        check_trangcanhan_gioithieu_songtai = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai1).text
        logging.info("Trang cá nhân - Giới thiệu  - Nơi từng sống - Sống tại")
        logging.info("check font-end: Sống tại - " + data['trangcanhan_noitungsong']['noitungsong_songtai'])
        logging.info(check_trangcanhan_gioithieu_songtai == data['trangcanhan_noitungsong']['noitungsong_songtai'])

        # Đến từ
        driver.execute_script("window.scrollBy(0,500)", "")
        # time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_x).click()
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_input).send_keys(data['trangcanhan_noitungsong']['noitungsong_dentu'])

        wait = WebDriverWait(driver, 10)
        dentu_thainguyen = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_dentu_thainguyen)))
        dentu_thainguyen.click()

        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_dentu_luu).click()
        time.sleep(1)
        writeData(var.path_baocao, "Sheet1", 63, 2, "x")
        check_gioithieu_dentu = driver.find_element(By.XPATH, var.trangcanhan_check_gioithieu_dentu1).text
        print(check_gioithieu_dentu)
        logging.info("Trang cá nhân - Giới thiệu - Nơi từng sống - Đến từ")
        logging.info("check font-end: Đến từ - " + data['trangcanhan_noitungsong']['noitungsong_dentu'])
        logging.info(check_gioithieu_dentu == data['trangcanhan_noitungsong']['noitungsong_dentu'])
        del driver.requests
        driver.refresh()
        time.sleep(2)


class banbe():
    def tatcabanbe(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()

        driver.find_element(By.XPATH, var.trangcanhan_banbe_ngocmai).click()
        time.sleep(3)
        check_ngocmai =driver.find_element(By.XPATH, var.trangcanhan_banbe_ngocmai1).text
        logging.info("Trang cá nhân - Bạn bè  - Tất cả bạn bè - Xem trang cá nhân của bạn bè")
        logging.info("check font-end: Trang cá nhân của - " + data['trangcanhan_banbe']['trangcanhan_banbe_ngocmai'])
        logging.info(check_ngocmai)
        logging.info(check_ngocmai == data['trangcanhan_banbe']['trangcanhan_banbe_ngocmai'])
        driver.back()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,700)", "")
        #bo theo dõi
        driver.find_element(By.XPATH, var.trangcanhan_banbe_icon_manhcuong).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_botheodoi).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_botheodoi_xacnhan).click()
        time.sleep(4)
        driver.refresh()
        time.sleep(2)
        #theodoi
        driver.find_element(By.XPATH, var.trangcanhan_banbe_icon_manhcuong).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_botheodoi).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_botheodoi_xacnhan).click()
        time.sleep(2)
        driver.refresh()
        #huỷ kết bạn
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_icon_manhcuong).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_huyketban).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_huyketban_xacnhan).click()
        time.sleep(2)
        huyketban_manhcuong =driver.find_element(By.XPATH, var.huyketban_manhcuong_text_thembanbe).text
        print(huyketban_manhcuong)
        logging.info("Trang cá nhân - Bạn bè  - Tất cả bạn bè - Huỷ kết bạn")
        logging.info("check font-end: Huỷ kết bạn thành công")
        logging.info(huyketban_manhcuong == huyketban_manhcuong)
        time.sleep(5)

        #thêm bạn be - huỷ
        # wait = WebDriverWait(driver, 10)
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_banbe_thembanbe_manhcuong)))
        # element.click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_thembanbe_manhcuong).click()
        time.sleep(1)
        login.login4(self, "truongvck22@gmail.com", "atgmj123456")
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_loimoi_huy).click()
        time.sleep(2)
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        check_banbe_tranquangtruong =driver.find_element(By.XPATH, var.check_banbe_tranquangtruong_tinhtrang).text
        check_banbe_name = driver.find_element(By.XPATH, var.check_banbe_tranquangtruong2).text
        print(check_banbe_tranquangtruong)
        logging.info("Xoá lời mời kết bạn - check trang cá nhân người vừa kết bạn")
        logging.info("check font-end: tên Người gửi lời mời kết bạn: " + check_banbe_name)
        logging.info("check font-end: tình trạng - Thêm bạn bè")
        logging.info(check_banbe_tranquangtruong == "Thêm bạn bè")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_guiloimoi).click()
        time.sleep(2)

        # thêm bạn bè - đồng ý
        login.login4(self, "truongvck33@gmail.com", "atgmj123456")
        driver.find_element(By.XPATH, var.trangcanhan_banbe_loimoi_chapnhan).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan).click()
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_icon_manhcuong).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_huyketban).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_huyketban_xacnhan).click()
        time.sleep(5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_thembanbe_manhcuong).click()
        time.sleep(2)
        login.login4(self, "truongvck22@gmail.com", "atgmj123456")
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_banbe_loimoi_chapnhan).click()
        time.sleep(2)
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        check_banbe_tranquangtruong = driver.find_element(By.XPATH, var.check_banbe_tranquangtruong1).text
        check_banbe_name = driver.find_element(By.XPATH, var.check_banbe_tranquangtruong2).text
        print(check_banbe_tranquangtruong)
        logging.info("Chấp nhận kết bạn - check trang cá nhân người vừa kết bạn")
        logging.info("check font-end: tên Người gửi lời mời kết bạn: " + check_banbe_name)
        logging.info("check font-end: tình trạng - Bạn bè")
        logging.info(check_banbe_tranquangtruong == "Bạn bè")
        time.sleep(1)
        login.login3(self, "truongvck33@gmail.com", "atgmj123456")

    def banbe_chinhsuaquyenriengtu(self):
        driver.implicitly_wait(15)

        #Danh sách bạn be
        #quyền riengtu
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_iconchinhsuaquyen).click()
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_dsbb_riengtu1).click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(1)
        check_banbe_riengtu1 = driver.find_element(By.XPATH, var.check_banbe_riengtu1).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư ")
        logging.info("check font-end: Danh sách bạn bè khi chỉnh quyền thành riêng tư có hiển thị không?")
        logging.info(check_banbe_riengtu1 == "hue nguyen")
        #Người lạ
        login.login4(self, "truongvck222@gmail.com", "atgmj123456")
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.execute_script("window.scrollBy(0,510)", "")
        time.sleep(1)
        check_nguoila_riengtu = driver.find_element(By.XPATH, var.check_nguoila_riengtu3).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - riêng tư")
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - Không có bạn bè nào")
        logging.info(check_nguoila_riengtu)
        logging.info(check_nguoila_riengtu == "Không có bạn bè nào")
        time.sleep(1.5)
        #Bạn bè
        login.login4(self, "truongvck333@gmail.com", "atgmj123456")
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.execute_script("window.scrollBy(0,510)", "")
        time.sleep(1)
        check_banbe_riengtu = driver.find_element(By.XPATH, var.check_banbe_riengtu3).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - Rêng tư")
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - Không có bạn bè nào")
        logging.info(check_banbe_riengtu == "Không có bạn bè nào")
        time.sleep(1.5)



        #quyền bạn bè
        login.login3(self, "truongvck33@gmail.com", "atgmj123456")
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_iconchinhsuaquyen).click()
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_dsbb_banbe2).click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(1)
        check_banbe_riengtu = driver.find_element(By.XPATH, var.check_dsbb_quyenbanbe).text
        time.sleep(1)
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư")
        logging.info("check font-end: Danh sách bạn bè khi chỉnh quyền thành Bạn bè có hiển thị không")
        logging.info(check_banbe_riengtu == "hue nguyen")
        time.sleep(0.5)
        #người lạ
        login.login4(self, "truongvck222@gmail.com", "atgmj123456")
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.execute_script("window.scrollBy(0,510)", "")
        time.sleep(1)
        check_banbe_riengtu = driver.find_element(By.XPATH, var.check_nguoila_riengtu3a).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - bạn bè")
        print(check_banbe_riengtu)
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - chỉ hiện thị bạn bè chung")
        logging.info(check_banbe_riengtu == "hue nguyen")
        time.sleep(1.5)
        #Bạn bè
        login.login4(self, "truongvck333@gmail.com", "atgmj123456")
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.execute_script("window.scrollBy(0,510)", "")
        time.sleep(1)
        check_banbe_quyenbanbe = driver.find_element(By.XPATH, var.check_banbe_quyenbanbe1).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - Bạn bè")
        logging.info("check font-end: login bằng tài khoản khác(bạn bè) và check  - có bạn bè tên Ngọc Mai")
        logging.info(check_banbe_quyenbanbe == "Ngọc Mai")
        time.sleep(1.5)



        # quyền công khai
        login.login3(self, "truongvck33@gmail.com", "atgmj123456")
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.find_element(By.XPATH, var.trangcanhan_banbe_iconchinhsuaquyen).click()
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_dsbb_congkhai3).click()

        # driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb).click()
        # driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_dsbb_congkhai).click()
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,700)", "")
        time.sleep(1)
        check_banbe_quyenbanbe_huenguyen = driver.find_element(By.XPATH, var.check_banbe_quyenbanbe_huenguyen1).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư")
        logging.info(check_banbe_quyenbanbe_huenguyen)
        logging.info("check font-end: Danh sách bạn bè khi chỉnh quyền thành Công khai có hiển thị không")
        logging.info(check_banbe_quyenbanbe_huenguyen == "hue nguyen")
        time.sleep(0.5)

        # người lạ
        login.login4(self, "truongvck222@gmail.com", "atgmj123456")
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.execute_script("window.scrollBy(0,510)", "")
        time.sleep(1)
        check_nguoila_congkhai = driver.find_element(By.XPATH, var.check_banbe_quyencongkhaia).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - Công khai")
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - xem được bạn bè")
        logging.info(check_nguoila_congkhai == "hue nguyen")
        time.sleep(1.5)

        # Bạn bè
        login.login4(self, "truongvck333@gmail.com", "atgmj123456")
        driver.get("https://sn.emso.vn/user/111169896815147328")
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangcanhan_banbe).click()
        driver.execute_script("window.scrollBy(0,510)", "")
        time.sleep(1)
        check_banbe_quyenbanbe = driver.find_element(By.XPATH, var.check_banbe_quyenbanbe).text
        print(check_banbe_quyenbanbe)
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - Công khai")
        logging.info("check font-end: login bằng tài khoản khác(bạn bè) và check  - xem được bạn bè")
        logging.info(check_banbe_quyenbanbe == "hue nguyen\n1 bạn chung")
        time.sleep(1.5)


class anh_video:
    def anh(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_anh).click()
        driver.execute_script("window.scrollBy(0,700)", "")
        #ảnh
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_anh_xemanh).click()
        time.sleep(3)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_thich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).send_keys(data['trangcanhan_anh_video']['trangcanhan_anh_binhluan'])
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).submit()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_anh_xemanh_x).click()

        #album
        driver.find_element(By.XPATH, var.trangcanhan_anh_album).click()
        driver.find_element(By.XPATH, var.trangcanhan_anh_alum_taomoi).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_ten).send_keys(data['trangcanhan_anh_video']['trangcanhan_anh_anh'])
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_mota).send_keys(data['trangcanhan_anh_video']['trangcanhan_anh_mota'])
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_tailen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia1.exe")
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_anhtailen_chuthich).send_keys(data['trangcanhan_anh_video']['chuthich'])
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_dang).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_iconxoa).click()
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_xoa).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_xoa).click()
        time.sleep(1)

    def video(self):
        #video
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.execute_script("window.scrollBy(0,300)", "")
        driver.find_element(By.XPATH, var.trangcanhan_video).click()
        driver.find_element(By.XPATH, var.trangcanhan_video_xem).click()
        time.sleep(3)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_thich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).send_keys(data['trangcanhan_anh_video']['trangcanhan_video_binhluan'])
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).submit()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_video_xemvideo_x).click()

        #khoanh khắc
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac).click()
        driver.find_element(By.XPATH, var.trangcanhan_video_xem).click()
        time.sleep(3)
        # driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_like).click()
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_thich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).send_keys(data['trangcanhan_anh_video']['trangcanhan_video_binhluan1'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).submit()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_x).click()
        del driver.requests
        time.sleep(2)


class check_thongtin_trangcanhan():
    def check_thongtin_trangcanhan(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        #giới thiệu(tổng quan, cong việc, nơi sống...)
        # driver.refresh()
        # time.sleep(3)
        try:
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
            tongquan_songtai1 = driver.find_element(By.XPATH, var.tongquan_songtai1).text
            tongquan_dentu1 = driver.find_element(By.XPATH, var.tongquan_dentu1).text
        except:
            driver.refresh()
            time.sleep(3)
            driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
            tongquan_songtai1 = driver.find_element(By.XPATH, var.tongquan_songtai1).text
            tongquan_dentu1 = driver.find_element(By.XPATH, var.tongquan_dentu1).text

        tongquan_tinhtrang_mqh1 = driver.find_element(By.XPATH, var.tongquan_tinhtrang_mqh1).text
        tongquan_nguoithan_mqh1 = driver.find_element(By.XPATH, var.tongquan_nguoithan_mqh1).text
        tongquan_sodienthoai1 = driver.find_element(By.XPATH, var.tongquan_sodienthoai1).text
        tongquan_bietdanh1 = driver.find_element(By.XPATH, var.tongquan_bietdanh1).text
        time.sleep(0.5)

        #công việc và học vấn
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_congviecvahocvan).click()
        cvvahocvan_cv_chucvu1 = driver.find_element(By.XPATH, var.cvvahocvan_cv_chucvu1).text
        cvvahocvan_cv_congty1 = driver.find_element(By.XPATH, var.cvvahocvan_cv_chucvu1).text
        cvvahocvan_daihoc_truonghoc1 = driver.find_element(By.XPATH, var.cvvahocvan_daihoc_truonghoc1).text
        cvvahocvan_trunghoc_truonghoc1 = driver.find_element(By.XPATH, var.cvvahocvan_trunghoc_truonghoc1).text
        time.sleep(0.5)

        # nơi từng sống
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_noitungsong).click()
        noitungsong_songtai1 = driver.find_element(By.XPATH, var.noitungsong_songtai1).text
        noitungsong_dentu1 = driver.find_element(By.XPATH, var.noitungsong_dentu1).text
        time.sleep(0.5)

        # thông tin cơ bản
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_thongtincoban).click()
        thongtincoban_sodienthoai1 = driver.find_element(By.XPATH, var.thongtincoban_sodienthoai1).text
        thongtincoban_web1 = driver.find_element(By.XPATH, var.thongtincoban_web1).text
        thongtincoban_lienket1 = driver.find_element(By.XPATH, var.thongtincoban_lienket1).text
        thongtincoban_tieusu1 = driver.find_element(By.XPATH, var.thongtincoban_tieusu1).text
        thongtincoban_bietdanh1 = driver.find_element(By.XPATH, var.thongtincoban_bietdanh1).text
        time.sleep(0.5)

        # Gia đình và các mối quan hệ
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_gdvacacmqh).click()
        tongquan_gdvacacmqh_tingtrang_mqh1 = driver.find_element(By.XPATH, var.tongquan_gdvacacmqh_tingtrang_mqh1).text
        tongquan_gdvacacmqh_nguoithan_mqh1 = driver.find_element(By.XPATH, var.tongquan_gdvacacmqh_nguoithan_mqh1).text
        time.sleep(0.5)

        # Sự kiện trong đời
        driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sukientrongdoi).click()
        tongquan_sukientrongdoi_trunghoc_tentruong1 = driver.find_element(By.XPATH, var.tongquan_sukientrongdoi_trunghoc_tentruong1).text
        tongquan_sukientrongdoi_daihoc_tentruong1 = driver.find_element(By.XPATH, var.tongquan_sukientrongdoi_daihoc_tentruong1).text
        tongquan_sukientrongdoi_congviec_congty1 = driver.find_element(By.XPATH, var.tongquan_sukientrongdoi_congviec_congty1).text
        time.sleep(0.5)

        # GIỚI THIỆU(trang cá nhân)
        driver.find_element(By.XPATH, var.trangcanhan_baiviet).click()
        bietdanh2 = driver.find_element(By.XPATH, var.bietdanh2).text   #
        tieusu2 = driver.find_element(By.XPATH, var.tieusu2).text   #Mãi chả xong zzz
        congviec_chucvu2 = driver.find_element(By.XPATH, var.congviec_chucvu2).text  #Nhân Viên
        congviec_congty2 = driver.find_element(By.XPATH, var.congviec_chucvu2).text     #Cafe+
        daihoc_truonghoc2 = driver.find_element(By.XPATH, var.daihoc_truonghoc2).text       #Đại học bách khoa hà nội
        trunghoc_truonghoc2 = driver.find_element(By.XPATH, var.trunghoc_truonghoc2).text       #Trường THPT Phú Bình ( Phú Bình High School )
        songtai2 = driver.find_element(By.XPATH, var.songtai2).text     #Lạng Sơn
        dentu2 = driver.find_element(By.XPATH, var.dentu2).text     #Hưng Yên
        moiquanhe_tinhtrang2 = driver.find_element(By.XPATH, var.moiquanhe_tinhtrang2).text     #Hẹn hò
        moiquanhe_nguoithan2 = driver.find_element(By.XPATH, var.moiquanhe_nguoithan2).text     #Ngọc Mai
        web2 = driver.find_element(By.XPATH, var.web2).text     #https://plusplus.vn/
        lienket2 = driver.find_element(By.XPATH, var.lienket2).text     #https://pypi.org/
        sothich2 = driver.find_element(By.XPATH, var.sothich2).text
        time.sleep(0.5)
        # del driver.requests

        # Chỉnh sửa trang cá nhân
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuatrangcanhan).click()
        time.sleep(1)
        tieusu3 = driver.find_element(By.XPATH, var.tieusu3).text   #Mãi chả xong zzz
        congviec_chucvu3 = driver.find_element(By.XPATH, var.congviec_chucvu3).text  #Nhân Viên
        congviec_congty3 = driver.find_element(By.XPATH, var.congviec_chucvu3).text     #Cafe+
        daihoc_truonghoc3 = driver.find_element(By.XPATH, var.daihoc_truonghoc3).text       #Đại học bách khoa hà nội
        trunghoc_truonghoc3 = driver.find_element(By.XPATH, var.trunghoc_truonghoc3).text       #Trường THPT Phú Bình ( Phú Bình High School )
        songtai3 = driver.find_element(By.XPATH, var.songtai3).text     #Lạng Sơn
        dentu3 = driver.find_element(By.XPATH, var.dentu3).text     #Hưng Yên
        moiquanhe_tinhtrang3 = driver.find_element(By.XPATH, var.moiquanhe_tinhtrang3).text     #Hẹn hò
        moiquanhe_nguoithan3 = driver.find_element(By.XPATH, var.moiquanhe_tinhtrang3).text     #Ngọc Mai
        sodienthoai3 = driver.find_element(By.XPATH, var.sodienthoai3).text     #Số diẹn thoại
        bietdanh3 = driver.find_element(By.XPATH, var.bietdanh3).text     #Bit danh
        web3 = driver.find_element(By.XPATH, var.web3).text     #https://plusplus.vn/
        lienket3 = driver.find_element(By.XPATH, var.lienket3).text     #https://pypi.org/
        sothich3 = driver.find_element(By.XPATH, var.sothich3).text
        driver.refresh()
        time.sleep(2)
        for request in driver.requests:
            if request.url == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/abouts":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)

                #tiểu sử
                logging.info("check back-end, font-end trường: Trang cá nhân - Tiểu sử ")
                logging.info("respone: " + res['general_information']['description'])
                logging.info("Giới thiêu - thông tin cơ bản: " + thongtincoban_tieusu1)
                logging.info("Giới thiệu - Trang cá nhân: " + tieusu2)
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + tieusu3)
                logging.info(res['general_information']['description'] == thongtincoban_tieusu1 == tieusu2 == tieusu3)

                #sống tại
                logging.info("check back-end, font-end trường: Trang cá nhân - Sống tai ")
                logging.info("respone: " + res['general_information']['place_live']['title'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_songtai1)
                logging.info("Giới thiêu - Nơi từng sống: " + noitungsong_songtai1)
                logging.info("Giới thiệu - Trang cá nhân: " + songtai2[9::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + songtai3[9::])
                logging.info(res['general_information']['place_live']['title'] == tongquan_songtai1 == noitungsong_songtai1 == songtai2[9::] == songtai3[9::])

                #đến từ
                logging.info("check back-end, font-end trường: Trang cá nhân - Đến từ ")
                logging.info("respone: " + res['general_information']['hometown']['title'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_dentu1)
                logging.info("Giới thiêu - Nơi từng sống: " + noitungsong_dentu1)
                logging.info("Giới thiệu - Trang cá nhân: " + dentu2[7::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + dentu3[7::])
                logging.info(res['general_information']['hometown']['title'] == tongquan_dentu1 == noitungsong_dentu1 == dentu2[7::] == dentu3[7::])

                #Mối quan hệ
                #tình trạng
                logging.info("check back-end, font-end trường: Trang cá nhân - Mối quan hệ - Tình trạng ")
                logging.info("respone: " + res['account_relationship']['relationship_category']['name'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_tinhtrang_mqh1[0:6])
                logging.info("Giới thiêu - Gia đình và các mối quan hệ: " + tongquan_gdvacacmqh_tingtrang_mqh1[0:6])
                logging.info("Giới thiệu - Trang cá nhân: " + moiquanhe_tinhtrang2[0:6])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + moiquanhe_tinhtrang3[0:6])
                logging.info(res['account_relationship']['relationship_category']['name'] == tongquan_tinhtrang_mqh1[0:6] == tongquan_gdvacacmqh_tingtrang_mqh1[0:6] == moiquanhe_tinhtrang2[0:6] == moiquanhe_tinhtrang3[0:6])

                #Người thân
                logging.info("check back-end, font-end trường: Trang cá nhân - Mối quan hệ - Người thân ")
                logging.info("respone: " + res['account_relationship']['partner']['display_name'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_nguoithan_mqh1)
                logging.info("Giới thiêu - Gia đình và các mối quan hệ: " + tongquan_gdvacacmqh_nguoithan_mqh1)
                logging.info("Giới thiệu - Trang cá nhân: " + moiquanhe_nguoithan2[17:25])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + moiquanhe_nguoithan3[16:24])
                logging.info(res['account_relationship']['partner']['display_name'] == tongquan_nguoithan_mqh1 == tongquan_gdvacacmqh_nguoithan_mqh1 == moiquanhe_nguoithan2[17:25] == moiquanhe_nguoithan3[16:24])

                #Số điện thoại
                logging.info("check back-end, font-end trường: Trang cá nhân - Số điện thoai ")
                logging.info("respone: " + res['general_information']['phone_number'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_sodienthoai1)
                logging.info("Giới thiệu - Thông tin cơ bản: " + thongtincoban_sodienthoai1)
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + sodienthoai3)
                logging.info(res['general_information']['phone_number'] == tongquan_sodienthoai1 == thongtincoban_sodienthoai1 == sodienthoai3)

                #biêt danh
                logging.info("check back-end, font-end trường: Trang cá nhân - Biệt danh ")
                logging.info("respone: " + res['general_information']['other_name'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_bietdanh1)
                logging.info("Giới thiêu - Thông tin cơ bản: " + thongtincoban_bietdanh1)
                logging.info("Giới thiệu - Trang cá nhân: " + bietdanh2[1:13])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + bietdanh3)
                logging.info(res['general_information']['other_name'] == tongquan_bietdanh1 == thongtincoban_bietdanh1 == bietdanh2[1:13] == bietdanh3)

                #web
                logging.info("check back-end, font-end trường: Trang cá nhân - Web ")
                logging.info("respone: " + res['general_information']['account_web_link'][0]['url'])
                logging.info("Giới thiêu - thông tin cơ bản: " + thongtincoban_web1)
                logging.info("Giới thiệu - Trang cá nhân: " + web2[::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + web3[::])
                logging.info(res['general_information']['account_web_link'][0]['url'] == web2[::] == thongtincoban_web1 == web3[::])

                #lien kết
                logging.info("check back-end, font-end trường: Trang cá nhân - Liên kết ")
                logging.info("respone: " + res['general_information']['account_social'][0]['text'])
                logging.info("Giới thiêu - thông tin cơ bản: " + thongtincoban_lienket1)
                logging.info("Giới thiệu - Trang cá nhân: " + lienket2[::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + lienket3[::])
                logging.info(res['general_information']['account_social'][0]['text'] == thongtincoban_lienket1 == lienket2[::] == lienket3[::])

                #Sở thích
                logging.info("check back-end, font-end trường: Trang cá nhân - Sở thích ")
                logging.info("respone: " + res['hobbies'][0]['text'])
                logging.info("Giới thiệu - Trang cá nhân: " + sothich2)
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + sothich3)
                logging.info(res['hobbies'][0]['text'] == sothich2 == sothich3)

                break
            else:
                pass
                # print("không có  response api abouts")
        time.sleep(0.5)
        for request in driver.requests:
            if request.url[0:70] == "https://snapi.emso.asia/api/v1/accounts/111169896815147328/life_events":
                data1 = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
                data1 = data1.decode("utf8")
                res = json.loads(data1)
                # print("r1")
                # print(res[0]['life_event'])
                # print("r2")
                # print(res[1]['life_event'])
                # print("r3")
                # print(res[2]['life_event'])
                # print("r4")
                # print(res[3]['life_event'])
                # print("r5")
                # print(res[4]['life_event'])

                #công viêc - công ty
                logging.info("check back-end, font-end trường: Trang cá nhân - Công ty ")
                logging.info("respone: " + res[0]['life_event']['company'])
                logging.info("Giới thiêu - công việc và học vấn: " + cvvahocvan_cv_congty1[12::])
                logging.info("Giới thiêu - Sự kiên trong đời: " + tongquan_sukientrongdoi_congviec_congty1[4::])
                logging.info("Giới thiệu - Trang cá nhân: " + congviec_congty2[14::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + congviec_congty3[14::])
                logging.info(res[0]['life_event']['company'] == cvvahocvan_cv_congty1[12::] == tongquan_sukientrongdoi_congviec_congty1[4::] == congviec_congty2[14::] == congviec_congty3[14::])

                #công viêc - chức vu
                logging.info("check back-end, font-end trường: Trang cá nhân - Chức vụ ")
                logging.info("respone: " + res[0]['life_event']['position'])
                logging.info("Giới thiêu - công việc và học vấn: " + cvvahocvan_cv_chucvu1[0:9])
                logging.info("Giới thiệu - Trang cá nhân: " + congviec_chucvu2[0:9])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + congviec_chucvu3[0:9])
                logging.info(res[0]['life_event']['position'] == cvvahocvan_cv_chucvu1[0:9] == congviec_chucvu2[0:9] == congviec_chucvu3[0:9])

                #đai hoc
                logging.info("check back-end, font-end trường: Trang cá nhân - Trường đại học ")
                logging.info("respone: " + res[1]['life_event']['company'])
                logging.info("Giới thiêu - công việc và học vấn: " + cvvahocvan_daihoc_truonghoc1[4::])
                logging.info("Giới thiêu - Sự kiên trong đời: " + tongquan_sukientrongdoi_daihoc_tentruong1[4::])
                logging.info("Giới thiệu - Trang cá nhân: " + daihoc_truonghoc2[13::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + daihoc_truonghoc3[13::])
                logging.info(res[1]['life_event']['company'] == cvvahocvan_daihoc_truonghoc1[4::] == tongquan_sukientrongdoi_daihoc_tentruong1[4::] == daihoc_truonghoc2[13::] == daihoc_truonghoc3[13::])

                #trung hoc
                logging.info("check back-end, font-end trường: Trang cá nhân - Trường trung học ")
                logging.info("respone: " + res[2]['life_event']['company'])
                logging.info("Giới thiêu - công việc và học vấn: " + cvvahocvan_trunghoc_truonghoc1)
                logging.info("Giới thiêu - Sự kiện trong đời: " + tongquan_sukientrongdoi_trunghoc_tentruong1[4::])
                logging.info("Giới thiệu - Trang cá nhân: " + trunghoc_truonghoc2[11::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + trunghoc_truonghoc3[11::])
                logging.info(res[2]['life_event']['company'] == cvvahocvan_trunghoc_truonghoc1 == tongquan_sukientrongdoi_trunghoc_tentruong1[4::] == trunghoc_truonghoc2[11::] == trunghoc_truonghoc3[11::])

                break
            else:
                pass
                # print("không có  response api life events")


class trangchu():
    def taobaiviet(self, trangthai, mota, camxuc, hoatdong, tinhtrang):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.taobaiviet_anhvideo).click()
        driver.find_element(By.XPATH, var.taobaiviet_trangthai_icon).click()
        # driver.find_element(By.XPATH, var.taobaiviet_trangthai_riengtu).click()
        driver.find_element(By.XPATH, trangthai).click()
        driver.find_element(By.XPATH, var.taobaiviet_mota).send_keys(mota)
        driver.find_element(By.XPATH, var.taobaiviet_tailenanhvideo).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia1.exe")
        time.sleep(2)
        driver.find_element(By.XPATH, var.chinhsua).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.chinhsua1).click()
        driver.find_element(By.XPATH, var.chinhsua_cat).click()
        driver.find_element(By.XPATH, var.chinhsua_xoay).click()
        driver.find_element(By.XPATH, var.chinhsua_chenvanvan).click()
        driver.find_element(By.XPATH, var.chinhsua_nhapvanvan).send_keys(data['trangchu_taobaiviet']['chinhsua_nhapvanvan'])
        driver.find_element(By.XPATH, var.chinhsua_luu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.themanhvideo).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.chinhsua).click()
        driver.find_element(By.XPATH, var.chinhsua_chuthich1).send_keys(data['trangchu_taobaiviet']['chinhsua_chuthich1'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.chinhsua_chuthich2).click()
        driver.find_element(By.XPATH, var.chinhsua_chuthich2).send_keys(data['trangchu_taobaiviet']['chinhsua_chuthich2'])
        driver.find_element(By.XPATH, var.chinhsua_xong).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.taobaiviet_camxuchoatdong).click()
        driver.find_element(By.XPATH, var.taobaiviet_camxuchoatdong_camxuc).click()
        driver.find_element(By.XPATH, camxuc).click()
        driver.find_element(By.XPATH, var.taobaiviet_camxuchoatdong).click()
        driver.find_element(By.XPATH, var.taobaiviet_hoatdong).click()
        driver.find_element(By.XPATH, hoatdong).click()
        # driver.find_element(By.XPATH, var.hoatdong_x).click()
        button = driver.find_element(By.XPATH, var.hoatdong_x)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.taobaiviet_ganthenguoikhac).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.taobaiviet_ngocmai).click()
        driver.find_element(By.XPATH, var.xong).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.dang).click()
        time.sleep(3.5)
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.messgae_taobaiviet1)))
        print(element.text)
        logging.info(element.text)
        check_taobaiviet = driver.find_element(By.XPATH, var.check_taobaiviet2).text
        logging.info("Trang chủ - Tạo bài viết ")
        logging.info("Tạo bài viết - Mô tả:  Đây là bai viết "+ tinhtrang)
        logging.info("check font-end: Bài viết đang để quyền " + tinhtrang)
        logging.info(check_taobaiviet == "Đây là bai viết "+ tinhtrang)
        time.sleep(1)

    def taobaimoment(self):
        driver.implicitly_wait(15)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH, var.khoanhkhac).click()
        driver.find_element(By.XPATH, var.khoanhkhac_nhapnoidung).send_keys(data['trangchu_taobaiviet']['khoanhkhac_noidung'])
        driver.find_element(By.XPATH, var.khoanhkhac_tailenvideo).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/quangaygiongbao.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.khoanhkhac_dangbai).click()
        time.sleep(15)

    def camxuc_hoatdong(self):
        driver.implicitly_wait(15)
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH, var.camxuc_hoatdong).click()
        driver.find_element(By.XPATH, var.camxuc).click()
        driver.find_element(By.XPATH, var.camxuc_xucdong).click()
        time.sleep(1)
        check_taobaiviet_camxuc = driver.find_element(By.XPATH,var.check_taobaiviet_camxuc1).text
        logging.info("Trang chủ - Cảm xúc/Hoạt động")
        logging.info("check font-end: đang cảm thấy xúc động ")
        logging.info(check_taobaiviet_camxuc)
        logging.info(check_taobaiviet_camxuc =="đang  cảm thấy xúc động ")
        driver.find_element(By.XPATH, var.x).click()

        driver.find_element(By.XPATH, var.camxuc_hoatdong).click()
        driver.find_element(By.XPATH, var.camxuc_hoatdong_hoatdong).click()
        driver.find_element(By.XPATH, var.hoatdong_dangxem).click()
        logging.info("Trang chủ - Cảm xúc/Hoạt động")
        logging.info("check font-end: Options của hoạt động")
        logging.info("Chức năng chưa hoạt động")


        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1)
        check_taobaiviet_hoatdong = driver.find_element(By.XPATH,var.check_taobaiviet_hoatdong1).text
        logging.info("Trang chủ - Cảm xúc/Hoạt động")
        logging.info("check font-end: đang xem")
        logging.info(check_taobaiviet_hoatdong)
        logging.info(check_taobaiviet_hoatdong == "đang xem")
        driver.find_element(By.XPATH, var.x).click()

    def taobaiviet_congkhai(self):
        trangchu.taobaiviet(self, var.taobaiviet_trangthai_congkhai, "Đây là bai viết công khai", var.taobaiviet_camxuc_tuyet, var.taobaiviet_hoatdong_dangxem, "công khai" )

    def taobaiviet_banbe(self):
        trangchu.taobaiviet(self, var.taobaiviet_trangthai_banbe, "Đây là bai viết bạn bè", var.taobaiviet_camxuc_yeu, var.taobaiviet_hoatdong_dangnghive, "bạn bè" )

    def taobaiviet_riengtu(self):
        trangchu.taobaiviet(self, var.taobaiviet_trangthai_riengtu, "Đây là bai viết riêng tư", var.taobaiviet_camxuc_vuive2, var.taobaiviet_hoatdong_dangtim, "riêng tư" )

    def menu(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).clear()
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys(data['trangchu_menu']['timkiem'])
        driver.find_element(By.XPATH, var.trangchu_menu_banbe).click()
        time.sleep(2)
        check_menu_name1 = driver.find_element(By.XPATH,var.check_menu_name1).text
        logging.info("Trang chủ - Menu - Bạn bè")
        logging.info("check font-end: Tiêu đề: " + check_menu_name1)
        logging.info(check_menu_name1 == "Bạn bè")
        driver.refresh()
        time.sleep(2)

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).clear()
        driver.find_element(By.XPATH, var.trangchu_menu_nhom).click()
        check_menu_name2 = driver.find_element(By.XPATH,var.check_menu_name2).text
        logging.info("Trang chủ - Menu - Nhóm")
        logging.info("check font-end: Tiêu đề: " + check_menu_name2)
        logging.info(check_menu_name2 == "Nhóm")



        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_trang).click()
        check_menu_name3 = driver.find_element(By.XPATH,var.check_menu_name3).text
        logging.info("Trang chủ - Menu - Trang")
        logging.info("check font-end: Tiêu đề: " + check_menu_name3)
        logging.info(check_menu_name3 == "Trang")


        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_sukien).click()
        check_menu_name4 = driver.find_element(By.XPATH,var.check_menu_name4).text
        logging.info("Trang chủ - Menu - Sự kiện")
        logging.info("check font-end: Tiêu đề: " + check_menu_name4)
        logging.info(check_menu_name4 == "Sự kiện")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_goivon).click()
        check_menu_name5 = driver.find_element(By.XPATH,var.check_menu_name5).text
        logging.info("Trang chủ - Menu - Gọi vốn cộng đồng")
        logging.info("check font-end: Tiêu đề: " + check_menu_name5)
        logging.info(check_menu_name5 == "Gọi vốn cộng đồng")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_tuyendung).click()
        check_menu_name6 = driver.find_element(By.XPATH,var.check_menu_name6).text
        logging.info("Trang chủ - Menu - Tuyển dụng")
        logging.info("check font-end: Tiêu đề: " + check_menu_name6)
        logging.info(check_menu_name6 == "Tuyển dụng")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_khoahoc).click()
        check_menu_name7 = driver.find_element(By.XPATH,var.check_menu_name7).text
        logging.info("Trang chủ - Menu - Khoá học")
        logging.info("check font-end: Tiêu đề: " + check_menu_name7)
        logging.info(check_menu_name7 == "Khóa học")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_hienmau).click()
        check_menu_name8 = driver.find_element(By.XPATH,var.check_menu_name8).text
        logging.info("Trang chủ - Menu - Hiến máu")
        logging.info("check font-end: Tiêu đề: " + check_menu_name8)
        logging.info(check_menu_name8 == "Hiến máu")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Không gian âm nhạc")
        driver.find_element(By.XPATH, var.trangchu_menu_khonggianamnhac).click()
        check_menu_name9 = driver.find_element(By.XPATH,var.check_menu_name9).text
        logging.info("Trang chủ - Menu - Không gian âm nhạc")
        logging.info("check font-end: Tiêu đề: " + check_menu_name9)
        logging.info(check_menu_name9 == "Không gian Âm nhạc")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1.5)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Trò chuyện")
        driver.find_element(By.XPATH, var.trangchu_menu_trochuyen).click()
        check_menu_name10 = driver.find_element(By.XPATH,var.check_menu_name10).text
        logging.info("Trang chủ - Menu - Trò chuyện")
        logging.info("check font-end: Tiêu đề: " + check_menu_name10)
        logging.info(check_menu_name10 == "Chat")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Khoảnh khắc")
        driver.find_element(By.XPATH, var.trangchu_menu_khoanhkhac).click()
        check_menu_name11 = driver.find_element(By.XPATH,var.check_menu_name11).text
        logging.info("Trang chủ - Menu - Khoảnh khắc")
        logging.info("check font-end: Tiêu đề: " + check_menu_name11)
        logging.info(check_menu_name11 == "Khoảnh khắc")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Watch")
        driver.find_element(By.XPATH, var.trangchu_menu_watch).click()
        check_menu_name12 = driver.find_element(By.XPATH,var.check_menu_name12).text
        logging.info("Trang chủ - Menu - Watch")
        logging.info("check font-end: Tiêu đề: " + check_menu_name12)
        logging.info(check_menu_name12 == "Watch")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Không gian thương mại")
        driver.find_element(By.XPATH, var.trangchu_menu_khonggianthuongmai).click()
        check_menu_name13 = driver.find_element(By.XPATH,var.check_menu_name13).text
        logging.info("Trang chủ - Menu - Không gian thương mại")
        logging.info("check font-end: Tiêu đề: " + driver.title)
        logging.info(check_menu_name13 == "Shop của tôi")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Kỷ niệm")
        driver.find_element(By.XPATH, var.trangchu_menu_kyniem).click()
        check_menu_name14 = driver.find_element(By.XPATH,var.check_menu_name14).text
        logging.info(check_menu_name14)
        logging.info("Trang chủ - Menu - Kỷ niệm")
        logging.info("check font-end: Tiêu đề: " + check_menu_name14)
        logging.info(check_menu_name14 == "Kỷ niệm")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Đã lưu")
        driver.find_element(By.XPATH, var.trangchu_menu_daluu).click()
        check_menu_name15 = driver.find_element(By.XPATH,var.check_menu_name15).text
        print(check_menu_name15)
        logging.info("Trang chủ - Menu - Đã lưu")
        logging.info("check font-end: Tiêu đề: " + check_menu_name15)
        logging.info(check_menu_name15 == "Đã lưu")

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trangchu_timkiem_menu)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangchu_timkiem_menu).send_keys("Đơn đặt hàng và thanh toán")
        driver.find_element(By.XPATH, var.trangchu_menu_dondathangvathanhtoan).click()
        driver.find_element(By.XPATH, var.trangchu_menu_dondathangvathanhtoan_huy).click()
        check_menu_name16 = driver.find_element(By.XPATH,var.check_menu_name16).text
        logging.info("Trang chủ - Menu - Đơn đặt hàng và thanh toán")
        logging.info("check font-end: Tiêu đề: " + check_menu_name16)
        logging.info(check_menu_name16 == "Đơn đặt hàng và thanh toán")
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)

    def menu_tao(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_tao_post).click()
        check_taobaiviet = driver.find_element(By.XPATH, var.check_taobaiviet1).text
        print(check_taobaiviet)
        logging.info("Trang chủ - Tạo bài viết - Post")
        logging.info("check font-end: chuyển tới POPUP: " + check_taobaiviet)
        logging.info(check_taobaiviet == "Tạo bài viết")
        driver.find_element(By.XPATH, var.taobaiviet_x).click()

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_tao_khoanhkhac).click()
        check_taobaimoment = driver.find_element(By.XPATH, var.check_taobaimoment1).text
        print(check_taobaimoment)
        logging.info("Trang chủ - Tạo bài viết - Khoảnh khắc")
        logging.info("check font-end: chuyển tới POPUP: " + check_taobaimoment)
        logging.info(check_taobaimoment == "Tạo bài khoảnh khắc")
        driver.find_element(By.XPATH, var.check_taobaimoment_x).click()

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_tao_trang).click()
        check_taotrang = driver.find_element(By.XPATH, var.check_taotrang1).text
        print(check_taotrang)
        logging.info("Trang chủ - Tạo bài viết - Trang")
        logging.info("check font-end: chuyển tới POPUP: " + check_taotrang)
        logging.info(check_taotrang == "Tạo Trang")
        driver.find_element(By.XPATH, var.check_taotrang_x).click()

        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_tao_nhom).click()
        check_taonhom = driver.find_element(By.XPATH, var.check_taonhom1).text
        print(check_taonhom)
        logging.info("Trang chủ - Tạo bài viết - Nhóm")
        logging.info("check font-end: chuyển tới POPUP: " + check_taonhom)
        logging.info(check_taonhom == "Tạo nhóm")
        driver.find_element(By.XPATH, var.check_taonhom_x).click()


        driver.find_element(By.XPATH, var.trangchu_menu).click()
        driver.find_element(By.XPATH, var.trangchu_menu_tao_sukien).click()
        check_taosukien = driver.find_element(By.XPATH, var.check_taosukien1).text
        print(check_taosukien)
        logging.info("Trang chủ - Tạo bài viết - Sự kiện")
        logging.info("check font-end: chuyển tới POPUP: " + check_taonhom)
        logging.info(check_taosukien == "Tạo sự kiện")
        driver.find_element(By.XPATH, var.check_taosukien_x).click()
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)

    def tinnhanmoi(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_den_input).send_keys(data['trangchu_tinnhan']['tinnhanmoi_den'])
        time.sleep(3)
        try:
            driver.find_element(By.XPATH, var.tinnhanmoi_ngocmai).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangchu_tinnhanmoi).click()
            driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_den_input).send_keys(data['trangchu_tinnhan']['tinnhanmoi_den'])
            time.sleep(3)
            driver.find_element(By.XPATH, var.tinnhanmoi_ngocmai).click()

        #Ghi âm
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong_guiamthanh).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong_guiamthanh_x).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong_guiamthanh).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong_guiamthanh_ghiam).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icondaucong_guiamthanh_gui).click()

        #Đính kèm file
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icontailenfile).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)

        #Gif
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icongif).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icongif_input).send_keys(data['trangchu_tinnhan']['tinnhanmoi_meo'])
        time.sleep(5)

        try:
            driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icongif_anh1a).click()
        except:
            driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icongif_anh1).click()
            # driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icongif_anh4).click()
        #Nhãn dán
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_2).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_3).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_4).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_1).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_1_chonnhandan).click()

        #input
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_input).send_keys(data['trangchu_tinnhan']['tinnhanmoi_input'])
        #Biểu tượng cảm xúc
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page2).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page3).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page4).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page5).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page6).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page7).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page8).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page9).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_lichsu).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_chon).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_input).send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc).click()
        #Like
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_like).click()
        # button = driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_like)
        # driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_input).send_keys(Keys.ENTER)
        time.sleep(10)

    def chat(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.get("https://sn.emso.vn/user/truongvck33")
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu_chat).click()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(2)
        check_trangchu_chat_tuychon = driver.find_element(By.XPATH,var.check_trangchu_chat_tuychon1).text
        print(check_trangchu_chat_tuychon)
        logging.info("Trang chủ - Chat - Tuỳ chọn")
        logging.info("check font-end: Cài đặt chat")
        logging.info(check_trangchu_chat_tuychon == "Cài đặt Chat")

        #Âm thanh cuộc gọi đến
        amthanhgoiden_tat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhgoiden_tat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Âm thanh cuộc gọi đến")
        logging.info("check font-end: Âm thanh cuộc gọi đến: đang tắt")
        logging.info(amthanhgoiden_tat == "Âm thanh cuộc gọi đến: đang tắt")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhgoiden_tat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)
        amthanhgoiden_bat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhgoiden_bat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Âm thanh cuộc gọi đến")
        logging.info("check font-end: Âm thanh cuộc gọi đến: đang bật")
        logging.info(amthanhgoiden_bat == "Âm thanh cuộc gọi đến: đang bật")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhgoiden_bat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)

        #Âm thanh tin nhắn
        amthanhgoiden_tat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhtinnhan_tat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Âm thanh tin nhắn")
        logging.info("check font-end: Âm thanh tin nhắn: đang tắt")
        logging.info(amthanhgoiden_tat == "Âm thanh tin nhắn: đang tắt")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhtinnhan_tat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)
        amthanhgoiden_bat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhtinnhan_bat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Âm thanh tin nhắn")
        logging.info("check font-end: Âm thanh tin nhắn: đang bật")
        logging.info(amthanhgoiden_bat == "Âm thanh tin nhắn: đang bật")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_amthanhtinnhan_bat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)
        try:
            tudongmotinnhan_tat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_tudongmotinnhan_tat).text
        except:
            driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
            tudongmotinnhan_tat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_tudongmotinnhan_tat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Tự động mở tin nhắn")
        logging.info("check font-end: Tự động mở tin nhắn mới: đang tắt")
        logging.info(tudongmotinnhan_tat == "Tự động mở tin nhắn mới: đang tắt")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_tudongmotinnhan_tat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)
        tudongmotinnhan_bat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_tudongmotinnhan_bat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Tự động mở tin nhắn")
        logging.info("check font-end: Tự động mở tin nhắn mới: đang bật")
        logging.info(tudongmotinnhan_bat == "Tự động mở tin nhắn mới: đang bật")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_tudongmotinnhan_bat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)

        trangthaihoatdong_tat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_trangthaihoatdong_tat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Trạng thái hoạt động")
        logging.info("check font-end: Trạng thái hoạt động: đang tắt")
        logging.info(trangthaihoatdong_tat == "Trạng thái hoạt động: đang tắt")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_trangthaihoatdong_tat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)
        trangthaihoatdong_bat = driver.find_element(By.XPATH, var.trangchu_chat_tuychon_trangthaihoatdong_bat).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Trạng thái hoạt động")
        logging.info("check font-end: Trạng thái hoạt động: đang bật")
        logging.info(trangthaihoatdong_bat == "Trạng thái hoạt động: đang bật")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_trangthaihoatdong_bat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_tinnhancho).click()
        time.sleep(1)
        check_tinnhandangcho = driver.find_element(By.XPATH, var.check_tinnhandangcho1).text
        check_tinnhancho = driver.find_element(By.XPATH, var.check_tinnhancho1).text
        logging.info("Trang chủ - Chat - Tuỳ chọn - Tin nhắn chờ")
        logging.info("check font-end: Tin nhắn đang chờ")
        logging.info(check_tinnhandangcho == "Tin nhắn đang chờ")
        logging.info("check font-end: Người gửi tin nhắn - Vương Lâm")
        logging.info(check_tinnhancho == "Vương Lâm")


        driver.find_element(By.XPATH, var.trangchu_chat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_caidatguitinnhan).click()
        time.sleep(1)
        logging.info("Trang chủ - Chat - Tuỳ chọn - Cài đặt gửi tin nhắn")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.trangchu_chat_tuychon).click()
        time.sleep(1)

        driver.find_element(By.XPATH, var.trangchu_chat_tuychon_caidatchan).click()
        logging.info("Trang chủ - Chat - Tuỳ chọn - Cài đặt chặn")
        logging.info("Chức năng chưa hoạt động")
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)


    def chat_xemtatca(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu_chat).click()
        driver.find_element(By.XPATH, var.trangchu_emsochat).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.emsochat_goi).click()
        driver.find_element(By.XPATH, var.emsochat_video).click()

        #gửi text
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(data['trangchu_tinnhan']['input1'])
        driver.find_element(By.XPATH, var.emsochat_input).click()
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(Keys.ENTER)
        time.sleep(2)

        #xoá, gỡ bỏ
        chat_hover = driver.find_element(By.XPATH, var.chat_hover1)
        actions = ActionChains(driver)
        try:
            actions.move_to_element(chat_hover).perform()
        except:
            actions.move_to_element(chat_hover).perform()
        time.sleep(1)
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
        try:
            actions.move_to_element(xemthem).click().perform()
        except:
            actions.move_to_element(xemthem).click().perform()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_xoagobo).click()
        time.sleep(1.5)
        check_xoatinnhan = driver.find_element(By.XPATH,var.check_xoatinnhan1).text
        print(check_xoatinnhan)
        logging.info("Trang cá nhân - Chat - Xoá tin nhắn")
        logging.info("check font-end: message - Đã xóa tin nhắn thành công.")
        logging.info(check_xoatinnhan == "Đã xóa tin nhắn thành công.")
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_message_x).click()

        #Chỉnh sửa text
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(data['trangchu_tinnhan']['input'])
        driver.find_element(By.XPATH, var.emsochat_input).click()
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(Keys.ENTER)
        time.sleep(1)
        chat_hover = driver.find_element(By.XPATH, var.chat_hover1)
        try:
            actions.move_to_element(chat_hover).perform()
        except:
            actions.move_to_element(chat_hover).perform()
        time.sleep(1)
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
        try:
            actions.move_to_element(xemthem).click().perform()
        except:
            actions.move_to_element(xemthem).click().perform()
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_chinhsua).click()
        time.sleep(0.5)
        input_chat = driver.find_element(By.XPATH, var.emsochat_input)
        input_chat.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(data['trangchu_tinnhan']['input2'])
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(Keys.ENTER)
        time.sleep(0.5)
        check_suatinnhan = driver.find_element(By.XPATH,var.check_suatinnhan1).text
        print(check_suatinnhan)
        logging.info("Trang cá nhân - Chat - Sửa tin nhắn")
        logging.info("check font-end: Sửa tin nhắn - alo alo 123")
        logging.info(check_suatinnhan == "alo alo 123")

        #Chuyển tiếp
        chat_hover = driver.find_element(By.XPATH, var.chat_hover1)
        try:
            actions.move_to_element(chat_hover).perform()
        except:
            actions.move_to_element(chat_hover).perform()
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
        try:
            actions.move_to_element(xemthem).click().perform()
        except:
            actions.move_to_element(xemthem).click().perform()
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_chuyentiep).click()
        time.sleep(1)
        check_chyentiep = driver.find_element(By.XPATH,var.check_chyentiep1).text
        print(check_chyentiep)
        logging.info("Trang cá nhân - Chat - Chuyển tiếp tin nhắn")
        logging.info("check font-end: đang ở popup - Chuyển tiếp ")
        logging.info(check_chyentiep == "Chuyển tiếp")
        driver.find_element(By.XPATH, var.emsochat_chuyentiep_timkiem).click()
        driver.find_element(By.XPATH, var.emsochat_chuyentiep_timkiem).send_keys(data['trangchu_tinnhan']['timkiem_huenguyen'])
        time.sleep(2)
        driver.find_element(By.XPATH, var.emsochat_chuyentiep_timkiem_gui).click()
        time.sleep(2)
        check_chyentiep_dagui = driver.find_element(By.XPATH,var.check_chyentiep_dagui1).text
        print(check_chyentiep_dagui)
        logging.info("Trang cá nhân - Chat - Chuyển tiếp tin nhắn")
        logging.info("check font-end: tình trạng - Đã gửi ")
        logging.info(check_chyentiep_dagui == "Đã gửi")
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(0.5)

        #Gim
        try:
            actions.move_to_element(chat_hover).perform()
            actions.move_to_element(xemthem).click().perform()
        except:
            actions.move_to_element(chat_hover).perform()
            actions.move_to_element(xemthem).click().perform()
        time.sleep(1)
        check_gimtinnhan = driver.find_element(By.XPATH,var.emsochat_iconxemthem_gim).text
        print(check_gimtinnhan)
        logging.info("Trang cá nhân - Chat - Ghim tin nhắn")
        logging.info("check font-end: Ghim")
        logging.info(check_gimtinnhan)
        logging.info(check_gimtinnhan == "Ghim")
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_gim).click()
        time.sleep(1)
        #Bỏ gim
        try:
            actions.move_to_element(chat_hover).perform()
            actions.move_to_element(xemthem).click().perform()
        except:
            actions.move_to_element(chat_hover).perform()
            actions.move_to_element(xemthem).click().perform()
        time.sleep(1)
        check_bogimtinnhan = driver.find_element(By.XPATH,var.emsochat_iconxemthem_bogim).text
        print(check_bogimtinnhan)
        logging.info("Trang cá nhân - Chat - Bỏ Ghim tin nhắn")
        logging.info("check font-end: Bỏ ghim ")
        logging.info(check_bogimtinnhan == "Bỏ ghim")

        driver.find_element(By.XPATH, var.emsochat_iconxemthem_bogim).click()
        #Gim
        chat_hover4 = driver.find_element(By.XPATH, var.chat_hover4)
        actions.move_to_element(chat_hover4).perform()
        time.sleep(1)
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
        actions.move_to_element(xemthem).click().perform()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_gim).click()
        time.sleep(1)

        #Trả lời
        try:
            actions.move_to_element(chat_hover).perform()
            traloi = driver.find_element(By.XPATH, var.emsochat_input_icontraloi)
        except:
            actions.move_to_element(chat_hover).perform()
            traloi = driver.find_element(By.XPATH, var.emsochat_input_icontraloi)
        try:
            actions.move_to_element(traloi).click().perform()
        except:
            actions.move_to_element(traloi).click().perform()
        driver.find_element(By.XPATH, var.emsochat_traloi).send_keys(data['trangchu_tinnhan']['traloi'])
        driver.find_element(By.XPATH, var.emsochat_traloi).send_keys(Keys.ENTER)
        time.sleep(1.5)
        check_traloitinnhan = driver.find_element(By.XPATH,var.check_traloitinnhan1).text
        print(check_traloitinnhan)
        logging.info("Trang cá nhân - Chat - Trả lời tin nhắn")
        logging.info("check font-end: Trả lời tin nhắn  - Bạn đã trả lời chính mình")
        logging.info(check_traloitinnhan == "Bạn đã trả lời chính mình")
        time.sleep(2)

        #Bày tỏ cảm xúc
        chat_hover3 = driver.find_element(By.XPATH, var.chat_hover3)
        actions.move_to_element(chat_hover3).perform()
        print("r1")
        time.sleep(1)
        baytocamxuc = driver.find_element(By.XPATH, var.emsochat_input_iconbaytocamxuc)
        actions.move_to_element(baytocamxuc).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_yeuthich).click()
        time.sleep(1)

        #Icon ! dấu thăng hộp thoại
        #Trạng thái hoạt động
        driver.find_element(By.XPATH, var.emsochat_caidathopthoai).click()
        check_chat_tatthongbao = driver.find_element(By.XPATH,var.trangthaihoatdong).text
        print(check_chat_tatthongbao)
        logging.info("Trang chủ - Chat - tuỳ chon - Trạng thái hoạt động")
        logging.info("check font-end: Trạng thái hoạt động - Tắt thông báo")
        logging.info(check_chat_tatthongbao == "Tắt thông báo")
        driver.find_element(By.XPATH, var.emsochat_icontatthongbao).click()      #tắt thông báo
        time.sleep(1)
        check_chat_batthongbao = driver.find_element(By.XPATH,var.trangthaihoatdong).text
        print(check_chat_batthongbao)
        logging.info("Trang chủ - Chat - tuỳ chon - Trạng thái hoạt động")
        logging.info("check font-end: Trạng thái hoạt động - Bật thông báo")
        logging.info(check_chat_batthongbao == "Bật thông báo")
        driver.find_element(By.XPATH, var.emsochat_icontatthongbao).click()      #bật thông báo
        driver.find_element(By.XPATH, var.emsochat_icontimkiem).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_timkiem_input).send_keys(data['trangchu_tinnhan']['timkiem'])
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.emsochat_timkiem_input).click()
        driver.find_element(By.XPATH, var.emsochat_timkiem_input).send_keys(Keys.ENTER)
        time.sleep(1)
        check_chat_timkiem = driver.find_element(By.XPATH,var.check_chat_timkiem1).text
        print(check_chat_timkiem)
        print(data['trangchu_tinnhan']['timkiem'])
        logging.info(data['trangchu_tinnhan']['timkiem'])
        logging.info("Trang chủ - Chat - tuỳ chon - tìm kiếm")
        logging.info("check font-end: text hộp thoại - nghe rõ trả lời")
        logging.info(check_chat_timkiem == "nghe rõ trả lời")
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_timkiem_dong).click()

        #thông tin về đoạn chat
        driver.find_element(By.XPATH, var.emsochat_thongtinvedoanchat).click()
        driver.find_element(By.XPATH, var.emsochat_xemtinnhandaghim).click()
        time.sleep(1)
        check_tinnhandaghim = driver.find_element(By.XPATH,var.check_tinnhandaghim1).text
        print(check_tinnhandaghim)
        logging.info("Trang chủ - Chat - tuỳ chon - tin nhắn đã ghim")
        logging.info("check font-end: đang ở popup - Tin nhắn đã ghim")
        logging.info(check_tinnhandaghim == "Tin nhắn đã ghim")
        driver.find_element(By.XPATH, var.emsochat_xemtinnhandaghim_x).click()

        # # Tuỳ chỉnh đoạn chat
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat).click()
        #màu hồng tìm
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_doichude).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_doichude_mauhongtim).click()
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        check_mauchude = driver.find_element(By.XPATH,var.check_mauchude1).text
        print(check_mauchude)
        logging.info("Trang chủ - Chat - tuỳ chon - Màu chủ đề")
        logging.info("check font-end: Bạn đã đổi chủ đề thành Tuổi thơ.")
        logging.info(check_mauchude == "Bạn đã đổi chủ đề thành Tuổi thơ.")

        # màu mặc định
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat).click()
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_doichude).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_doichude_maumacdinh).click()
        driver.find_element(By.XPATH, var.luu).click()
        check_mauchude2 = driver.find_element(By.XPATH,var.check_mauchude2).text
        print(check_mauchude2)
        logging.info("Trang chủ - Chat - tuỳ chon - Màu chủ đề")
        logging.info(check_mauchude2)
        logging.info("check font-end: Bạn đã đổi chủ đề thành Mặc định.")
        logging.info(check_mauchude2 == "Bạn đã đổi chủ đề thành Mặc định.")

        #Biểu tượng cảm xúc
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_thaydoibieutuongcamxuc).click()
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_thaydoibieutuongcamxuc_iconthu6).click()
        time.sleep(1)
        check_bieutuongcamxuc1 = driver.find_element(By.XPATH,var.check_bieutuongcamxucthaydoi).text
        print(check_bieutuongcamxuc1)
        logging.info("Trang chủ - Chat - tuỳ chon - Cảm xúc nhanh")
        logging.info("check font-end: Bạn đã đặt cảm xúc nhanh thành 😱.")
        logging.info(check_bieutuongcamxuc1 == "Bạn đã đặt cảm xúc nhanh thành 😱.")

        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_thaydoibieutuongcamxuc).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_thaydoibieutuongcamxuc_macdinh).click()
        time.sleep(1)
        check_bieutuongcamxuc2 = driver.find_element(By.XPATH,var.check_bieutuongcamxucmacdinh).text
        print(check_bieutuongcamxuc2)
        logging.info("Trang chủ - Chat - tuỳ chon - Cảm xúc nhanh")
        logging.info("check font-end: Bạn đã gỡ biểu tượng cảm xúc nhanh.")
        logging.info(check_bieutuongcamxuc2)
        logging.info(check_bieutuongcamxuc2 == "Bạn đã gỡ biểu tượng cảm xúc nhanh.")
        time.sleep(2)

        #File phương tiện và file liên kết
        driver.find_element(By.XPATH, var.emsochat_file).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_anh).click()
        time.sleep(1.5)
        try:
            check_filephuongtien_anh = driver.find_element(By.XPATH, var.check_filephuongtien_anh1).is_displayed()
            print(check_filephuongtien_anh)
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có ảnh trong file phương tiện hay không")
            logging.info(check_filephuongtien_anh)
        except NoSuchElementException:
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có ảnh trong file phương tiện hay không")
            logging.info("False")

        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_video).click()
        time.sleep(1.5)
        try:
            check_filephuongtien_video = driver.find_element(By.XPATH, var.check_filephuongtien_video1).is_displayed()
            print(check_filephuongtien_video)
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có video trong file phương tiện hay không")
            logging.info(check_filephuongtien_video)
        except NoSuchElementException:
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có video trong file phương tiện hay không")
            logging.info("False")

        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_file).click()
        time.sleep(1)
        try:
            check_filephuongtien_file = driver.find_element(By.XPATH, var.check_filephuongtien_file1).is_displayed()
            print(check_filephuongtien_file)
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có file trong file phương tiện hay không")
            logging.info(check_filephuongtien_file)
        except NoSuchElementException:
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có file trong file phương tiện hay không")
            logging.info("False")

        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_lienket).click()
        time.sleep(1)
        try:
            check_filephuongtien_lienket = driver.find_element(By.XPATH, var.check_filephuongtien_lienket1).is_displayed()
            print(check_filephuongtien_lienket)
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có liên kết trong file phương tiện hay không")
            logging.info(check_filephuongtien_lienket)
        except NoSuchElementException:
            logging.info("Trang chủ - Chat - tuỳ chon - File phương tiện")
            logging.info("check font-end: Có liên kết trong file phương tiện hay không")
            logging.info("False")
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_back).click()
        time.sleep(2)

        # Quyền riêng tư & hỗ trợ
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro).click()
        #Tắt thông báo
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_tatthongbao).click()
        check_batthongbao_tuychon = driver.find_element(By.XPATH,var.check_batthongbao_tuychon1).text
        check_batthongbao_quyenriengtu = driver.find_element(By.XPATH, var.check_batthongbao_quyenriengtu1).text
        print(check_batthongbao_tuychon)
        print(check_batthongbao_quyenriengtu)
        logging.info("Trang chủ - Chat - tuỳ chon - Thông báo")
        logging.info("check font-end: Thông báo(tuỳ chọn) - " + check_batthongbao_tuychon)
        logging.info("check font-end: Thông báo quyền riêng tư - " + check_batthongbao_quyenriengtu)
        logging.info(check_batthongbao_tuychon == check_batthongbao_quyenriengtu)
        time.sleep(1)

        #Bật thông báo
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_batthongbao).click()
        time.sleep(2)
        check_tatthongbao_tuychon = driver.find_element(By.XPATH,var.check_tatthongthongbao_tuychon1).text
        check_tatthongbao_quyenriengtu = driver.find_element(By.XPATH, var.check_tatthongbao_quyenriengtu1).text
        print(check_tatthongbao_tuychon)
        print(check_tatthongbao_quyenriengtu)
        logging.info("Trang chủ - Chat - tuỳ chon - Thông báo")
        logging.info("check font-end: Thông báo(tuỳ chọn) - " + check_batthongbao_tuychon)
        logging.info("check font-end: Thông báo quyền riêng tư - " + check_batthongbao_quyenriengtu)
        logging.info(check_tatthongbao_tuychon == check_tatthongbao_quyenriengtu)

        #Chặn
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_chan).click()
        check_chan_ngocmai = driver.find_element(By.XPATH, var.check_chan_ngocmai1).text
        print(check_chan_ngocmai)
        logging.info("Trang chủ - Chat - tuỳ chon - Chặn")
        logging.info("check font-end: popup - Chặn Ngọc Mai")
        logging.info(check_chan_ngocmai == "Chặn Ngọc Mai")
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_chan_xacnhan).click()
        time.sleep(1)
        check_chan_ngocmai_dachan = driver.find_element(By.XPATH, var.check_chan_ngocmai_dachan).text
        print(check_chan_ngocmai_dachan)
        logging.info("Trang chủ - Chat - tuỳ chon - Chặn")
        logging.info("check font-end: Bạn đã chặn Ngọc Mai")
        logging.info(check_chan_ngocmai_dachan == "Bạn đã chặn Ngọc Mai")

        #Bỏ chặn
        # driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_bochan1).click()
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_bochan2).click()
        driver.find_element(By.XPATH, var.emsochat_quuyenriengtuhotro_chan_xacnhan).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)


    def taonhom(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.get("https://sn.emso.vn/messages/111169896815147328111169900882891225")
        driver.find_element(By.XPATH, var.trangchu_emsochat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_icontaotinnhanmoi).click()

        #Chọn Ngọc Mai lần 1 đê xoá
        driver.find_element(By.XPATH, var.tinnhanmoi_den).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).send_keys(data['trangchu_tinnhan']['den'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.tinnhanmoi_den_ngocmai)))
        element.click()
        time.sleep(1)
        #Chọn hue nguyen lần 1 đê xoá
        driver.find_element(By.XPATH, var.tinnhanmoi_den).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).send_keys(data['trangchu_tinnhan']['den1'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.tinnhanmoi_den_huenguyen)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_icontaotinnhanmoi_x).click()
        time.sleep(1)

        #Chọn Ngọc Mai lần 2
        driver.find_element(By.XPATH, var.emsochat_icontaotinnhanmoi).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).send_keys(data['trangchu_tinnhan']['den'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.tinnhanmoi_den_ngocmai)))
        element.click()
        time.sleep(1)
        #Chọn hue nguyen lần 2
        driver.find_element(By.XPATH, var.tinnhanmoi_den).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).send_keys(data['trangchu_tinnhan']['den1'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.tinnhanmoi_den_huenguyen)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tinnhanmoi_input).send_keys(data['trangchu_tinnhan']['tinnhanmoi_input'])
        driver.find_element(By.XPATH, var.tinnhanmoi_input).send_keys(Keys.ENTER)
        time.sleep(2)
        check_tinnhanmoi_taonhom = driver.find_element(By.XPATH, var.check_tinnhanmoi_taonhom1).text
        logging.info("Chat - icon tạo tin nhắn mới - Tạo nhóm")
        logging.info("check font-end: đã tạo nhóm -  Mai, nguyen")
        logging.info(check_tinnhanmoi_taonhom == "Mai, nguyen")

        #Tùy chọn nhóm
        actions = ActionChains(driver)
        hover_hopchat = driver.find_element(By.XPATH, var.hover_hopchat1)
        actions.move_to_element(hover_hopchat).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        #Đánh dáu là chưa đọc

        driver.find_element(By.XPATH, var.tuychonnhom_danhdaulachuadoc).click()
        time.sleep(1)
        element1 = driver.find_element(By.XPATH, var.check_color_mautennhom)
        color = element1.value_of_css_property("color")
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Đánh dấu là chưa đọc")
        logging.info(color)
        logging.info(color == "rgba(53, 120, 229, 1)")
        print(color)

        # Đánh dáu là đã đọc
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        driver.find_element(By.XPATH, var.tuychonnhom_danhdauladadoc).click()
        time.sleep(1)
        element1 = driver.find_element(By.XPATH, var.check_color_mautennhom)
        color = element1.value_of_css_property("color")
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Đánh dấu là đã đọc")
        logging.info(color)
        logging.info(color == "rgba(101, 103, 107, 1)")
        print(color)

        #Ghim
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        driver.find_element(By.XPATH, var.tuychonnhom_ghim).click()
        time.sleep(1)
        try:
            check_nhomcaidat_ghim = driver.find_element(By.XPATH, var.check_nhomcaidat_ghim1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Ghim - Có icon Ghim")
            logging.info(check_nhomcaidat_ghim)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Ghim - Có icon Ghim")
            logging.info("False")


        #Bỏ ghim
        hover_hopchat2 = driver.find_element(By.XPATH, var.hover_hopchat2)
        actions.move_to_element(hover_hopchat2).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tuychonnhom2).click()
        driver.find_element(By.XPATH, var.tuychonnhom_boghim).click()
        time.sleep(1)
        # try:
        #     check_nhomcaidat_ghim = driver.find_element(By.XPATH, var.check_nhomcaidat_ghim1).is_displayed()
        #     logging.info("Chat - Nhóm - Cài đặt nhóm")
        #     logging.info("check font-end: Bỏ Ghim - Không Có icon Ghim")
        #     logging.info("False")
        # except NoSuchElementException:
        #     logging.info("Chat - Nhóm - Cài đặt nhóm")
        #     logging.info("check font-end:Bỏ Ghim - Không Có icon Ghim")
        #     logging.info("True")

        #Tắt thông báo
        hover_hopchat = driver.find_element(By.XPATH, var.hover_hopchat1)
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        driver.find_element(By.XPATH, var.tuychonnhom_tatthongbao).click()
        time.sleep(1)
        try:
            check_nhomcaidat_tatthongbao = driver.find_element(By.XPATH, var.check_nhomcaidat_tatthongbao1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Tắt thông báo - có icon tắt thông báo")
            logging.info(check_nhomcaidat_tatthongbao)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Tắt thông báo - có icon tắt thông báo")
            logging.info("False")

        #Bật thông báo
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        check_nhomcaidat_batthongbao = driver.find_element(By.XPATH, var.check_nhomcaidat_batthongbao1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Bật thông báo")
        logging.info(check_nhomcaidat_batthongbao == "Bật thông báo")
        driver.find_element(By.XPATH, var.tuychonnhom_batthongbao).click()
        time.sleep(2)


        #Xoá đoạn chat
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        button = driver.find_element(By.XPATH, var.tuychonnhom_xoadoanchat)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        check_nhomcaidat_xoadoanchat = driver.find_element(By.XPATH, var.check_nhomcaidat_xoadoanchat1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Xoá đoạn chat message - Bạn không thể hoàn tác sau khi xoá bản sao của cuộc trò chuyện này.")
        logging.info(check_nhomcaidat_xoadoanchat == "Bạn không thể hoàn tác sau khi xoá bản sao của cuộc trò chuyện này.")
        driver.find_element(By.XPATH, var.xoa).click()
        time.sleep(2)

        # #Rời khỏi nhóm
        driver.find_element(By.XPATH, var.emsochat_icontaotinnhanmoi).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).send_keys(data['trangchu_tinnhan']['den'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.tinnhanmoi_den_ngocmai)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tinnhanmoi_den).click()
        driver.find_element(By.XPATH, var.tinnhanmoi_den).send_keys(data['trangchu_tinnhan']['den1'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.tinnhanmoi_den_huenguyen)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tinnhanmoi_input).send_keys(data['trangchu_tinnhan']['tinnhanmoi_input'])
        driver.find_element(By.XPATH, var.tinnhanmoi_input).send_keys(Keys.ENTER)
        time.sleep(2)
        #Message rời khỏi nhóm
        hover_hopchat = driver.find_element(By.XPATH, var.hover_hopchat1)
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tuychonnhom_roikhoinhom1).click()
        time.sleep(1)
        check_popup_roikhoinhom = driver.find_element(By.XPATH, var.check_popup_roikhoinhom1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Popup Rời khỏi nhóm - Rời khỏi cuộc trò chuyện này ?")
        logging.info(check_popup_roikhoinhom == "Rời khỏi cuộc trò chuyện này ?")

        check_messagepopup_roikhoinhom = driver.find_element(By.XPATH, var.check_message_roikhoinhom1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Message POPUP - Rời khỏi nhóm -Bạn sẽ không nhận được tin nhắn từ cuộc trò chuyện này nữa và mọi người sẽ thấy bạn rời nhóm.")
        logging.info(check_messagepopup_roikhoinhom == "Bạn sẽ không nhận được tin nhắn từ cuộc trò chuyện này nữa và mọi người sẽ thấy bạn rời nhóm.")
        driver.find_element(By.XPATH, var.huy).click()
        time.sleep(1)
        actions.move_to_element(hover_hopchat).perform()
        driver.find_element(By.XPATH, var.tuychonnhom).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tuychonnhom_roikhoinhom1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.tuychonnhom_roikhoinhom1_ok).click()
        time.sleep(1)
        check_message_roikhoinhom_thatbai = driver.find_element(By.XPATH, var.check_message_roikhoinhom_thatbai1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Message Rời khỏi nhóm thất bại - Vui lòng chọn một quản trị viên mới trước khi rời khỏi nhóm.")
        logging.info(check_message_roikhoinhom_thatbai == "Vui lòng chọn một quản trị viên mới trước khi rời khỏi nhóm.")


    def thongtindoanchat_nhom(self):
        driver.implicitly_wait(3)
        # driver.get("https://sn.emso.vn/messages/87eCxffFhRbTx8Zs2")
        driver.find_element(By.XPATH, var.emsochat_caidathopthoai).click()
        time.sleep(1)
        #Thay ảnh
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat).click()
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat_thaydoidanh).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhmes1.exe")
        time.sleep(1)
        try:
            check_nhom_thayanh = driver.find_element(By.XPATH, var.check_nhom_thayanh1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thay ảnh - Thông báo - Bạn đã đổi ảnh đại diện nhóm.")
            logging.info(check_nhom_thayanh)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thay ảnh - Thông báo - Bạn đã đổi ảnh đại diện nhóm.")
            logging.info("False")

        #Tên cuộc trò chuyện
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat_tencuoctrochuyen).click()
        xoa = driver.find_element(By.XPATH, var.tencuoctrochuyen_input)
        xoa.send_keys(Keys.CONTROL, "a")
        #Tên nhóm có chưa ký tự đặc biệt
        driver.find_element(By.XPATH, var.tencuoctrochuyen_input).send_keys(data['trangchu_tinnhan']['dattennhom'])
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        check_nhom_doiten_sai = driver.find_element(By.XPATH, var.check_nhom_doiten_sai1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Nhập ký tự đặc biệt - Tên nhóm không được chứa kí tự đặc biệt.")
        logging.info(check_nhom_doiten_sai == "Tên nhóm không được chứa kí tự đặc biệt.")

        xoa = driver.find_element(By.XPATH, var.tencuoctrochuyen_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.tencuoctrochuyen_input).send_keys(data['trangchu_tinnhan']['dattennhom1'])
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        try:
            check_nhom_doitennhom = driver.find_element(By.XPATH, var.check_nhom_doitennhom1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Đổi tên nhóm - Bạn đã đặt tên nhóm là Bực mình.")
            logging.info(check_nhom_doitennhom)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Đổi tên nhóm - Bạn đã đặt tên nhóm là Bực mình.")
            logging.info("False")

        #Tuỳ chọn nhóm
        time.sleep(1)
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat_tuychonnhom).click()
        #Chỉ quản trị viên thêm thành viên mới
        button = driver.find_element(By.XPATH, var.tuychonnhom_chiquantrithemthanhvien)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        check_tuychonnhom_themthanhvienmoi_bat = driver.find_element(By.XPATH, var.check_tuychonnhom_themthanhvienmoi_bat1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Chỉ quản trị viên thêm thành viên mới - Bạn đã bật tính năng phê duyệt thành viên và chỉ có quản trị viên có thể thêm người mới vào nhóm.")
        logging.info(check_tuychonnhom_themthanhvienmoi_bat)
        logging.info(check_tuychonnhom_themthanhvienmoi_bat == "Bạn đã bật tính năng phê duyệt thành viên và chỉ có quản trị viên có thể thêm người mới vào nhóm.")

        button = driver.find_element(By.XPATH, var.tuychonnhom_chiquantrithemthanhvien)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        try:
            check_tuychonnhom_themthanhvienmoi_tat = driver.find_element(By.XPATH, var.check_tuychonnhom_themthanhvienmoi_tat1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Chỉ quản trị viên thêm thành viên mới - Bạn đã tắt tính năng phê duyệt thành viên và bất cứ ai đều có thể thêm người mới vào nhóm.")
            logging.info(check_tuychonnhom_themthanhvienmoi_tat)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Chỉ quản trị viên thêm thành viên mới - Bạn đã tắt tính năng phê duyệt thành viên và bất cứ ai đều có thể thêm người mới vào nhóm.")
            logging.info("False")
        time.sleep(1)


        #Chỉ quản trị viên có thể nhắn tin
        button = driver.find_element(By.XPATH, var.tuychonnhomchiquanchinhantin)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        try:
            check_tuychonnhom_quantricothenhan_bat = driver.find_element(By.XPATH, var.check_tuychonnhom_quantricothenhan_bat1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Chỉ quản trị viên có thể nhắn tin - Bạn chỉ cho phép quản trị viên gửi tin nhắn.")
            logging.info(check_tuychonnhom_quantricothenhan_bat)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Chỉ quản trị viên có thể nhắn tin - Bạn chỉ cho phép quản trị viên gửi tin nhắn.")
            logging.info("False")
        time.sleep(1)

        button = driver.find_element(By.XPATH, var.tuychonnhomchiquanchinhantin)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        try:
            check_tuychonnhom_quantricothenhan_tat = driver.find_element(By.XPATH, var.check_tuychonnhom_quantricothenhan_tat1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Chỉ quản trị viên có thể nhắn tin - Bạn cho phép tất cả mọi người gửi tin nhắn.")
            logging.info(check_tuychonnhom_quantricothenhan_tat)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Chỉ quản trị viên có thể nhắn tin - Bạn cho phép tất cả mọi người gửi tin nhắn.")
            logging.info("False")
        time.sleep(1)

        #Thành viên trong đoạn chat
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat_thanhvientrongdoanchat).click()
        #Thêm người
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_themnguoi).click()
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_themnguoi_input).send_keys(data['trangchu_tinnhan']['thanhvien_themnguoi'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.vuonglam)))
        element.click()
        driver.find_element(By.XPATH, var.them).click()
        time.sleep(1)
        try:
            check_thanhvientrongdoanchat_themnguoi = driver.find_element(By.XPATH, var.check_thanhvientrongdoanchat_themnguoi1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo thêm người - Bạn đã thêm Vương Lâm vào nhóm.")
            logging.info(check_thanhvientrongdoanchat_themnguoi)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo thêm người - Bạn đã thêm Vương Lâm vào nhóm.")
            logging.info("False")
        time.sleep(1)

        driver.execute_script("window.scrollBy(0,700)", "")

        #Xoá người
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham).click()
        time.sleep(1)
        button = driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham_xoa)
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham_xoa).click()
        time.sleep(1)
        try:
            check_thanhvientrongdoanchat_xoanguoi = driver.find_element(By.XPATH, var.check_thanhvientrongdoanchat_xoanguoi1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo xoá người - Bạn đã xóa Vương Lâm khỏi nhóm.")
            logging.info(check_thanhvientrongdoanchat_xoanguoi)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo xoá người - Bạn đã xóa Vương Lâm khỏi nhóm.")
            logging.info("False")
        time.sleep(1)


        #Chỉ định làm quản trị viên
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1).click()
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1_chidinhlamquantrivien).click()
        time.sleep(1)
        try:
            check_thanhvientrongdoanchat_chidinhlamqtv = driver.find_element(By.XPATH, var.check_thanhvientrongdoanchat_chidinhlamqtv1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo chỉ định làm quản trị viên - Bạn đã thêm Ngọc Mai làm quản trị viên.")
            logging.info(check_thanhvientrongdoanchat_chidinhlamqtv)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo chỉ định làm quản trị viên - Bạn đã thêm Ngọc Mai làm quản trị viên.")
            logging.info("False")
        time.sleep(1)

        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1_xoaquantrivien).click()
        time.sleep(1)
        try:
            check_thanhvientrongdoanchat_xoachidinhlamqtv = driver.find_element(By.XPATH, var.check_thanhvientrongdoanchat_xoachidinhlamqtv1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo xoá chỉ định làm quản trị viên - Bạn đã gỡ quyền quản trị viên của Ngọc Mai.")
            logging.info(check_thanhvientrongdoanchat_xoachidinhlamqtv)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Thông báo xoá chỉ định làm quản trị viên - Bạn đã gỡ quyền quản trị viên của Ngọc Mai.")
            logging.info("False")
        time.sleep(1)
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1_chidinhlamquantrivien).click()
        time.sleep(1)
        #Tham gia bằng link nhóm
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1).click()
        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1_thamgiabanglinknhom).click()
        check_nhom_thamgiabanglink = driver.find_element(By.XPATH, var.check_nhom_thamgiabanglink1).text
        logging.info("Chat - Nhóm - Cài đặt nhóm")
        logging.info("check font-end: Popup Tham gia bằng link - Link tham gia nhóm")
        logging.info(check_nhom_thamgiabanglink == "Link tham gia nhóm")

        driver.find_element(By.XPATH, var.thanhvientrongdoanchat_icon3cham1_thamgiabanglinknhom_iconcoppy).click()
        time.sleep(1)
        try:
            check_nhom_thamgiabanglink_icon = driver.find_element(By.XPATH, var.check_nhom_thamgiabanglink_icon1).is_displayed()
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Popup Tham gia bằng link - Link tham gia nhóm - đã coppy")
            logging.info(check_nhom_thamgiabanglink_icon)
        except NoSuchElementException:
            logging.info("Chat - Nhóm - Cài đặt nhóm")
            logging.info("check font-end: Popup Tham gia bằng link - Link tham gia nhóm - đã coppy")
            logging.info("False")
        time.sleep(1)
        driver.back()
        time.sleep(0.5)
        driver.forward()
        time.sleep(1)

        #Đổi tên nhóm
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat).click()
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat_tencuoctrochuyen).click()
        xoa = driver.find_element(By.XPATH, var.tencuoctrochuyen_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.tencuoctrochuyen_input).send_keys(data['trangchu_tinnhan']['dattennhom3'])
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)

        #Quyền riêng tư & hỗ trợ
        driver.find_element(By.XPATH, var.nhom_caidathopthoai_tuychinhdoanchat_quyenriengtuvahotro).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quyenriengtuvahotro_roikhoinhom).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quyenriengtuvahotro_roikhoinhom_ok).click()
        time.sleep(2)






    def caidatcanhan_chuyentaikhoan(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        login.login4(self, "truongvck222@gmail.com", "atgmj123456")
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        driver.find_element(By.XPATH, var.caidatcanhan_chuyentaikhoankhac).click()
        driver.find_element(By.XPATH, var.caidatcanhan_chuyentaikhoankhac_tranquangtruong).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_password).send_keys("atgmj123456")
        driver.find_element(By.XPATH, var.login_nho_mat_khau).click()
        driver.find_element(By.XPATH, var.login_chon_tk_dang_nhap_gan_day_dang_nhap).click()
        time.sleep(3)
        check_chuyentaikhoan = driver.find_element(By.XPATH,var.check_chuyentaikhoan1).text
        print(check_chuyentaikhoan)
        logging.info("Trang chủ -Tài khoản - Chuyển tài khoản")
        logging.info("check font-end: Đã chuyển qua tài khoản - Trần Quang Trường")
        logging.info(check_chuyentaikhoan == "Trần Quang Trường")

    def caidatvaquyenriengtu_chung(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        driver.find_element(By.XPATH, var.caidatcanhan_caidatvaquyenriengtu).click()
        time.sleep(1.5)
        check_caidatvaquyenriengtu_chung = driver.find_element(By.XPATH,var.check_caidatvaquyenriengtu_chung1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư")
        logging.info("check font-end: Cài đặt")
        logging.info(check_caidatvaquyenriengtu_chung == "Cài đặt")

        #CHUNG
        #Tên
        driver.find_element(By.XPATH, var.chung_ten_chinhsua).click()
        check_chung_ten = driver.find_element(By.XPATH,var.check_chung_ten1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chung")
        logging.info("check font-end: Tên - Chỉnh sửa")
        logging.info(check_chung_ten == "Họ và tên")
        driver.find_element(By.XPATH, var.chung_ten_huy).click()
        time.sleep(0.5)
        #Tên người dùng
        driver.find_element(By.XPATH, var.chung_tennguoidung_chinhsua).click()
        check_chung_tennguoidung = driver.find_element(By.XPATH,var.check_chung_tennguoidung1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chung")
        logging.info("check font-end: Tên người dùng - Chỉnh sửa")
        logging.info(check_chung_tennguoidung == "Tên người dùng:")
        driver.find_element(By.XPATH, var.chung_ten_huy).click()
        time.sleep(0.5)
        #Số điện thoại
        driver.find_element(By.XPATH, var.chung_sodienthoai_chinhsua).click()
        check_chung_sodienthoai = driver.find_element(By.XPATH,var.check_chung_sodienthoai1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chung")
        logging.info("check font-end: Số điện thoại - Chỉnh sửa")
        logging.info(check_chung_sodienthoai == "Số điện thoại:")
        driver.find_element(By.XPATH, var.chung_ten_huy).click()
        time.sleep(0.5)
        #Xác nhận danh tính
        driver.find_element(By.XPATH, var.chung_xacnhandanhtinh_chinhsua).click()
        check_chung_xacnhandanhtinh = driver.find_element(By.XPATH,var.check_chung_xacnhandanhtinh1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chung")
        logging.info("check font-end: Xác nhận danh tính - Xem")
        logging.info(check_chung_xacnhandanhtinh == "Bật kiếm tiền")
        driver.back()
        time.sleep(0.5)
        #Liên hệ
        driver.find_element(By.XPATH, var.chung_lienhe_chinhsua).click()
        time.sleep(1)
        check_chung_lienhe = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chung")
        logging.info("check font-end: Liên hệ - Chỉnh sửa")
        logging.info("Chức năng chưa hoạt động")
        logging.info(check_chung_lienhe)
        logging.info("check font-end: message - " + check_chung_lienhe)
        logging.info(check_chung_lienhe == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)

    def caidatvaquyenriengtu_baomatvadangnhap(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        #BẢO MẬT VÀ ĐĂNG NHẬP
        driver.find_element(By.XPATH, var.baomatvadangnhap).click()
        #Đổi mật khẩu
        driver.find_element(By.XPATH, var.baomatvadangnhap_doimatkhau).click()
        check_baomatvadangnhap_doimatkhau = driver.find_element(By.XPATH,var.check_baomatvadangnhap_doimatkhau1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Đổi mật khẩu - Nhập mật khẩu cũ")
        logging.info(check_baomatvadangnhap_doimatkhau == "Nhập mật khẩu cũ")
        driver.find_element(By.XPATH, var.chung_ten_huy).click()
        time.sleep(0.5)
        #Lưu thông tin đăng nhập
        driver.find_element(By.XPATH, var.baomatvadangnhap_luuthongtindangnhap).click()
        time.sleep(1)
        check_baomatvadangnhap_luuthongtindangnhap = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Lưu thông tin đăng nhập của bạn - Chỉnh sửa")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_baomatvadangnhap_luuthongtindangnhap)
        logging.info(check_baomatvadangnhap_luuthongtindangnhap)
        logging.info(check_baomatvadangnhap_luuthongtindangnhap == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)
        #Dùng tính năng xác thực 2 yếu tố
        driver.find_element(By.XPATH, var.baomatvadangnhap_xacthuc2yeuto).click()
        time.sleep(1)
        check_baomatvadangnhap_xacthuc = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Dùng tính năng xác thực 2 yếu tố - Chỉnh sửa")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_baomatvadangnhap_xacthuc)
        logging.info(check_baomatvadangnhap_xacthuc)
        logging.info(check_baomatvadangnhap_xacthuc == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)
        #Đăng nhập hợp lệ
        driver.find_element(By.XPATH, var.baomatvadangnhap_dangnhaphople).click()
        time.sleep(1)
        check_baomatvadangnhap_dangnhaphople = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Đăng nhập hợp lệ - Xem")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_baomatvadangnhap_dangnhaphople)
        logging.info(check_baomatvadangnhap_dangnhaphople)
        logging.info(check_baomatvadangnhap_dangnhaphople == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)
        #Nhận cảnh báo về những lần đăng nhập lạ
        driver.find_element(By.XPATH, var.baomatvadangnhap_nhancanhbao).click()
        time.sleep(1)
        check_baomatvadangnhap_dangnhapla = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Nhận cảnh báo về những lần đăng nhập lạ - Chỉnh sửa")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_baomatvadangnhap_dangnhapla)
        logging.info(check_baomatvadangnhap_dangnhapla)
        logging.info(check_baomatvadangnhap_dangnhapla == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)
        #Mã hóa email thông báo
        driver.find_element(By.XPATH, var.baomatvadangnhap_mahoaemail).click()
        time.sleep(1)
        check_baomatvadangnhap_emailthongbao = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Mã hóa email thông báo - Chỉnh sửa")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_baomatvadangnhap_emailthongbao)
        logging.info(check_baomatvadangnhap_emailthongbao)
        logging.info(check_baomatvadangnhap_emailthongbao == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)
        #Xem email gần đây từ emso
        driver.find_element(By.XPATH, var.baomatvadangnhap_emailganday).click()
        time.sleep(1)
        check_baomatvadangnhap_xememailganday = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bảo mật và đăng nhập")
        logging.info("check font-end: Xem email gần đây từ emso - Xem")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_baomatvadangnhap_xememailganday)
        logging.info(check_baomatvadangnhap_xememailganday)
        logging.info(check_baomatvadangnhap_xememailganday == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(0.5)

    def caidatvaquyenriengtu_thongtinbantrenemso(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        #THÔNG TIN CỦA BẠN TRÊN EMSO
        driver.find_element(By.XPATH, var.thongtincuabantrenemso).click()
        #Truy cập thông tin của bạn
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_truycapthongtincuaban).click()
        time.sleep(1)
        check_thongtincuaban_truycapthongtin = driver.find_element(By.XPATH,var.tinhangdangphattrien).text
        print(check_thongtincuaban_truycapthongtin)
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bạn trên emso")
        logging.info("check font-end: Truy cập thông tin của bạn - Xem")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end: message - " + check_thongtincuaban_truycapthongtin)
        logging.info(check_thongtincuaban_truycapthongtin)
        logging.info(check_thongtincuaban_truycapthongtin == "Tính năng đang phát triển.Vui lòng thử lại sau!!")
        driver.find_element(By.XPATH, var.ok).click()
        time.sleep(1)
        #Nhật ký hoạt động
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_nhatkyhoatdong).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.baivietcuaban_lichsuxembaiviet).click()
        time.sleep(3)
        check_baivietcuaban_lichsuxembaiviet = driver.find_element(By.XPATH,var.check_baivietcuaban_lichsuxembaiviet1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Lịch sử xem bài viết")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_lichsuxembaiviet != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_lichsutimkiem).click()
        time.sleep(3)
        check_baivietcuaban_lichsutimkiem = driver.find_element(By.XPATH,var.check_baivietcuaban_lichsutimkiem1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Lịch sử tìm kiếm")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_lichsutimkiem != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_nhombandatimkiem).click()
        time.sleep(3)
        check_baivietcuaban_nhombandatimkiem = driver.find_element(By.XPATH,var.check_baivietcuaban_nhombandatimkiem1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Nhóm bạn đã tìm kiếm")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_nhombandatimkiem != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_trangluotthichsothich).click()
        time.sleep(3)
        check_baivietcuaban_trangluotthichsothich = driver.find_element(By.XPATH,var.check_baivietcuaban_trangluotthichsothich1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Trang, lượt thích Trang và sở thích")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_trangluotthichsothich != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_binhluan).click()
        time.sleep(3)
        check_baivietcuaban_binhluan = driver.find_element(By.XPATH,var.check_baivietcuaban_binhluan1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Bình luận")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_binhluan != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_luotthichvacamxuc).click()
        time.sleep(3)
        check_baivietcuaban_luotthichvacamxuc = driver.find_element(By.XPATH,var.check_baivietcuaban_luotthichvacamxuc1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Lượt thích và cảm xúc")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_luotthichvacamxuc != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_baivietluotcheckinanhvavideo).click()
        time.sleep(3)
        check_baivietcuaban_baivietluotcheckinanhvavideo = driver.find_element(By.XPATH,var.check_baivietcuaban_baivietluotcheckinanhvavideo1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Bài viết, lượt checkin, ảnh và video của bạn")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_baivietluotcheckinanhvavideo != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_baivietcuabantrendongthoigiannguoikhac).click()
        time.sleep(2)
        check_baivietcuaban_baivietcuabantrendongthoigiannguoikhac = driver.find_element(By.XPATH,var.check_baivietcuaban_baivietcuabantrendongthoigiannguoikhac1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Bài viết của bạn trên dòng thời gian của người khác")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_baivietcuabantrendongthoigiannguoikhac != None)
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_baivietnguoikhacdanglenfeedcuaban).click()
        time.sleep(2)
        check_baivietcuaban_baivietnguoikhacdanglenfeedcuaban = driver.find_element(By.XPATH,var.check_baivietcuaban_baivietnguoikhacdanglenfeedcuaban1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Bài viết người khác đăng lên bảng feed của bạn")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_baivietnguoikhacdanglenfeedcuaban != None)
        # driver.back()
        # driver.find_element(By.XPATH, var.baivietcuaban_livestream).click()       #ko load duoc trang
        # time.sleep(2)
        # check_baivietcuaban_livestream = driver.find_element(By.XPATH,var.check_baivietcuaban_livestream1).text
        # logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Livestream")
        # logging.info("Chức năng chưa hoạt động")
        # logging.info("check font-end:Có thông báo hay không ")
        # logging.info(check_baivietcuaban_livestream != "Không có dữ liệu!")
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_baivietvabinhluangantheban).click()
        time.sleep(2)
        check_baivietcuaban_baivietvabinhluangantheban = driver.find_element(By.XPATH,var.check_baivietcuaban_baivietvabinhluangantheban1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Bài viết và bình luận có gắn thẻ bạn")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_baivietvabinhluangantheban != "Không có dữ liệu!")
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_anhvavideocogantheban).click()
        time.sleep(2)
        check_baivietcuaban_anhvavideocogantheban = driver.find_element(By.XPATH,var.check_baivietcuaban_anhvavideocogantheban1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Ảnh và video có gắn thẻ bạn")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_anhvavideocogantheban != "Không có dữ liệu!")
        driver.back()
        #Hoạt động có gắn thẻ bạn
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_hoatdongcogantheban).click()
        time.sleep(2)
        driver.implicitly_wait(3)
        try:
            check_hoatdongcogantheban = driver.find_element(By.XPATH,var.check_hoatdongcogantheban1).is_displayed()
            logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Hoạt động có gắn thẻ bạn")
            logging.info("check font-end:Có thông báo hay không ")
            logging.info(check_hoatdongcogantheban)
        except NoSuchElementException:
            logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Hoạt động có gắn thẻ bạn")
            logging.info("check font-end:Có thông báo hay không ")
            logging.info("False")
        driver.implicitly_wait(15)

        #Bộ sưu tập và mục đã lưu
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_bosuutapvamucdaluu).click()
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_bosuutapvamucdaluu_mucbandaluu).click()
        check_mucbandaluu = driver.find_element(By.XPATH,var.check_mucbandaluu1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bộ sưu tập và mục đã lưu")
        logging.info("check font-end:Mục bạn đã lưu - Có thông báo hay không ")
        logging.info(check_mucbandaluu != "Không có dữ liệu!")
        time.sleep(1)

        driver.find_element(By.XPATH, var.thongtincuabantrenemso_bosuutapvamucdaluu_bosuutap).click()
        check_bosuutap = driver.find_element(By.XPATH,var.check_bosuutap1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bộ sưu tập và mục đã lưu")
        logging.info("check font-end:Bộ sưu tập Có thông báo hay không ")
        logging.info(check_bosuutap != "Không có dữ liệu!")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_bosuutapvamucdaluu).click()
        time.sleep(1)

        #Trang
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_trang).click()
        time.sleep(2)
        check_trang = driver.find_element(By.XPATH,var.check_trang1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Trang")
        logging.info("check font-end:Trang Có thông báo hay không ")
        logging.info(check_trang != "Không có dữ liệu!")
        time.sleep(1)

        #các chức năng khác
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_nhomsukienthuocphim).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Nhóm, sự kiện và thước phim")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_thongtintrentrangcanhan).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Thông tin trên trang cá nhân")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_quanheketnoi).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Quan hệ kết nối")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_hoatdongdaghilaivahoatdongkhac).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Hoạt động đã ghi lại và hoạt động khác")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_kholuutru).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Kho lưu trữ")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_thungrac).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Thùng rác")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_lichsuhoatdong).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Lịch sử hoạt động")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_xemlaidongthoigianvanhthe).click()
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Xem lại dòng thời gian và ảnh thẻ")
        logging.info("Chức năng chưa hoạt động")
        time.sleep(1)
        driver.get("https://sn.emso.vn/settings/information")
        time.sleep(2)
        #Vô hiẹu hoá tài khoản
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_vohieuhoataikhoan).click()
        time.sleep(0.5)
        check_vohieuquataikhoan = driver.find_element(By.XPATH,var.check_vohieuquataikhoan1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Vô hiệu hóa tài khoản")
        logging.info("check font-end: popup - Vô hiệu hóa tài khoản Emso")
        logging.info(check_vohieuquataikhoan == "Vô hiệu hóa tài khoản Emso")
        driver.find_element(By.XPATH, var.huy).click()
        time.sleep(1)
        #Quản lý thông tin của bạn
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_quanlythongtincuaban).click()
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0,1000)", "")
        time.sleep(2)
        driver.back()
        time.sleep(1)

    def caidatvaquyenriengtu_trangcanhanvaganthe(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        #TRANG CÁ NHÂN VÀ GẮN THẺ
        #Trang cá nhân
        driver.find_element(By.XPATH, var.trangcanhanvaganthe).click()
        #Ai có thể đăng lên trang cá nhân của bạn?
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_1).click()
        driver.find_element(By.XPATH, var.trangcanhan_x).click()
        time.sleep(0.5)
        #Ai có thể xem những gì người khác đăng lên trang cá nhân của bạn?
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_2).click()
        driver.find_element(By.XPATH, var.trangcanhan_x).click()
        time.sleep(0.5)
        #Ẩn bình luận chứa một số từ nhất định khỏi trang của bạn
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_3).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_3).click()
        time.sleep(0.5)
        #Găn thẻ
        # Ai có thể xem bài viết có gắn thẻ bạn trên trang cá nhân của bạn?
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_4).click()
        driver.find_element(By.XPATH, var.trangcanhan_x).click()
        time.sleep(0.5)
        # Khi bạn được gắn thẻ trong một bài viết, bạn muốn thêm ai vào đối tượng của bài viết nếu họ chưa thể nhìn thấy bài viết?
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_5).click()
        driver.find_element(By.XPATH, var.trangcanhan_x).click()
        time.sleep(0.5)
        #Xem lại
        #Xét duyệt bài viết có gắn thẻ bạn trước khi bài viết đó xuất hiện trên trang cá nhân của bạn
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_6).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_6).click()
        time.sleep(0.5)
        #Xem lại thẻ mọi người thêm vào bài viết của bạn trước khi thẻ xuất hiện trên EMSO?
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_7).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.trangcanhanvaganthe_7).click()
        time.sleep(0.5)

    def caidatvaquyenriengtu_baivietcongkhai(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        #BÀI VIẾT CÔNG KHAI
        driver.find_element(By.XPATH, var.baivietcongkhai).click()
        #Ai có thể theo dõi tôi
        driver.find_element(By.XPATH, var.baivietcongkhai_aicothetheodoitoi).click()
        driver.find_element(By.XPATH, var.baivietcongkhai_x).click()
        time.sleep(1)
        #Bình luận về bài viết công khai
        driver.find_element(By.XPATH, var.baivietcongkhai_binhluanvebaivietcongkhai).click()
        driver.find_element(By.XPATH, var.baivietcongkhai_x).click()
        time.sleep(1)
        #Thông báo về bài viết công khai
        driver.find_element(By.XPATH, var.baivietcongkhai_thongbaovebaivietcongkhai).click()
        driver.find_element(By.XPATH, var.baivietcongkhai_x).click()
        time.sleep(1)
        #Thông báo công khai trên trang cá nhân
        driver.find_element(By.XPATH, var.baivietcongkhai_thongbaocongkhaitrentrangcanhan).click()
        driver.find_element(By.XPATH, var.baivietcongkhai_x).click()
        time.sleep(1)
        #Bản xem trước ngoài Emso
        driver.find_element(By.XPATH, var.baivietcongkhai_banxemtruocngoaiemsso).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.baivietcongkhai_banxemtruocngoaiemsso).click()
        time.sleep(1)
        #Hiển thị bình luận phù hợp nhất trước tiên
        driver.find_element(By.XPATH, var.baivietcongkhai_hienthiphuhoptruoctien).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.baivietcongkhai_hienthiphuhoptruoctien).click()
        time.sleep(1)
        #Tên người dùng
        driver.find_element(By.XPATH, var.baivietcongkhai_tennguoidung).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.huy).click()
        time.sleep(1)

    def caidatvaquyenriengtu_chan(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        #CHẶN
        driver.find_element(By.XPATH, var.chan).click()
        #Chặn ngưoi dùng
        driver.find_element(By.XPATH, var.chan_channguoidung).click()
        time.sleep(0.5)
        check_channguoidung = driver.find_element(By.XPATH,var.check_channguoidung1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chặn - Chặn người dùng")
        logging.info("check font-end: Chặn người dùng - chức năng có hoạt động không ")
        logging.info(check_channguoidung)
        logging.info(check_channguoidung == "Bạn đã chặn 1 người")
        driver.find_element(By.XPATH, var.chan_themvaodanhsach).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1)
        #Chặn tin nhắn
        driver.find_element(By.XPATH, var.chan_tinhan).click()
        time.sleep(0.5)
        check_chantinnhan = driver.find_element(By.XPATH,var.check_chantinnhan1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chặn - Chặn người dùng")
        logging.info("check font-end: Chặn tin nhắn - chức năng có hoạt động không ")
        logging.info(check_chantinnhan)
        logging.info(check_chantinnhan == "Bạn đã chặn 1 người")
        driver.find_element(By.XPATH, var.chan_themvaodanhsach).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1)
        #Chặn trang
        driver.find_element(By.XPATH, var.chan_trang).click()
        time.sleep(0.5)
        check_chantrang = driver.find_element(By.XPATH,var.check_chantrang1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Chặn - Chặn người dùng")
        logging.info("check font-end: Chặn trang - chức năng có hoạt động không ")
        logging.info(check_chantrang)
        logging.info(check_chantrang == "Bạn đã chặn 1 trang")
        driver.find_element(By.XPATH, var.chan_themvaodanhsach).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1)

    def caidatvaquyenriengtu_batkiemtien(self):
        driver.implicitly_wait(15)
        time.sleep(1)
        #BẬT KIẾM TIỀN
        driver.find_element(By.XPATH, var.batkiemtien).click()
        #Trần Quang Trường
        driver.find_element(By.XPATH, var.batkiemtien_timkiem).send_keys("Trần Quang Trường")
        time.sleep(2)
        driver.find_element(By.XPATH, var.batkiemtien_xacminhdanhtinh).click()
        time.sleep(1)
        check_xacminhdanhtinh = driver.find_element(By.XPATH,var.check_xacminhdanhtinh1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Bật kiếm tiền")
        logging.info("check font-end: popup - Xác minh danh tính")
        logging.info(check_xacminhdanhtinh == "Xác minh danh tính")
        driver.find_element(By.XPATH, var.xacminhdanhtinh_cccdmattruoc).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia1.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.xacminhdanhtinh_cccdmatsau).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia2.exe")
        driver.find_element(By.XPATH, var.xacminhdanhtinh_video).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/quangaygiongbao.exe")
        time.sleep(3)
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(2)

        #Trường test bản tin
        driver.find_element(By.XPATH, var.batkiemtien_timkiem).click()
        imput = driver.find_element(By.XPATH, var.batkiemtien_timkiem)
        imput.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.batkiemtien_timkiem).send_keys("Trường")
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.batkiemtien_truongtestbantin).click()
        driver.find_element(By.XPATH, var.batkiemtien_xacminhdanhtinh).click()
        driver.find_element(By.XPATH, var.xacminhdanhtinh_GPKDKD).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia1.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.xacminhdanhtinh_masothue).send_keys(data['trangchu_banthan']['masothue'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.xacminhdanhtinh_tenchudoanhnghiep).send_keys(data['trangchu_banthan']['tenchudoanhnghiep'])
        time.sleep(2)
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)

    def trogiupvahotro_sudungemso(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        driver.find_element(By.XPATH, var.caidatcanhan_trogiupvahotro).click()
        time.sleep(2)

        #Sử dụng emso
        driver.find_element(By.XPATH, var.sudungemso).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan1).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan1).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan2).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan2).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan3).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan3).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan4).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan4).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan5).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan5).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan6).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_taotaikhoan6).click()

        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_xacnhantaikhoan1).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_xacnhantaikhoan1).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_xacnhantaikhoan2).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_xacnhantaikhoan2).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_xacnhantaikhoan3).click()
        driver.find_element(By.XPATH, var.sudungemso_cachtaotaikhoan_xacnhantaikhoan3).click()

        #Trang cá nhân của bạn
        #Thêm và chỉnh sửa thông tin trên trang cá nhân của bạn
        driver.find_element(By.XPATH, var.trangcanhancuaban).click()
        driver.find_element(By.XPATH, var.trangcanhancuaban_themvachinhsuatrentrangcanhan).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban1).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban1).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban2).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban2).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban3).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban3).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban4).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban4).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban5).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_thongtincoban5).click()

        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren1).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren1).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren2).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren2).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren3).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren3).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren4).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren4).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren5).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren5).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren6).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren6).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren7).click()
        driver.find_element(By.XPATH, var.themvachinhsuatrentrangcanhan_gioithieutren7).click()

        #Ảnh đại diện và ảnh bìa của bạn
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_1).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_1).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_2).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_2).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_3).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_3).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_4).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_4).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_5).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_5).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_6).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_6).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_7).click()
        driver.find_element(By.XPATH, var.anhdaidienvanhbiacuaban_7).click()

        #Chia sẻ và quản lý bài viết trên trang cá nhân
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_1).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_1).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_2).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_2).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_3).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_3).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_4).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_4).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_5).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_5).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_6).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_6).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_7).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_7).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_8).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_8).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_9).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_9).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_10).click()
        driver.find_element(By.XPATH, var.chiasevaquanlybaiviet_10).click()

        #Khắc phục sự cố
        driver.find_element(By.XPATH, var.khacphucsuco).click()
        driver.find_element(By.XPATH, var.khacphucsuco_1).click()
        driver.find_element(By.XPATH, var.khacphucsuco_1).click()
        driver.find_element(By.XPATH, var.khacphucsuco_2).click()
        driver.find_element(By.XPATH, var.khacphucsuco_2).click()
        driver.find_element(By.XPATH, var.khacphucsuco_3).click()
        driver.find_element(By.XPATH, var.khacphucsuco_3).click()
        driver.find_element(By.XPATH, var.khacphucsuco_4).click()
        driver.find_element(By.XPATH, var.khacphucsuco_4).click()
        driver.find_element(By.XPATH, var.khacphucsuco_5).click()
        driver.find_element(By.XPATH, var.khacphucsuco_5).click()
        driver.find_element(By.XPATH, var.khacphucsuco_6).click()
        driver.find_element(By.XPATH, var.khacphucsuco_6).click()
        driver.find_element(By.XPATH, var.khacphucsuco_7).click()
        driver.find_element(By.XPATH, var.khacphucsuco_7).click()
        driver.find_element(By.XPATH, var.khacphucsuco_8).click()
        driver.find_element(By.XPATH, var.khacphucsuco_8).click()
        driver.find_element(By.XPATH, var.khacphucsuco_9).click()
        driver.find_element(By.XPATH, var.khacphucsuco_9).click()
        driver.find_element(By.XPATH, var.khacphucsuco_10).click()
        driver.find_element(By.XPATH, var.khacphucsuco_10).click()

        #Thêm bạn bè
        driver.find_element(By.XPATH, var.sudungemsso_thembanbe).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_thembanbe_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_thembanbe_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_thembanbe_3).click()
        driver.find_element(By.XPATH, var.sudungemsso_thembanbe_4).click()

        #Trang chủ của bạn
        driver.find_element(By.XPATH, var.sudungemsso_trangchucuaban).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_trangchucuaban_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_trangchucuaban_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_trangchucuaban_3).click()
        driver.find_element(By.XPATH, var.sudungemsso_trangchucuaban_4).click()
        driver.find_element(By.XPATH, var.sudungemsso_trangchucuaban_5).click()

        #Nhắn tin
        driver.find_element(By.XPATH, var.sudungemsso_nhantin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_nhantin_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhantin_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhantin_3).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhantin_4).click()

        #Ảnh và video
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo_3).click()
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo_4).click()
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo_5).click()
        driver.find_element(By.XPATH, var.sudungemsso_anhvavideo_6).click()

        #Video trên watch
        driver.find_element(By.XPATH, var.sudungemsso_videotrenwatch).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_videotrenwatch_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_videotrenwatch_2).click()

        #VTrang
        cuon = driver.find_element(By.XPATH, var.sudungemsso_trang_9)
        driver.execute_script("arguments[0].scrollIntoView();", cuon)

        driver.find_element(By.XPATH, var.sudungemsso_trang).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_trang_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_3).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_4).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_5).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_6).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_7).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_8).click()
        driver.find_element(By.XPATH, var.sudungemsso_trang_9).click()

        #VNhóm
        driver.find_element(By.XPATH, var.sudungemsso_nhom).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_nhom_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhom_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhom_3).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhom_4).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhom_5).click()
        driver.find_element(By.XPATH, var.sudungemsso_nhom_6).click()

        #Sự kiện
        driver.find_element(By.XPATH, var.sudungemsso_sukien).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_sukien_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_sukien_2).click()
        driver.find_element(By.XPATH, var.sudungemsso_sukien_3).click()

        #Úng dụng Emso trên di động
        driver.find_element(By.XPATH, var.sudungemsso_emsotrendidong).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.sudungemsso_emsotrendidong_1).click()
        driver.find_element(By.XPATH, var.sudungemsso_emsotrendidong_2).click()

        #Trợ năng
        driver.find_element(By.XPATH, var.sudungemsso_tronang).click()
        time.sleep(1)

        #QUẢN LÝ TÀI KHOẢN
        driver.find_element(By.XPATH, var.quanlytaikhoan).click()
        time.sleep(1)
        #đăng nhập và mật khẩu
        driver.find_element(By.XPATH, var.quanlytaikhoan_dangnhapvamatkhau).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_dangnhapvamatkhau_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_dangnhapvamatkhau_2).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_dangnhapvamatkhau_3).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_dangnhapvamatkhau_4).click()

        #cài đặt tài khoản
        driver.find_element(By.XPATH, var.quanlytaikhoan_caidattaikhoan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quanlytaikhoan_caidattaikhoan_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_caidattaikhoan_2).click()

        #Thông báo
        driver.find_element(By.XPATH, var.quanlytaikhoan_thongbao).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quanlytaikhoan_thongbao_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_thongbao_2).click()

        #Vô hiệu hoá hoặc xoá tài khoản của bạn
        driver.find_element(By.XPATH, var.quanlytaikhoan_vohieuhoahoacxoataikhoan).click()
        time.sleep(1)

        #QUYỀN RIÊNG TƯ AN TOÀN VÀ BẢO MẬT
        driver.find_element(By.XPATH, var.quyenriengtuantoanbaomat).click()
        time.sleep(1)
        #Quyền riêng tư của bạn
        driver.find_element(By.XPATH, var.quanlytaikhoan_quyenriengtucuaban).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quanlytaikhoan_quyenriengtucuaban_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_quyenriengtucuaban_2).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_quyenriengtucuaban_3).click()

        #Giữ an toàn
        driver.find_element(By.XPATH, var.quanlytaikhoan_giuantoan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quanlytaikhoan_giuantoan_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_giuantoan_2).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_giuantoan_3).click()

        #Duy trì tính bảo mật cho tài khoản của bạn
        driver.find_element(By.XPATH, var.quanlytaikhoan_duytribaomat).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.quanlytaikhoan_duytribaomat_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_duytribaomat_2).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_duytribaomat_3).click()

        #An toàn khi mua sắm
        driver.find_element(By.XPATH, var.quanlytaikhoan_antoankhimuasam).click()
        time.sleep(1)
        logging.info("Trợ giúp và hỗ trợ - Quyền riêng tư, an toàn và bảo mật - An toàn khi mua sắm")
        logging.info("Chức năng chưa hoạt động")
        driver.find_element(By.XPATH, var.quanlytaikhoan_antoankhimuasam_1).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_antoankhimuasam_2).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_antoankhimuasam_3).click()
        driver.find_element(By.XPATH, var.quanlytaikhoan_antoankhimuasam_4).click()
        time.sleep(1)

        #CHÍNH SÁCH VÀ BÁO CÁO
        driver.find_element(By.XPATH, var.chinhsachvabaocao).click()
        time.sleep(1)
        #Báo cáo lạm dụng
        driver.find_element(By.XPATH, var.chinhsachvabaocao_baocaolamdung).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.chinhsachvabaocao_baocaolamdung_1).click()
        driver.find_element(By.XPATH, var.chinhsachvabaocao_baocaolamdung_2).click()
        #Báo cáo sự cố với Emso
        driver.find_element(By.XPATH, var.chinhsachvabaocao_baocaosucovoiemso).click()
        #Báo cáo vi phạm quyền riêng tư
        driver.find_element(By.XPATH, var.chinhsachvabaocao_baocaoviphamquyenriengtu).click()
        #Tài khoản hack và tài khoản giả
        driver.find_element(By.XPATH, var.chinhsachvabaocao_taikhoanhackvataikhoangia).click()
        #Quyền sở hữu trí tuệ
        driver.find_element(By.XPATH, var.chinhsachvabaocao_quyensohuutritue).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.chinhsachvabaocao_quyensohuutritue_1).click()
        driver.find_element(By.XPATH, var.chinhsachvabaocao_quyensohuutritue_2).click()
        time.sleep(1)

        #ĐIỀU KHOAN VÀ CHÍNH SÁCH
        driver.find_element(By.XPATH, var.dieukhoanvachinhsach).click()
        #Điều khoản dịch vụ
        driver.find_element(By.XPATH, var.dieukhoanvachinhsach_dieukhoandichvu).click()
        time.sleep(0.5)
        #Chính sách riêng tư và tiêu chuẩn bảo mật
        driver.find_element(By.XPATH, var.dieukhoanvachinhsach_chinhsachriengtuvatieuchuanbaomat).click()
        time.sleep(0.5)
        #Tiêu chuẩn cộng đồng
        driver.find_element(By.XPATH, var.dieukhoanvachinhsach_tieuchuancongdong).click()
        time.sleep(0.5)
        #Chính sách quảng cáo
        driver.find_element(By.XPATH, var.dieukhoanvachinhsach_chinhsachquangcao).click()
        time.sleep(0.5)
        #Báo cáo khiếu nại
        driver.find_element(By.XPATH, var.dieukhoanvachinhsach_baobaokhieunai).click()
        time.sleep(1)

        #ĐIỀU KHOẢN VÀ CHÍNH SÁCH RIÊNG
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng).click()
        #Tuyển dụng
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_tuyendung).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_tuyendung_1).click()
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_tuyendung_2).click()
        time.sleep(0.5)
        #Gọi vốn cộng đồng
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_goivoncongdong).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_goivoncongdong_1).click()
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_goivoncongdong_2).click()
        time.sleep(0.5)
        #Không gian âm nhạc
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianamnhac).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianamnhac_1).click()
        time.sleep(0.5)
        #Không gian học tập
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianhoctap).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianhoctap_1).click()
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianhoctap_2).click()
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianhoctap_3).click()
        time.sleep(0.5)
        #Không gian thương mại
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianthuongmai).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianthuongmai_1).click()
        driver.find_element(By.XPATH, var.dieukhoanvachinhsachrieng_khonggianthuongmai_2).click()
        logging.info("Trợ giúp và hỗ trợ - Điều khoản và chính sách riêng - Không gian thương mại - Thoả thuận dịch vụ chung không gian thương mại")
        logging.info("Chức năng chưa hoạt động")
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)

    def caidatcanhan_manhinh(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        driver.find_element(By.XPATH, var.caidatcanhan_manhinh).click()
        time.sleep(1)
        check_chedomanhinh = driver.find_element(By.XPATH,var.check_chedomanhinh1).text
        print(check_chedomanhinh)
        logging.info("Trang chủ - Tài Khoản - Màn hình")
        logging.info("check font-end: popup - Chế độ màn hình")
        logging.info(check_chedomanhinh == "Chế độ màn hình")
        driver.find_element(By.XPATH, var.caidatcanhan_manhinh_bat).click()
        time.sleep(2)
        check_bat = driver.find_element(By.XPATH, var.caidatcanhan_manhinh_bat)
        print("Có đang được bật không", check_bat.is_enabled())
        print("Có đang được chọn không", check_bat.is_selected())
        check_bat2 = driver.find_element(By.XPATH, var.caidatcanhan_manhinh_bat).is_enabled()
        logging.info("Màn hình tối có được chọn không?")
        logging.info(check_bat2)
        check_bat1 = driver.find_element(By.XPATH, var.caidatcanhan_manhinh_bat).is_selected()
        logging.info("Màn hình tối có được bật không?")
        logging.info(check_bat1)

        driver.find_element(By.XPATH, var.caidatcanhan_manhinhtudong).click()
        time.sleep(1)
        check_tudong1 = driver.find_element(By.XPATH, var.caidatcanhan_manhinhtudong).is_selected()
        logging.info("Màn hình tự động có được chọn không?")
        logging.info(check_tudong1)
        check_tudong2 = driver.find_element(By.XPATH, var.caidatcanhan_manhinhtudong).is_enabled()
        logging.info("Màn hình tự động có được bật không?")
        logging.info(check_tudong2)

        driver.find_element(By.XPATH, var.caidatcanhan_manhinh_tat).click()
        time.sleep(1)

        check_tat1 = driver.find_element(By.XPATH, var.caidatcanhan_manhinh_tat).is_selected()
        logging.info("Màn hình tối(tắt) có được chọn không?")
        logging.info(check_tat1)
        check_tat2 = driver.find_element(By.XPATH, var.caidatcanhan_manhinh_tat).is_enabled()
        logging.info("Màn hình tối(tắt) có được bật không?")
        logging.info(check_tat2)

        driver.find_element(By.XPATH, var.caidatcanhan_manhinh_iconquaylai).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        time.sleep(1)

    def caidatcanhan_donggopykien(self):
        driver.implicitly_wait(15)
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        driver.find_element(By.XPATH, var.caidatcanhan_donggopykien).click()
        time.sleep(1)
        #Chung tay cải thiện emso
        driver.find_element(By.XPATH, var.donggopykien_chungtaycaithienemso).click()
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chonsanpham).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chonsanpham_choigame).click()
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet).click()
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet).send_keys(data['trangchu_donggopykien']['chitiet'])
        time.sleep(1)
        button = driver.find_element(By.XPATH, var.chungtaycaithienemso_tailenfile)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia2.exe")
        time.sleep(1)
        check_gui2 = driver.find_element(By.XPATH, var.donggopykien_chungtaycaithienemso_buttongui).is_enabled()
        logging.info("Trang chủ - Tài khoản - Đóng góp ý kiến - Chung tay cải thiện EMSO")
        logging.info("Nút GỬI đang ở trạng thái bật không?")
        logging.info(check_gui2)
        time.sleep(1)
        driver.find_element(By.XPATH, var.chungtaycaithienemso_huy).click()
        time.sleep(2)

        #Đã xảy ra lỗi
        driver.find_element(By.XPATH, var.donggopykien_daxayraloi).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chonsanpha1).click()
        # driver.find_element(By.XPATH, var.chungtaycaithienemso_chonsanpham_chatdongdong).click()
        button = driver.find_element(By.XPATH, var.chungtaycaithienemso_chonsanpham_chatdongdong)
        driver.execute_script("arguments[0].click();", button)

        # driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet).click()
        button = driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet)
        driver.execute_script("arguments[0].click();", button)

        driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet).clear()
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet).send_keys(data['trangchu_donggopykien']['chitiet_daxayraloi'])
        time.sleep(1)
        button = driver.find_element(By.XPATH, var.chungtaycaithienemso_tailenfile)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia2.exe")
        time.sleep(2)
        check_gui2 = driver.find_element(By.XPATH, var.donggopykien_chungtaycaithienemso_buttongui).is_enabled()
        logging.info("Trang chủ - Tài khoản - Đóng góp ý kiến - Đã xảy ra lỗi")
        logging.info("Nút GỬI đang ở trạng thái bật không?")
        logging.info(check_gui2)
        time.sleep(1)
        driver.find_element(By.XPATH, var.chungtaycaithienemso_huy).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.caidatcanhan_donggopykien_x).click()
        time.sleep(2)

    def caidatcanhan_dangxuat(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.icon_caidatcanhan).click()
        driver.find_element(By.XPATH, var.caidatcanhan_dangxuat).click()
        time.sleep(1)
        check_dangxuat = driver.find_element(By.XPATH, var.check_dangxuat).text
        print(check_dangxuat)
        logging.info("Trang chủ - Tài khoản - Đăng xuất")
        logging.info(check_dangxuat == "Đăng nhập")
        login.login4(self, "truongvck33@gmail.com", "atgmj123456")
        time.sleep(2.5)

    def trangchu_timkiem(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu).click()
        driver.find_element(By.XPATH, var.trangchu_timkiem).click()
        driver.find_element(By.XPATH, var.trangchu_timkiem1).send_keys(data['trangchu_timkkiem']['timkiem'])
        driver.find_element(By.XPATH, var.trangchu_timkiem_nam).click()
        time.sleep(3)
        check_ketquatimkiem = driver.find_element(By.XPATH, var.check_ketquatimkiem1).text

        #tất cả
        check_timkiem_tatca = driver.find_element(By.XPATH,var.check_timkiem_tatca1).text
        logging.info("Trang chủ - Tìm kiếm - Tất cả")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc tất cả")
        logging.info(check_timkiem_tatca == "Duy Nam")

        #Mọi người
        driver.find_element(By.XPATH, var.trangchu_timkiem_moinguoi).click()
        time.sleep(2)
        check_timkiem_moinguoi = driver.find_element(By.XPATH,var.check_timkiem_moinguoi).text
        logging.info("Trang chủ - Tìm kiếm - Mọi người")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc mọi người")
        logging.info(check_timkiem_moinguoi == "Duy Nam")

        #Bài viết
        driver.find_element(By.XPATH, var.trangchu_timkiem_baiviet).click()
        time.sleep(2)
        check_timkiem_baiviet = driver.find_element(By.XPATH,var.check_timkiem_baiviet1).text
        logging.info("Trang chủ - Tìm kiếm - Bài viết")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc bài viết")
        logging.info(check_timkiem_baiviet == "Năm nay chắc phát tài lắm")

        #Nhóm
        driver.find_element(By.XPATH, var.trangchu_timkiem_nhom).click()
        time.sleep(2)
        check_timkiem_nhom = driver.find_element(By.XPATH,var.check_timkiem_nhom1).text
        logging.info("Trang chủ - Tìm kiếm - Nhóm")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Nhóm")
        logging.info(check_timkiem_nhom == "nam test")

        #Trang
        driver.find_element(By.XPATH, var.trangchu_timkiem_trang).click()
        time.sleep(2)
        check_timkiem_trang = driver.find_element(By.XPATH,var.check_timkiem_trang1).text
        logging.info("Trang chủ - Tìm kiếm - Trang")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Trang")
        logging.info(check_timkiem_trang == "THỜI TRANG NAM")

        #Sự kiện
        driver.find_element(By.XPATH, var.trangchu_timkiem_sukien).click()
        time.sleep(2)
        check_timkiem_sukien = driver.find_element(By.XPATH,var.check_timkiem_sukien1).text
        logging.info("Trang chủ - Tìm kiếm - Sự kiện")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Sự kiện")
        logging.info(check_timkiem_sukien == "Offline Fan Harry Potter 20 năm")

        #Gọi vốn
        driver.find_element(By.XPATH, var.trangchu_timkiem_goivon).click()
        time.sleep(2)
        check_timkiem_goivon = driver.find_element(By.XPATH,var.check_timkiem_goivon1).text
        logging.info("Trang chủ - Tìm kiếm - Gọi vốn")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Gọi vốn")
        logging.info(check_timkiem_goivon == "nam test tìm kiếm")

        #Tuyển dụng
        driver.find_element(By.XPATH, var.trangchu_timkiem_tuyendung).click()
        time.sleep(2)
        check_timkiem_tuyendung = driver.find_element(By.XPATH,var.check_timkiem_tuyendung1).text
        logging.info("Trang chủ - Tìm kiếm - Tuyển dụng")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Tuyển dụng")
        logging.info(check_timkiem_tuyendung == "tuyển nam")

        # #Khoá học
        driver.find_element(By.XPATH, var.trangchu_timkiem_khoahoc).click()     #không tim kiếm đợc khoá học
        time.sleep(2)
        check_timkiem_khoahoc = driver.find_element(By.XPATH,var.check_timkiem_khoahoc1).text
        logging.info("Trang chủ - Tìm kiếm - Khoá học")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Khoá học")
        logging.info(check_timkiem_khoahoc == "học nam")

        #San phẩm
        driver.find_element(By.XPATH, var.trangchu_timkiem_sanpham).click()
        time.sleep(2)

        driver.find_element(By.XPATH, var.timkiem_input).click()
        # driver.find_element(By.XPATH, var.timkiem_input).clear()
        xoa = driver.find_element(By.XPATH, var.timkiem_input1)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.timkiem_input1).send_keys("Áo polo nam")
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.timkiem_input1).send_keys(Keys.ENTER)
        time.sleep(2)

        check_timkiem_sanpham = driver.find_element(By.XPATH,var.check_timkiem_sanpham1).text
        logging.info("Trang chủ - Tìm kiếm - Sản phẩm")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Sản phẩm")
        logging.info(check_timkiem_sanpham)
        logging.info(check_timkiem_sanpham == "Áo polo nam")
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)



    # def youtobe(self):
    #     driver.implicitly_wait(15)
    #     time.sleep(1.5)
    #     driver.get("https://www.youtube.com/")
    #     time.sleep(2)
    #     driver.find_element(By.XPATH, "//*[@placeholder='Search']").send_keys("khoảnh khắc thu vị")
    #     driver.find_element(By.XPATH, "//*[@placeholder='Search']").submit()
    #     time.sleep(2)
    #     button = driver.find_element(By.XPATH, "//*[text()='Filters']")
    #     driver.execute_script("arguments[0].click();", button)
    #     time.sleep(1)
    #     # driver.find_element(By.XPATH, "//*[text()='Filters']").click()
    #     driver.find_element(By.XPATH, "//*[text()='Under 4 minutes']").click()
    #     time.sleep(3)
    #     danhsachvideo = driver.find_elements(By.XPATH, "//*[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail']")
    #     r = 0
    #     while r<1002:
    #         for video in danhsachvideo:
    #             r += 1
    #             link = video.get_attribute('href')
    #             writeData(var.linkvideo, "Sheet1", r, 1, link)
    #             print(link)
    #             driver.execute_script("window.scrollBy(0,300)", "")
    #             time.sleep(0.3)
    #         if  r ==1000:
    #             break



class khoanhkhac():
    def danhchoban(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        # driver.find_element(By.XPATH, var.icon_khoanhkhac).click()
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #đang theo dõi
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        time.sleep(3)
        try:
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        except:
            driver.refresh()
            time.sleep(1)
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        driver.find_element(By.XPATH, var.like).click()
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_thich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).send_keys(data['khoanhkhac']['binhluan'])
        driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_binhluan).submit()
        time.sleep(1)

        #chia se ngay
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiasengay).click()
        time.sleep(2)
        check_message_chiasengay = driver.find_element(By.XPATH,var.check_message_chiase).text
        print(check_message_chiasengay)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ ngay")
        logging.info("check font-end: Message - Chia sẻ bài viết thành công")
        logging.info(check_message_chiasengay == "Chia sẻ bài viết thành công")
        time.sleep(5)
        driver.get("https://sn.emso.vn/user/truongvck333")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,1100)", "")
        check_chiasengay_time = driver.find_element(By.XPATH,var.check_chiasengay1).text
        print(check_chiasengay_time)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ ngay")
        logging.info(check_chiasengay_time)
        logging.info("check font-end: Message - Check Thời gian trên trang cá nhân - Vài giây trước")
        logging.info(check_chiasengay_time == "Vài giây trước ")

        check_chiasengay_tieude = driver.find_element(By.XPATH,var.check_chiasengay_tieude1).text
        print(check_chiasengay_tieude)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ ngay")
        logging.info(check_chiasengay_tieude)
        logging.info("check font-end: Message - Check Tiêu đề trên trang cá nhân - Test khoảng khắc")
        logging.info(check_chiasengay_tieude == "Test khoảng khắc")
        time.sleep(1)

        #Tuỳ chọn bài viết
        #Ghim
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_gimbaiviet).click()
        time.sleep(1)
        check_tuychonbaiviet_chinhsuabaiviet_ghim = driver.find_element(By.XPATH,var.check_tuychonbaiviet_chinhsuabaiviet_ghim1).text
        print(check_tuychonbaiviet_chinhsuabaiviet_ghim)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Chỉnh sửa bài viết")
        logging.info("check font-end: Message Ghim - Đã ghim bài viết của bạn ")
        logging.info(check_tuychonbaiviet_chinhsuabaiviet_ghim == "Đã ghim bài viết của bạn")

        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon1).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_bogimbaiviet).click()
        time.sleep(1)
        check_tuychonbaiviet_chinhsuabaiviet_boghim = driver.find_element(By.XPATH,var.check_tuychonbaiviet_chinhsuabaiviet_boghim1).text
        print(check_tuychonbaiviet_chinhsuabaiviet_boghim)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Chỉnh sửa bài viết")
        logging.info("check font-end: Message Ghim - Đã bỏ ghim bài viết của bạn")
        logging.info(check_tuychonbaiviet_chinhsuabaiviet_boghim == "Đã bỏ ghim bài viết của bạn")
        time.sleep(1)

        #lưu bài viết
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_luubaiviet).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_luubaiviet_no1).click()
        driver.find_element(By.XPATH, var.xong).click()
        time.sleep(1)
        check_tuychonbaiviet_luubaiviet = driver.find_element(By.XPATH,var.check_tuychonbaiviet_luubaiviet1).text
        print(check_tuychonbaiviet_luubaiviet)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Lưu bài viết")
        logging.info("check font-end: Message - Đã lưu vào no1")
        logging.info(check_tuychonbaiviet_luubaiviet == "Đã lưu vào no1")

        #Chỉnh sửa bài viết
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuabaiviet).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuabaiviet_input).send_keys(data['khoanhkhac']['noidung2'])
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        check_tuychonbaiviet_chinhsuabaiviet = driver.find_element(By.XPATH,var.check_tuychonbaiviet_chinhsuabaiviet1).text
        print(check_tuychonbaiviet_chinhsuabaiviet)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Chỉnh sửa bài viết")
        logging.info("check font-end: Message - Chỉnh sửa bài viết thành công")
        logging.info(check_tuychonbaiviet_chinhsuabaiviet == "Chỉnh sửa bài viết thành công")

        #Ai có thể bình luận về bài viết này?
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_aicothebinhluan).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_aicothebinhluan_banbe).click()
        driver.find_element(By.XPATH, var.xong).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_aicothebinhluan).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_aicothebinhluan_tcnvtbnd).click()
        driver.find_element(By.XPATH, var.xong).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_aicothebinhluan).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_aicothebinhluan_moinguoi).click()
        driver.find_element(By.XPATH, var.xong).click()
        time.sleep(1)

        #Bật thông báo về bài viết này
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_batthongbao).click()
        check_tuychonbaiviet_batthongbao = driver.find_element(By.XPATH,var.check_tuychonbaiviet_batthongbao1).text
        print(check_tuychonbaiviet_batthongbao)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Bật thông báo về bài viết này")
        logging.info("check font-end: Message - Đã bật thông báo")
        logging.info(check_tuychonbaiviet_batthongbao == "Đã bật thông báo")
        time.sleep(1)
        #Tắt thông báo về bài viết này
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.check_tuychonbaiviet_tatthongbao11).click()
        check_tuychonbaiviet_tatthongbao = driver.find_element(By.XPATH,var.check_tuychonbaiviet_tatthongbao1).text
        print(check_tuychonbaiviet_tatthongbao)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Tắt thông báo về bài viết này")
        logging.info("check font-end: Message - Đã tắt thông báo")
        logging.info(check_tuychonbaiviet_tatthongbao == "Đã tắt thông báo")
        #Nhúng
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_nhung).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_nhung_saochep).click()
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1)

        #Chỉnh sửa ngày
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuangay).click()
        xoa = driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuangay_2022)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuangay_2022).send_keys("27-10-2022")
        driver.find_element(By.XPATH, var.xong).click()
        time.sleep(1)

        check_tuychonbaiviet_chinhsuangay = driver.find_element(By.XPATH,var.check_tuychonbaiviet_chinhsuangay1).text
        print(check_tuychonbaiviet_chinhsuangay)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Chỉnh sửa ngày")
        logging.info("check font-end: Message - Chỉnh sửa ngày thành công.")
        logging.info(check_tuychonbaiviet_chinhsuangay == "Chỉnh sửa ngày thành công.")

        #Xoá bài viết
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_xoabaiviet).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.xoa).click()
        time.sleep(1)
        check_tuychonbaiviet_xoa = driver.find_element(By.XPATH,var.check_tuychonbaiviet_xoa1).text
        print(check_tuychonbaiviet_xoa)
        logging.info("Trang cá nhân - Tuỳ chọn bài viết - Tắt thông báo về bài viết này")
        logging.info("check font-end: Message - Bài viết của bạn đã bị xóa.")
        logging.info(check_tuychonbaiviet_xoa == "Bài viết của bạn đã bị xóa.")
        time.sleep(1.5)

        # chia sẻ lên bảng tin
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        button = driver.find_element(By.XPATH, var.dangtheodoi)
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, var.dangtheodoi).click()

        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        time.sleep(3)
        try:
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        except:
            driver.refresh()
            time.sleep(1)
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselenbangtin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselenbangtin_mota).send_keys(data['khoanhkhac']['binhluan'])
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, var.dang).click()
            time.sleep(3)
            check_message_chiaselenbbangtin = driver.find_element(By.XPATH,var.check_message_chiase).text
            print(check_message_chiaselenbbangtin)
            logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên bảng tin")
            logging.info("check font-end: Message - Chia sẻ bài viết thành công")
            logging.info(check_message_chiaselenbbangtin == "Chia sẻ bài viết thành công")
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselenbangtin).click()
            time.sleep(1)
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselenbangtin_mota).send_keys(data['khoanhkhac']['binhluan'])
            time.sleep(1)
            driver.find_element(By.XPATH, var.dang).click()
            time.sleep(3)
            check_message_chiaselenbbangtin = driver.find_element(By.XPATH,var.check_message_chiase).text
            print(check_message_chiaselenbbangtin)
            logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên bảng tin")
            logging.info("check font-end: Message - Chia sẻ bài viết thành công")
            logging.info(check_message_chiaselenbbangtin == "Chia sẻ bài viết thành công")

        time.sleep(5)
        driver.get("https://sn.emso.vn/user/truongvck333")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,1100)", "")
        check_chiasengay_time = driver.find_element(By.XPATH,var.check_chiasengay1).text
        print(check_chiasengay_time)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên bảng tin")
        logging.info("check font-end: Message - Check Thời gian trên trang cá nhân - Vài giây trước")
        logging.info(check_chiasengay_time == "Vài giây trước ")

        check_chiasengay_tieude = driver.find_element(By.XPATH,var.check_chiasengay_tieude1).text
        print(check_chiasengay_tieude)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên bảng tin")
        logging.info("check font-end: Message - Check Tiêu đề trên trang cá nhân - Test khoảng khắc")
        logging.info(check_chiasengay_tieude == "Test khoảng khắc")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuabaiviet).click()
        driver.find_element(By.XPATH, var.trangcanhan_baiviet_tuychon_chinhsuabaiviet_input).send_keys(data['khoanhkhac']['noidung3'])
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)

        # #Gửi bằng message
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        time.sleep(3)
        try:
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        except:
            driver.refresh()
            time.sleep(1)
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_guibangmessage).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_guibangmessage_noidung).send_keys(data['khoanhkhac']['noidung1'])
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_guibangmessage_timkiemtqt).send_keys(data['khoanhkhac']['tranquangtruong'])
        driver.find_element(By.XPATH, var.gui).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1.5)
        driver.get("https://sn.emso.vn/messages/111169896815147328111169900882891225")
        time.sleep(2)
        # check_chiase_guibangmessage = driver.find_element(By.XPATH,var.check_chiase_guibangmessage1).text
        # print(check_chiase_guibangmessage)
        # logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Gửi bằng message")
        # logging.info("check font-end: chat - có gửi link khoảnh khắc")
        # logging.info(check_chiase_guibangmessage == "Mạng xã hội Emso")
        check_chiase_guibangmessage = driver.find_element(By.XPATH,var.check_chiase_guibangmessage2).text
        print(check_chiase_guibangmessage)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Gửi bằng message")
        logging.info("check font-end: chat - có gửi link khoảnh khắc")
        logging.info(check_chiase_guibangmessage == "Mạng xã hội Emso")




        # #Chia sẻ lên cộng đồng
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        time.sleep(3)
        try:
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        except:
            driver.refresh()
            time.sleep(1)
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselencongdong).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselencongdong_timkiem).send_keys(data['khoanhkhac']['chiaselennhom'])
        driver.find_element(By.XPATH, var.chiase_iconchonnhom).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.chiase_iconchonnhom_mota).send_keys(data['khoanhkhac']['mota1'])
        try:
            driver.find_element(By.XPATH, var.dang).click()
            time.sleep(2)
            check_message_chiaselencongdong = driver.find_element(By.XPATH,var.check_message_chiaselencongdong1).text
            print(check_message_chiaselencongdong)
            logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên cộng đồng")
            logging.info("check font-end: Message - Chia sẻ bài viết thành công")
            logging.info(check_message_chiaselencongdong == "Chia sẻ bài viết thành công")
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselencongdong).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselencongdong_timkiem).send_keys(data['khoanhkhac']['chiaselennhom'])
            driver.find_element(By.XPATH, var.chiase_iconchonnhom).click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, var.chiase_iconchonnhom_mota).send_keys(data['khoanhkhac']['mota1'])
            driver.find_element(By.XPATH, var.dang).click()
            time.sleep(2)
            check_message_chiaselencongdong = driver.find_element(By.XPATH,var.check_message_chiaselencongdong1).text
            print(check_message_chiaselencongdong)
            logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên cộng đồng")
            logging.info("check font-end: Message - Chia sẻ bài viết thành công")
            logging.info(check_message_chiaselencongdong == "Chia sẻ bài viết thành công")
        driver.get("https://sn.emso.vn/group/111294698105007828")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,500)", "")
        check_chiaselencongdong_time = driver.find_element(By.XPATH,var.check_chiaselencongdong_time1).text
        print(check_chiaselencongdong_time)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên cộng đồng")
        logging.info("check font-end: Message - Check Thời gian trong nhóm - Vài giây trước")
        logging.info(check_chiaselencongdong_time == "Vài giây trước ")

        check_chiaselencongdong_tieude = driver.find_element(By.XPATH,var.check_chiaselencongdong_tieude1).text
        print(check_chiaselencongdong_tieude)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên cộng đồng")
        logging.info("check font-end: Message - Check Tiêu đề trong nhóm - nutri boost")
        logging.info(check_chiaselencongdong_tieude == "nutri boost")
        time.sleep(2)

        # #Chia sẻ lên trang
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        time.sleep(3)
        try:
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        except:
            driver.refresh()
            time.sleep(1)
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrang).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrang_timkiem).send_keys(data['khoanhkhac']['chiaselennhom'])
        driver.find_element(By.XPATH, var.chiase_iconchontrang).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.chiase_iconchontrang_mota).send_keys(data['khoanhkhac']['mota2'])
        try:
            driver.find_element(By.XPATH, var.dang).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrang).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrang_timkiem).send_keys(data['khoanhkhac']['chiaselennhom'])
            driver.find_element(By.XPATH, var.chiase_iconchontrang).click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, var.chiase_iconchontrang_mota).send_keys(data['khoanhkhac']['mota2'])
            driver.find_element(By.XPATH, var.dang).click()
        time.sleep(2)
        check_chiase_chiaselentrang = driver.find_element(By.XPATH, var.check_chiase_chiaselentrang1).text
        print(check_chiase_chiaselentrang)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên trang")
        logging.info("check font-end: Message - Chia sẻ bài viết thành công")
        logging.info(check_chiase_chiaselentrang == "Chia sẻ bài viết thành công")
        driver.get("https://sn.emso.vn/page/108277159419224383")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,1000)", "")

        check_chiaselentrang_time = driver.find_element(By.XPATH,var.check_chiaselentrang_time1).text
        print(check_chiaselentrang_time)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên cộng đồng")
        logging.info("check font-end: Message - Check Thời gian trên trang - Vài giây trước")
        logging.info(check_chiaselencongdong_time == "Vài giây trước ")

        check_chiaselentrang_tieude = driver.find_element(By.XPATH,var.check_chiaselentrang_tieude1).text
        print(check_chiaselentrang_tieude)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên cộng đồng")
        logging.info("check font-end: Message - Check Tiêu đề trên trang - nutri boost")
        logging.info(check_chiaselentrang_tieude == "nutri caffee")
        time.sleep(2)

        #Chia sẻ lên trang cá nhân của bạn bè
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        driver.find_element(By.XPATH, var.dangtheodoi).click()
        time.sleep(3)
        try:
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        except:
            driver.refresh()
            time.sleep(1)
            button = driver.find_element(By.XPATH, var.dangtheodoi_xemvideo)
            driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrangcanhanbanbe).click()
        driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrang_timkiem).send_keys(data['khoanhkhac']['chiaselentrangcanhanbanbe'])
        driver.find_element(By.XPATH, var.chiase_iconchonbanbe).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.chiase_iconchontrangcanhanbanbe_mota).send_keys(data['khoanhkhac']['mota3'])
        try:
            driver.find_element(By.XPATH, var.dang).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrangcanhanbanbe).click()
            driver.find_element(By.XPATH, var.khoanhkhac_xemvideo_chiase_chiaselentrang_timkiem).send_keys(data['khoanhkhac']['chiaselentrangcanhanbanbe'])
            driver.find_element(By.XPATH, var.chiase_iconchonbanbe).click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, var.chiase_iconchontrangcanhanbanbe_mota).send_keys(data['khoanhkhac']['mota3'])
            driver.find_element(By.XPATH, var.dang).click()
        time.sleep(2)
        check_chiase_chiaselentrangcanhanbanbe = driver.find_element(By.XPATH, var.check_chiase_chiaselentrangcanhanbanbe1).text
        print(check_chiase_chiaselentrangcanhanbanbe)
        logging.info("Khoảnh khắc - Đang theo dõi - Chia sẻ - Chia sẻ lên trang cá nhân bạn bè")
        logging.info("check font-end: Message - Chia sẻ bài viết thành công")
        logging.info(check_chiase_chiaselentrangcanhanbanbe == "Chia sẻ bài viết thành công")
        driver.get("https://sn.emso.vn/user/truongvck22")
        time.sleep(2)

    def tructiep(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #trực tiếp
        driver.find_element(By.XPATH, var.tructiep).click()
        time.sleep(3)
        check_tructiep_videocuanguoiphattructiepdatheodoi = driver.find_element(By.XPATH,var.check_tructiep_videocuanguoiphattructiepdatheodoi1).text
        print(check_tructiep_videocuanguoiphattructiepdatheodoi)
        logging.info("Khoảnh khắc - Trực tiếp -  Video của người phát trực tiếp đã theo dõi")
        logging.info("check font-end:  Video của người phát trực tiếp đã theo dõi")
        logging.info(check_tructiep_videocuanguoiphattructiepdatheodoi == "Video của người phát trực tiếp đã theo dõi")

    def taokhoanhkhac(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Tạo khoảnh khắc
        driver.find_element(By.XPATH, var.taokhoanhkhac).click()
        time.sleep(3)
        try:
            driver.find_element(By.XPATH, var.khoanhkhac_nhapnoidung).send_keys(data['khoanhkhac']['taokhoanhkhac'])
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.taokhoanhkhac).click()
            time.sleep(3)
            driver.find_element(By.XPATH, var.khoanhkhac_nhapnoidung).send_keys(data['khoanhkhac']['taokhoanhkhac'])
        driver.find_element(By.XPATH, var.khoanhkhac_tailenvideo).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/quangaygiongbao.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.khoanhkhac_dangbai).click()
        time.sleep(15)
        check_taokhoanhkhac_tieude = driver.find_element(By.XPATH,var.check_taokhoanhkhac_tieude1).text
        print(check_taokhoanhkhac_tieude)
        logging.info("Khoảnh khắc - Tạo khoảnh khắc")
        logging.info("check font-end: Tiêu đề - Test tạo khoảnh khắc")
        logging.info(check_taokhoanhkhac_tieude == "Test tạo khoảnh khắc")

    def taikhoan_duocdexuat(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Tài khoản được đề xuất
        driver.find_element(By.XPATH, var.taikhoandexuat).click()
        time.sleep(1)
        button = driver.find_element(By.XPATH, var.yenvu_trangcanhan)
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, var.yenvu_trangcanhan).click()
        time.sleep(1)
        check_khoanhkhac_trangcanhan_yenvu = driver.find_element(By.XPATH,var.check_khoanhkhac_trangcanhan_yenvu1).text
        print(check_khoanhkhac_trangcanhan_yenvu)
        logging.info("Khoảnh khắc - Tài khoản được đề xuất")
        logging.info("check font-end: Xem trang cá nhân - Yến Vũ")
        logging.info(check_khoanhkhac_trangcanhan_yenvu == "Yến Vũ")
        driver.back()
        time.sleep(2)
        button = driver.find_element(By.XPATH, var.taikhoanduocdexuat_xemvideo)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.taikhoandexuat_xemvideo_iconnextxuongduoi).click()
        time.sleep(3)
        check_taikhoandexuat_xemvideo_iconnextxuongduoi = driver.find_element(By.XPATH,var.taikhoandexuat_xemvideo_iconnextxuongduoi1).text
        print(check_taikhoandexuat_xemvideo_iconnextxuongduoi)
        logging.info("Khoảnh khắc - Tài khoản được đề xuất - Xem video")
        logging.info("check font-end: Xem video khi chọn mũi tên xuồng")
        logging.info(check_taikhoandexuat_xemvideo_iconnextxuongduoi == "jjsd")
        time.sleep(1)
        driver.find_element(By.XPATH, var.taikhoandexuat_xemvideo_iconnextlentren).click()
        time.sleep(3)
        check_taikhoandexuat_xemvideo_iconnextlentren = driver.find_element(By.XPATH,var.check_taikhoandexuat_xemvideo_iconnextlentren1).text
        print(check_taikhoandexuat_xemvideo_iconnextlentren)
        logging.info("Khoảnh khắc - Tài khoản được đề xuất - Xem video")
        logging.info("check font-end: Xem video khi chọn mũi tên lên")
        logging.info(check_taikhoandexuat_xemvideo_iconnextlentren == "fdfd")
        time.sleep(1)

    def taikhoan_dangtheodoi(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Tài khoản đang theo dõi
        driver.find_element(By.XPATH, var.taikhoandangtheodoi).click()
        time.sleep(1)
        button = driver.find_element(By.XPATH, var.dev4_trangcanhan)
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, var.dev4_trangcanhan).click()
        time.sleep(1)
        check_khoanhkhac_trangcanhan_dev4 = driver.find_element(By.XPATH,var.check_khoanhkhac_trangcanhan_dev4).text
        print(check_khoanhkhac_trangcanhan_dev4)
        logging.info("Khoảnh khắc - Tài khoản đang theo dõi")
        logging.info("check font-end: Xem trang cá nhân - Developer 4 EMSO")
        logging.info(check_khoanhkhac_trangcanhan_dev4 == "Developer 4 EMSO")
        driver.back()
        time.sleep(2)
        button = driver.find_element(By.XPATH, var.taikhoandangtheodoi_xemvideo)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.taikhoandexuat_xemvideo_iconnextxuongduoi).click()
        time.sleep(3)
        check_taikhoandangtheodoi_xemvideo_iconnextxuongduoi = driver.find_element(By.XPATH,var.check_taikhoandangtheodoi_xemvideo_iconnextxuongduoi1).text
        print(check_taikhoandangtheodoi_xemvideo_iconnextxuongduoi)
        logging.info("Khoảnh khắc - Tài khoản đang theo dõi - Xem video")
        logging.info("check font-end: Xem video khi chọn mũi tên xuồng")
        logging.info(check_taikhoandangtheodoi_xemvideo_iconnextxuongduoi == "test")
        time.sleep(1)
        driver.find_element(By.XPATH, var.taikhoandexuat_xemvideo_iconnextlentren).click()
        time.sleep(3)
        check_taikhoandangtheodoi_xemvideo_iconnextlentren = driver.find_element(By.XPATH,var.check_taikhoandangtheodoi_xemvideo_iconnextxuongduoi1).text
        print(check_taikhoandangtheodoi_xemvideo_iconnextlentren)
        logging.info("Khoảnh khắc - Tài khoản đang theo dõi - Xem video")
        logging.info("check font-end: Xem video khi chọn mũi tên lên")
        logging.info(check_taikhoandangtheodoi_xemvideo_iconnextlentren == "sad")
        time.sleep(2)

    def khoanhkhac_timkiem(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_khoanhkhac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Tìm kiếm video
        driver.find_element(By.XPATH, var.khoanhkhac_input).send_keys(data['khoanhkhac']['timkiem'])
        driver.find_element(By.XPATH, var.khoanhkhac_input).send_keys(Keys.ENTER)
        time.sleep(4)
        check_timikiem_goiy = driver.find_element(By.XPATH,var.check_timikiem_goiy1).text
        print(check_timikiem_goiy)
        logging.info("Khoảnh khắc - Tìm kiếm - Gợi ý")
        logging.info("check font-end: Gợi ý 1 - Fan anh Huấn anh Bảnh")
        logging.info(check_timikiem_goiy == "Fan anh Huấn anh Bảnh")

        #Top
        check_timikiem_top = driver.find_element(By.XPATH,var.check_timikiem_top1).text
        print(check_timikiem_top)
        logging.info("Khoảnh khắc - Tìm kiếm - Top")
        logging.info("check font-end: Top - Fan anh Huấn anh Bảnh")
        logging.info(check_timikiem_goiy == "Fan anh Huấn anh Bảnh")

        #Tài khoản
        driver.find_element(By.XPATH, var.khoanhkhac_timkiem_taikhoan).click()
        time.sleep(1)
        check_timikiem_taikhoan = driver.find_element(By.XPATH,var.check_timikiem_taikhoan1).text
        print(check_timikiem_taikhoan)
        logging.info("Khoảnh khắc - Tìm kiếm - Tài khoản")
        logging.info("check font-end: Top - Fan anh Huấn anh Bảnh")
        logging.info(check_timikiem_goiy == "Fan anh Huấn anh Bảnh")

        #Video
        driver.find_element(By.XPATH, var.timkiem_video).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.khoanhkhac_timkiem_video).click()
        time.sleep(6)
        check_timikiem_video = driver.find_element(By.XPATH,var.check_timikiem_video1).text
        print(check_timikiem_video)
        logging.info("Khoảnh khắc - Tìm kiếm - Video")
        logging.info("check font-end: Mô tả - Huấn tìm đến nhà #gopnhatcaida #huanhoahong #xuhuong2023")
        logging.info(check_timikiem_video == "Huấn tìm đến nhà #gopnhatcaida #huanhoahong #xuhuong2023")
        time.sleep(1)
        driver.find_element(By.XPATH, var.esc).click()
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)



class watch():

    def timkiem(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_watch)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Tìm kiếm video
        driver.find_element(By.XPATH, var.khoanhkhac_input).send_keys(data['watch']['timkiem'])
        driver.find_element(By.XPATH, var.khoanhkhac_input).send_keys(Keys.ENTER)
        time.sleep(5)
        check_watch_timikiem_goiy = driver.find_element(By.XPATH,var.check_watch_timikiem_goiy1).text
        print(check_watch_timikiem_goiy)
        logging.info("Watch - Tìm kiếm - Gợi ý")
        logging.info("check font-end: Gợi ý 1 - Bên người khác em có hạnh phúc hơn?")
        logging.info(check_watch_timikiem_goiy == "Bên người khác em có hạnh phúc hơn?")

        #Kết quả tìm kiếm
        check_watch_timikiem_ketqua = driver.find_element(By.XPATH,var.check_watch_timikiem_ketqua1).text
        print(check_watch_timikiem_ketqua)
        logging.info("Watch - Tìm kiếm - Gợi ý")
        logging.info("check font-end: Gợi ý 1 - Bên người khác em có hạnh phúc hơn?")
        logging.info(check_watch_timikiem_ketqua == "Bên người khác em có hạnh phúc hơn?")
        button = driver.find_element(By.XPATH, var.watch_xemvideo)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(3)
        driver.find_element(By.XPATH, var.watch_xemvideo_like).click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).send_keys(data['watch']['mota'])
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).send_keys(Keys.ENTER)
        time.sleep(2)
        # driver.find_element(By.XPATH, var.watch_xemvideo_x).click()
        button = driver.find_element(By.XPATH, var.watch_xemvideo_x)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)



    def trangchu(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_watch)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Xem video
        button = driver.find_element(By.XPATH, var.watch_trangchu_xemvideo)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(4)

        #like video
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.watch_xemvideo_like)))
        element.click()

        # chọn cách tương tác
        button = driver.find_element(By.XPATH, var.xemvideo_iconchoncachtuongtac)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        driver.find_element(By.XPATH, var.xemvideo_iconchoncachtuongtac_trang).click()
        #Bình luận 1
        button = driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_button)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).send_keys(data['watch']['mota1'])
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).submit()
        wait = WebDriverWait(driver, 10)
        time.sleep(3)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_like)))
        time.sleep(3)
        element.click()

        check_binhluan_dalike = driver.find_element(By.XPATH,var.check_binhluan_dalike).get_attribute('style')
        print(check_binhluan_dalike)
        logging.info("Watch - Trang chủ - Bình luận - Like")
        logging.info("check font-end: Đã like bình luận")
        logging.info(check_binhluan_dalike == "color: rgb(113, 101, 224);")

        check_choncachtuongtac_trang = driver.find_element(By.XPATH,var.check_choncachtuongtac_trang1).text
        print(check_choncachtuongtac_trang)
        logging.info("Watch - Trang chủ - Chọn cách tương tác")
        logging.info("check font-end: Trang - Trường test bản tin")
        logging.info("Trang" + check_choncachtuongtac_trang)
        logging.info(check_choncachtuongtac_trang == "Trường test bản tin")

        check_watch_binhluan = driver.find_element(By.XPATH,var.check_watch_binhluan1).text
        print(check_watch_binhluan)
        logging.info("Watch - Trang chủ - Chọn cách tương tác")
        logging.info("check font-end: comment - Test watch trang chủ")
        logging.info(check_watch_binhluan == "Test watch trang chủ")

        #phản hồi
        driver.find_element(By.XPATH, var.binhluan_phanhoi).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_input)))
        element.send_keys(data['watch']['mota2'])

        #phản hồi - icon cảm xúc
        driver.find_element(By.XPATH, var.binhluan_phanhoi_inputiconcamxuc).click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_inputiconcamxuc_chon).click()
        time.sleep(1)
        #phản hồi - ảnh
        driver.find_element(By.XPATH, var.binhluan_phanhoi_tailen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.binhluan_phanhoi_tailen_x).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.binhluan_phanhoi_tailen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhdaidien1.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).submit()
        time.sleep(1.5)

        check_phanhoi_comment_camxuc = driver.find_element(By.XPATH,var.check_phanhoi_comment_camxuc1).text
        print(check_phanhoi_comment_camxuc)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: phản hồi comment và cảm xuc - Test watch phản hồi😃")
        logging.info(check_phanhoi_comment_camxuc)
        logging.info(check_phanhoi_comment_camxuc == "Test watch phản hồi😃")

        check_phanhoi_anh = driver.find_element(By.XPATH,var.check_phanhoi_anh1).is_displayed()
        print(check_phanhoi_anh)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: phản hồi ảnh - tải ảnh lên thành công")
        logging.info(check_phanhoi_anh)


        wait = WebDriverWait(driver, 10)      #Lỗi trắng trang khi  chưa load xong ảnh mà lại like
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_like)))
        element.click()

        #phản hồi - gif
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi)))
        element.click()

        driver.find_element(By.XPATH, var.binhluan_phanhoi_gif).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.binhluan_phanhoi_gif_timkiem).send_keys(data['watch']['gif_timkiem'])
        time.sleep(5)
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_gif_chon)))
            element.click()
        except:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_gif_chon2)))
            element.click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).send_keys(data['watch']['gif'])
        driver.find_element(By.XPATH, var.binhluan_phanhoi_inputiconcamxuc).click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_inputiconcamxuc_chon).click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).submit()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_inputiconcamxuc).click()

        check_phanhoi_commentgif = driver.find_element(By.XPATH,var.check_phanhoi_commentgif1).text
        print(check_phanhoi_commentgif)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: phản hồi comment và cảm xuc khi chọn Gif - Test giff phản hồi nè😃")
        logging.info(check_phanhoi_commentgif)
        logging.info(check_phanhoi_commentgif == "Test giff phản hồi nè😃")

        check_phanhoi_gif = driver.find_element(By.XPATH,var.check_phanhoi_gif1).is_displayed()
        print(check_phanhoi_gif)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: Gif - tải gif lên thành công")
        logging.info(check_phanhoi_gif)


        # phản hồi -nhãn dán
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi1)))
        element.click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_nhandan).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_nhandan_chon)))
        element.click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).send_keys(data['watch']['nhandan'])
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).send_keys(Keys.ENTER)

        check_phanhoi_commentnhandan = driver.find_element(By.XPATH,var.check_phanhoi_commentnhandan1).text
        print(check_phanhoi_commentnhandan)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: phản hồi comment khi chọn nhãn dán - Test nhãn dán phản hồi nè")
        logging.info(check_phanhoi_commentnhandan)
        logging.info(check_phanhoi_commentnhandan == "Test nhãn dán phản hồi nè")

        check_phanhoi_nhandan = driver.find_element(By.XPATH,var.check_phanhoi_nhandan1).is_displayed()
        print(check_phanhoi_nhandan)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: nhãn dán - tải nhãn dán lên thành công")
        logging.info(check_phanhoi_nhandan)


        # #phản hồi - sửa
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi1)))
        element.click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).send_keys(data['watch']['phanhoi_sua'])
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).submit()
        wait = WebDriverWait(driver, 10)
        time.sleep(1)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_hover)))
        element.click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_icontuychon).click()
        time.sleep(1)
        # driver.find_element(By.XPATH, var.binhluan_phanhoi_sua).click()
        button = driver.find_element(By.XPATH, var.binhluan_phanhoi_sua)
        driver.execute_script("arguments[0].click();", button)

        xoa = driver.find_element(By.XPATH, var.binhluan_phanhoi_input1)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input1).send_keys(data['watch']['phanhoi_sua1'])
        time.sleep(2)
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input1).send_keys(Keys.ENTER)
        time.sleep(2)
        check_watch_phanhoi_suacomment = driver.find_element(By.XPATH,var.check_watch_phanhoi_suacomment1).text
        print(check_watch_phanhoi_suacomment)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: Sửa comment - Mua nước uống nheee")
        logging.info(check_watch_phanhoi_suacomment == "Mua nước uống nheee")
        time.sleep(5)

        #phản hồi - xoá           #Lỗi không xoá được comment
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi1)))
        element.click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).send_keys(data['watch']['phanhoi_sua'])
        driver.find_element(By.XPATH, var.binhluan_phanhoi_input).submit()
        time.sleep(5)
        driver.find_element(By.XPATH, var.binhluan_phanhoi_hover1).click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_icontuychon1).click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_xoa1).click()
        driver.find_element(By.XPATH, var.xoa).click()
        time.sleep(2.5)

        # Bình luận 2
        button = driver.find_element(By.XPATH, var.xemvideo_iconchoncachtuongtac1)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        driver.find_element(By.XPATH, var.xemvideo_iconchoncachtuongtac_ngocmai).click()

        #bình luận - tải lên ảnh
        driver.find_element(By.XPATH, var.binhluan_tailenanh).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia2.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).send_keys(data['watch']['mota4'])
        driver.find_element(By.XPATH, var.binhluan_iconcamxuc).click()
        driver.find_element(By.XPATH, var.binhluan_phanhoi_inputiconcamxuc_chon9).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).submit()
        time.sleep(1)
        driver.find_element(By.XPATH, var.binhluan_iconcamxuc).click()
        time.sleep(1.5)
        check_comment_camxuc_cuaanh = driver.find_element(By.XPATH,var.check_comment_camxuc_cuaanh1).text
        print(check_comment_camxuc_cuaanh)
        logging.info("Watch - Trang chủ - Bình luận - Ảnh")
        logging.info("check font-end: Comment và cảm xúc của ảnh - Test watch bình luận tải lên ảnh😍")
        logging.info(check_comment_camxuc_cuaanh)
        logging.info(check_comment_camxuc_cuaanh == "Test watch bình luận tải lên ảnh😍")

        check_binhluan_anh = driver.find_element(By.XPATH,var.check_binhluan_anh1).is_displayed()
        print(check_binhluan_anh)
        logging.info("Watch - Trang chủ - Bình luận ")
        logging.info("check font-end: Tải ảnh lên thành công")
        logging.info(check_binhluan_anh)

        #bình luận - gif
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.watch_binhluan_gif)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.binhluan_gif_timkiem).send_keys(data['watch']['gif_timkiem'])
        try:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_gif_timkiem1)))
            element.click()
        except:
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_gif_timkiem6)))
            element.click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).send_keys(data['watch']['gif1'])
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_iconcamxuc).click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_iconcamxuc_chon13).click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).submit()
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_iconcamxuc).click()
        time.sleep(1.5)

        check_binhluan_commentgif = driver.find_element(By.XPATH,var.check_binhluan_commentgif1).text
        print(check_binhluan_commentgif)
        logging.info("Watch - Trang chủ - Bình luận -gif")
        logging.info("check font-end: Bình luận - comment và cảm xuc khi chọn Gif - Test giff bnh luận  nè😋")
        logging.info(check_binhluan_commentgif)
        logging.info(check_binhluan_commentgif == "Test giff bnh luận  nè😋")

        check_binhluan_gif = driver.find_element(By.XPATH,var.check_binhluan_gif1).is_displayed()
        print(check_binhluan_gif)
        logging.info("Watch - Trang chủ - Bình luận - Phản hồi")
        logging.info("check font-end: Gif - tải gif lên thành công")
        logging.info(check_binhluan_gif)


        #bình luận - nhãn dán
        driver.find_element(By.XPATH, var.watch_binhluan_nhandan).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.binhluan_phanhoi_nhandan_chon)))
        element.click()
        driver.find_element(By.XPATH, var.binhluan_nhandan_input).send_keys(data['watch']['nhandan1'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_iconcamxuc).click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_iconcamxuc_chon12).click()
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan).submit()
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_xemvideo_binhluan_iconcamxuc).click()
        time.sleep(1.5)
        check_binhluan_commentnhandan = driver.find_element(By.XPATH,var.check_binhluan_commentnhandan1).text
        print(check_binhluan_commentnhandan)
        logging.info("Watch - Trang chủ - Bình luận - Nhãn dán")
        logging.info("check font-end: Bình luận comment khi chọn nhãn dán - Test nhãn dán bình luận nè😚")
        logging.info(check_binhluan_commentnhandan)
        logging.info(check_binhluan_commentnhandan == "Test nhãn dán bình luận nè😚")

        check_binhluan_nhandan = driver.find_element(By.XPATH,var.check_binhluan_nhandan1).is_displayed()
        print(check_binhluan_nhandan)
        logging.info("Watch - Trang chủ - Bình luận - Nhãn dán")
        logging.info("check font-end: nhãn dán - tải nhãn dán lên thành công")
        logging.info(check_binhluan_nhandan)
        time.sleep(1)
        driver.get("https://sn.emso.vn/")
        time.sleep(2)




    def chuongtrinh(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_watch)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Chương trình
        driver.find_element(By.XPATH, var.watch_chuongtrinh).click()
        check_watch_chuongtrinh_nguyentac1 = driver.find_element(By.XPATH,var.check_watch_chuongtrinh_nguyentac1).is_displayed()
        check_watch_chuongtrinh_nguyentac2 = driver.find_element(By.XPATH,var.check_watch_chuongtrinh_nguyentac2).is_displayed()
        logging.info("Watch - Chương trình - Nguyên tác trên EMSO")
        logging.info("check font-end: Có nguyên tác 1 không?")
        logging.info(check_watch_chuongtrinh_nguyentac1 != None)

        logging.info("check font-end: Có nguyên tác 2 không?")
        logging.info(check_watch_chuongtrinh_nguyentac2 != None)
        time.sleep(1)
        driver.find_element(By.XPATH, var.watch_chuongtrinhdangtheodoi).click()
        check_chuongtrinh_dangtheodoi_mota = driver.find_element(By.XPATH,var.check_chuongtrinh_dangtheodoi_mota1).text
        print(check_chuongtrinh_dangtheodoi_mota)
        logging.info(check_chuongtrinh_dangtheodoi_mota)
        logging.info("Watch - Chương trình - Chương trình bạn bè đang theo dõi")
        logging.info("check font-end: mô tả - Nhìn bả tàn tạ thấy thương🤣🤣")
        logging.info(check_chuongtrinh_dangtheodoi_mota == "Nhìn bả tàn tạ thấy thương🤣🤣")

        check_chuongtrinh_dangtheodoi_trangthai = driver.find_element(By.XPATH,var.check_chuongtrinh_dangtheodoi_trangthai1).text
        print(check_chuongtrinh_dangtheodoi_trangthai)
        logging.info("Watch - Chương trình - Chương trình bạn bè đang theo dõi")
        logging.info("check font-end: Trạng thái - Đang theo dõi")
        logging.info(check_chuongtrinh_dangtheodoi_trangthai)
        logging.info(check_chuongtrinh_dangtheodoi_trangthai == "Đang theo dõi")
        time.sleep(2)

        #Chương trình - xem videp
        driver.find_element(By.XPATH, var.watch_chuongtrinhdangtheodoi_xemvideo1).click()
        time.sleep(3)
        check_chuongtrinh_dangtheodoi_video1 = driver.find_element(By.XPATH,var.check_chuongtrinh_dangtheodoi_video1).text
        print(check_chuongtrinh_dangtheodoi_video1)
        logging.info("Watch - Chương trình - Chương trình bạn bè đang theo dõi")
        logging.info("check font-end: mô tả video 1 - nooo1")
        logging.info(check_chuongtrinh_dangtheodoi_video1 == "nooo1")
        driver.find_element(By.XPATH, var.watch_chuongtrinhdangtheodoi_xemvideo1_x).click()
        time.sleep(1)

        driver.find_element(By.XPATH, var.watch_chuongtrinhdangtheodoi_xemvideo2).click()
        time.sleep(3)
        check_chuongtrinh_dangtheodoi_video2 = driver.find_element(By.XPATH,var.check_chuongtrinh_dangtheodoi_video2).text
        print(check_chuongtrinh_dangtheodoi_video2)
        logging.info("Watch - Chương trình - Chương trình bạn bè đang theo dõi")
        logging.info("check font-end: mô tả video 2 - aaww")
        logging.info(check_chuongtrinh_dangtheodoi_video2 == "aaww")
        driver.find_element(By.XPATH, var.watch_chuongtrinhdangtheodoi_xemvideo1_x).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)



    def videodaluu(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_watch)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Video đã lưu
        driver.find_element(By.XPATH, var.watch_videodaluu).click()
        time.sleep(2)
        check_watch_videodaluu_video1_trangthai = driver.find_element(By.XPATH,var.check_watch_videodaluu_video1).text
        print(check_watch_videodaluu_video1_trangthai)
        logging.info("Watch - Video đã lưu - video1 - Trạng thái ")
        logging.info("check font-end: Trạng thái - Bỏ lưu")
        logging.info(check_watch_videodaluu_video1_trangthai)
        logging.info(check_watch_videodaluu_video1_trangthai == "Bỏ lưu")

        #Xem video
        #Lưu bài viết
        driver.find_element(By.XPATH, var.watch_videodaluu_xemvideo1).click()
        time.sleep(3)
        driver.find_element(By.XPATH, var.videodaluu_xemvideo1_icondau3cham).click()
        check_watch_videodaluu_video1_xemvideo_trangthai = driver.find_element(By.XPATH,var.check_watch_videodaluu_video1_xemvideo_trangthai1).text
        print(check_watch_videodaluu_video1_xemvideo_trangthai)
        logging.info("Watch - Video đã lưu - Video1 - Xem - Trạng thái video1")
        logging.info("check font-end: Trạng thái - Bỏ lưu bài viết Xóa bài viết khỏi danh sách mục đã lưu")
        logging.info(check_watch_videodaluu_video1_xemvideo_trangthai)
        logging.info(check_watch_videodaluu_video1_xemvideo_trangthai == "Bỏ lưu bài viết\nXóa bài viết khỏi danh sách mục đã lưu")

        #Báo cáo
        driver.find_element(By.XPATH, var.watch_videodaluu_xemvideo1_baocao).click()
        check_xemvideo_baocao = driver.find_element(By.XPATH,var.check_xemvideo_baocao1).text
        print(check_xemvideo_baocao)
        logging.info("Watch - Video đã lưu - Video1 - Xem - Báo cáo")
        logging.info("check font-end: Popup - Báo cáo")
        logging.info(check_xemvideo_baocao)
        logging.info(check_xemvideo_baocao == "Báo cáo")

        driver.find_element(By.XPATH, var.baocao_noidungomghiec).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_khungbo).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_ngontugaythughet).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_banhangtraiphep).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_spam).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_tutuhoacgaythuongtich).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_quayroi).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_baoluc).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, var.baocao_anhkhoathan).click()
        driver.find_element(By.XPATH, var.baocao_quaylai).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.baocao_x).click()
        time.sleep(1)

        #Tắt thông báo về bài viết này
        driver.find_element(By.XPATH, var.videodaluu_xemvideo1_icondau3cham).click()
        driver.find_element(By.XPATH, var.icondau3cham_tatthongbaovebaivietnay).click()
        time.sleep(1)
        check_luuvideo_tatthongbaobaiviet = driver.find_element(By.XPATH,var.check_luuvideo_tatthongbaobaiviet1).text
        print(check_luuvideo_tatthongbaobaiviet)
        logging.info("Watch - Video đã lưu - Video1 - Xem - Tắt thông báo bài viết")
        logging.info("check font-end: Message - Đã tắt thông báo")
        logging.info(check_luuvideo_tatthongbaobaiviet)
        logging.info(check_luuvideo_tatthongbaobaiviet == "Đã tắt thông báo")

        #Bật thông báo về bài viết này
        driver.find_element(By.XPATH, var.videodaluu_xemvideo1_icondau3cham).click()
        driver.find_element(By.XPATH, var.icondau3cham_batthongbaovebaivietnay).click()
        time.sleep(1)
        check_luuvideo_batthongbaobaiviet = driver.find_element(By.XPATH,var.check_luuvideo_batthongbaobaiviet1).text
        print(check_luuvideo_batthongbaobaiviet)
        logging.info("Watch - Video đã lưu - Video1 - Xem - Bật thông báo bài viết")
        logging.info("check font-end: Message - Đã bật thông báo")
        logging.info(check_luuvideo_batthongbaobaiviet)
        logging.info(check_luuvideo_batthongbaobaiviet == "Đã bật thông báo")
        time.sleep(1)

        #Nhúng
        driver.find_element(By.XPATH, var.videodaluu_xemvideo1_icondau3cham).click()
        driver.find_element(By.XPATH, var.icondau3cham_nhung).click()
        time.sleep(0.5)
        check_luuvideo_nhung = driver.find_element(By.XPATH,var.check_luuvideo_nhung1).text
        print(check_luuvideo_nhung)
        logging.info("Watch - Video đã lưu - Video1 - Xem - Nhúng")
        logging.info("check font-end: Popup - Nhúng bài viết")
        logging.info(check_luuvideo_nhung)
        logging.info(check_luuvideo_nhung == "Nhúng bài viết")
        time.sleep(1)

        check_luuvideo_nhung_motavideo = driver.find_element(By.XPATH,var.check_luuvideo_nhung_motavideo1).text
        print(check_luuvideo_nhung_motavideo)
        logging.info("Watch - Video đã lưu - Video1 - Xem - Nhúng - Mô tả video")
        logging.info("check font-end: Mô tả video nhúng - Vợ báo quá báo,chồng có ý tốt mà lại bị hiểu nhầm cuối cùng đẩy chồng vào t.ù #phimhay")
        logging.info(check_luuvideo_nhung_motavideo)
        logging.info(check_luuvideo_nhung_motavideo == "Vợ báo quá báo,chồng có ý tốt mà lại bị hiểu nhầm cuối cùng đẩy chồng vào t.ù #phimhay")
        driver.find_element(By.XPATH, var.x).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.videodaluu_xem_x).click()
        time.sleep(1)
        try:
            check_luuvideo_title = driver.find_element(By.XPATH,var.test1).is_displayed()
            logging.info("Watch - Video đã lưu - xem video - x")
            logging.info("check font-end: Có trở lại trang Video đã lưu không")
            logging.info(check_luuvideo_title)
            time.sleep(2)
        except NoSuchElementException:
            logging.info("Watch - Video đã lưu - xem video - x")
            logging.info("check font-end: Có trở lại trang Video đã lưu không")
            logging.info("False")
            time.sleep(2)



    def dangtheodoi(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_watch)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Dang theo dõi - Thông tin chính phủ
        driver.find_element(By.XPATH, var.watch_dangtheodoi).click()
        time.sleep(2)
        #Trạng thái
        check_dangtheodoi_trangthai = driver.find_element(By.XPATH,var.check_dangtheodoi_trangthai1).text
        print(check_dangtheodoi_trangthai)
        logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
        logging.info("check font-end: Trạng thái - Đã thích")
        logging.info(check_dangtheodoi_trangthai == "  Đã thích")

        #Phổ biến nhất
        try:
            check_dangtheodoi_phobiennhat = driver.find_element(By.XPATH,var.check_dangtheodoi_phobiennhat1).is_displayed()
            print(check_dangtheodoi_phobiennhat)
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Phổ biến nhất - Có video hiển thị hay không")
            logging.info(check_dangtheodoi_phobiennhat)
        except  NoSuchElementException:
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Phổ biến nhất - Có video hiển thị hay không")
            logging.info("False")

        #Bài đăng
        try:
            check_dangtheodoi_baidang = driver.find_element(By.XPATH,var.check_dangtheodoi_baidang1).is_displayed()
            print(check_dangtheodoi_baidang)
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Bài đăng - Có video hiển thị hay không")
            logging.info(check_dangtheodoi_baidang)
        except  NoSuchElementException:
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Bài đăng - Có video hiển thị hay không")
            logging.info("False")

        #Khoảnh khăc
        driver.find_element(By.XPATH, var.watch_dangtheodoi_khoanhkhac).click()
        time.sleep(2)
        try:
            check_dangtheodoi_khoanhkhac = driver.find_element(By.XPATH,var.check_dangtheodoi_khoanhkhac1).is_displayed()
            print(check_dangtheodoi_khoanhkhac)
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Khoảnh khắc - Có video hiển thị hay không")
            logging.info(check_dangtheodoi_khoanhkhac)
        except  NoSuchElementException:
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Khoảnh khắc - Có video hiển thị hay không")
            logging.info("False")

        #Danh sách phát
        driver.find_element(By.XPATH, var.watch_dangtheodoi_danhsachphat).click()
        time.sleep(2)
        try:
            check_dangtheodoi_danhsachphat = driver.find_element(By.XPATH,var.check_dangtheodoi_danhsachphat1).is_displayed()
            print(check_dangtheodoi_danhsachphat)
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Danh sách phát - Có video hiển thị hay không")
            logging.info(check_dangtheodoi_danhsachphat)
        except  NoSuchElementException:
            logging.info("Watch - Đang theo dõi - Thông tin chinh phủ ")
            logging.info("check font-end: Danh sách phát - Có video hiển thị hay không")
            logging.info("False")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)



class trang():
    def timkiem_trangcuaban(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(2)
        #Tìm kiếm trang page
        driver.find_element(By.XPATH, var.trang_timkiem).send_keys(data['trang']['timkiem'])
        driver.find_element(By.XPATH, var.trang_timkiem).send_keys(Keys.ENTER)
        time.sleep(3)
        trang_timkiem_trang = driver.find_element(By.XPATH,var.trang_timkiem_trang1).text
        print(trang_timkiem_trang)
        logging.info("Trang - Tìm kiếm")
        logging.info("check font-end: Tìm kiếm - Trường test bản tin")
        logging.info(trang_timkiem_trang == "Trường test bản tin")
        driver.back()
        driver.back()
        time.sleep(1)
        #Trang của bạn
        #Bình thuận
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_binhthuan).click()
        time.sleep(1)
        check_trang_trangcuaban_binhthuan = driver.find_element(By.XPATH,var.trang_trangcuaban_binhthuan1).text
        print(check_trang_trangcuaban_binhthuan)
        logging.info("Trang - Trang của bạn")
        logging.info("check font-end: Trang của bạn - Bình Thuận")
        logging.info(check_trang_trangcuaban_binhthuan == "Bình Thuận")
        driver.back()
        #Trường test bản tin
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(1)
        check_trang_trangcuaban_truongtest = driver.find_element(By.XPATH,var.trang_trangcuaban_truongtest1).text
        print(check_trang_trangcuaban_truongtest)
        logging.info("Trang - Trang của bạn")
        logging.info("check font-end: Trang của bạn - Trường test bản tin")
        logging.info(check_trang_trangcuaban_truongtest == "Trường test bản tin")



    def khampha(self):
        driver.implicitly_wait(15)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_khampha).click()
        #Gợi ý cho bạn
        check_trang_khampha_goiy1 = driver.find_element(By.XPATH,var.check_trang_khampha_goiy1a).text
        print(check_trang_khampha_goiy1)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Khám phá - Có trang gợi ý hay không")
        logging.info(check_trang_khampha_goiy1 != None)

        khampha_tentranggoiy1 = driver.find_element(By.XPATH,var.khampha_tentranggoiy1aa).text
        print(khampha_tentranggoiy1)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Hiện tên gợi ý 1 hay không")
        logging.info(khampha_tentranggoiy1)
        logging.info(khampha_tentranggoiy1 != None)

        khampha_linhvuc_tranggoiy1 = driver.find_element(By.XPATH,var.khampha_linhvuc_tranggoiy11).text
        print(khampha_linhvuc_tranggoiy1)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Hiện lĩnh vực gợi ý 1 hay không")
        logging.info(khampha_linhvuc_tranggoiy1)
        logging.info(khampha_linhvuc_tranggoiy1 != None)

        khampha_luotthich_tranggoiy1 = driver.find_element(By.XPATH,var.khampha_luotthich_tranggoiy11).text
        print(khampha_luotthich_tranggoiy1)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Hiện lượt thích gợi ý 1 hay không")
        logging.info(khampha_luotthich_tranggoiy1)
        logging.info(khampha_luotthich_tranggoiy1 != None)

        check_trang_khampha_goiy1_trangthai = driver.find_element(By.XPATH,var.check_trang_khampha_goiy1_trangthai1).text
        print(check_trang_khampha_goiy1_trangthai)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Trạng thái gợi ý 1 - Thích")
        logging.info(check_trang_khampha_goiy1_trangthai == "  Thích")

        #Vào Trang đầu tiên của Gợi ý cho bạn
        driver.find_element(By.XPATH, var.khampha_goiy1).click()
        time.sleep(1)
        check_goiy1_vaotrang_ten = driver.find_element(By.XPATH,var.check_goiy1_vaotrang_ten1).text
        print(check_goiy1_vaotrang_ten)
        logging.info(khampha_tentranggoiy1)
        logging.info(check_goiy1_vaotrang_ten)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Vào trang gợi ý 1 " + khampha_tentranggoiy1)
        logging.info(check_goiy1_vaotrang_ten == khampha_tentranggoiy1)

        check_goiy1_trangthai = driver.find_element(By.XPATH,var.check_goiy1_trangthai1).text
        print(check_goiy1_trangthai)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Trạng thái gợi ý 1 khi đã like và vào trang - Thích")
        logging.info(check_goiy1_trangthai == "  Thích")

        khampha_linhvuc_tranggoiy1_vaotrang = driver.find_element(By.XPATH,var.khampha_linhvuc_tranggoiy1_vaotrang1).text
        print(khampha_linhvuc_tranggoiy1_vaotrang[2::])
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Lĩnh vực gợi ý 1 khi vào trang có giống không?")
        logging.info(khampha_linhvuc_tranggoiy1_vaotrang[2::])
        logging.info(khampha_linhvuc_tranggoiy1)
        logging.info(khampha_linhvuc_tranggoiy1_vaotrang[2::] == khampha_linhvuc_tranggoiy1)

        khampha_luotthich_tranggoiy1_vaotrang = driver.find_element(By.XPATH,var.khampha_luotthich_tranggoiy1_vaotrang1).text
        print(khampha_luotthich_tranggoiy1_vaotrang)
        logging.info("Trang - Khám phá")
        logging.info("check font-end: Lượt thích gợi ý 1 khi vào trang có giống nhau không?")
        logging.info(khampha_luotthich_tranggoiy1_vaotrang)
        logging.info(khampha_luotthich_tranggoiy1)
        logging.info(khampha_luotthich_tranggoiy1_vaotrang[0:10] == khampha_luotthich_tranggoiy1[0:10])
        time.sleep(1)



    def trangdathich(self):
        driver.implicitly_wait(15)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)
        #Thích sơm nhất
        trangdathich_tentranggoiy1 = driver.find_element(By.XPATH,var.khampha_tentranggoiy1).text
        print(trangdathich_tentranggoiy1)
        logging.info("Trang - Trang đã thích")
        logging.info("check font-end: Hiện tên trang đã thích 1 hay không")
        logging.info(trangdathich_tentranggoiy1)
        logging.info(trangdathich_tentranggoiy1 != None)

        trangdathich_linhvuc_tranggoiy1 = driver.find_element(By.XPATH,var.trangdathich_linhvuc_tranggoiy1).text
        print(trangdathich_linhvuc_tranggoiy1)
        logging.info("Trang - Trang đã thích")
        logging.info("check font-end: Hiện lĩnh vực trang đã thích 1 hay không")
        logging.info(trangdathich_linhvuc_tranggoiy1)
        logging.info(trangdathich_linhvuc_tranggoiy1 != None)

        driver.find_element(By.XPATH, var.trangdathich_goiy1_icom3cham).click()
        trangdathich_goiy1_trangthai = driver.find_element(By.XPATH,var.trangdathich_goiy1_trangthaibb).text
        print(trangdathich_goiy1_trangthai)
        logging.info("Trang - Trang đã thích")
        logging.info("check font-end: Trạng thái gợi ý 1 - Đã thích")
        logging.info(trangdathich_goiy1_trangthai)
        logging.info(trangdathich_goiy1_trangthai == "Đã thích")
        driver.find_element(By.XPATH, var.trang_trangdathich_sapxep).click()
        # Đã thích gần đây trước
        driver.find_element(By.XPATH, var.trang_trangdathich_sapxep_dathichgandaytruoc).click()
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trang_trangdathich_sapxep).click()
        try:
            check_sapxep_dathichganday= driver.find_element(By.XPATH,var.check_sapxep_dathichganday).is_displayed()
            logging.info("Trang - Trang đã thích")
            logging.info("check font-end: Đã thích gần đây trước - có icon dấu tích")
            logging.info(check_sapxep_dathichganday)
        except:
            logging.info("Trang - Trang đã thích")
            logging.info("check font-end: Đã thích gần đây trước - có icon dấu tích")
            logging.info("False")
        driver.find_element(By.XPATH, var.trang_trangdathich_sapxep).click()

        trangdathich_tentranggoiy2 = driver.find_element(By.XPATH,var.trangdathich_tentranggoiy2).text
        print(trangdathich_tentranggoiy2)
        logging.info("Trang - Trang đã thích")
        logging.info("check font-end: Hiện tên trang sau khi sắp xếp Đã thích gần đây trước không")
        logging.info(trangdathich_tentranggoiy2)
        logging.info(trangdathich_tentranggoiy2 != trangdathich_tentranggoiy1)

        #Gửi tin nhắn
        driver.find_element(By.XPATH, var.trang_trangdathich_guitinnhan).click()
        driver.find_element(By.XPATH, var.trang_trangdathich_guitinnhan_input).send_keys(data['trang']['trangdathich'])
        driver.find_element(By.XPATH, var.trang_trangdathich_guitinnhan_input).send_keys(Keys.ENTER)
        checK_trangdathich_tinnhan = driver.find_element(By.XPATH,var.checK_trangdathich_tinnhan1).text
        print(checK_trangdathich_tinnhan)
        logging.info("Trang - Trang đã thích")
        logging.info("check font-end: Gửi tinn nhắn - Test trang hoy")
        logging.info(checK_trangdathich_tinnhan)
        logging.info(checK_trangdathich_tinnhan =="Test trang hoy")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trang_trangdathich_guitinnhan_input).send_keys(data['trang']['trangdathich1'])
        driver.find_element(By.XPATH, var.trang_trangdathich_guitinnhan_input_x).click()
        time.sleep(1)


    def trangdathich_dau3cham(self):
        driver.implicitly_wait(15)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)
        # #Theo dõi
        # #Khi chưa click theo dõi
        driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        check_trangthaitrang_benngoai = driver.find_element(By.XPATH, var.check_trangthaitrang_benngoai).text
        driver.find_element(By.XPATH, var.trangdathich_xemtrangdau).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_bentrong).click()
        check_trangthaitrang_bentrong = driver.find_element(By.XPATH, var.check_trangthaitrang_bentrong).text
        print(check_trangthaitrang_benngoai)
        print(check_trangthaitrang_bentrong)
        logging.info("Trang - Trang đã thích - Theo dõi")
        logging.info("check font-end: Trạng thái bên ngoài trang khi chưa Theo dõi: " + check_trangthaitrang_benngoai)
        logging.info("check font-end: Trạng thái bên trong trang khi chưa theo dõi: " + check_trangthaitrang_bentrong)
        logging.info(check_trangthaitrang_benngoai ==check_trangthaitrang_bentrong)
        #Khi click vào theo dõi
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_theodoi).click()
        time.sleep(2.5)
        driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        check_trangthaitrang_benngoai = driver.find_element(By.XPATH, var.check_trangthaitrang_benngoai1).text
        driver.find_element(By.XPATH, var.trangdathich_xemtrangdau).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_bentrong).click()
        check_trangthaitrang_bentrong = driver.find_element(By.XPATH, var.check_trangthaitrang_bentrong).text
        # print(check_trangthaitrang_benngoai)
        # print(check_trangthaitrang_bentrong)
        logging.info("Trang - Trang đã thích - Theo dõi")
        logging.info("check font-end: Trạng thái bên ngoài trang khi đã chọn Theo dõi: " + check_trangthaitrang_benngoai)
        logging.info("check font-end: Trạng thái bên trong trang khi đã chọn theo dõi: " + check_trangthaitrang_bentrong)
        logging.info(check_trangthaitrang_benngoai ==check_trangthaitrang_bentrong)

        #Lưu
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        driver.find_element(By.XPATH, var.luu).click()              #Trang - Đang theo dõi -nút lưu không hoạt động
        # driver.find_element(By.XPATH, var.trangdathich_icom3cham_luu_no1).click()
        # driver.find_element(By.XPATH, var.xong).click()
        # time.sleep(1)
        # check_message_luutrang = driver.find_element(By.XPATH,var.check_message_luutrang1).text
        # print(check_message_luutrang)
        # logging.info("Trang - Trang đã thích - Lưu")
        # logging.info("check font-end: Message - ")
        # logging.info(check_message_luutrang == "Đã lưu vào no1")
        #
        # #Bỏ lưu
        # driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        # driver.find_element(By.XPATH, var.boluu).click()


        #Chia sẻ
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_chiase).click()
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_chiase_mota).send_keys(data['trang']['chiase_mota'])
        driver.find_element(By.XPATH, var.dang).click()
        time.sleep(2)
        checK_trangdathich_chiase_message = driver.find_element(By.XPATH,var.checK_trangdathich_chiase_message1).text
        print(checK_trangdathich_chiase_message)
        logging.info("Trang - Trang đã thích - Chia sẻ")
        logging.info("check font-end: Message - Đăng bài viết thành công.")
        logging.info(checK_trangdathich_chiase_message)
        logging.info(checK_trangdathich_chiase_message =="Đăng bài viết thành công.")
        time.sleep(0.5)
        driver.get("https://sn.emso.vn/user/truongvck33")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,1000)", "")

        #Vào trang cá nhân check chia sẻ trang
        checK_chiase_trang_tieude = driver.find_element(By.XPATH,var.checK_chiase_trang_tieude1).text
        print(checK_chiase_trang_tieude)
        logging.info("Trang - Trang đã thích - Chia sẻ")
        logging.info("check font-end: Vào trang cá nhân check Tiêu đề - Trần Quang Trường đã chia sẻ trang")
        logging.info(checK_chiase_trang_tieude)
        logging.info(checK_chiase_trang_tieude =="Trần Quang Trường\n đã chia sẻ trang")

        checK_chiase_trang_mota = driver.find_element(By.XPATH,var.checK_chiase_trang_mota1).text
        print(checK_chiase_trang_mota)
        logging.info("Trang - Trang đã thích - Chia sẻ")
        logging.info("check font-end: Vào trang cá nhân check Mô tả- " + data['trang']['chiase_mota'])
        logging.info(checK_chiase_trang_mota)
        logging.info(checK_chiase_trang_mota ==data['trang']['chiase_mota'])
        time.sleep(1)

    def loimoi(self):
        driver.implicitly_wait(15)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)
        try:
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_moibanbe).click()
        time.sleep(0.5)
        #Nút chọn người
        driver.find_element(By.XPATH, var.trang_moibanbe_nutchon).click()
        driver.find_element(By.XPATH, var.trang_moibanbe_nutchon_thong).click()
        check_trang_moibanbe_khongcoban = driver.find_element(By.XPATH,var.check_trang_moibanbe_khongcoban).text
        print(check_trang_moibanbe_khongcoban)
        logging.info("Trang - Trang đã thích - Mời bạn bè")
        logging.info("check font-end: Chọn nhóm không có bạn bè chung")
        logging.info(check_trang_moibanbe_khongcoban)
        logging.info(check_trang_moibanbe_khongcoban == "Không có dữ liệu")

        driver.find_element(By.XPATH, var.trang_moibanbe_nutchon).click()
        driver.find_element(By.XPATH, var.trang_moibanbe_nutchon_namtest).click()
        check_trang_moibanbe_nhomcobanchung = driver.find_element(By.XPATH,var.check_trang_moibanbe_nhomcobanchung).text
        print(check_trang_moibanbe_nhomcobanchung)
        logging.info("Trang - Trang đã thích - Mời bạn bè")
        logging.info("check font-end: Chọn nhóm có bạn bè chung - Ngọc Mai")
        logging.info(check_trang_moibanbe_nhomcobanchung)
        logging.info(check_trang_moibanbe_nhomcobanchung == "Ngọc Mai")

        driver.find_element(By.XPATH, var.trang_moibanbe_nutchon).click()
        driver.find_element(By.XPATH, var.trang_moibanbe_nutchon_tatcabanbe).click()
        check_trang_moibanbe_tatcabanbe = driver.find_element(By.XPATH,var.check_trang_moibanbe_tatcabanbe).text
        print(check_trang_moibanbe_tatcabanbe)
        logging.info("Trang - Trang đã thích - Mời bạn bè")
        logging.info("check font-end: Tất cả bạn bè")
        logging.info(check_trang_moibanbe_tatcabanbe)
        logging.info(check_trang_moibanbe_tatcabanbe == "hue nguyen")

        driver.find_element(By.XPATH, var.huenguyen).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.check_trang_moibanbe_tatcabanbe_guiloimoi).click()
        time.sleep(2)
        check_trang_moibanbe_damoi = driver.find_element(By.XPATH,var.huenguyen).text
        print(check_trang_moibanbe_damoi)
        logging.info("Trang - Trang đã thích - Mời bạn bè")
        logging.info("check font-end: Đã mời - hue nguyen")
        logging.info(check_trang_moibanbe_damoi)
        logging.info(check_trang_moibanbe_damoi == "hue nguyen")
        time.sleep(0.5)

        #Gửi lời mời - đồng ý
        login.login4(self, "nguyenhue608196@gmail.com", "atgmj123456")
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangchu_iconthongbao).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_iconthongbao_thongbaodautien).click()
        time.sleep(2)
        check_trang_loimoithichtrang = driver.find_element(By.XPATH,var.check_trang_loimoithichtrang).text
        print(check_trang_loimoithichtrang)
        logging.info("Trang - Trang đã thích - Mời bạn bè - hue nguyen")
        logging.info("check font-end: hue nguyen - xem thống báo - Lời mời thích trang")
        logging.info(check_trang_loimoithichtrang)
        logging.info(check_trang_loimoithichtrang == "Lời mời thích trang")
        time.sleep(0.5)
        driver.find_element(By.XPATH,var.chapnhan).click()
        check_trang_loimoithichtrang_dachapnhan = driver.find_element(By.XPATH,var.check_trang_loimoithichtrang_dachapnhan).text
        print(check_trang_loimoithichtrang_dachapnhan)
        logging.info("Trang - Trang đã thích - Mời bạn bè - hue nguyen")
        logging.info("check font-end: hue nguyen - xem thống báo - Lời mời thích trang - Đã chấp nhận")
        logging.info(check_trang_loimoithichtrang_dachapnhan)
        logging.info(check_trang_loimoithichtrang_dachapnhan == "  Đã chấp nhận")

        driver.find_element(By.XPATH,var.loimoithichtrang_xemtrang).click()
        time.sleep(2)
        driver.find_element(By.XPATH,var.loimoithichtrang_xemtrang_bothich).click()
        time.sleep(3)
        loimoithichtrang_xemtrang_dabothich = driver.find_element(By.XPATH,var.loimoithichtrang_xemtrang_dabothich1).text
        logging.info("Trang - Trang bạn bè mời")
        logging.info("check font-end: đã bỏ thích")
        logging.info(loimoithichtrang_xemtrang_dabothich)
        logging.info(loimoithichtrang_xemtrang_dabothich == "  Thích")
        time.sleep(2)

        #Gửi lời mời -Từ chối
        login.login4(self, "truongvck33@gmail.com", "atgmj123456")
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_trangdathich).click()
        time.sleep(2)

        try:
            driver.find_element(By.XPATH, var.trangdathich_icom3cham).click()
        except:
            driver.refresh()
            time.sleep(2)
            driver.get("https://sn.emso.vn/pages/liked")
        driver.find_element(By.XPATH, var.trangdathich_icom3cham_moibanbe).click()
        driver.find_element(By.XPATH, var.huenguyen).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.check_trang_moibanbe_tatcabanbe_guiloimoi).click()
        time.sleep(2)
        login.login4(self, "nguyenhue608196@gmail.com", "atgmj123456")
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_loimoi).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trang_loimoi_dau3cham).click()
        driver.find_element(By.XPATH, var.tuchoi).click()
        driver.find_element(By.XPATH, var.tuchoi).click()
        time.sleep(2)
        check_trang_loimoithichtrang_datuchoi = driver.find_element(By.XPATH,var.check_trang_loimoithichtrang_datuchoi).text
        print(check_trang_loimoithichtrang_datuchoi)
        logging.info("Trang - Trang đã thích - Mời bạn bè - hue nguyen")
        logging.info("check font-end: hue nguyen - xem thống báo - Lời mời thích trang - Đã từ chối")
        logging.info(check_trang_loimoithichtrang_datuchoi)
        logging.info(check_trang_loimoithichtrang_datuchoi == "  Đã từ chối")
        time.sleep(2)

        driver.find_element(By.XPATH,var.loimoithichtrang_xemtrang).click()
        time.sleep(2)
        loimoithichtrang_xemtrang_dabothich = driver.find_element(By.XPATH,var.loimoithichtrang_xemtrang_dabothich1).text
        logging.info("Trang - Trang bạn bè mời")
        logging.info("check font-end:xem trang - trạng thái đã từ chối")
        logging.info(loimoithichtrang_xemtrang_dabothich)
        logging.info(loimoithichtrang_xemtrang_dabothich == "  Thích")
        time.sleep(2)


    def taotrangmoi(self, tentrang, loaitrang, loaihinhkinhdoanh):
        driver.implicitly_wait(15)
        # login.login4(self, "truongvck33@gmail.com", "atgmj123456")
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trang_taotrangmoi).click()
        time.sleep(1)
        #Thông tin về trang
        driver.find_element(By.XPATH, var.taotrangmoi_thongtinvetrang).send_keys(tentrang)
        #Loai trang
        driver.find_element(By.XPATH, var.taotrangmoi_loaitrang).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, loaitrang)))
        element.click()
        #Loai hình kinh doanh
        driver.find_element(By.XPATH, var.taotrangmoi_loaihinhkinhdoanh).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, loaihinhkinhdoanh)))
        element.click()
        #Hạng mục
        driver.find_element(By.XPATH, var.taotrangmoi_hangmuc).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.taotrangmoi_hangmuc_giaitri)))
        element.click()

        driver.find_element(By.XPATH, var.taotrangmoi_hangmuc).click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.taotrangmoi_hangmuc_thietkethoitrang)))
        element.click()
        #Mô tả
        driver.find_element(By.XPATH, var.taotrangmoi_mota).send_keys(data['trang']['taotrangmoi_mota'])
        #Ảnh đai diện
        button = driver.find_element(By.XPATH, var.taotrangmoi_tailenanhdaidien)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhmes1.exe")
        time.sleep(1)
        #Ảnh bìaa
        button = driver.find_element(By.XPATH, var.taotrangmoi_tailenanhbia)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbiatrang.exe")
        time.sleep(1)

        driver.find_element(By.XPATH, var.taotrangmoi_taotrang).click()
        time.sleep(5)
        taotrangmoi_taotrang_loaitrang = driver.find_element(By.XPATH,var.taotrangmoi_taotrang_loaitrang).text
        logging.info("Trang - Tạo trang mới")
        logging.info("check font-end: Loại trang - " + tentrang)
        logging.info(taotrangmoi_taotrang_loaitrang)
        logging.info(taotrangmoi_taotrang_loaitrang == tentrang)
        time.sleep(1)
        #Xoá trang
        driver.find_element(By.XPATH, var.trang_caidat).click()
        driver.execute_script("window.scrollBy(0,900)", "")
        driver.find_element(By.XPATH, var.trang_caidat_xoatrang).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trang_caidat_xoatrang_gotrangvinhvien).click()
        time.sleep(3)

    def taotrangmoi_banhang(self):
        trang.taotrangmoi(self, data['trang']['trangbanhang'], var.banhang, var.doanhnghiep)

    def taotrangmoi_bankhoahoc(self):
        trang.taotrangmoi(self, data['trang']['trangbankhoahoc'], var.bankhoahoc, var.canhan)

    def taotrangmoi_trangnoidung(self):
        trang.taotrangmoi(self, data['trang']['trangnoidung'], var.trangnoidung, var.doanhnghiep)


    def trang_gioithieu(self):
        driver.implicitly_wait(15)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        #Trang của bạn
        #Trường test bản tin
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(2)
        #Giới thiệu
        driver.find_element(By.XPATH, var.trang_gioithieu).click()
        #Nhập vị trí
        # driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri).click()
        # time.sleep(1)
        driver.find_element(By.XPATH, var.trang_gioithieu_datlaivitri).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban).send_keys(data['trang']['vitri'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hanoi)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        #Mô tả
        driver.find_element(By.XPATH, var.trang_gioithieu_mota).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_mota_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_mota_input).send_keys(data['trang']['gioithieu_mota'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_x).click()

        #Hạng mục
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri_x).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri_input).send_keys(data['trang']['gioithieu_trangphucquanao'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangphucquanao)))
        element.click()
        driver.implicitly_wait(5)
        try:
            gioithieu_dautich = driver.find_element(By.XPATH, var.gioithieu_dautich).is_displayed()
            logging.info("Trang - Trang của bạn - Giới thiệu ")
            logging.info("check font-end: Hạng mục - có dấu tích không không")
            logging.info(gioithieu_dautich)
            driver.find_element(By.XPATH, var.gioithieu_dautich).click()          #Giới thiệu - hạng mục chưa có dấu tích xanh khi lưu
        except NoSuchElementException:
            logging.info("Trang - Trang của bạn - Giới thiệu ")
            logging.info("check font-end: Hạng mục - có dấu tích không không")
            logging.info("False")
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_x).click()
        driver.implicitly_wait(15)

        #Số điện thoại
        driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input).send_keys(data['trang']['gioithieu_sdt'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_x).click()

        #Email
        driver.find_element(By.XPATH, var.trang_gioithieu_email).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_email_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_email_input).send_keys(data['trang']['gioithieu_email'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_x).click()

        #Web
        driver.find_element(By.XPATH, var.trang_gioithieu_web).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_web_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_web_input).send_keys(data['trang']['gioithieu_web'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_x).click()

        #Thông tin bổ sung
        driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung_input).send_keys(data['trang']['gioithieu_thongtinbosung'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.icon_x).click()
        time.sleep(1)

        #Check giới thiệu
        #Mô tả
        driver.find_element(By.XPATH, var.trang_gioithieu_mota)
        check_trang_gioithieu_mota = driver.find_element(By.XPATH,var.check_trang_gioithieu_mota1).text
        print(check_trang_gioithieu_mota)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Mô tả - "+ data['trang']['gioithieu_mota'])
        logging.info(check_trang_gioithieu_mota == data['trang']['gioithieu_mota'])
        #Hang mục
        check_trang_gioithieu_hangmuc = driver.find_element(By.XPATH,var.check_trang_gioithieu_hangmuc1).text
        print(check_trang_gioithieu_hangmuc)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Hạng mục - "+ data['trang']['gioithieu_trangphucquanao'])
        logging.info(check_trang_gioithieu_hangmuc == data['trang']['gioithieu_trangphucquanao'])
        #số điện thoại
        check_trang_gioithieu_sodienthoai = driver.find_element(By.XPATH,var.check_trang_gioithieu_sodienthoai1).text
        print(check_trang_gioithieu_sodienthoai)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Số điện thoại - "+ data['trang']['gioithieu_sdt'])
        logging.info(check_trang_gioithieu_sodienthoai == data['trang']['gioithieu_sdt'])
        #email
        check_trang_gioithieu_email = driver.find_element(By.XPATH,var.check_trang_gioithieu_email1).text
        print(check_trang_gioithieu_email)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Email - "+ data['trang']['gioithieu_email'])
        logging.info(check_trang_gioithieu_email == data['trang']['gioithieu_email'])
        #web
        check_trang_gioithieu_web = driver.find_element(By.XPATH,var.check_trang_gioithieu_web1).text
        print(check_trang_gioithieu_web)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Web - "+ data['trang']['gioithieu_web'])
        logging.info(check_trang_gioithieu_web == data['trang']['gioithieu_web'])
        #Thông tin bổ sung
        check_trang_gioithieu_thongtinbosung = driver.find_element(By.XPATH,var.check_trang_gioithieu_thongtinbosung1).text
        print(check_trang_gioithieu_thongtinbosung)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Thông tin bổ sung - "+ data['trang']['gioithieu_thongtinbosung'])
        logging.info(check_trang_gioithieu_thongtinbosung == data['trang']['gioithieu_thongtinbosung'])
        time.sleep(0.5)




    def trang_gioithieu_dulieusai(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        #Trang của bạn
        #Trường test bản tin
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(2)
        #Giới thiệu
        driver.find_element(By.XPATH, var.trang_gioithieu).click()
        #Nhập vị trí
        driver.find_element(By.XPATH, var.trang_gioithieu_datlaivitri).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban).send_keys(data['trang']['vitri_sai'])
        time.sleep(1.5)
        check_trang_gioithieu_vitrisai = driver.find_element(By.XPATH,var.check_trang_gioithieu_vitrisai1).text
        print(check_trang_gioithieu_vitrisai)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Vị trí sai - "+ check_trang_gioithieu_vitrisai)
        logging.info(check_trang_gioithieu_vitrisai == "Không có dữ liệu...")

        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban).send_keys(data['trang']['vitri1'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_langson)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        #Mô tả
        driver.find_element(By.XPATH, var.trang_gioithieu_mota).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_mota_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_mota_input).send_keys(data['trang']['gioithieu_mota_dai'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        check_trang_gioithieu_motadai = driver.find_element(By.XPATH,var.check_trang_gioithieu_motadai1).text
        print(check_trang_gioithieu_motadai)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Mô tả dài - "+ check_trang_gioithieu_motadai)
        logging.info(check_trang_gioithieu_motadai == "Mô tả không được quá 255 ký tự")

        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_mota_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_mota_input).send_keys(data['trang']['gioithieu_mota1'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.gioithieu_dautich_sai).click()
        driver.find_element(By.XPATH, var.icon_x).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trang_gioithieu_mota)

        #Hạng mục
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri).click()
        time.sleep(1)
        #hạng mục 1
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri_input).send_keys(data['trang']['gioithieu_trangphucquanao'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangphucquanao)))
        element.click()
        #hạng mục 2
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri_input).send_keys(data['trang']['gioithieu_phongcanh'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.phongcanh)))
        element.click()
        #hạng mục 3
        driver.find_element(By.XPATH, var.trang_gioithieu_webgiaitri_input).send_keys(data['trang']['gioithieu_trangtrinhacua'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangtrinhacua)))
        element.click()
        check_trang_gioithieu_hangmuc_daiqua3 = driver.find_element(By.XPATH,var.check_trang_gioithieu_hangmuc_daiqua3).text
        print(check_trang_gioithieu_hangmuc_daiqua3)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Hjang mục - "+ check_trang_gioithieu_hangmuc_daiqua3)
        logging.info(check_trang_gioithieu_hangmuc_daiqua3 == "Chỉ được chọn tối đa 3 hạng mục")
        time.sleep(1)
        driver.find_element(By.XPATH, var.trang_gioithieu_hangmuc_x).click()
        driver.find_element(By.XPATH, var.trang_gioithieu_hangmuc_x).click()
        driver.find_element(By.XPATH, var.trang_gioithieu_hangmuc_x).click()
        driver.implicitly_wait(5)
        try:
            gioithieu_dautich = driver.find_element(By.XPATH, var.gioithieu_dautich).is_displayed()
            logging.info("Trang - Trang của bạn - Giới thiệu ")
            logging.info("check font-end: Hạng mục - có dấu tích không không")
            logging.info(gioithieu_dautich)
            driver.find_element(By.XPATH, var.gioithieu_dautich).click()          #Giới thiệu - hạng mục chưa có dấu tích xanh khi lưu
        except NoSuchElementException:
            logging.info("Trang - Trang của bạn - Giới thiệu ")
            logging.info("check font-end: Hạng mục - có dấu tích không không")
            logging.info("False")
        driver.implicitly_wait(15)
        driver.find_element(By.XPATH, var.icon_x).click()

        #Số điện thoại
        driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai).click()
        time.sleep(1)
        #Số điện thoại ngắn
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input).send_keys(data['trang']['gioithieu_sdt_ngan'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        check_trang_gioithieu_sodienthoai_ngan = driver.find_element(By.XPATH,var.check_trang_gioithieu_sodienthoai_ngan1).text
        print(check_trang_gioithieu_sodienthoai_ngan)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Số điện thoại ngắn - " + check_trang_gioithieu_sodienthoai_ngan)
        logging.info(check_trang_gioithieu_sodienthoai_ngan == "Số điện thoại không hợp lệ")
        time.sleep(1)
        #Số điện thoại dài
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input).send_keys(data['trang']['gioithieu_sdt_dai'])
        driver.find_element(By.XPATH, var.gioithieu_dautich_sai).click()
        check_trang_gioithieu_sodienthoai_dai = driver.find_element(By.XPATH,var.check_trang_gioithieu_sodienthoai_ngan1).text
        print(check_trang_gioithieu_sodienthoai_dai)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Số điện thoại dài - " + check_trang_gioithieu_sodienthoai_dai)
        logging.info(check_trang_gioithieu_sodienthoai_dai == "Số điện thoại không hợp lệ")
        time.sleep(2)
        #Số điện thoại hợp lệ
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_sodienthoai_input).send_keys(data['trang']['gioithieu_sdt_trung'])
        driver.find_element(By.XPATH, var.gioithieu_dautich_sai).click()
        driver.find_element(By.XPATH, var.icon_x).click()
        time.sleep(2)
        check_trang_gioithieu_sodienthoai = driver.find_element(By.XPATH,var.check_trang_gioithieu_sodienthoai1).text
        print(check_trang_gioithieu_sodienthoai)

        #Email
        driver.find_element(By.XPATH, var.trang_gioithieu_email).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_email_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_email_input).send_keys(data['trang']['gioithieu_email_dulieusai'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(1)
        check_trang_gioithieu_email_dulieusai = driver.find_element(By.XPATH,var.check_trang_gioithieu_email_dulieusai1).text
        print(check_trang_gioithieu_email_dulieusai)
        logging.info("Trang - Trang của bạn - Giới thiệu ")
        logging.info("check font-end: Email dữ liệu sai - "+ check_trang_gioithieu_email_dulieusai)
        logging.info(check_trang_gioithieu_email_dulieusai == "email không hợp lệ")
        time.sleep(1)

        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_email_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_email_input).send_keys(data['trang']['gioithieu_email1'])
        driver.find_element(By.XPATH, var.gioithieu_dautich_sai).click()
        driver.find_element(By.XPATH, var.icon_x).click()
        time.sleep(1)

        #Web
        driver.find_element(By.XPATH, var.trang_gioithieu_web).click()
        time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_web_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_web_input).send_keys(data['trang']['gioithieu_web_dulieusai'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        time.sleep(1)
        driver.implicitly_wait(3)
        try:
            check_trang_gioithieu_web_dulieusai = driver.find_element(By.XPATH,var.check_trang_gioithieu_web_dulieusai1).is_displayed()
            logging.info("Trang - Trang của bạn - Giới thiệu ")
            logging.info("check font-end: Web dữ liệu sai - website không hợp lệ")
            logging.info(check_trang_gioithieu_web_dulieusai)
        except NoSuchElementException:
            logging.info("Trang - Trang của bạn - Giới thiệu ")
            logging.info("check font-end: Web dữ liệu sai - website không hợp lệ")
            logging.info("False")
        time.sleep(1)

        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_web_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_web_input).send_keys(data['trang']['gioithieu_web1'])
        try:
            driver.find_element(By.XPATH, var.gioithieu_dautich_sai).click()
        except:
            driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        driver.find_element(By.XPATH, var.icon_x).click()
        time.sleep(1)

        driver.implicitly_wait(15)
        #Thông tin bổ sung
        driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung).click()
        time.sleep(1)
        #Dài quá 50k ký tự
        # xoa = driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung_input)     #dài quá đơ máy luôn
        # xoa.send_keys(Keys.CONTROL, "a")
        # driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung_input).send_keys(data['trang']['gioithieu_thongtinbosung_daiqua50k'])
        # driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        # time.sleep(1)
        # check_trang_gioithieu_thongtinbosung_daiqua50k = driver.find_element(By.XPATH,var.check_trang_gioithieu_thongtinbosung_daiqua50k).text
        # print(check_trang_gioithieu_thongtinbosung_daiqua50k)
        # logging.info("Trang - Trang của bạn - Giới thiệu ")
        # logging.info("check font-end: Thông tin bổ sung dài quá 50k ký tự - "+ check_trang_gioithieu_thongtinbosung_daiqua50k)
        # logging.info(check_trang_gioithieu_thongtinbosung_daiqua50k == "Thông tin bổ sung không được quá 50000 ký tự")
        # time.sleep(1)
        xoa = driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung_input)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.trang_gioithieu_thongtinbosung_input).send_keys(data['trang']['gioithieu_thongtinbosung1'])
        driver.find_element(By.XPATH, var.gioithieu_dautich).click()
        driver.find_element(By.XPATH, var.icon_x).click()
        time.sleep(3)


    def anh(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        #Trang của bạn
        #Trường test bản tin
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(2)
        #Ảnh
        driver.find_element(By.XPATH, var.trang_anh).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        #ảnh
        time.sleep(1)
        driver.find_element(By.XPATH, var.trang_anh_xemanhdau).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.thich).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.vietbinhluan).send_keys(data['trang']['anh_binhluan'])
        driver.find_element(By.XPATH, var.vietbinhluan).submit()
        time.sleep(2)
        driver.find_element(By.XPATH, var.esc).click()

        #album
        # driver.find_element(By.XPATH, var.trang_anh_album).click()
        button = driver.find_element(By.XPATH, var.trang_anh_album)
        driver.execute_script("arguments[0].click();", button)

        driver.find_element(By.XPATH, var.trang_anh_alum_taomoi).click()
        time.sleep(1.5)
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_ten).send_keys(data['trangcanhan_anh_video']['trangcanhan_anh_anh'])
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_mota).send_keys(data['trangcanhan_anh_video']['trangcanhan_anh_mota'])
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_tailen).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia1.exe")
        time.sleep(2)
        #chọn vị trí
        driver.find_element(By.XPATH, var.trang_alum_chonvitri).click()
        driver.find_element(By.XPATH, var.trang_gioithieu_nhapvitri_chonvitricuaban).send_keys(data['trang']['vitri1'])
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_langson)))
        element.click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangcanhan_anh_album_anhtailen_chuthich).send_keys(data['trangcanhan_anh_video']['chuthich'])
        # driver.find_element(By.XPATH, var.trangcanhan_anh_album_dang).click()
        time.sleep(3)
        driver.back()
        time.sleep(1)
        # driver.find_element(By.XPATH, var.trangcanhan_anh_album_iconxoa).click()        #Chưa có dấu 3 chấm để xoá và cập nhật album
        # driver.find_element(By.XPATH, var.trangcanhan_anh_album_xoa).click()          #Xem album bị trắng trang
        # time.sleep(1.5)
        # driver.find_element(By.XPATH, var.trangcanhan_khoanhkhac_xemvideo_xoa).click()
        # time.sleep(1)


    def music(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        #Trang của bạn
        #Trường test bản tin
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trang_music).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        #Phổ biến nhất
        tenbainhac1 = driver.find_element(By.XPATH, var.tenbainhac1).text
        logging.info("Trang - Music - Phổ biến nhất")
        logging.info("check font-end: Tên bài hát phổ biến nhất 1 " + tenbainhac1)
        logging.info(tenbainhac1 == "(여자)아이들((G)I-DLE) - '퀸카 (Queencard)' Official Music Video")

        tacgia1 = driver.find_element(By.XPATH, var.tacgia1).text
        logging.info("Trang - Music - Phổ biến nhất")
        logging.info("check font-end: Tác giả bài hát phổ biến nhất 1 " + tacgia1)
        logging.info(tacgia1 == "Trường test bản tin")

        # driver.find_element(By.XPATH, var.trang_music_phobiennhat_nghebai1).click()
        button = driver.find_element(By.XPATH, var.trang_music_phobiennhat_nghebai1)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        driver.implicitly_wait(3)
        #Chọn xem có hiển thị popup nghe không
        try:
            tenbainhac1_dangnghe = driver.find_element(By.XPATH, var.tenbainhac1_dangnghe1).text
            logging.info("Trang - Music - Phổ biến nhất")
            logging.info("check font-end: nghe bài số 1 - Có hiển thị popup nghe không")
            logging.info(tenbainhac1_dangnghe == tenbainhac1)
        except NoSuchElementException:
            logging.info("Trang - Music - Phổ biến nhất")
            logging.info("check font-end: nghe bài số 1 - có hiển thị popup nghe không")
            logging.info("False")

        try:
            tenbainhac1_dangnghe_trangthai = driver.find_element(By.XPATH, var.tenbainhac1_dangnghe_trangthai).is_displayed()
            logging.info("Trang - Music - Phổ biến nhất")
            logging.info("check font-end: nghe bài số 1 - Có nghe được bài số 1 không")
            logging.info(tenbainhac1_dangnghe_trangthai)
        except NoSuchElementException:
            logging.info("Trang - Music - Phổ biến nhất")
            logging.info("check font-end: nghe bài số 1 - Có nghe được bài số 1 không")
            logging.info("False")
        driver.implicitly_wait(15)
        time.sleep(1)

        #Fan cũng thích
        driver.find_element(By.XPATH, var.fancungthich1).click()
        check_trang_fancungthich = driver.find_element(By.XPATH, var.check_trang_fancungthich1).text
        logging.info("Trang - Music - Fan cũng thích")
        logging.info("check font-end: xem được trang hâhhah không")
        logging.info(check_trang_fancungthich == "hâhhah")
        driver.back()
        time.sleep(3)



    def video(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        #Trang của bạn
        #Trường test bản tin
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trang_video).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        #Phổ biến nhất
        try:
            check_trang_video_phobiennhat = driver.find_element(By.XPATH,var.check_trang_video_phobiennhat1).is_displayed()
            print(check_trang_video_phobiennhat)
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Phổ biến nhất - Có video hiển thị hay không")
            logging.info(check_trang_video_phobiennhat)
        except NoSuchElementException:
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Phổ biến nhất - Có video hiển thị hay không")
            logging.info("False")

        #Bài đăng
        try:
            check_trang_video_baidang = driver.find_element(By.XPATH,var.check_trang_video_baidang1).is_displayed()
            print(check_trang_video_baidang)
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Tất cả video - Bài đăng - Có video hiển thị hay không")
            logging.info(check_trang_video_baidang)
        except NoSuchElementException:
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Tất cả video - Bài đăng - Có video hiển thị hay không")
            logging.info("False")

        #Khoảnh khăc
        driver.find_element(By.XPATH, var.trang_video_khoanhkhac).click()
        time.sleep(2)
        try:
            check_trang_video_khoanhkhac = driver.find_element(By.XPATH,var.check_trang_video_khoanhkhac1).is_displayed()
            print(check_trang_video_khoanhkhac)
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Tất cả video - Khoảnh khắc - Có video hiển thị hay không")
            logging.info(check_trang_video_khoanhkhac)
        except  NoSuchElementException:
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Tất cả video - Khoảnh khắc - Có video hiển thị hay không")
            logging.info("False")

        #Danh sách phát
        driver.find_element(By.XPATH, var.trang_video_danhsachphat).click()
        time.sleep(2)
        try:
            check_trang_video_danhsachphat = driver.find_element(By.XPATH,var.check_trang_video_danhsachphat1).is_displayed()
            print(check_trang_video_danhsachphat)
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Tất cả video - Danh sách phát - Danh sách có hiển thị hay không")
            logging.info(check_trang_video_danhsachphat)
        except  NoSuchElementException:
            logging.info("Trang - Trang của bạn - Video")
            logging.info("check font-end: Tất cả video - Danh sách phát - Danh sách có hiển thị hay không")
            logging.info("False")
        time.sleep(1)

        #Tạo danh sách phát
        driver.find_element(By.XPATH, var.trang_video_taodanhsachphat).click()
        driver.find_element(By.XPATH, var.trang_video_taodanhsachphat_viettieude).send_keys(data['trang']['danhsachphat_tieude'])
        driver.find_element(By.XPATH, var.trang_video_taodanhsachphat_mota).send_keys(data['trang']['danhsachphat_mota'])
        time.sleep(1)
        driver.find_element(By.XPATH, var.trang_video_taodanhsachphat_tailenanhbia).click()
        time.sleep(1)
        subprocess.Popen("C:/Users/Admin/PycharmProjects/pythonProject/import/anhbia2.exe")
        time.sleep(1)
        driver.find_element(By.XPATH, var.dang).click()
        time.sleep(3)

        #Xem danh sách phát vừa tạo
        driver.find_element(By.XPATH, var.danhsachphat_xem).click()
        time.sleep(1)
        #Chọn video 1
        driver.find_element(By.XPATH, var.danhsachphat_xem_themvideo).click()
        driver.find_element(By.XPATH, var.danhsachphat_xem_themvideo_timkiemvideo).send_keys(data['trang']['timkiem_video1'])
        driver.find_element(By.XPATH, var.danhsachphat_xem_themvideo_chonvideo1).click()
        #Chọn video 2
        xoa = driver.find_element(By.XPATH, var.danhsachphat_xem_themvideo_timkiemvideo)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.danhsachphat_xem_themvideo_timkiemvideo).send_keys(data['trang']['timkiem_video2'])
        driver.find_element(By.XPATH, var.danhsachphat_xem_themvideo_chonvideo1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.luu).click()
        time.sleep(1)
        check_danhsachphat_themvideo = driver.find_element(By.XPATH, var.check_danhsachphat_themvideo1).text
        logging.info("Trang - Video - Danh sách phát - Thêm video")
        logging.info("check font-end: Message - Thêm video vào danh sách phát thành công")
        logging.info(check_danhsachphat_themvideo == "Thêm video vào danh sách phát thành công")
        #Xoá video
        driver.find_element(By.XPATH, var.danhsachphat_icon3chamxoavideo1).click()
        driver.find_element(By.XPATH, var.danhsachphat_xoavideo1).click()
        driver.find_element(By.XPATH, var.xoa).click()
        check_danhsachphat_xoavideo = driver.find_element(By.XPATH, var.check_danhsachphat_xoavideo1).text
        logging.info("Trang - Video - Danh sách phát - Xoá video")
        logging.info("check font-end: Message - Xoá video thành công")
        logging.info(check_danhsachphat_xoavideo == "Xoá video thành công")

        #Dấu 3 chấm của danh sách phát
        #Chỉnh sửa danh sách phát
        driver.find_element(By.XPATH, var.danhsachphat_icon3cham).click()
        driver.find_element(By.XPATH, var.danhsachphat_icon3cham_chinhsuadanhsachphat).click()
        xoa = driver.find_element(By.XPATH, var.chinhsuadanhsachphat_mota)
        xoa.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.chinhsuadanhsachphat_mota).send_keys(data['trang']['danhsachphat_mota1'])
        # driver.find_element(By.XPATH, var.capnhat).click()        #Trang - video - dánh sách phát - chỉnh sửa - bị trắng trang
        driver.find_element(By.XPATH, var.huy).click()
        time.sleep(2)
        #Sao chép ID danh sách phát
        driver.find_element(By.XPATH, var.danhsachphat_icon3cham).click()
        driver.find_element(By.XPATH, var.danhsachphat_icon3cham_saochepid).click()
        check_danhsachphat_saochepid = driver.find_element(By.XPATH, var.check_danhsachphat_saochepid1).text
        logging.info("Trang - Video - Danh sách phát - Sao chép id")
        logging.info("check font-end: Message - Sao chép id thành công")
        logging.info(check_danhsachphat_saochepid == "Sao chép id thành công")
        time.sleep(2)
        #Xoá
        driver.find_element(By.XPATH, var.xoa1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.xoa).click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,800)", "")
        driver.implicitly_wait(3)
        try:
            check_danhsachphat2 = driver.find_element(By.XPATH, var.check_danhsachphat2).is_displayed()
            logging.info("Trang - Video - Danh sách phát - Xem - Xoá")
            logging.info("check font-end: Xoá danh sách phát thành công")
            logging.info("Fasle")
        except NoSuchElementException:
            logging.info("Trang - Video - Danh sách phát - Xem - Xoá")
            logging.info("check font-end: Xoá danh sách phát thành công")
            logging.info("True")
        time.sleep(2)


    def cuahang(self):              #Tài khoản test
        driver.implicitly_wait(15)
        time.sleep(1.5)
        button = driver.find_element(By.XPATH, var.icon_trang)
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        #Trang của bạn
        #A12
        driver.find_element(By.XPATH, var.trang_trangcuaban).click()
        driver.find_element(By.XPATH, var.trang_trangcuaban_truongtest).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.trang_cuahang).click()
        driver.execute_script("window.scrollBy(0,400)", "")
        time.sleep(4)
        #Mã giảm giá của shop
        try:
            trang_cuahang_magiamgia = driver.find_element(By.XPATH, var.trang_cuahang_magiamgia1).is_displayed()
            logging.info("Trang - Cửa hàng - Mã giảm giá")
            logging.info("check font-end: Shop có mã giảm giá không?")
            logging.info(trang_cuahang_magiamgia)
        except NoSuchElementException:
            logging.info("Trang - Cửa hàng - Mã giảm giá")
            logging.info("check font-end: Shop có mã giảm giá không?")
            logging.info("False")





