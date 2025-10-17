from abc import ABC, abstractmethod
import re
from datetime import datetime

class Person(ABC):
    def __init__(self, full_name="", age=0):
        self.full_name = full_name
        self.age = age

    @abstractmethod
    def input_info(self): # Hàm ảo để nhập thông tin người
        pass

    @abstractmethod
    def display_info(self): # Hàm ảo để hiển thị thông tin người
        pass

class Reader(Person):
    def __init__(self, full_name="", age=0, reader_id="", class_name="", register_date=""):
        super().__init__(full_name, age)
        self.reader_id = reader_id
        self.class_name = class_name
        self.register_date = register_date

    def input_info(self):
        # FullName: Viết hoa chữ cái đầu mỗi từ, không chứa số/ký tự đặc biệt
        while True:
            name = input("Nhập họ tên: ").strip()
            if re.match(r"^[A-ZÀ-Ỹ][a-zà-ỹ]*(\s[A-ZÀ-Ỹ][a-zà-ỹ]*)*$", name):
                self.full_name = name
                break
            print("Họ tên không hợp lệ.")

        # Age: từ 18 đến 30 tuổi
        while True:
            try:
                age = int(input("Nhập tuổi: "))
                if 18 <= age <= 30:
                    self.age = age
                    break
                else:
                    print("Tuổi sinh viên phải từ 18–30.")
            except ValueError:
                print("Tuổi phải là số nguyên!")

        # ReaderID: R[Khóa/Năm][5 số] (VD: R24_00001)
        while True:
            rid = input("Nhập mã độc giả (VD: R24_00001): ").strip()
            if re.match(r"^R\d{2}_\d{5}$", rid):
                self.reader_id = rid
                break
            print("Mã độc giả không hợp lệ.")

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
        print(f"Tuổi: {self.age}")
        print(f"Lớp: {self.class_name}")
        print(f"Ngày đăng ký: {self.register_date}")

class Staff(Person):
    def __init__(self, full_name="", age=0, staff_id="", position=""):
        super().__init__(full_name, age)
        self.staff_id = staff_id
        self.position = position

    def input_info(self):
        # Họ tên
        while True:
            name = input("Nhập họ tên nhân viên: ").strip()
            if re.match(r"^[A-ZÀ-ỸĐ][a-zà-ỹđ]+(\s[A-ZÀ-ỸĐ][a-zà-ỹđ]+)*$", name):
                self.full_name = name
                break
            print("Họ tên không hợp lệ!")

        # Tuổi nhân viên: 18–65
        while True:
            try:
                age = int(input("Nhập tuổi: "))
                if 18 <= age <= 65:
                    self.age = age
                    break
                else:
                    print("Tuổi nhân viên phải từ 18–65.")
            except ValueError:
                print("Tuổi phải là số nguyên!")

        # Mã nhân viên: NV + 4 số
        while True:
            sid = input("Nhập mã nhân viên (VD: NV0001): ").strip()
            if re.match(r"^NV\d{4}$", sid):
                self.staff_id = sid
                break
            print("Mã nhân viên không hợp lệ!")

        # Chức vụ
        while True:
            pos = input("Nhập chức vụ (VD: Thủ thư, Quản lý...): ").strip()
            if len(pos) >= 2:
                self.position = pos
                break
            print("Chức vụ không hợp lệ!")

    def display_info(self):
        print("\n--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Họ tên: {self.full_name}")
        print(f"Tuổi: {self.age}")
        print(f"Mã nhân viên: {self.staff_id}")
        print(f"Chức vụ: {self.position}")

    # Các phương thức riêng
    def import_book(self):
        print(f"{self.full_name} đang nhập sách mới vào kho.")

    def lend_book(self):
        print(f"{self.full_name} đang thực hiện cho bạn đọc mượn sách")

    def receive_book(self):
        print(f"{self.full_name} đang nhận trả sách đã mượn từ bạn đọc.")


# =========================
# CHƯƠNG TRÌNH CHẠY THỬ
# =========================
if __name__ == "__main__":
    print("=== THỬ NGHIỆM LỚP BẠN ĐỌC (READER) ===")
    reader = Reader()
    reader.input_info()
    reader.display_info()

    print("\n=== THỬ NGHIỆM LỚP NHÂN VIÊN (STAFF) ===")
    staff = Staff()
    staff.input_info()
    staff.display_info()

    # Gọi thử các phương thức riêng của nhân viên
    print("\n=== THỬ NGHIỆM CHỨC NĂNG CỦA NHÂN VIÊN ===")
    staff.import_book()
    staff.lend_book()
    staff.receive_book()


