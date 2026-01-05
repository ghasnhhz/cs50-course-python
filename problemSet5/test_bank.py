from bank import greeting

def test_hello():
  assert greeting("hellou") == "$0"

def test_hi():
  assert greeting("hi") == "$20"

def test_something():
  assert greeting("somethingElse") == "$100"

