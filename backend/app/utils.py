def pr[T](val: T, title: str = "") -> T:
    print(f" -------------- {title} -------------- ")
    print(f"type: {type(val)}")
    print(val)
    print("")
    return val
