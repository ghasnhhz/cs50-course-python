from lines import get_num_of_lines

def test_students_write_py():
  assert get_num_of_lines("students_write.py") == 18

def test_hello_py():
  assert get_num_of_lines("hello.py") == 2

def test_lines_py():
  assert get_num_of_lines("lines.py") == 28