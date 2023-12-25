import unittest

from swap import swap


class SwapTesting(unittest.TestCase):
    def test_en_to_ru(self):
        wait = "съешь ещё этих мягких булок, да выпей чаю!"
        result = swap("c]tim to` 'nb[ vzurb[ ,ekjr? lf dsgtq xf.!")

        self.assertEqual(result, wait)

    def test_ru_to_en(self):
        wait = "for it work, need use this function"
        result = swap("ащк ше цщклб туув гыу ершы агтсешщт")

        self.assertEqual(result, wait)


if __name__ == '__main__':
    unittest.main()
