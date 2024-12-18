import main
import unittest


class Tests(unittest.TestCase):
    def first_test(self):
        test_data = [("test1", "test1", "test1"), ("test2", "test2", "test2")]
        result = main.first_task(test_data)
        good_result = sorted(test_data, key=lambda x: x[0])
        self.assertEqual(result, good_result)

    def second_test(self):
        test_data = [('some_text.txt', 1, 'Texts'), ('more_text.txt', 2, 'Texts'), ('first.py', 3, 'PythonCode'), ('second.py', 4, 'PythonCode'), ('third.py', 5, 'PythonCode')]
        result = main.second_task(test_data)
        good_result = [('PythonCode', 3), ('Texts', 2)]
        self.assertEqual(result, good_result)
        
    def third_test(self):
        test_data = [('some_text.txt', 1, 'Texts'), ('some_text.txt', 1, 'PythonCode'), ('more_text.txt', 2, 'Texts'), ('first.py', 3, 'PythonCode'), ('second.py', 4, 'PythonCode'), ('third.py', 5, 'PythonCode')]
        result = main.third_task(test_data, "txt")
        good_result = [('some_text.txt', 'Texts'), ('some_text.txt', 'PythonCode'), ('more_text.txt', 'Texts')]
        self.assertEqual(result, good_result)

t = Tests()

t.first_test()
t.second_test()
t.third_test()