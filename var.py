PATH ="C:/Users/Admin/PycharmProjects/pythonProject/chromedriver.exe"
path_baocao = "C:/Users/Admin/PycharmProjects/pythonProject/baocao_emso.xlsx"




# 1.login
url = "https://sn.emso.vn/login"
login_user = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div/input"
login_password = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/input"
login_submit = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[3]/button"
login_google = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[4]/button"
login_google_chontaikhoan = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div"
login_google_nhap_gmail = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
login_google_tiep = "//*[text()='Next']"
login_google_nhap_password = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
login_chon_tk_dang_nhap_gan_day = "//*[text()='Thùyyy']"
login_nho_mat_khau = "/html/body/div[2]/div[3]/div/div/div/div[3]/div/label/span[1]/input"
login_chon_tk_dang_nhap_gan_day_password = "/html/body/div[2]/div[3]/div/div/div/div[2]/div/div/input"
login_chon_tk_dang_nhap_gan_day_dang_nhap = "/html/body/div[2]/div[3]/div/div/div/button[1]"
message_sai_tk_mk1 = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[3]/div/div[2]/p"
message_bo_trong_tk1 = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/p"
message_bo_trong_mk1 = "/html/body/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/p"
login_thanhcong_khoanh_khac = "/html/body/div/div/div/main/div/div[1]/div[2]/div[1]/nav/a[2]/div/div[2]/p"
message_ganday_sai_mk1 = "/html/body/div[2]/div[3]/div/div/div/div[4]/div/div[2]/p"
message_ganday_khong_nhap_mk1 = "/html/body/div[2]/div[3]/div/div/div/div[2]/div/p"


# 1.1 logout
logout_chontaikhoan = "//*[@class='MuiPaper-root MuiPaper-elevation MuiPaper-elevation4 jss25 MuiAppBar-root MuiAppBar-colorInherit MuiAppBar-positionFixed mui-fixed css-wh6dm0']/div/div/div[2]/div/div[2]/div[1]/div[2]"
logout_chontaikhoan1 = "/html/body/div/div/div/div[1]/div/header/div/div/div[2]/div/div[2]"
logout_dangxuat = "//*[text()='Đăng xuất']"
logout_chat = "/html/body/div/div/div/div[1]/div/header/div/div/div[2]/div/button[1]"


#2.trang cá nhân
#2.1 ảnh đại diện
trangcanhan = "/html/body/div/div/div/main/div/div[1]/div[2]/div[1]/nav/a[1]/div/div[2]/p"
trangcanhan_iconmayanh = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/div[2]/button"
capnhatanhdaidien_taianhlen = "/html/body/div[2]/div[3]/div/div/div[1]/div/div/div/div[2]/div/button[2]"
capnhatanhdaidien_icon_taianhlen = "/html/body/div[2]/div[3]/div/div/div[2]/button"
capnhatanhdaidien_mota = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div/input"
capnhatanhdaidien_luu = "/html/body/div[2]/div[3]/div/div[2]/div[2]/button[2]"
capnhatanhdaidien_chonanhdautien = "/html/body/div[2]/div[3]/div/div/div[2]/div/div/div/div[1]"
capnhatanhdaidien_chonanhthu2 = "/html/body/div[2]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div"

capnhatanhdaidien_chonanhcosan_huy = "/html/body/div[2]/div[3]/div/div[2]/div[2]/button[1]"
capnhatanhdaidien_chonanhcosan_luu = "/html/body/div[2]/div[3]/div/div[2]/div[2]/button[2]"
capnhatanhdaidien_themkhung = "/html/body/div[2]/div[3]/div/div/div[1]/div/div/div/div[2]/div/button[3]"

capnhatanhdaidien_chonkhung_dangquauday = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]"
capnhatanhdaidien_chonkhung_dangbuonday = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]"
capnhatanhdaidien_chonkhung_yeuthuongvn = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[3]/div/div[1]"
capnhatanhdaidien_chonkhung_wowvn       = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[4]/div/div[1]"
capnhatanhdaidien_chonkhung_tuhaovn     = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[5]/div/div[1]"
capnhatanhdaidien_chonkhung_trungthu    = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[6]/div/div[1]"
capnhatanhdaidien_chonkhung_rangrovietnam = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[7]/div/div[1]"
capnhatanhdaidien_chonkhung_quockhanhvietnam = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[8]/div/div[1]"
capnhatanhdaidien_chonkhung_phunuvietnam = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[9]/div/div[1]"
capnhatanhdaidien_chonkhung_noel = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[10]/div/div[1]"
capnhatanhdaidien_chonkhung_nhagiaovietnam = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[11]/div/div[1]"
capnhatanhdaidien_chonkhung_lacquanvietnam = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[12]/div/div[1]"
capnhatanhdaidien_chonkhung_cmsn         = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[13]/div/div[1]"
capnhatanhdaidien_chonkhung_vulanbaohieu = "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div/div[14]/div/div[1]"
capnhatanhdaidien_chonkhung_luu = "/html/body/div[2]/div[3]/div/div[2]/div/button"
capnhatanhdaidien_chonkhung_x = "/html/body/div[2]/div[3]/div/h2/button"

# 2.2 ảnh bìa
trangcanhan_iconchinhsua_anhbia= "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/button"
trangcanhan_anhbia_taianhlen ="/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/li[3]/p/p"
trangcanhan_anhbia_capnhat     = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/button[2]"
trangcanhan_anhbia_capnhat1 = "//*[text()='Cập nhật']"
trangcanhan_dautrang = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[1]/p"
trangcanhan_dautrang1 = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div/img"
trangcanhan_anhbia_chontuanhcuaban = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/li[1]/p"
trangcanhan_anhbia_chonanhthu2 = "/html/body/div[2]/div[3]/div/div/div[2]/div/div/div/div[2]/div/div"
trangcanhan_anhbia_datlaivitri = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/div/li[2]/p"
trangcanhan_anhbia = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[2]/div[1]"
trangcanhan_button_themmoi = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/button[1]"



#2.3 Trang cá nhân - Giới thiệu tổng quan
trangcanhan_gioithieu = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[2]/div[1]/div/div/button[2]/button"
trangcanhan_gioithieu_songtai = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/li/div/div[2]"
trangcanhan_gioithieu_songtai_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
trangcanhan_gioithieu_songtai_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div/div/input"
trangcanhan_gioithieu_songtai_x = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div/div/div/button"
trangcanhan_gioithieu_songtai_hanoi = "//*[text()='Hà Nội']"
trangcanhan_gioithieu_songtai_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div[2]/button[2]"
trangcanhan_gioithieu_songtai_ok = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_gioithieu_songtai_huy = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div[2]/button[1]"
trangcanhan_gioithieu_songtai1 = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/li/div/div[1]/div[2]/p/span/span"
trangcanhan_check_gioithieu_songtai_dulieusai1 = "/html/body/div[2]/div[3]/div/div[1]/p"

trangcanhan_gioithieu_dentu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/li/div/div[2]"
trangcanhan_gioithieu_dentu_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
trangcanhan_gioithieu_dentu_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div/div/input"
trangcanhan_gioithieu_dentu_x = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div/div/div/button"
trangcanhan_gioithieu_dentu_langson = "//*[text()='Lạng Sơn']"
trangcanhan_gioithieu_dentu_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[2]/button[2]"
trangcanhan_gioithieu_dentu_huy = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[2]/button[1]"
trangcanhan_gioithieu_dentu_ok = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_check_gioithieu_dentu1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/li/div/div[1]/div[2]/p/span/span"
trangcanhan_check_gioithieu_dentu_dulieusai1 = "/html/body/div[2]/div[3]/div/div[1]/p"


trangcanhan_gioithieu_mqh = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[2]"
trangcanhan_gioithieu_mqh_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
trangcanhan_gioithieu_mqh_icon_chonmqh = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[1]/button/span[1]"
trangcanhan_gioithieu_mqh_lythan = "//*[text()='Ly Thân']"
trangcanhan_gioithieu_mqh_docthan = "//*[text()='Độc thân']"
trangcanhan_gioithieu_mqh_goa    = "//*[text()='Góa']"
trangcanhan_gioithieu_mqh_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/div[2]/button[2]"
trangcanhan_gioithieu_mqh1 = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[1]/div/div[2]/p[2]"
trangcanhan_gioithieu_mqh2 = "/html/body/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[1]/div/div[2]/p[2]"
trangcanhan_gioithieu_mqh3 = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[1]/div/p"
trangcanhan_gioithieu_mqh4 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[1]/div/p"
tongquan_mqh_ngocmai1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div/div/input"
trangcanhan_gioithieu_mqh_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div/div/input"
trangcanhan_gioithieu_mqh_input_x  ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div/div/div/button[1]"
trangcanhan_gioithieu_mqh_nam ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div[1]/button"
trangcanhan_gioithieu_mqh_nam_2022 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div[1]/div/div/li[2]"
trangcanhan_gioithieu_mqh_thang ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div[2]/button"
trangcanhan_gioithieu_mqh_thang_1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div[2]/div/div/li[1]"
trangcanhan_gioithieu_mqh_ngay ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div[3]/button"
trangcanhan_gioithieu_mqh_ngay_1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div[3]/div[3]/div/div/li[1]"


trangcanhan_gioithieu_sodienthoai = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/li/div/div[2]"
trangcanhan_gioithieu_sodienthoai1= "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/li/div/div[2]/i"
trangcanhan_gioithieu_sodienthoai_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
# trangcanhan_gioithieu_sodienthoai_chinhsua = "//*[text()='Chỉnh sửa thông tin']"
trangcanhan_gioithieu_sodienthoai_chinhsua2 = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/li/div/div[2]"

trangcanhan_gioithieu_sodienthoai_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/div/div/div/div[2]/input"
trangcanhan_gioithieu_sodienthoai_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[5]/div[2]/button[2]"
trangcanhan_gioithieu_sodienthoai_ok = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_check_gioithieu_sodienthoai1 = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/li/div/div[1]/div[2]/p"
trangcanhan_check_gioithieu_sodienthoai_dai1 = "/html/body/div[2]/div[3]/div/div[1]/p"
trangcanhan_check_gioithieu_sodienthoai_ngan1 ="/html/body/div[2]/div[3]/div/div[1]/p"
trangcanhan_check_gioithieu_sodienthoai_trungso1 = "/html/body/div[2]/div[3]/div/div[1]/p"

trangcanhan_gioithieu_bietdanh = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[5]/li/div/div[2]"
trangcanhan_gioithieu_bietdanh_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p    "
trangcanhan_gioithieu_bietdanh_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[5]/div/div/div/div[2]/input"
trangcanhan_gioithieu_bietdanh_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[6]/div[2]/button[2]"
trangcanhan_gioithieu_bietdanh_ok = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_check_gioithieu_bietdanh1 = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[5]/li/div/div[1]/div[2]/p"
trangcanhan_check_gioithieu_bietdanh_quadai1 ="/html/body/div[2]/div[3]/div/div[1]/p"


#2.4 Trang cá nhân - Công việc và học vấn
trangcanhan_gioithieu_iconcongviec = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[1]/ul/li/div/div[3]/div[2]"
trangcanhan_gioithieu_chinhsuacongviec = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[2]"
trangcanhan_gioithieu_cv_vahocvan = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[2]"
trangcanhan_gioithieu_congty_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[1]/div/div/input"
trangcanhan_gioithieu_congty_input_x = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[1]/div/div/div/button[1]"
trangcanhan_gioithieu_congty_input_quantrada = "//*[text()='Quán trà đá']"
trangcanhan_gioithieu_cv_chucvu_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[2]/div[2]/div/div/textarea[1]"
trangcanhan_gioithieu_cv_tp_input_x = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[3]/div/div/div/button[1]"
trangcanhan_gioithieu_cv_tp_hanoi = "//*[text()='Hà Nội']"
trangcanhan_gioithieu_cv_tp_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[3]/div/div/input"
trangcanhan_gioithieu_cv_mota_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[4]/div[2]/div/div/textarea[1]"
trangcanhan_gioithieu_cv_ngaybatdau_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[7]/div/div/div/div/input"
trangcanhan_gioithieu_cv_ngayketthuc_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[8]/div/div/div/div/input"
trangcanhan_gioithieu_cv_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[2]/div[2]/button[2]"
trangcanhan_gioithieu_addthem_congviec = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/p"
trangcanhan_gioithieu_cvvahocvan_iconxoa = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[1]/ul[1]/li/div/div[3]/div[2]"
trangcanhan_gioithieu_cvvahocvan_xoa = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[3]/p"
trangcanhan_gioithieu_cvvahocvan_xoa1 = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_gioithieu_congty_input_quancf ="//*[text()='Cafe+']"
trangcanhan_gioithieu_cv_tp_langson = "//*[text()='Lạng Sơn']"
trangcanhan_gioithieu_cv_khoangthoigian = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[1]/div/div[1]/div[6]/div/label/span[1]/input"
trangcanhan_gioithieu_cv_khoangthoigian_validate_ok = "/html/body/div[2]/div[3]/div/div[2]/button"
trangcanhan_check_gioithieu_khoangthoigian_validate1 = "/html/body/div[2]/div[3]/div/div[1]/p"


trangcanhan_gioithieu_chinhsuadaihoc ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[2]/p"
trangcanhan_gioithieu_icondaihoc = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[2]/ul/li/div/div[3]/div[2]"
trangcanhan_gioithieu_daihoc_truonghoc_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[1]/div/div/input"
trangcanhan_gioithieu_daihoc_truonghoc_input_x = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[1]/div/div/div/button[1]"
trangcanhan_gioithieu_daihoc_truonghoc_dhbachkhoa = "//*[text()='Đại học bách khoa hà nội']"
trangcanhan_gioithieu_daihoc_truonghoc_datotnghiep = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[3]/div/label/span[1]/input"
trangcanhan_gioithieu_daihoc_ngaybatdau_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[4]/div/div/div/div/input"
trangcanhan_gioithieu_daihoc_ngayketthuc_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[5]/div/div/div/div/input"
trangcanhan_gioithieu_daihoc_mota_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[6]/div[2]/div/div/textarea[1]"
trangcanhan_gioithieu_daihoc_chuyennghanh1_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[7]/div[2]/div/div/textarea[1]"
trangcanhan_gioithieu_daihoc_dahoctai_caodang = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[10]/div/div/label[1]/span[1]/input"
trangcanhan_gioithieu_daihoc_dahoctai_daihoc = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[10]/div/div/label[2]/span[1]/input"
trangcanhan_gioithieu_daihoc_bangcap_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[1]/div[11]/div[2]/div/div/textarea[1]"
trangcanhan_gioithieu_daihoc_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/div/div[2]/div[2]/button[2]"
trangcanhan_gioithieu_addtruongdaihoc = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[2]/p"
trangcanhan_gioithieu_daihoc_truonghoc_dhkingkong  = "//*[text()='Trường Đại học Kinh doanh và Công nghệ Hà Nội']"
trangcanhan_gioithieu_daihoc_iconxoa = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[2]/ul[2]/li/div/div[3]/div[2]"
trangcanhan_gioithieu_daihoc_xoa = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[3]/p"
trangcanhan_gioithieu_daihoc_xoa1 = "/html/body/div[2]/div[3]/div/div[2]/button[2]"

trangcanhan_gioithieu_icontrunghoc = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[3]/ul/li/div/div[3]/div[2]"
trangcanhan_gioithieu_chinhsuatrunghoc ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[2]/p"
trangcanhan_gioithieu_trunghoc_truonghoc_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[1]/div[1]/div/div/input"
trangcanhan_gioithieu_trunghochoc_truonghoc_input_x = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[1]/div[1]/div/div/div/button[1]"
trangcanhan_gioithieu_trunghoc_truonghoc_thpt_dinhlap = "//*[text()='Trường THPT Đình Lập']"
trangcanhan_gioithieu_trunghochoc_mota_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[1]/div[2]/div[2]/div/div/textarea[1]"
trangcanhan_gioithieu_trunghoc_datotnghiep = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[1]/div[4]/div/label/span[1]/input"
trangcanhan_gioithieu_trunghochoc_ngaybatdau_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[1]/div[5]/div/div/div/div/input"
trangcanhan_gioithieu_trunghoc_ngayketthuc_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[1]/div[6]/div/div/div/div/input"
trangcanhan_gioithieu_trunghoc_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/div/div[2]/div[2]/button[2]"
trangcanhan_gioithieu_addthemtrunghoc = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/p"
trangcanhan_gioithieu_trunghoc_truonghoc_thpt_phubinh = "//*[text()='Trường THPT Phú Bình ( Phú Bình High School )']"
trangcanhan_gioithieu_trunghoc_iconxoa = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[3]/ul[1]/li/div/div[3]/div[2]"
trangcanhan_gioithieu_trunghoc_xoa = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[3]/p"
trangcanhan_gioithieu_trunghoc_xoa1  ="/html/body/div[2]/div[3]/div/div[2]/button[2]"

#2.5 Trang cá nhân - Công việc và học vấn - xem sự kiện trong đời
trangcanhan_gioithieu_xemsukientrongdoi  ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[1]/p"
trangcanhan_xemsukientrongdoi_congviec_congty= "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[1]"
trangcanhan_xemsukientrongdoi_congviec_ngaythangchucvu = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[2]"
trangcanhan_xemsukientrongdoi_congviec_thanhpho = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[3]"

trangcanhan_gioithieu_daihoc_xemsukientrongdoi = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[1]/p"
trangcanhan_xemsukientrongdoi_daihoc_tentruong = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[1]"
trangcanhan_xemsukientrongdoi_check_daihoc_ngaythang = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[2]"
trangcanhan_xemsukientrongdoi_daihoc_dahoctai_chuyennghanh = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[3]"

trangcanhan_gioithieu_trunghoc_xemsukientrongdoi = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[1]/p"
trangcanhan_xemsukientrongdoi_trunghoc_tentruong = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[1]"
trangcanhan_xemsukientrongdoi_check_trunghoc_ngaythang = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[2]"
trangcanhan_xemsukientrongdoi_trunghoc_captruong = "/html/body/div/div/div/main/div/div[2]/div/div/div/div[2]/div[2]/p[3]"

# 2.6 thông tin cơ bản
#SĐT
thongtincoban = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[4]"
thongtincoban_icon_sdt = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[1]/li/div/div[2]"
thongtincoban_sdt_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_sdt_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[1]/div/div/div/div[2]/input"
thongtincoban_sdt_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[2]/div[2]/button[2]"
thongtincoban_sdt_fe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[1]/li/div/div[1]/div[2]/p"
trangcanhan_check_thongtincoban_sodienthoai_dai1 = "/html/body/div[2]/div[3]/div/div[1]/p"
trangcanhan_thongtincoban_sodienthoai_ok = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_check_thongtincoban_sodienthoai_ngan1 = "/html/body/div[2]/div[3]/div/div[1]/p"
trangcanhan_check_thongtincoban_sodienthoai_trungso1 ="/html/body/div[2]/div[3]/div/div[1]/p"


#Các trang web và liên kết xã hội
#web
thongtincoban_icon_web = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/li/div/div[2]"
thongtincoban_web_chinhsua = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_web_input = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/div/div/div[2]/input"
thongtincoban_web_luu = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[2]/div[2]/button[2]"
thongtincoban_web_fe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/li/div/div[1]/div[2]/span/p"
thongtincoban_web_ok ="/html/body/div[2]/div[3]/div/div[2]/button[2]"
thongtincoban_web_fe_dulieusai ="/html/body/div[2]/div[3]/div/div[1]/p"

#liên kết
thongtincoban_icon_lienket ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[3]/li/div/div[2]"
thongtincoban_lienket_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_lienket_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[2]/div/div/div/div[2]/input"
thongtincoban_lienket_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[3]/div[2]/button[2]"
thongtincoban_lienket_fe= "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[3]/li/div/div[1]/div/div/div/p"
thongtincoban_lienket_fe_dulieusai ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[3]/li/div/div[1]/div/div/div/p"
thongtincoban_lienket_saidinhdang = "//*[text()='URL You provided invalid URL']"

#tiểu sử
thongtincoban_icon_tieusu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[1]/li/div/div[2]"
thongtincoban_tieusu_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_tieusu_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[1]/div/div/div/div[2]/input"
thongtincoban_tieusu_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[2]/div[2]/button[2]"
thongtincoban_tieusu_fe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[1]/li/div/div[1]/div[2]/p"
thongtincoban_tieusu_qua100kytu ="//*[text()='Description Không vượt quá 100 ký tự']"
thongtincoban_tieusu_huy ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[2]/div[2]/button[1]"
thongtincoban_tieusu_fe_dulieusai ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[1]/div/div/div/div[2]/input"

#giới tính
thongtincoban_icon_gioitinh = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[2]/li/div/div[2]"
thongtincoban_gioitinh_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_gioitinh_iconchongioitinh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[2]/div/div/button"
thongtincoban_gioitinh_nu ="//*[text()='Nữ']"
thongtincoban_gioitinh_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[3]/div[2]/button[2]"
thongtincoban_gioitinh_fe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[2]/li/div/div[1]/div[2]/p"
thongtincoban_gioitinh_nam = "//*[text()='Nam']"

#Ngày sinh
thongtincoban_icon_ngaysinh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[3]/li/div/div[2]"
thongtincoban_ngaysinh_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_ngaysinh_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[4]/div/button[2]"
thongtincoban_ngaysinh_fe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[3]/li/div/div[1]/div[2]/p"
thongtincoban_ngaysinh_iconchonnam ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[3]/div/div[3]/div[1]/button"
thongtincoban_ngaysinh_duoi14t_2022 ="//*[text()='2022']"
thongtincoban_ngaysinh_fe_chuadu14t ="/html/body/div[2]/div[3]/div/div[1]/p"
thongtincoban_ngaysinh_ok ="/html/body/div[2]/div[3]/div/div[2]/button[2]"
thongtincoban_ngaysinh_tren14t_2000 = "//*[text()='2000']"


#biệt danh
thongtincoban_icon_bietdanh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[4]/li/div/div[2]"
thongtincoban_bietdanh_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
thongtincoban_bietdanh_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[4]/div/div/div/div[2]/input"
thongtincoban_bietdanh_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[5]/div[2]/button[2]"
thongtincoban_bietdanh_fe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[3]/div[4]/li/div/div[1]/div[2]/p"
thongtincoban_bietdanhdai_fe = "/html/body/div[2]/div[3]/div/div[1]/p"
thongtincoban_bietdanh_ok ="/html/body/div[2]/div[3]/div/div[2]/button[2]"


#gia đình và các mối quan hệ
#mối quan hệ
giadinhvamqh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[5]"
giadinhvamqh_icon_mqh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div/div[2]"
giadinhvamqh_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li/p"
giadinhvamqh_icon_chonmqh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[1]/div[1]/button"
giadinhvamqh_henho ="//*[text()='Hẹn hò']"
giadinhvamqh_chonnguoithan_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[1]/div[3]/div/div/input"
giadinhvamqh_chonnguoithan_input_x ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[1]/div[3]/div/div/div/button[1]"
giadinhvamqh_ngocmai ="//*[text()='Ngọc Mai']"
giadinhvamqh_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div[2]/div[2]/button[2]"
giadinhvamqh_mqh_ngocmai1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div/div[1]/div/div[2]/p[1]"
giadinhvamqh_mqh_trangthai_thoigian1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div/div[1]/div/div[2]/p[2]"
giadinhvamqh_mqh_trangthai_thoigian4 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[1]/div/div[1]/div/p"

#gia đinh
giadinhvamqh_icon_giadinh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/div[2]"
giadinhvamqh_sdt_chinhsua ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/li[1]/p"
giadinhvamqh_nguoithan_input ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div/div/div[1]/div/div/input"
giadinhvamqh_nguoithan_input_x ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div/div/div[1]/div/div/div/button[1]"
giadinhvamqh_nguoithan_chongiadinh ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div/div/div[3]/button"
giadinhvamqh_giadinh ="//*[text()='Gia đình']"
giadinhvamqh_giadinh_luu ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div/div/div[4]/div[2]/button[2]"
giadinhvamqh_manhcuong ="//*[text()='Mạnh Cường']"
giadinhvamqh_icon_nguoithan ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/div[2]"
giadinhvamqh_gd_manhcuong1 ="/html/body/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/div[1]/div/div[2]/p[1]"
giadinhvamqh_mqh_gd_tinhtrang1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul[2]/div[1]/div[1]/div/div[2]/p[2]"

#sự kiện trong đời
sukientrongdoi_trunghoc_icon ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[1]/li/div[2]"
sukientrongdoi_trunghoc_xem ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/div/li[1]/p"
sukientrongdoi_daihoc_icon ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[2]/li/div[2]"
sukientrongdoi_daihoc_xem ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/div/li[1]/p"
sukientrongdoi_congviec_icon ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[3]/li/div[2]"
sukientrongdoi_congviec_xem ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[4]/div/li[1]/p"
sukientrongdoi ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[6]"

#Tạo sự kiện riêng
taosukienrieng1 ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[1]/p"
sukientrongdoi_iconthemmoi ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[3]/i"
taosukientrongdoi_x ="/html/body/div[2]/div[3]/div/h2/button"
taosukienrieng_tailenfile ="/html/body/div[2]/div[3]/div/div[1]/div[1]/div/button/div/p"
taosukienrieng_input = "/html/body/div[2]/div[3]/div/div[1]/div[3]/div[1]/div[2]/input"

#Nhà cửa và đời sống
nhacuavadoisong ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[2]/p"
nhacuavadoisong_nhaptieude ="/html/body/div[2]/div[3]/div/div/div[1]/h6"
nhacuavadoisong_tieude_input ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[1]/div[2]/input"
nhacuavadoisong_chondiachi_input ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[2]/div/div/input"
nhacuavadoisong_chondiachi_thainguyen ="//*[text()='Thái Nguyên']"
nhacuavadoisong_tailenfile ="/html/body/div[2]/div[3]/div/div[1]/div[1]/div/button/div/p"
nhacuavadoisong_thoigian = "/html/body/div[2]/div[3]/div/div[1]/div[3]/div[4]/div/button"
nhungnoitoidasong ="/html/body/div[2]/div[3]/div/div/div[2]/div[2]/h6"
chuyenchoo ="/html/body/div[2]/div[3]/div/div/div[2]/div[3]/h6"

#mối quan hệ
moiquanhe ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[3]"
moiquanhe_nhaptieude ="/html/body/div[2]/div[3]/div/div/div[1]/h6"
moiquanhe_diachi_input ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[2]/div/div/input"
moiquanhe_diachi_laocai1 ="//*[text()='Lào Cai']"

#work
work ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[4]/p"
work_nhaptieude ="/html/body/div[2]/div[3]/div/div/div[1]/h6"

#Tưởng nhớ
tuongnho ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[5]/p"

#dấu mốc và thành tựu
daumocvathanhtuu ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[6]/p"
suckhoethechatvatinhthan ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[7]/p"
sothichhoatdong ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[8]/p"
dulich ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[9]/p"
giadinh = "/html/body/div[2]/div[3]/div/div/div/div[5]/div[10]/p"
hocvan = "/html/body/div[2]/div[3]/div/div/div/div[5]/div[11]/p"

##add thêm sự kiện
dulich_add1 ="/html/body/div[2]/div[3]/div/div/div/div[5]/div[9]/p"
nhacuavadoisong_thoigian_nam ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/button"
nhacuavadoisong_thoigian_nam_2022 ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[4]/div[2]/div/div/div[1]/div/div/li[2]"
nhacuavadoisong_thoigian_thang ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[4]/div[2]/div/div/div[2]/button"
nhacuavadoisong_thoigian_thang_9 ="//*[text()='Tháng 9']"
nhacuavadoisong_thoigian_ngay ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[4]/div[2]/div/div/div[3]/button"
nhacuavadoisong_thoigian_ngay_1 ="//*[text()='1']"
nhacuavadoisong_thoigian_ngay_1a ="/html/body/div[2]/div[3]/div/div[1]/div[3]/div[4]/div[2]/div/div/div[3]/div/div/li[1]"
taosukientrongdoi_luu ="/html/body/div[2]/div[3]/div/div[2]/button"
taosukientrongdoi_mota ="/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[1]/div/div/textarea"
taosukientrongdoi_dang ="/html/body/div[2]/div[3]/div/div[4]/div/button"
dongthoigian_sukienthemmoi1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/p"
dongthoigian_sukien_diadiem1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[3]/p[1]"
dongthoigian_sukien_thoigian1 ="/html/body/div[1]/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[3]/p[2]"
dongthoigian_sukien_mota ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[1]/div/div/div/p"
dongthoigian_sukien_diadiem ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[2]/div[3]/p[3]"
icon_chinhsuabaiviet ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[1]/li/div[3]/button"
chinhsuabaiviet ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div[2]/div[2]/div[4]/div/div[1]/div[1]/div[1]/div[1]/div/li[3]/p"
chinhsuabaiviet_mota_input ="/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div[1]/div/div/textarea"
chinhsuabaiviet_luu ="/html/body/div[2]/div[3]/div/div[4]/div/button"
sukientrongdoi_iconxoa_dulich ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/ul[4]/li/div[2]"
sukientrongdoi_xoa_dulich ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[2]/ul/div[5]/div/li[2]/p"

#Nơi từng sống
trangcanhan_noitungsong ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[3]"
trangcanhan_gioithieu_songtai_hungyen ="//*[text()='Hưng Yên']"
trangcanhan_gioithieu_dentu_thainguyen = "//*[text()='Thái Nguyên']"


#3.Bạn bè
#3.1 tất cả bạn bè
trangcanhan_banbe ="/html/body/div/div/div/main/div/div[2]/div/div[1]/div[2]/div[1]/div/div/button[3]/button"
trangcanhan_banbe_icon_manhcuong ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div[2]"
trangcanhan_banbe_botheodoi = "/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/li[1]/p"
trangcanhan_banbe_botheodoi_xacnhan ="/html/body/div[2]/div[3]/div/div[2]/button[2]"
trangcanhan_banbe_ngocmai ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/div[1]/div/div/a/div[2]"
trangcanhan_banbe_ngocmai1 ="/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/h4"
trangcanhan_banbe_huyketban ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/li[2]/p"
trangcanhan_banbe_huyketban_xacnhan = "/html/body/div[2]/div[3]/div/div[2]/button[2]"
huyketban_manhcuong_text_thembanbe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div[2]/div"
trangcanhan_banbe_thembanbe_manhcuong ='/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[2]/div/div[2]/div'
trangcanhan_banbe_loimoi_chapnhan ="//*[text()='Chấp nhận']"
check_banbe_tranquangtruong1 ="/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/button"
check_banbe_tranquangtruong2 = "/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/h4"
trangcanhan_banbe_loimoi_huy = "//*[text()='Xóa']"
check_banbe_tranquangtruong_tinhtrang ='/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/button[1]'
trangcanhan_banbe_guiloimoi ="/html/body/div/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div/div[2]/div/button[1]"
trangcanhan_banbe_iconchinhsuaquyen ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[1]/div/button"
trangcanhan_chínhsuaquyenriengtu ='/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/div/span/p'
trangcanhan_chínhsuaquyenriengtu_icon_dsbb ="/html/body/div[2]/div[3]/div/div/div[1]/button"
trangcanhan_chínhsuaquyenriengtu_dsbb_riengtu ="/html/body/div[3]/div[3]/div/div/div/div[3]/div[2]/span"
check_nguoila_riengtu1 ="//*[text()='Không có bạn bè để hiển thị.']"
trangcanhan_chínhsuaquyenriengtu_dsbb_banbe ="/html/body/div[3]/div[3]/div/div/div/div[2]/div[2]/span"
check_banbe_quyenbanbe1 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[3]/div/div[1]/div/div/a/div[2]"
check_banbe_riengtu2 ="//*[text()='Không có bạn bè nào']"
check_nguoila_riengtu3 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/p"
check_banbe_riengtu3 ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/p"
trangcanhan_chínhsuaquyenriengtu_dsbb_congkhai ="/html/body/div[3]/div[3]/div/div/div/div[1]/div[2]/span"
check_banbe_quyenbanbe ="/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div/div[1]/div/div[1]/div/div/a/div[2]"
check_banbe_quyencongkhai ='/html/body/div/div/div/main/div/div[2]/div/div[2]/div/div/div/p'
trangcanhan_chínhsuaquyenriengtu_x ="/html/body/div[2]/div[3]/div/h2/button"
check_dsbb_quyenbanbe ="/html/body/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div[3]/p"









