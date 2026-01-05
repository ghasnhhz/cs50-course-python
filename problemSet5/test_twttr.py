from twttr import shorten

def test_hello():
  assert shorten("hello") == "hll"

def test_name():
  assert shorten("name") == "nm"