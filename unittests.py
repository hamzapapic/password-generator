import unittest
import password_generator
class TestStringMethods(unittest.TestCase):

    def test_lenght(self):
        password = password_generator.password_generator(True, True, 20)
        self.assertEqual(len(password),20)

if __name__ == '__main__':
    unittest.main()