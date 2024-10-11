from Library_class_model import *

tayyor = input("Tayyormisiz(h/y)?\n>>>>>>>>>>>>>> ")

if tayyor != 'h':
    print("Dastur to'xtatildi!")
    exit()

lib = Library()

while True:
    tanlov = int(input("Menu:\n"
                       "1. Kitoblarni ko'rsatish\n"
                       "2. Kitob qo'shish\n"
                       "3. Kitob o'chirish\n"
                       "4. Kitob qidirish\n"
                       "5. Qarzga kitob olish\n"
                       "6. Qarzni o'chirish\n"
                       "7. Dasturni to'xtatish\n"
                       ">>>>>>>>>>>>>>> "))

    match tanlov:
        case 1:
            lib.show_books()
        case 2:
            lib.add_book()
        case 3:
            lib.delete_book()
            lib.show_books()
        case 4:
            lib.search_book()
        case 5:
            ism = input("Ismingizni kiriting: ")
            kitob = input("Olmoqchi bo'lgan kitobingiz nomini kiriting: ")
            lib.qarz(ism, kitob)
        case 6:
            ism = input("Ismingizni kiriting: ")
            lib.qarz_delete(ism)
        case 7:
            exit()
        case _:
            print("Noto'gri amal!")