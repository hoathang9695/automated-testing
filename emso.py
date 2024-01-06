import numpy
import self
import json
import funcion
from threading import Thread
from selenium.webdriver.common.by import By
import var
from selenium import webdriver
import time
import action
import threaded
import decode
from seleniumwire.utils import decode as sw_decode



def dang_nhap(self):
    funcion.login.khong_thanh_cong_tk_emso1(self)
    funcion.login.khong_thanh_cong_tk_emso2(self)
    funcion.login.thanh_cong_tk_emso(self)
    funcion.login.chon_tk_dang_nhap_gan_day_khong_nhap_pass(self)
    funcion.login.chon_tk_dang_nhap_gan_day_nhap_sai_pass(self)
    funcion.login.chon_tk_dang_nhap_gan_day_chua_luu_mk(self)
    funcion.login.chon_tk_dang_nhap_gan_day_da_luu_mk(self)

    funcion.login.thanh_cong_tk_google1(self)
    funcion.login.thanh_cong_tk_google2(self) #để chạy cuối, đang lỗi


def trangcanhan(self):
    action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
    funcion.thongtincanhan_anhdaidien(self)
    funcion.thongtincanhan_anhbia(self)
    funcion.gioithieu.gioithieu_tongquan(self)
    funcion.gioithieu.congviec_vahocvan(self)
    funcion.gioithieu.xemsukientrongdoi_congviecvahocvan(self)
    funcion.gioithieu.trangcanhan_gioithieu_congviecvahocvan_addthem(self)
    funcion.gioithieu.trangcanhan_gioithieu_thongtincoban(self)
    funcion.gioithieu.trangcanhan_gioithieu_gd_va_mqh(self)
    funcion.gioithieu.trangcanhan_gioithieu_sukientrongdoi(self)
    funcion.gioithieu.trangcanhan_gioithieu_noitungsong(self)
    funcion.anh_video.anh_video(self)
    funcion.check_thongtin_trangcanhan.check_thongtin_trangcanhan(self)
    funcion.check_thongtin_trangcanhan.phandangchuy(self)
    funcion.banbe.banbe_tatcabanbe(self)


def trangchu(self):
    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
    funcion.trangchu.taobaiviet_khoangkhac(self)
    funcion.trangchu.menu(self)
    funcion.trangchu.caidatcanhan_chuyentaikhoan(self)
    funcion.trangchu.canhan_caidatvaquyenriengtu(self)
    funcion.trangchu.trogiupvahotro(self)
    funcion.trangchu.caidatcanhan_manhinh(self)
    funcion.trangchu.caidatcanhan_donggopykien(self)
    funcion.trangchu.caidatcanhan_dangxuat(self)
    funcion.trangchu.trangchu_timkiem(self)

def chat(self):
    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
    funcion.trangchu.tinnhanmoi(self)
    funcion.trangchu.chat(self)
    funcion.trangchu.chat_xemtatca(self)

    funcion.trangchu.taonhom(self)
    funcion.trangchu.thongtindoanchat_nhom(self)



def khoanhkhac(self):
    action.login.login4(self, "truongvck333@gmail.com", "voncamk22")
    funcion.khoanhkhac.dangtheodoi(self)
    # funcion.khoanhkhac.tructiep(self) #khoong co phien live
    funcion.khoanhkhac.taokhoanhkhac(self)
    # funcion.khoanhkhac.taikhoan_duocdexuat(self)
    funcion.khoanhkhac.taikhoan_dangtheodoi(self)
    funcion.khoanhkhac.khoanhkhac_timkiem(self)


def watch(self):
    action.login.login4(self, "truongvck333@gmail.com", "voncamk22")
    # funcion.watch.timkiem(self)   #đang bị trắng trang
    funcion.watch.trangchu(self)
    funcion.watch.chuongtrinh(self)
    funcion.watch.videodaluu(self)
    funcion.watch.dangtheodoi(self)


def trang(self):
    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
    # funcion.trang.timkiem_trangcuaban(self)     #ko chọn được
    funcion.trang.khampha(self)
    funcion.trang.trangdathich(self)
    funcion.trang.trangdathich_dau3cham(self)
    funcion.trang.loimoi(self)
    # funcion.trang.taotrangmoi(self) #vẫn bị lỗi ảnh
    funcion.trang.trang_gioithieu(self)
    funcion.trang.anh(self)
    funcion.trang.music(self)
    funcion.trang.video(self)
    funcion.trang.xemthem(self)
    funcion.trang.cuahang(self)
    funcion.trang.cacnutkhac(self)
    funcion.trang.themnuthanhdong(self)
    funcion.trang.anhdaidien_anhbia(self)
    funcion.trang.taobaiviet(self)
    funcion.trang.hopthu(self)
    funcion.trang.thongbao(self)
    funcion.trang.chatluongtrang(self)
    funcion.trang.baivietdalenlich(self)        #6597 ko đăng ngay được
    funcion.trang.chinhsuathongtintrang(self)
    funcion.trang.caidat(self)


def nhom(self):
    action.login.login4(self, "truongvck333@gmail.com", "voncamk22")
    funcion.nhom.timkiem(self)        #Lỗi icon
    funcion.nhom.bangtincuaban(self)
    funcion.nhom.khampha(self)
    funcion.nhom.moithamgianhom(self)
    funcion.nhom.taonhommoi(self)
    funcion.nhom.nhombanquanly(self)
    funcion.nhom.nhombanthamgia(self)
    funcion.nhom.thaoluan(self)
    funcion.nhom.thanhvien(self)
    funcion.nhom.filephuongtien(self)
    funcion.nhom.yeucaulamthanhvien(self)
    funcion.nhom.baivietdalenlich(self)
    funcion.nhom.nhatkyhoatdong(self)
    funcion.nhom.quytacnhom(self)
    funcion.nhom.noidungthanhvienbaocao(self)
    funcion.nhom.thongbaokiemduyet(self)
    funcion.nhom.cauhoichonthanhvien(self)
    funcion.nhom.caidatnhom(self)



def muahangthanhcong(self):
    funcion.quatrinhmuahang.timkiemsanpham(self)
    funcion.quatrinhmuahang.xacnhandon(self)
    funcion.quatrinhmuahang.chuanbihang(self)
    funcion.quatrinhmuahang.donvivanchuyendanglayhang(self)
    funcion.quatrinhmuahang.donvivanchuyendalayhang(self)
    funcion.quatrinhmuahang.danggiaohang(self)
    funcion.quatrinhmuahang.danhanhang(self)

def muahangthatbai(self):
    funcion.quatrinhmuahang.chothanhtoan_dahuy(self)
    funcion.quatrinhmuahang.shop_het_hang(self)
    funcion.quatrinhmuahang.shophuydon(self)
    funcion.quatrinhmuahang.trahanghoantien_nguoimuahuy(self)
    funcion.quatrinhmuahang.trahanghoantien_dongy(self)
    funcion.quatrinhmuahang.trahanghoantien_khongdongy_dongy(self)
    funcion.quatrinhmuahang.trahanghoantien_khongdongy_khongdongy(self)


def quanlysanpham(self):
    funcion.quanlysanpham.themsanphammoi(self)
    funcion.quanlysanpham.danhsachsanpham(self)


def add_dulieuemso(self):
    # funcion.add_dulieuemso.themsanphammoi1(self)
    # funcion.add_dulieuemso.themsanphammoi1_khongconghanhcha(self)
    # funcion.add_dulieuemso.vietfilesanpham(self)
    # funcion.add_dulieuemso.get_data_lazada(self)
    funcion.add_dulieuemso.get_data_lazada_theonghanh(self)
    # funcion.add_dulieuemso.get_image(self)


def kenhmarketing(self):
    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
    funcion.kenhmarketing.magiamgiacuashop(self)
    funcion.kenhmarketing.chuongtrinhkhuyenmai(self)















