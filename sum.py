import sys

args = sys.argv[1:]  # Exclude script name from arguments

total = 0
for arg in args:
    try:
        num = float(arg)
        total += num
    except ValueError:
        pass  # Ignore non-numeric arguments

print("Sum:", total)