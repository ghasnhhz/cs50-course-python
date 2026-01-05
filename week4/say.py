import cowsay
import sys
from sayings import hello, goodBye


if len(sys.argv) == 2:
    # cowsay.cow("hello, " + sys.argv[1])
    hello(sys.argv[1])
    goodBye(sys.argv[1])

    