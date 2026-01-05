import re

def main():
  print(validate(input("IPv4 Address: ")))


def validate(ip):
  pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

  match = re.match(pattern, ip)

  if match:
    parts = [int(part) for part in match.groups()]
    print(parts)
    for part in parts:
      if part < 0 or part > 255:
        return False
      else:
        return True
  else:
    return False
  

if __name__ == "__main__":
  main()