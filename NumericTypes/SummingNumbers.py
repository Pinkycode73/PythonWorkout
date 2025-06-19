def mysum():
    print("Hi there! i hope you are doing well and fine 😊😊😊, plz type only numbers 🙃😉")
    user_input = input("Enter the numbers you want to sum (space-separated): ")
    number_list = [int(x) for x in user_input.strip().split()]
    print("Parsed numbers:", number_list)
    sum =  0
    for item in number_list:
        sum += item
    print(f'the sum of {number_list} is {sum}')
    print("Bye friend see you soon 😘😘")
    
if __name__ == "__main__":
    mysum()
    