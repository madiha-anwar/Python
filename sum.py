import sys

def sum_numeric_args(args):
    total = 0
    for arg in args:
        try:
            num = float(arg)
            total += num
        except ValueError:
            pass  # Ignore non-numeric arguments
    return total

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude script name from arguments
    result = sum_numeric_args(args)
    print("Sum:", result)
