class Meme:
    def __init__(self, name, size, price):
        self.__name = name
        self.__size = size
        self.__price = price
        self.__weight = price/size

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def price(self):
        return self.__price

    @property
    def weight(self):
        return self.__weight


def calculate(usb_size: int, memes: list):
    usb_size_in_mib = usb_size * 1024
    memes_list = []
    for mem in memes:
        try:
            memes_list.append(Meme(mem[0], mem[1], mem[2]))
        except ValueError:
            print("Error. Something wrong with mem info. Wrong value.")
