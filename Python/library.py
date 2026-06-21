from book import Book
from student import Student

class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.students: list[Student] = []

    def get_input_positive_int(self, prompt):
        while True:
            try:
                val = int(input(prompt).strip())
                if val < 0:
                    print("Số lượng không được âm (-5). Vui lòng nhập lại!")
                    continue
                return val
            except ValueError:
                print("Sai kiểu dữ liệu (abc). Vui lòng nhập lại số nguyên!")

    def add_book(self):
        book_id = input("Nhập mã sách: ").strip()
        if not book_id:
            print("Mã sách không được để trống.")
            return
        for b in self.books:
            if b.id == book_id:
                print("Mã sách này đã tồn tại.")
                return

        title = input("Nhập tên sách: ").strip()
        author = input("Nhập tác giả: ").strip()
        quantity = self.get_input_positive_int("Nhập số lượng: ")

        new_book = Book(book_id, title, author, quantity)
        self.books.append(new_book)
        print("Thêm sách thành công!")

    def view_books(self):
        if not self.books:
            print("Thư viện hiện chưa có sách.")
            return
        print("-" * 75)
        print(f"{'Mã sách':<10} | {'Tên sách':<25} | {'Tác giả':<20} | {'Số lượng':<10}")
        print("-" * 75)
        for b in self.books:
            b.show_info()
        print("-" * 75)

    def search_book(self):
        book_id = input("Nhập mã sách cần tìm: ").strip()
        found = False
        for b in self.books:
            if b.id == book_id:
                print("Đã tìm thấy sách:")
                print("-" * 75)
                b.show_info()
                print("-" * 75)
                found = True
                break
        if not found:
            print("Book not found (Không tìm thấy sách)!")

    def delete_book(self):
        book_id = input("Nhập mã sách cần xóa: ").strip()
        found_book = ""
        for b in self.books:
            if b.id == book_id:
                found_book = b
                break
        if found_book != "":
            self.books.remove(found_book)
            print("Xóa sách thành công!")
        else:
            print("Book not found (Không tìm thấy sách)!")

    def add_student(self):
        student_id = input("Nhập mã sinh viên: ").strip()
        if not student_id:
            print("Mã sinh viên không được để trống.")
            return
        for s in self.students:
            if s.id == student_id:
                print("Mã sinh viên đã tồn tại.")
                return

        name = input("Nhập họ tên sinh viên: ").strip()
        class_name = input("Nhập lớp: ").strip()

        new_student = Student(student_id, name, class_name)
        self.students.append(new_student)
        print("Thêm sinh viên thành công!")

    def view_students(self):
        if not self.students:
            print("Danh sách sinh viên trống.")
            return
        print("-" * 60)
        print(f"{'Mã SV':<10} | {'Họ tên':<25} | {'Lớp':<15}")
        print("-" * 60)
        for s in self.students:
            s.show_info()
        print("-" * 60)

    def search_student(self):
        student_id = input("Nhập mã sinh viên cần tìm: ").strip()
        found = False
        for s in self.students:
            if s.id == student_id:
                print("Đã tìm thấy sinh viên:")
                print("-" * 60)
                s.show_info()
                print("-" * 60)
                found = True
                break
        if not found:
            print("Student not found (Không tìm thấy sinh viên)!")

    def delete_student(self):
        student_id = input("Nhập mã sinh viên cần xóa: ").strip()
        found_student = ""
        for s in self.students:
            if s.id == student_id:
                found_student = s
                break
        if found_student != "":
            self.students.remove(found_student)
            print("Xóa sinh viên thành công!")
        else:
            print("Student not found (Không tìm thấy sinh viên)!")

    def borrow_book(self):
        student_id = input("Nhập mã sinh viên mượn sách: ").strip()
        found_student = ""
        for s in self.students:
            if s.id == student_id:
                found_student = s
                break
        if found_student == "":
            print("Student not found (Sinh viên không tồn tại)!")
            return

        book_id = input("Nhập mã sách muốn mượn: ").strip()
        found_book = ""
        for b in self.books:
            if b.id == book_id:
                found_book = b
                break
        if found_book == "":
            print("Book not found (Sách không tồn tại)!")
            return

        if found_book.borrow_item():
            print(f"Sinh viên {found_student.name} mượn thành công sách {found_book.title}!")
        else:
            print("Mượn thất bại! Số lượng sách trong thư viện đã hết (quantity = 0).")

    def return_book(self):
        student_id = input("Nhập mã sinh viên trả sách: ").strip()
        found_student = ""
        for s in self.students:
            if s.id == student_id:
                found_student = s
                break
        if found_student == "":
            print("Student not found!")
            return

        book_id = input("Nhập mã sách muốn trả: ").strip()
        found_book = ""
        for b in self.books:
            if b.id == book_id:
                found_book = b
                break
        if found_book == "":
            print("Book not found!")
            return

        found_book.return_item()
        print(f"Sinh viên {found_student.name} đã trả thành công sách {found_book.title}!")