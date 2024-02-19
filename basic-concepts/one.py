def func():
    print("func() from one.py")


print("Top level in one.py")

if __name__ == "__main__":
    print("one.py runs directly")
else:
    print("one.py is being imported into another module")
