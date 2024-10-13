import tasks.t_2_1

if __name__ == '__main__':
    user_input = input("Enter a number (1-16) to choose an option: ")
    match user_input:
        case '1':
            tasks.t_2_1.task()
        case _:
            print("Invalid")
