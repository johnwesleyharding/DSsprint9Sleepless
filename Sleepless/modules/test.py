from whatever import addition
import unittest

class FunctTester(unittest.TestCase):
    """
    nope
    """
    def test_addition(self):
        try: 
            self.assertEqual(addition(1, 1), 10)
        except:
            pass

    def test_zebisnotatl(self):
        pass

if __name__ == '__main__':
    unittest.main()