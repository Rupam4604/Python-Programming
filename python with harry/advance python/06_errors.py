while True:
    try:
        a= int(input("enter the number 1: "))
        b= int(input("enter the number 2: "))
        print(f"sum of the number: {a+b}")

    except ValueError:
        print("Invalid input! Please enter a number.")

    except Exception as e:
        print("some  error occurerd!", e)

  