
check_trunghoc_captruong = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_trunghoc_captruong).text
print(check_trunghoc_captruong)
logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - trung học- cấp trường - xem sự kiện trong đời")
logging.info("check font-end: Trường trung học")
logging.info(check_trunghoc_captruong == "Trường trung học

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


//*[@class='']/div[@class='']/span[@class='']




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
    time.sleep(2)
except NoSuchElementException:
    logging.info("Watch - Video đã lưu - xem video - x")
    logging.info("check font-end: Có trở lại trang Video đã lưu không")
    logging.info("False")
    time.sleep(2)