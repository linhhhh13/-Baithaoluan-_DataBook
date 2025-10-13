import re
from datetime import datetime

class Reader:
    def __init__(self, reader_id="", full_name="", class_name="", register_date=""):
        self.reader_id = reader_id
        self.full_name = full_name
        self.class_name = class_name
        self.register_date = register_date

    def input_info(self):
        # ReaderID: R[Khóa/Năm][5 số] (VD: R24_00001)
        while True:
            rid = input("Nhập mã độc giả (VD: R24_00001): ").strip()
            if re.match(r"^R\d{2}_\d{5}$", rid):
                self.reader_id = rid
                break
            print("Mã độc giả không hợp lệ.")

        # FullName: Viết hoa chữ cái đầu mỗi từ, không chứa số/ký tự đặc biệt
        while True:
            name = input("Nhập họ tên: ").strip()
            if re.match(r"^[A-ZÀ-Ỹ][a-zà-ỹ]*(\s[A-ZÀ-Ỹ][a-zà-ỹ]*)*$", name):
                self.full_name = name
                break
            print("Họ tên không hợp lệ.")

        # Class: Không để trống, đúng định dạng (VD: K60S)
        while True:
            class_name = input("Nhập lớp (VD: K60S): ").strip()
            if class_name and re.match(r"^[A-Z]\d{2,3}[A-Z]\d?$", class_name):
                self.class_name = class_name
                break
            print("Lớp không hợp lệ.")

        # RegisterDate: Đúng định dạng ngày, nhỏ hơn hoặc bằng hiện tại
        while True:
            date = input("Nhập ngày đăng ký (DD/MM/YYYY): ").strip()
            try:
                reg_date = datetime.strptime(date, "%d/%m/%Y")
                if reg_date <= datetime.now():
                    self.register_date = date
                    break
                else:
                    print("Ngày đăng ký không được lớn hơn ngày hiện tại.")
            except:
                print("Ngày đăng ký sai định dạng (DD/MM/YYYY).")

    def display_info(self):
        print("\n===== THÔNG TIN ĐỘC GIẢ =====")
        print(f"Mã độc giả: {self.reader_id}")
        print(f"Họ tên: {self.full_name}")
        print(f"Lớp: {self.class_name}")
        print(f"Ngày đăng ký: {self.register_date}")

