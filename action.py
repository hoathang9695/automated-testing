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
        # driver.find_element(By.XPATH, var.trangcanhan).click()
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
        time.sleep(5)
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
        time.sleep(5)
    def anhdaidien_tuanhcosan(self):
        driver.implicitly_wait(15)
        # Chọn từ 1 ảnh có sẵn
        # huỷ
        driver.find_element(By.XPATH, var.trangcanhan_iconmayanh).click()
        time.sleep(2)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonanhthu2).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.capnhatanhdaidien_chonanhcosan_luu).click()
        time.sleep(5)
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
        time.sleep(1)
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
                logging.info((res['start_date']) == "2019-10-16")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học")
                logging.info("check back-end: Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_ngayketthuc'])
                logging.info((res['end_date']) == "2023-10-08T00:00:00.000+07:00")

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
                logging.info((res['life_event']['start_date']) == "2019-10-16")

                logging.info("check back-end: Trang cá nhân - Giới thiệu - Công việc và học vấn - Đại học - Xem sự kiện trong đời")
                logging.info("check back-end: Đại học - Ngày kết thúc - " + data['trangcanhan_gioithieu_congviecvahocvan']['daihoc_ngayketthuc'])
                logging.info((res['life_event']['end_date']) == "2023-10-08T00:00:00.000+07:00")

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
        logging.info(check_daihoc_ngaythang == "16 tháng 10, 2019")

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
        driver.find_element(By.XPATH, var.thongtincoban_icon_lienket).click()
        driver.find_element(By.XPATH, var.thongtincoban_lienket_chinhsua).click()
        driver.find_element(By.XPATH, var.thongtincoban_lienket_input).click()
        thongtincoban_lienket1 = driver.find_element(By.XPATH, var.thongtincoban_lienket_input)
        thongtincoban_lienket1.send_keys(Keys.CONTROL, "a")
        driver.find_element(By.XPATH, var.thongtincoban_lienket_input).send_keys(data['trangcanhan_gioithieu_thongtincoban']['lienket_dulieusai'])
        driver.find_element(By.XPATH, var.thongtincoban_lienket_luu).click()
        time.sleep(1)
        # thongtincoban_lienket_dulieusai = driver.find_element(By.XPATH, var.thongtincoban_lienket_fe_dulieusai).text
        # logging.info("Trang cá nhân - Giới thiệu - Thông tin cơ bản - Các trang web và liên kết xã hội")
        # logging.info("check font-end: Liên kết(nhập sai định dạng web) - message: URL You provided invalid URL")
        # logging.info(thongtincoban_lienket_dulieusai == data['trangcanhan_gioithieu_thongtincoban']['lienket'])

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
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu).click()
        # time.sleep(0.5)
        # driver.find_element(By.XPATH, var.sukientrongdoi).click()
        # driver.find_element(By.XPATH, var.sukientrongdoi_iconxoa_dulich).click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, var.sukientrongdoi_xoa_dulich).click()
        # time.sleep(2)
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
        print(check_ngocmai)

        logging.info("Trang cá nhân - Bạn bè  - Tất cả bạn bè - Xem trang cá nhân của bạn bè")
        logging.info("check font-end: Trang cá nhân của - " + data['trangcanhan_banbe']['trangcanhan_banbe_ngocmai'])
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
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb2).click()
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
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - Không có bạn bè để hiển thị.")
        logging.info(check_nguoila_riengtu)
        logging.info(check_nguoila_riengtu == "Không có bạn bè để hiển thị.")
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
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb2).click()
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
        check_banbe_riengtu = driver.find_element(By.XPATH, var.check_nguoila_riengtu3).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - bạn bè")
        print(check_banbe_riengtu)
        print("aa")
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - Không hiển thị danh sách bạn bè.")
        logging.info(check_banbe_riengtu == "Không có bạn bè để hiển thị.")
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
        driver.find_element(By.XPATH, var.trangcanhan_chinhsuaquyenriengtu_icon_dsbb2).click()
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
        check_nguoila_congkhai = driver.find_element(By.XPATH, var.check_banbe_quyencongkhai).text
        logging.info("Trang cá nhân - bạn bè - chỉnh sửa quyền riêng tư - Công khai")
        logging.info("check font-end: login bằng tài khoản khác(chưa kết bạn) và check  - xem được bạn bè")
        logging.info("khác" + check_nguoila_congkhai)
        logging.info(check_nguoila_congkhai != "Không có bạn bè để hiển thị.")
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
        # driver.find_element(By.XPATH, var.trangcanhan_gioithieu_songtai_input).send_keys(data['trangcanhan_gioithieu_tongquan']['songtai'])
        # wait = WebDriverWait(driver, 10)
        # chon_hanoi = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hanoi)))
        # chon_hanoi.click()
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
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + songtai3[7::])
                logging.info(res['general_information']['place_live']['title'] == tongquan_songtai1 == noitungsong_songtai1 == songtai2[9::] == songtai3[7::])

                #đến từ
                logging.info("check back-end, font-end trường: Trang cá nhân - Đến từ ")
                logging.info("respone: " + res['general_information']['hometown']['title'])
                logging.info("Giới thiêu - Tổng quan: " + tongquan_dentu1)
                logging.info("Giới thiêu - Nơi từng sống: " + noitungsong_dentu1)
                logging.info("Giới thiệu - Trang cá nhân: " + dentu2[7::])
                logging.info("Giới thiệu - Chỉnh sửa trang cá nhân: " + dentu3[9::])
                logging.info(res['general_information']['hometown']['title'] == tongquan_dentu1 == noitungsong_dentu1 == dentu2[7::] == dentu3[9::])

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
        driver.find_element(By.XPATH, var.hoatdong_x).click()
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
        time.sleep(30)

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
        driver.find_element(By.XPATH, var.camxuc_hoatdong_x).click()

        driver.find_element(By.XPATH, var.camxuc_hoatdong).click()
        driver.find_element(By.XPATH, var.camxuc_hoatdong_hoatdong).click()
        driver.find_element(By.XPATH, var.hoatdong_dangxem).click()
        driver.find_element(By.XPATH, var.hoatdong_x).click()
        time.sleep(1)
        check_taobaiviet_hoatdong = driver.find_element(By.XPATH,var.check_taobaiviet_hoatdong1).text
        logging.info("Trang chủ - Cảm xúc/Hoạt động")
        logging.info("check font-end: đang xem")
        logging.info(check_taobaiviet_hoatdong)
        logging.info(check_taobaiviet_hoatdong == "đang xem")
        driver.find_element(By.XPATH, var.camxuc_hoatdong_x).click()

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
        check_menu_name14 = driver.find_element(By.XPATH,var.check_menu_name13).text
        logging.info("Trang chủ - Menu - Ký niệm")
        logging.info("check font-end: Tiêu đề: " + check_menu_name13)
        logging.info(check_menu_name14 == "Ký niệm")

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
        logging.info(check_taobaimoment == "Tạo bài moment")
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
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_icongif_anh1).click()

        #Nhãn dán
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_1).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_1_loving).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_2).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_3).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_nhandan_3_chonnhandan).click()

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
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_lichsu).click()

        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_page1).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_bieutuongcamxuc_chon).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_input).click()
        #Like
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_like).click()
        driver.find_element(By.XPATH, var.trangchu_tinnhanmoi_like).click()
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
        # driver.find_element(By.XPATH, var.emsochat_caidathopthoai).click()
        # driver.find_element(By.XPATH, var.emsochat_caidathopthoai_trangcanhan).click()
        # time.sleep(2)
        # driver.back()
        # time.sleep(2)

        #gửi text
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(data['trangchu_tinnhan']['input1'])
        driver.find_element(By.XPATH, var.emsochat_input).click()
        driver.find_element(By.XPATH, var.emsochat_input).send_keys(Keys.ENTER)
        time.sleep(2)

        #xoá, gỡ bỏ
        chat_hover = driver.find_element(By.XPATH, var.chat_hover1)
        actions = ActionChains(driver)
        actions.move_to_element(chat_hover).perform()
        time.sleep(1)
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
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
        actions.move_to_element(chat_hover).perform()
        time.sleep(1)
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
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
        actions.move_to_element(chat_hover).perform()
        xemthem = driver.find_element(By.XPATH, var.emsochat_input_iconxemthem)
        actions.move_to_element(xemthem).click().perform()
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_chuyentiep).click()
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
        driver.find_element(By.XPATH, var.emsochat_chuyentiep_timkiem_x).click()
        time.sleep(0.5)

        #Gim
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
        actions.move_to_element(chat_hover).perform()
        actions.move_to_element(xemthem).click().perform()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_iconxemthem_gim).click()
        time.sleep(1)

        #Trả lời
        actions.move_to_element(chat_hover).perform()
        traloi = driver.find_element(By.XPATH, var.emsochat_input_icontraloi)
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
        try:
            chat_hover1 = driver.find_element(By.XPATH, var.chat_hover2)
            actions.move_to_element(chat_hover1).perform()
            actions.move_to_element(chat_hover1).perform()
            print("r1")
            time.sleep(1)
            baytocamxuc = driver.find_element(By.XPATH, var.emsochat_input_iconbaytocamxuc)
            actions.move_to_element(baytocamxuc).perform()
            time.sleep(2)
            driver.find_element(By.XPATH, var.icon_yeuthich).click()
            time.sleep(1)
        except:
            chat_hover1 = driver.find_element(By.XPATH, var.chat_hover2)
            actions.move_to_element(chat_hover1).perform()
            actions.move_to_element(chat_hover1).perform()
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

        # Tuỳ chỉnh đoạn chat
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
        #màu mặc định
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_doichude).click()
        time.sleep(1)
        driver.find_element(By.XPATH, var.emsochat_tuychinhdoanchat_doichude_maumacdinh).click()
        driver.find_element(By.XPATH, var.luu).click()
        check_mauchude2 = driver.find_element(By.XPATH,var.check_mauchude2).text
        print(check_mauchude2)
        logging.info("Trang chủ - Chat - tuỳ chon - Màu chủ đề")
        logging.info("check font-end: Bạn đã đổi chủ đề thành Mặc định.")
        logging.info(check_mauchude2 == "Bạn đã đổi chủ đề thành Mặc định.")

        #Biểu tượng cảm xúc
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
        driver.refresh()
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,700)", "")
        check_bieutuongcamxuc2 = driver.find_element(By.XPATH,var.check_bieutuongcamxucmacdinh).text
        print(check_bieutuongcamxuc2)
        logging.info("Trang chủ - Chat - tuỳ chon - Cảm xúc nhanh")
        logging.info("check font-end: Bạn đã gỡ biểu tượng cảm xúc nhanh..")
        logging.info(check_bieutuongcamxuc2 == "Bạn đã gỡ biểu tượng cảm xúc nhanh.")
        time.sleep(2)

        #File phương tiện và file liên kết
        driver.find_element(By.XPATH, var.emsochat_caidathopthoai).click()
        driver.find_element(By.XPATH, var.emsochat_file).click()
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien).click()
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_anh).click()
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_video).click()
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_file).click()
        driver.find_element(By.XPATH, var.emsochat_file_file_phuongtien_lienket).click()
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
        time.sleep(1)

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
        logging.info("Chức năng chưa hoạt động")
        logging.info(check_baivietcuaban_nhombandatimkiem != "Không có dữ liệu!")
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
        driver.back()
        driver.find_element(By.XPATH, var.baivietcuaban_livestream).click()
        time.sleep(2)
        check_baivietcuaban_livestream = driver.find_element(By.XPATH,var.check_baivietcuaban_livestream1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Bài viết của bạn - Livestream")
        logging.info("Chức năng chưa hoạt động")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_baivietcuaban_livestream != "Không có dữ liệu!")
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
        #Hoạt động có gắn thẻ bạn và các chức năng khác
        driver.find_element(By.XPATH, var.thongtincuabantrenemso_hoatdongcogantheban).click()
        check_hoatdongcogantheban = driver.find_element(By.XPATH,var.check_hoatdongcogantheban1).text
        logging.info("Trang chủ - tài khoản - Cài đặt và quyền riêng tư - Thông tin của bản trên Emso - Nhật ký hoạt động - Hoạt động có gắn thẻ bạn")
        logging.info("check font-end:Có thông báo hay không ")
        logging.info(check_hoatdongcogantheban != "Không có dữ liệu!")

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
        driver.back()
        driver.back()
        time.sleep(1)
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
        logging.info("check font-end: chức năng có hoạt động không ")
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
        logging.info("check font-end: chức năng có hoạt động không ")
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
        logging.info("check font-end: chức năng có hoạt động không ")
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
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chonsanpham_chatdongdong).click()
        driver.find_element(By.XPATH, var.chungtaycaithienemso_chitiet).click()
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

        #Khoá học
        driver.find_element(By.XPATH, var.trangchu_timkiem_khoahoc).click()
        time.sleep(2)
        check_timkiem_khoahoc = driver.find_element(By.XPATH,var.check_timkiem_khoahoc1).text
        logging.info("Trang chủ - Tìm kiếm - Khoá học")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Khoá học")
        logging.info(check_timkiem_khoahoc == "học nam")

        #San phẩm
        driver.find_element(By.XPATH, var.trangchu_timkiem_sanpham).click()
        time.sleep(2)
        check_timkiem_sanpham = driver.find_element(By.XPATH,var.check_timkiem_sanpham1).text
        logging.info("Trang chủ - Tìm kiếm - Sản phẩm")
        logging.info("check font-end: Có kết quả tìm kiếm bộ lọc Sản phẩm")
        logging.info(check_timkiem_sanpham == "Áo polo nam")
        driver.find_element(By.XPATH, var.trangchu).click()
        time.sleep(2)




    def youtobe(self):
        driver.implicitly_wait(15)
        time.sleep(1.5)
        driver.get("https://www.youtube.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@placeholder='Search']").send_keys("khoảnh khắc thu vị")
        driver.find_element(By.XPATH, "//*[@placeholder='Search']").submit()
        time.sleep(2)
        button = driver.find_element(By.XPATH, "//*[text()='Filters']")
        driver.execute_script("arguments[0].click();", button)
        time.sleep(1)
        # driver.find_element(By.XPATH, "//*[text()='Filters']").click()
        driver.find_element(By.XPATH, "//*[text()='Under 4 minutes']").click()
        time.sleep(3)
        danhsachvideo = driver.find_elements(By.XPATH, "//*[@class='yt-simple-endpoint inline-block style-scope ytd-thumbnail']")
        r = 0
        while r<1002:
            for video in danhsachvideo:
                r += 1
                link = video.get_attribute('href')
                writeData(var.linkvideo, "Sheet1", r, 1, link)
                print(link)
                driver.execute_script("window.scrollBy(0,300)", "")
                time.sleep(0.3)
            if  r ==1000:
                break











