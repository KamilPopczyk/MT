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
        correct_answer = (22, {"sad_pepe_compilation.gif", "yodeling_kid.avi"})
        self.assertEqual(correct_answer, main.calculate(usb_size, memes))
