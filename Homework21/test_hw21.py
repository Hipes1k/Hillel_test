import unittest
from hw21 import *

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibo = Fibonacci()

    def test_letters_input(self):
        with self.assertRaises(ValueError):
            self.fibo('a')

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.fibo(-1)

    def test_fract_input(self):
        with self.assertRaises(ValueError):
            self.fibo(7.2)

    def test_large_number_input(self):
        try:
            self.fibo(50)
        except RecursionError as e:
            self.fail(f"Test failed with exception: {e}")

    def test_none_input(self):
        with self.assertRaises(ValueError):
            self.fibo(None)

    def test_dict_input(self):
        with self.assertRaises(ValueError):
            self.fibo(dict)

    def test_valid_number_input(self):
        self.assertEqual(self.fibo(0), 0)
        self.assertEqual(self.fibo(1), 1)

    def test_cache(self):
        self.fibo(1)
        self.assertEqual(self.fibo.cache, [0, 1])


class TestFormattedName(unittest.TestCase):
    def test_with_all_params(self):
        text_input = formatted_name("alexaNdr", "uShakov", "igorevich")
        self.assertEqual(text_input, "Alexandr Igorevich Ushakov")

    def test_without_first_param(self):
        text_input = formatted_name("", "ushakov", "igorevich")
        self.assertEqual(text_input, " Igorevich Ushakov")

    def test_without_second_param(self):
        text_input = formatted_name("alexandr", "", "igorevich")
        self.assertEqual(text_input, "Alexandr Igorevich ")

    def test_without_last_param(self):
        text_input = formatted_name("alexandr", "ushakov", "")
        self.assertEqual(text_input, "Alexandr Ushakov")

    def test_without_all_params(self):
        text_input = formatted_name("", "", "")
        self.assertEqual(text_input, " ")

    def test_with_different_register(self):
        text_input = formatted_name("alexandr", "UshAKov", "igorevich")
        self.assertEqual(text_input, "Alexandr Igorevich Ushakov")

    def test_none_param(self):
        with self.assertRaises(TypeError):
            formatted_name(None, "ushakov", "igorevich")

    def test_dict_param(self):
        with self.assertRaises(TypeError):
            formatted_name(dict, "ushakov", "igorevich")

    def test_set_param(self):
        with self.assertRaises(TypeError):
            formatted_name(set, "ushakov", "igorevich")

    def test_tuple_param(self):
        with self.assertRaises(TypeError):
            formatted_name(tuple, "ushakov", "igorevich")

    def test_list_param(self):
        with self.assertRaises(TypeError):
            formatted_name(list, "ushakov", "igorevich")

    def test_bool_param(self):
        with self.assertRaises(TypeError):
            formatted_name(bool, "ushakov", "igorevich")

    def test_float_param(self):
        with self.assertRaises(TypeError):
            formatted_name(float, "ushakov", "igorevich")

    def test_int_input(self):
        with self.assertRaises(TypeError):
            formatted_name(int, "ushakov", "igorevich")