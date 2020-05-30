if __name__ == "__main__":
    # simple if block
    p = int(input("Enter you percentage:"))
    if 100 >= p >= 80:
        print("Distinction")
    elif p >= 70:
        print("First class")
    elif p >= 60:
        print("Second Class")
    elif p >= 50:
        print("Pass")
    else:
        print("Fail")
    # while loop
    i = 0
    while i < 5:
        p = int(input("Enter you percentage:"))
        if 100 >= p >= 80:
            print("Distinction")
        elif 80 >= p >= 70:
            print("First class")
        elif 70 >= p >= 60:
            print("Second Class")
        elif 60 >= p >=50:
            print("Pass")
        else:
            print("Fail")

            i += 1  # it is similar to i = i+1

    #for block
    for i in range(10):
        if i == 3:
            break
        p = int(input("Enter you percentage:"))
        if 100 >= p >= 80:
            print("Distinction")
        elif 100 >= p >= 70:
            print("First class")
        elif 100 >= p >= 60:
            print("Second Class")
        elif 100 >= p >= 50:
            print("Pass")
        else:
            print("Fail")






