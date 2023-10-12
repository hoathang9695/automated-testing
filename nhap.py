
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

sdt1 = driver.find_element(By.XPATH, var.trangcanhan_gioithieu_sodienthoai_input)
sdt1.send_keys(Keys.CONTROL, "a")

logging.info("check back-end: Số điện thoại - " + data['trangcanhan_gioithieu_congviecvahocvan']['thanhpho'])

del driver.requests

lien ket xa hoi _ lien ket

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, var.trangcanhan_gioithieu_songtai_hanoi)))
element.click()

driver.execute_script("window.scrollBy(0,700)", "")

data['trangcanhan_sukientrongdoi']['taosukienrieng']