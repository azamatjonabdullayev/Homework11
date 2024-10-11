class Muallif:
    def __init__(self, ism: str, fam: str, ):                           #*
        self.__name = ism                                               #*
        self.__fam = fam                                                #*
                                                                        #*
                                                                        #*
    @property                                                           #*
    def ism(self):                                                      #*
        return self.__name                                              #*
                                                                        #*
    @property                                                           #*
    def fam(self):                                                      #*
        return self.__fam                                               #*
                                                                        #*
                                                                        #*
                                                                        #*
"""***********************************************************************"""

class Kitob:                                                              #*
    def __init__(self, muallif: Muallif, nom: str, janr: str, narx: int):   #*
        self.__avtor = muallif                                              #*
        self.__nom = nom                                                    #*
        self.__genre = janr                                                 #*
        self.__price = narx                                                 #*
                                                                            #*
    @property                                                               #*
    def name(self):                                                         #*
        return self.__nom                                                   #*
                                                                            #*
    @property                                                               #*
    def genre(self):                                                        #*
        return self.__genre                                                 #*
                                                                            #*
    @property                                                               #*
    def pul(self):                                                          #*
        return self.__price                                                 #*
                                                                            #*
    @property                                                               #*
    def muallif(self):                                                      #*
        return self.__avtor                                                 #*
                                                                            #*

"""***************************************************************************"""

"""*******************************************************************************************************************************************"""

class Library:
    def __init__(self):
        self.__all_books = []
        self.__qarz_kitoblar = {}


    def add_book(self):
        nom = input("Kitobni nomini kiriting: ")
        muallif_ism, muallif_fam = input("Muallifni ism va familiyasini kiriting: ").split()
        janr = input("Kitobning janrini kiriting: ")
        price = int(input("Narxini kiriting: "))

        avtor = Muallif(muallif_ism, muallif_fam)
        book = Kitob(avtor, nom, janr, price)

        for i in self.__all_books:
            if i.name == nom:
                print("Bunday kitob mavjud!")
                return

        self.__all_books.append(book)
        print("******* Kitob qo'shildi! *******")



    def delete_book(self):

        if len(self.__all_books) == 0:
            print("Kutubxonada kitob mavjud emas!")
            return None


        nom = input("Kitobni nomini kiriting: ")

        for i in self.__all_books:
            if i.name.lower() == nom.lower():
                self.__all_books.remove(i)
                print(f"{i.name} nomli kitob o'chirildi")
                return

        print("Bunday kitob mavjud emas!")
        return None




    def show_books(self):
        if len(self.__all_books) == 0:
            print("Kutubxona bo'sh!")
            return
        else:
            for i in self.__all_books:
                print(f"Kitob nomi: {i.name}, muallifi: {i.muallif.ism, i.muallif.fam}, janri: {i.genre}, narxi: {i.pul}")



    def search_book(self):
        print("**********-------------------------**********")
        tanlov = int(input("1. Nom bo'yicha qidirish\n2. Narx bo'yicha qidirisih\n>>>>>>>>>>>>>> "))
        print("**********-------------------------**********")

        match tanlov:
            case 1:
                nom = input("Kitob nomini kiriting: ")
                topildi = False


                for i in self.__all_books:
                    if i.name.lower() == nom.lower():
                        print("********-------------------------------------------------------------------------------------********")
                        print(f"Kitob: {i.name}, "
                              f"Muallifi: {i.muallif.ism, i.muallif.fam}, "
                              f"Janri: {i.genre}, Narxi: {i.pul}")
                        print("********-------------------------------------------------------------------------------------********")
                        return

                if not topildi:
                    print("Bunday kitob topilmadi!")
                    return

            case 2:
                try:
                    narx = int(input("Narxni kiriting: "))
                    bor = 0
                    for i in self.__all_books:
                        if i.pul <= narx:
                            bor += 1
                            break

                    if bor > 0:
                        for i in self.__all_books:
                            if i.pul <= narx:
                                print("**********------------------------------------------------------------------------------------**********")
                                print(f"Kitob: {i.name}, Muallifi: {i.muallif.ism, i.muallif.fam}, Janri: {i.genre}, Narxi: {i.pul}")
                                print("**********------------------------------------------------------------------------------------**********")
                    else:
                        print("Bu narxdagi kitobimiz yo'q!")

                except Exception as ex:
                    print(f"{ex.__class__.__name__} xatosi sodir bo'ldi!")

            case _:
                print("Not'g'ri amal!")
                return None



    def qarz(self, user_ism: str, kitob_nomi: str):

        if len(self.__all_books) == 0:
            print("Kutubxona bo'sh, kitob olishingiz imkonsiz!")
            return

        if user_ism in self.__qarz_kitoblar:
            print("Bu foydalanuvchi avvalgi qarzini bermaguncha kitob olishi mumkin emas!")
            return

        if kitob_nomi not in self.__all_books:
            print("Bunday kitob mavjud emas!")
            return

        for i in self.__all_books:
            if i.name.lower() == kitob_nomi.lower():
                self.__qarz_kitoblar[user_ism] = i
                print(f"{user_ism} {kitob_nomi} nomli kitobni qarzga oldi!")
                return

    def qarz_delete(self, user_ism: str):

        if len(self.__qarz_kitoblar) == 0:
            print("Qarzlar yo'q!")
            return

        bor = 0

        for i in list(self.__qarz_kitoblar.keys()):
            if user_ism.lower() == i.lower():
                self.__qarz_kitoblar.pop(i)
                bor += 1
                print(f"{user_ism}ning qarzi o'chirildi!")
                return

        if bor == 0:
            print("Bu foydalanuvchida qarz yo'q!")

"""*******************************************************************************************************************************************"""