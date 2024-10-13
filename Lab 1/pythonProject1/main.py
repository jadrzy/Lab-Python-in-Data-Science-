import example_code_1
import task_1_1
import task_1_2
import task_1_3
import task_1_4
import task_1_5
import task_1_6
import task_1_7
import task_1_9
import task_1_10
import task_1_11
import task_1_12
import task_1_13
import task_1_14
import task_1_15
import task_1_16

if __name__ == '__main__':
    #example_code_1.task()
    user_input = input("Enter a number (1-16) to choose an option: ")
    match user_input:
        case '1':
            task_1_1.task()
        case '2':
            task_1_2.task()
        case '3':
            task_1_3.task()
        case '4':
            task_1_4.task()
        case '5':
            task_1_5.task()
        case '6':
            task_1_6.task()
        case '7', '8':
            task_1_7.task()
        case '9':
            task_1_9.task()
        case '10':
            task_1_10.task()
        case '11':
            task_1_11.task()
        case '12':
            task_1_12.task()
        case '13':
            task_1_13.task()
        case '14':
            task_1_14.task()
        case '15':
            task_1_15.task()
        case '16':
            task_1_16.task()
        case _:
            print("Invalid")
