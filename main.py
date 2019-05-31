class Meme:
    def __init__(self, name, size, price):
        self.__name = name
        self.__size = size
        self.__price = price
        self.__weight = price / size

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


class USBStick:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__free_space = capacity
        self.__price_of_memes = 0
        self.__memes = []

    def add_mem(self, mem: Meme):
        if self.__free_space > mem.size:
            self.__memes.append(mem)
            self.__price_of_memes += mem.price
            self.__free_space -= mem.size
            return True
        else:
            return False

    def give_content(self):
        return self.price_of_memes, {x.name for x in self.__memes}

    @property
    def capacity(self):
        return self.capacity

    @property
    def price_of_memes(self):
        return self.__price_of_memes


def calculate(usb_size: int, memes: list):
    usb_stick = USBStick(usb_size * 1024)
    memes_list = []
    for mem in memes:
        try:
            memes_list.append(Meme(mem[0], mem[1], mem[2]))
        except ValueError:
            print("Error. Something wrong with mem info. Wrong value.")

    # Algorithm inspired with Knapsack problem
    memes_list.sort(key=lambda x: x.weight, reverse=False)
    for mem in memes_list:
        print(mem.size, mem.weight)
    for mem in memes_list:
        usb_stick.add_mem(mem)

    return usb_stick.give_content()
