from typing import List, Tuple, Set


class Meme:
    """Meme class represents basic mem info.

    The __init__ method get info about mem: name, size and price.

    Args:
        name (str): Meme's name.
        size (int): Size of meme in MiB.
        price (int): Meme's price.
    """

    def __init__(self, name: str, size: int, price: int):
        self.__name = name
        self.__size = size
        self.__price = price

    @property
    def name(self) -> str:
        """str: Return meme's name."""
        return self.__name

    @property
    def size(self) -> int:
        """int: Return meme's size."""
        return self.__size

    @property
    def price(self) -> int:
        """int: Return meme's price."""
        return self.__price


class USBStick:
    """USBStick class represents usb stick. It work as 'real' usb stick,
    because can 'store' data -> memes.

    The __init__ method get info about usb stick: capacity.

    Args:
        capacity (int): USB stick's capacity in MiB.
    """

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__free_space = capacity
        self.__price_of_memes = 0
        self.__memes = []

    def add_mem(self, mem: Meme) -> bool:
        """bool: If usb stick has free space, add new mem. Return True if success."""
        if self.__free_space > mem.size:
            if mem not in self.memes:
                self.__memes.append(mem)
                self.__price_of_memes += mem.price
                self.__free_space -= mem.size
                return True
        else:
            return False

    def give_content(self) -> Tuple:
        """Tuple: Return tuple of price of all memes and list of stored memes."""
        return self.price_of_memes, {x.name for x in self.__memes}

    def replace_memes(self, memes: list):
        """Copy data from another usb stick."""
        self.format()
        for mem in memes:
            self.add_mem(mem)

    def format(self):
        """Clear all stored data in usb stick."""
        self.__memes.clear()
        self.__price_of_memes = 0
        self.__free_space = self.__capacity

    @property
    def memes(self) -> List:
        """List: Return list of stored memes."""
        return self.__memes

    @property
    def capacity(self) -> int:
        """int: Return usb stick's capacity."""
        return self.__capacity

    @property
    def free_space(self) -> int:
        """int: Return left free space."""
        return self.__free_space

    @property
    def price_of_memes(self) -> int:
        """int: Return summary price of stored memes."""
        return self.__price_of_memes


def calculate(usb_size: int, memes: List[Tuple[str, int, int]]) -> Tuple[int, Set[str]]:
    """Function calculate return the most profitable set of given memes list.

    Algorithm:
        Chosen algorithm is ...

    Args:
        usb_size (int): USB stick's size in MiB.
        memes (List(Tuple(str,int,int)): List of memes'tuples with info about meme.

    Returns:
        Function returns Tuple of two elements:
            (int) price of all chosen memes.
            (Set) set of name of all chosen memes.
    """

    memes_list = [
        Meme(mem[0], mem[1], mem[2]) for mem in memes
    ]  # new list of objects of memes

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
