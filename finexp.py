def division(a,b):
    try:
        return int(a)/b
    except TypeError:
        print("Type eroor")
    except ValueError:
        print("Value error")
    finally:
        print("Finally")
    print("Done")
division('A',10)