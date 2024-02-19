import one

print("top-level from two.py")
one.func()

if __name__ == "__main__":
    print("two.py runs directly")
else:
    print("two.py is being imported into another module")
