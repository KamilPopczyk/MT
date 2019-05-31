import unittest
import main


class TestMain(unittest.TestCase):
    def test_calculate(self):
        usb_size = 1
        memes = [
            ("rollsafe.jpg", 205, 6),
            ("sad_pepe_compilation.gif", 410, 10),
            ("yodeling_kid.avi", 605, 12),
        ]
        correct_answear = (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})
        self.assertEqual(main.calculate(usb_size, memes), correct_answear)
