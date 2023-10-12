import openpyxl
import asyncio
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
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
from selenium.webdriver.chrome.options import Options
import datetime as dt
from seleniumwire import webdriver
# driver = webdriver.Chrome(var.PATH)
# import brotli
# import chormedriver_auto
import unittest
import logging
import action




# def trangcanhan_thongtincanhan_anhdaidien_themmoi():
#     driver.implicitly_wait(10)
#     print(driver.title)
#     driver.get("https://datienich.vn/")
#     print(driver.title)
#     time.sleep(2)
#     for request in driver.requests:
#         print(driver.title)
#         print("r1")
#         if request.response:
#             print("r2")
#             print(request.url)
#             if request.url == "https://snapi.emso.asia/api/v1/me":
#                 print("r3")
#                 res = request.response.body
#                 print("r4")
#                 res1 = json.loads(res)
#                 print("r5")
#                 data_anhdaidien = res1["data"]
#                 print("r6")
#                 print(data_anhdaidien)
#         else:
#             print("không có  response")
#
# def trangcanhan_thongtincanhan_anhdaidien_themmoi1():
#     driver.implicitly_wait(10)
#     for request in driver.requests:
#         if request.response:
#             print(request.url[0:33])
#             if request.url[0:33] == "https://snapi.emso.asia/api/v1/me":  # qa
#                 res = request.response.body
#                 res1 = json.loads(res)
#                 data_anhdaidien = res1["data"]
#                 print(data_anhdaidien)
#
#         else:
#             print("không có  response")
#





