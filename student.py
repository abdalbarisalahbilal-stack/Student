# برنامج إدارة الطلاب باستخدام الملفات

FILE_NAME = "students.txt"

# دالة لإضافة طالب
def add_student():
    name = input("أدخل اسم الطالب/ة: ")
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(name.strip() + "\n")
    print("✅ تم إضافة الطالب بنجاح!\n")

# دالة لعرض قائمة الطلاب
def show_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = file.read().strip()
            if students:
                print("\n📋 قائمة الطلاب:\n")
                print(students)
            else:
                print("⚠️ لا يوجد طلاب مسجلين بعد.\n")
    except FileNotFoundError:
        print("⚠️ الملف غير موجود، أضف طلاب أولاً.\n")

# دالة لحساب عدد الطلاب
def count_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = file.readlines()
            print("👥 عدد الطلاب هو:", len(students), "\n")
    except FileNotFoundError:
        print("⚠️ الملف غير موجود.\n")

# دالة للبحث عن طالب
def search_student():
    search_name = input("🔍 أدخل اسم الطالب الذي تبحث عنه: ").strip().lower()
    found = False
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            students = file.readlines()
            for student in students:
                if search_name == student.strip().lower():
                    print("✅ تم العثور على الطالب:", student.strip(), "\n")
                    found = True
                    break
        if not found:
            print("❌ لم يتم العثور على الطالب.\n")
    except FileNotFoundError:
        print("⚠️ الملف غير موجود.\n")

# القائمة الرئيسية
def main():
    print("ملاحظة مهمة: برجى كتابة الأسماء بالإنجليزي.\n")

    while True:
        print("----- القائمة الرئيسية -----")
        print("1 - إضافة طالب")
        print("2 - عرض قائمة الطلاب")
        print("3 - حساب عدد الطلاب")
        print("4 - بحث عن طالب")
        print("5 - خروج")
        print("----------------------------")

        choice = input("اختر رقم العملية: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            count_students()
        elif choice == "4":
            search_student()
        elif choice == "5":
            print("🚪 تم الخروج من البرنامج بنجاح!")
            break
        else:
            print("❌ الاختيار غير صحيح!\n")

        again = input("هل تريد إعادة الاختيار؟ (نعم/لا): ").strip().lower()
        if again == "لا":
            print("🔒 تم إغلاق البرنامج.")
            break

# تشغيل البرنامج
if __name__ == "__main__":
    main()