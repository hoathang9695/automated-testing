pip install selenium==3.141.0

check_trang_nhatkyhoatdong_thongbao1 = driver.find_element(By.XPATH, var.check_trang_nhatkyhoatdong_thongbao1).text
logging.info("Trang - Cài đặt - Nhật ký hoạt động")
logging.info("check font-end: Tất cả hành động - mọi người - mới nhất , có thông báo hay không")
logging.info(check_trang_nhatkyhoatdong_thongbao1)
logging.info(check_trang_nhatkyhoatdong_thongbao1 != None)

link = video.get_attribute('href')




data['trangcanhan_gioithieu_tongquan']['songtai']

xoa = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input)
xoa.send_keys(Keys.CONTROL, "a")

logging.info("check back-end: Số điện thoại - " + data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])

del driver.requests


wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hanoi)))
element.click()

driver.execute_script("window.scrollBy(0,700)", "")

data['trangcanhan_sukientrongdoi']['taosukienrieng']
driver.find_element(By.XPATH, var.popupmarket_x).click()

//*[@class='']/div[@class='']/span[@class='']
//*[@class='app']/div/main/div/div[2]/div
//*[@class='app']/div/div[3]
//*[@class='MuiBox-root css-1nqnusv']//*[text()='Nhóm']
timkiemsanpham_chonxem ="//*[@class='app']/div/main/div/div[1]//*[text()='"+ data['market']['timkiemtrangchu']+"']"

anh_bia = driver.find_element(By.XPATH, var.trangcanhan_anhbia)
button_themmoi = driver.find_element(By.XPATH, var.trangcanhan_button_themmoi)
action1 = ActionChains(driver)
action1.drag_and_drop(anh_bia, button_themmoi).perform()

Chức năng chưa hoạt động

cuon = driver.find_element(By.XPATH, var.sudungemsso_trang_9)
driver.execute_script("arguments[0].scrollIntoView();", cuon)

#click va fo nút ko baasm đc
button = driver.find_element(By.XPATH, var.chungtaycaithienemso_tailenfile)
driver.execute_script("arguments[0].click();", button)


check hiển thị với is_displayed()
try:
    check_luuvideo_title = driver.find_element(By.XPATH, var.check_luuvideo_title1).is_displayed()
    logging.info("Watch - Video đã lưu - xem video - x")
    logging.info("check font-end: Có trở lại trang Video đã lưu không")
    logging.info(check_luuvideo_title)
except NoSuchElementException:
    logging.info("Watch - Video đã lưu - xem video - x")
    logging.info("check font-end: Có trở lại trang Video đã lưu không")
    logging.info("False")
    driver.save_screenshot("C:/Users/Admin/PycharmProjects/pythonProject/anhchupmanhinh/" + "flashsalecuashop_timkiem.png")

driver.implicitly_wait(15)

#check màu
element1 = driver.find_element(By.XPATH, var.check_color_mautennhom)
color = element1.value_of_css_property("color")
logging.info("Chat - Nhóm - Cài đặt nhóm")
logging.info("check font-end: Đánh dấu là chưa đọc")
logging.info(color)
logging.info(color == "rgba(53, 120, 229, 1)")
print(color)


#the div nhay lien tuc
driver.implicitly_wait(0.1)
count = 0
n = 0
while (count < 25):
    n = int(n)
    n = n + 1
    count = count + 1
    n = str(n)
    trang_taobaiviet_gif_anh = "/html/body/div[" + n + "]/div[3]/div/div[2]/div/div/img[1]"
    print(trang_taobaiviet_gif_anh)
    try:
        button = driver.find_element(By.XPATH, trang_taobaiviet_gif_anh)
        driver.execute_script("arguments[0].click();", button)
        if driver.find_element(By.XPATH, var.check_taobaiviet_gif).is_displayed():
            break
    except:
        pass
driver.implicitly_wait(15)



# element S
r = 0
chedonhom = driver.find_elements(By.XPATH, var.nhom_timkiem_chedonhom)
for chedo in chedonhom:
    r = int(r)
    r += 1
    r = str(r)
    tenchedo = chedo.text
    print(tenchedo)
    driver.execute_script("window.scrollBy(0,200)", "")
    time.sleep(0.3)
    logging.info("Nhóm - Tìm kiếm")
    logging.info("check font-end: Quyền công khai - Nhóm số " + r)
    logging.info(tenchedo == "Nhóm Công khai")


Explicit Waits
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))







driver.implicitly_wait(0.1)
count = 0
n = 0
while (count < 25):
    n = int(n)
    n = n + 1
    count = count + 1
    n = str(n)
    check_nhom_khoanhkhac_binhluan = "//*[@class='scrollbar-container ps']/div[" + n + "]/ul/li[1]/div[1]/div[1]/div[2]/div/span/div/div/p"
    print(check_nhom_khoanhkhac_binhluan)
    try:
        driver.find_element(By.XPATH, var.check_nhom_khoanhkhac_binhluan).text
        break
    except:
        pass
driver.implicitly_wait(15)


#Chuyển sang trang
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)



#Tách chữ và số
letters = ''.join(re.findall(r'[a-zA-Z]+', text))
digits = ''.join(re.findall(r'\d+', text))
print("Chữ trong chuỗi:", letters)  # Kết quả: "HelloWorld"
print("Số trong chuỗi:", digits)  # Kết quả: "123"


#Chụp ảnh màn hình
if driver.title == "Mạng xã hội Emso - Mạng xã hội vì người Việt1":
    assert True
    print("đã đúng title")
else:
    driver.save_screenshot("C:/Users/Admin/PycharmProjects/pythonProject/anhchupmanhinh/" + "anh_title.png")
    print("sai title")
    assert False, "sai title web roi"
time.sleep(2)


#cookie
time.sleep(1)
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
time.sleep(2)

------------------------------------------------------------------------
---------------------------------------------------------------------------

#swipe(startX, startY, endX, endY, duration)
self.driver.swipe(150, 400, 150, 200, 1000)

#Vuốt
actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()

#Click
element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="tb-btn"]')
actions.tap(ele).perform()

#Zoom
zoom_action = MultiAction(driver)
# Zoom
finger1.long_press(x=xx, y=yy).move_to(x=0, y=50).wait(200).release()
finger2.long_press(x=xx, y=yy).move_to(x=0, y=-50).wait(200).release()
zoom_action.add(finger1, finger2)

#Giữ nút
actions = TouchAction(driver)
action.long_press(x=xx, y=yy).move_to(x=0, y=50).wait(200).release()

#Kéo và thả
actions = TouchAction(driver)
actions.press(element[0]).wait(1000).move_to(element[5]).perfrom().release()

#Alert
driver.switch_to.alert.accept()     #ok
driver.switch_to.alert.dismiss()     #cancel

#print text
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="nguyễn huy (ga)")
print("content-desc")
print(el.get_attribute("content-desc"))



//*[@class='app']/div/main/div/div[2]/div/div/div[1]/div/div/div[2]/div/div[1]/div/nav[2]/div[2]/div/div/div/div[1]/div[2]/p[1]
//*[@class='app']/div/main/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div[3]/div/div/p[1]
