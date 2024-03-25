import emso
import action
import var
import funcion
import threading
from threading import Thread
import time
import unittest
import multiprocessing
from selenium.webdriver.common.by import By
import asyncio

# class Test(unittest.TestCase):
#     def test_run(self):
# #         #Emso
# #         emso.dang_nhap(self="")
# #         emso.trangcanhan(self="")
# #         emso.trangchu(self="")
# #         emso.chat(self="")
# #         emso.khoanhkhac(self="")
# #         emso.watch(self="")
# #         emso.trang(self="")
#         emso.nhom(self="")
# #
# #         #Người mua
# #         # emso.muahangthanhcong(self="")
# #         # emso.muahangthatbai(self="")
# #
# #         #Người bán
# #         # emso.quanlysanpham(self="")
# #         emso.kenhmarketing(self="")
# #
# #         #Add dữ liệu
# #         # emso.add_dulieuemso(self="")
#
#
# if __name__ == "__main__":
#     unittest.main()





# class Test(unittest.TestCase):
def test_run(self):
    print("1.Emso\n2.Market space\n3.Get data market")
    x1 = int(input("Mời chọn phần mềm: "))
    if x1==1:
        print("1.Đăng nhập\n2.Trang cá nhân\n3.Trang chủ")
        x2 = int(input("Mời chọn phân hệ: "))
        if x2 ==1:
            emso.dang_nhap(self="")
        if x2 ==2:
            print("1.Ảnh đại diện\n2.Ảnh bìa\n3.Giới thiệu - Tổng quan\n4.Giới thiệu - Công việc và học vấn\n5.Giới thiệu - Thông tin cơ bản\n6.Giới thiệu - Gia đình và mối quan hệ\n7.Giới thiệu - Sự kiện trong đời\n8.Giới thiệu - Nơi từng sống\n9.Ảnh video\n10.Check thông tin trang cá nhân\n11.Phần đáng chú ý\n12.Tất cả bạn bè")
            x3 = int(input("Mời chọn chức năng thực hiện: "))
            if x3 == 1:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.thongtincanhan_anhdaidien(self)
            if x3==2:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.thongtincanhan_anhbia(self)
            if x3==3:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.gioithieu.gioithieu_tongquan(self)
            if x3==4:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.gioithieu.congviec_vahocvan(self)
                funcion.gioithieu.xemsukientrongdoi_congviecvahocvan(self)
                funcion.gioithieu.trangcanhan_gioithieu_congviecvahocvan_addthem(self)
            if x3==5:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.gioithieu.trangcanhan_gioithieu_thongtincoban(self)
            if x3==6:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.gioithieu.trangcanhan_gioithieu_gd_va_mqh(self)
            if x3==7:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.gioithieu.trangcanhan_gioithieu_sukientrongdoi(self)
            if x3==8:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.gioithieu.trangcanhan_gioithieu_noitungsong(self)
            if x3==9:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.anh_video.anh_video(self)
            if x3==10:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.check_thongtin_trangcanhan.check_thongtin_trangcanhan(self)
            if x3==11:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.check_thongtin_trangcanhan.phandangchuy(self)
            if x3==12:
                action.login.login3(self, "truongvck33@gmail.com", "voncamk22")
                funcion.banbe.banbe_tatcabanbe(self)

        if x2 ==3:
            print("1.Tạo bài viết - Tạo khoảnh khắc\n2.Menu\n3.Chuyển tài khoản\n4.Cài đặt và quyền riêng tư\n5.Trợ giúp và hỗ trợ\n6.Màn hình\n7.Đóng góp ý kiến\n8.Đăng xuất\n9.Tìm kiếm")
            x3 = int(input("Mời chọn chức năng thực hiện: "))
            if x3==1:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.taobaiviet_khoangkhac(self)
            if x3==2:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.menu(self)
            if x3==3:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.caidatcanhan_chuyentaikhoan(self)
            if x3==4:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.canhan_caidatvaquyenriengtu(self)
            if x3==5:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.trogiupvahotro(self)
            if x3==6:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.caidatcanhan_manhinh(self)
            if x3==7:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.caidatcanhan_donggopykien(self)
            if x3==8:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.caidatcanhan_dangxuat(self)
            if x3==9:
                action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                funcion.trangchu.trangchu_timkiem(self)
    if x1==2:
        print("1.Luồng người mua\n2.Luồng người bán")
        x2 = int(input("Mời chọn luồng market space: "))
        if x2 ==1:
            print("1.Mua hàng thành công\n2.Mua hàng thất bại")
            x3 = int(input("Mời chọn chức năng thực hiện: "))
            if x3 == 1:
                print("1.Check voucher market space\n2.Thanh toán online VN-PAY, VTC-PAY\n3.Mua hàng thành công")
                x4 = int(input("Mời chọn chức năng cần thực hiện: "))
                if x4==1:
                    funcion.quatrinhmuahang.timkiemsanpham_voucher(self)
                if x4==2:
                    funcion.quatrinhmuahang.timkiemsanpham_thanhtoanonline(self)
                if x4==3:
                    funcion.quatrinhmuahang.timkiemsanpham(self)
                    funcion.quatrinhmuahang.xacnhandon(self)
                    funcion.quatrinhmuahang.chuanbihang(self)
                    funcion.quatrinhmuahang.donvivanchuyendanglayhang(self)
                    funcion.quatrinhmuahang.donvivanchuyendalayhang(self)
                    funcion.quatrinhmuahang.danggiaohang(self)
                    funcion.quatrinhmuahang.danhanhang(self)
            if x3==2:
                print("1.Mua hàng thất bại - Chờ thanh toán - Đã hủy\n2.Mua hàng thất bại- Shop hết hàng\n3.Mua hàng thất bại - Shop hủy đơn\n4.Mua hàng thất bại - Người mua hủy\n5.Trả hàng hoàn tiền - người mua hủy\n6.Trả hàng hoàn tiền -đồng ý\n7.Trả hàng hoàn tiền - Shop không đồng ý - Người mua đồng ý\n8.Trả hàng hoàn tiền - Shop không đồng ý - Người mua không đồng ý")
                x4 = int(input("Mời chọn chức năng cần thực hiện: "))
                if x4 ==1:
                    funcion.quatrinhmuahang.chothanhtoan_dahuy(self)
                if x4 ==2:
                    funcion.quatrinhmuahang.shop_het_hang(self)
                if x4 ==3:
                    funcion.quatrinhmuahang.shophuydon(self)
                if x4 ==4:
                    funcion.quatrinhmuahang.trahanghoantien_nguoimuahuy(self)
                if x4 ==5:
                    funcion.quatrinhmuahang.trahanghoantien_dongy(self)
                if x4 ==6:
                    funcion.quatrinhmuahang.trahanghoantien_khongdongy_dongy(self)
                if x4 ==7:
                    funcion.quatrinhmuahang.trahanghoantien_khongdongy_khongdongy(self)

        if x2 ==2:
            print("1.Quản lý sản phẩm\n2.Kênh marketting")
            x3 = int(input("Mời chọn phân hệ người bán: "))
            if x3==1:
                print("1.Thêm sản phẩm mới\n2.Danh sách sản phẩm")
                x4 = int(input("Mời chọn chức năng thực hiện: "))
                if x4==1:
                    funcion.quanlysanpham.themsanphammoi(self)
                if x4==2:
                    funcion.quanlysanpham.danhsachsanpham(self)
            if x3==2:
                print("1.Mã giảm giá của shop\n2.Chương trình khuyến mãi\n3.Flash sale của shop\n4.Chương trình của shop")
                x4 = int(input("Mời chọn chức năng thực hiện: "))
                if x4==1:
                    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                    funcion.kenhmarketing.magiamgiacuashop(self)
                if x4==2:
                    print("1.Chương trình khuyến mãi - Tất cả\n2.Chương trình khuyến mãi - Flash sale\n3.Duyệt sản phẩm Flash sale\n4.Chương trình khuyến mãi - Emsocampaign\n5.Chương trình khuyến mãi - Duyệt sản phẩm Emsocampaign")
                    x5 = int(input("Mời chọn chức năng thực hiện: "))
                    if x5==1:
                        action.kenhmarketing.chuongtrinhkhuyenmai_tatca(self)
                    if x5==2:
                        action.kenhmarketing.chuongtrinhkhuyenmai_flashsale(self)
                    if x5==3:
                        action.kenhmarketing.chuongtrinhkhuyenmai_pheduyetsp_flashsale(self)
                    if x5==4:
                        action.kenhmarketing.chuongtrinhkhuyenmai_emsocampaign(self)
                    if x5==5:
                        action.kenhmarketing.chuongtrinhkhuyenmai_pheduyetsp_cambpaign(self)
                if x4==3:
                    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                    funcion.kenhmarketing.flashsalecuashop(self)
                if x4==4:
                    action.login.login4(self, "truongvck33@gmail.com", "voncamk22")
                    funcion.kenhmarketing.chuongtrinhcuashop(self)
    if x1==3:
        print("Tạm thời chưa có chức năng này!")



# if __name__ == "__main__":
    # unittest.main()



test_run(self="")

















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









