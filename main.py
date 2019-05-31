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
            if mem not in self.memes:
                self.__memes.append(mem)
                self.__price_of_memes += mem.price
                self.__free_space -= mem.size
                return True
        else:
            return False

    def format(self):
        self.__memes.clear()
        self.__price_of_memes = 0
        self.__free_space = self.__capacity

    def give_content(self):
        return self.price_of_memes, {x.name for x in self.__memes}

    @property
    def memes(self):
        return self.__memes

    @property
    def capacity(self):
        return self.__capacity

    @property
    def free_space(self):
        return self.__free_space

    @property
    def price_of_memes(self):
        return self.__price_of_memes


def calculate(usb_size: int, memes: list):
    # usb_stick = USBStick(usb_size * 1024)
    memes_list = []
    for mem in memes:
        try:
            memes_list.append(Meme(mem[0], mem[1], mem[2]))
        except ValueError:
            print("Error. Something wrong with mem info. Wrong value.")

    # Algorithm inspired with Knapsack problem
    # memes_list.sort(key=lambda x: x.weight, reverse=True)
    # for mem in memes_list:
    #     usb_stick.add_mem(mem)
    usb_sticks = [USBStick(x) for x in range(1, usb_size * 1024 + 1)]
    # for i_usb_stick in range(len(usb_sticks)):
    #     for i_mem in range(len(memes_list)):
    #         if memes_list[i_mem] > usb_sticks[i_usb_stick]:
    #             usb_sticks[i_usb_stick] = usb_sticks[i_usb_stick-1].add_mem(memes_list[i_mem])
    A = [[USBStick(j) for j in range(usb_size*1024+1)] for i in range(len(memes_list)+1)]
    for i in range(1, len(memes_list)+1):
        for j in range(1, usb_size*1024+1):
            if memes_list[i-1].size > j: # check if current mem can be stored in stick with j space
                # no ? so this stick can only has previous mem
                A[i][j].format()
                for mem in A[i-1][j].memes:
                    A[i][j].add_mem(mem)
            else:
                # choose better option
                if (memes_list[i-1].price + A[i-1][j-memes_list[i-1].size].price_of_memes) > A[i-1][j].price_of_memes:
                    A[i][j].format()
                    for mem in A[i-1][j-memes_list[i-1].size].memes:
                        A[i][j].add_mem(mem)
                    A[i][j].add_mem(memes_list[i-1])
                else:
                    A[i][j].format()
                    for mem in A[i-1][j].memes:
                        A[i][j].add_mem(mem)
                # dodac z poprzedniego memey = ta sama wartość

    return A[len(memes_list)][usb_size*1024].give_content()


usb_size = 1
memes = [
    ("rollsafe.jpg", 205, 6),
    ("sad_pepe_compilation.gif", 410, 10),
    ("yodeling_kid.avi", 605, 12),
]
print(calculate(usb_size, memes))