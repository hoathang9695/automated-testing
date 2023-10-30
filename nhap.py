
check_trunghoc_captruong = driver.find_element(By.XPATH, var.trangcanhan_xemsukientrongdoi_trunghoc_captruong).text
print(check_trunghoc_captruong)
logging.info("Trang cá nhân - giới thiệu - công việc và học vấn - trung học- cấp trường - xem sự kiện trong đời")
logging.info("check font-end: Trường trung học")
logging.info(check_trunghoc_captruong == "Trường trung học")




logging.info("Trang cá nhân - Giới thiệu tổng quan - Sống tại")
logging.info("check font-end: Hà Nội")
logging.info(check_trangcanhan_gioithieu_songtai == "Hà Nội")








for request in driver.requests:
    if request.url == "https://snapi.emso.asia/api/v1/me":
        data = sw_decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity'))
        data = data.decode("utf8")
        res = json.loads(data)
        print(res['avatar_media']['url'])
        print(res['avatar_media']['preview_url'])
        print(res['avatar_media']['description'])

        logging.info("check back-end: có file ảnh đại diện to không?")
        logging.info(res['avatar_media']['url'] != None)
        logging.info((res['avatar_media']['url']))

        logging.info("check back-end: có file ảnh đại diện nhỏ không?")
        logging.info(res['avatar_media']['preview_url'] != None)
        logging.info((res['avatar_media']['preview_url']))

        logging.info("check back-end: Mô tả ảnh đại diện")
        logging.info((res['avatar_media']['description']))
        logging.info(res['avatar_media']['description'] == "Trường đang cảm thấy vui vẻ")

        break
    else:
        print("không có  response")



data['trangcanhan_gioithieu_tongquan']['songtai']

xoa = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input)
xoa.send_keys(Keys.CONTROL, "a")

logging.info("check back-end: Số điện thoại - " + data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])

del driver.requests

lien ket xa hoi _ lien ket

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hanoi)))
element.click()

driver.execute_script("window.scrollBy(0,700)", "")

data['trangcanhan_sukientrongdoi']['taosukienrieng']


//*[@class='MuiAvatar-root MuiAvatar-circular jss65 css-1j6xs05']
"//*[@id='ext-global-floatWrap']/div[@class='x-float-wrap']/div[@class='x-dialog x-panel x-container x-component x-bordered x-header-position-top x-floated x-shadow x-managed-borders x-paint-monitored x-size-monitored']/div[2]/div/form/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]/div[1]/div/button"
/html/body/div[3]/div[3]/div/div/div/div[2]/div[2]/span
//*[@class='jss173 MuiBox-root css-0']/div[@class='jss176']/span[@class='MuiRadio-root MuiRadio-colorSecondary MuiButtonBase-root MuiRadio-root MuiRadio-colorSecondary PrivateSwitchBase-root css-y66rxb']
//*[@class='']/div[@class='']/span[@class='']
//*[@class='MuiModal-root MuiDialog-root css-5eviq2']//div[@class='MuiDialogContent-root MuiDialogContent-dividers css-1mu443t']/div/div[2]/div[2]/span
//*[@class='MuiModal-root MuiDialog-root css-126xj0f']/div[@class='MuiDialog-container MuiDialog-scrollPaper css-ekeie0']/div/div[1]/div[2][@class='scrollbar-container ps ps--active-y']/div[4]/div[1]/div[2]/div/div/button[1]
/div[4]/div[1]/div[2]/div/div/button


try:
    driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai).click()
except:
    driver.find_element(By.XPATH, var.trangcanhan_gioithieuhuy).click()
mqh_loi

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

Đã lưu vào no1