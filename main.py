from typing import List, Tuple, Set


class Meme:
    """"Class represtens mem info"""

    def __init__(self, name, size, price):
        self.__name = name
        self.__size = size
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def size(self):
        return self.__size

    @property
    def price(self):
        return self.__price


class USBStick:
    """"Class represents usb stick"""

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

    def give_content(self):
        return self.price_of_memes, {x.name for x in self.__memes}

    def replace_memes(self, memes: list):
        self.format()
        for mem in memes:
            self.add_mem(mem)

    def format(self):
        self.__memes.clear()
        self.__price_of_memes = 0
        self.__free_space = self.__capacity

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


def calculate(usb_size: int, memes: List[Tuple[str, int, int]]) -> Tuple[int, Set[str]]:
    memes_list = []
    for mem in memes:
        try:
            memes_list.append(Meme(mem[0], mem[1], mem[2]))
        except ValueError:
            print("Error. Something wrong with mem info. Wrong value.")

    # Algorithm inspired with Knapsack problem
    # Dynamic programming
    sticks = [
        [USBStick(j) for j in range(usb_size * 1024 + 1)]
        for i in range(len(memes_list) + 1)
    ]  # matrix od sticks
    for i in range(1, len(memes_list) + 1):
        for j in range(1, usb_size * 1024 + 1):
            if (
                memes_list[i - 1].size > j
            ):  # check if current mem can be stored in stick with j space
                sticks[i][j].replace_memes(
                    sticks[i - 1][j].memes
                )  # stick_ij formats and add new mem for stick_i-1,j
            else:
                # choose better option max(option1, option2)
                stick_tested = sticks[i - 1][j - memes_list[i - 1].size]
                if (memes_list[i - 1].price + stick_tested.price_of_memes) > sticks[
                    i - 1
                ][j].price_of_memes:
                    sticks[i][j].replace_memes(stick_tested.memes)
                    sticks[i][j].add_mem(memes_list[i - 1])  # add new mem
                else:
                    sticks[i][j].format()
                    for mem in sticks[i - 1][j].memes:
                        sticks[i][j].add_mem(mem)

    return sticks[len(memes_list)][usb_size * 1024].give_content()
