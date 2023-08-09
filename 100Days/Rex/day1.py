def fabonica(n):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        return n+fabonica(n-1)
    


if __name__ == "__main__":
    print(fabonica(3))