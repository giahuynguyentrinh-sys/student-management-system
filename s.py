def show_menu():
    print("1. Add student\n2. Show all students\n3. Update student\n4. Delete student\n5. Search student\n6. Statistics\n0. Exit")
    return  

def input_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number!")


def checkvalid_score(score): #score là một parameter thoải mái với nó
#đi vì nó chỉ là một tên ngẫu nhiên thôi
    while score < 0 or score > 10: 
        score = input_int("Enter a different score (1 to 10): ")
    return score

def add_student(students):
    student = {}
    student["id"] = input_int("press id: ")
    v = False
    while v == False:
        if student["id"] < 0:
            print("error: id < 0")    
            student["id"]=input_int("press a positive interger")
            continue
        for i in range (len(students)):
            if student["id"] == students[i]["id"]:
                student["id"]= input_int("this id exist press another id: ")
                v = False
                break #"Tôi đã tìm được thứ tôi cần (hoặc gặp điều kiện 
                            #cần dừng), không cần vòng lặp kiểm tra tiếp nữa."
        else:   
            v = True
                    
    student["name"] = input("press name: ")
    student["age"] = input_int("press age: ")
    while student["age"] < 16 or student["age"] > 100:
        student["age"] = input_int("press valid age (16 to 100): ")   
    student["gender"] = input("press gender: ")
    while student["gender"].lower() != "male" and student["gender"].lower() != "female":
        student["gender"] = input("press valid gender(male or female): ")
    student["major"] = input("press major: ")
    student["math"] = checkvalid_score(input_int("Press math score: "))
    student["english"] = checkvalid_score(input_int("Press english score: "))
    student["programming"] = checkvalid_score(input_int("Press programming score"))
    students.append(student)
    print("add student successfully")
    return

def showall_student(students):
    for i in range(len(students)):
        print(students[i])
        
def update_student(students):
    v = input_int("press to find student id: ")
    found_student = False
    while found_student == False:
        if v < 0:
            print("error: id < 0")    
            v =input_int("press a positive interger id")
            continue
        for i in range (len(students)):
            if v == students[i]["id"]:
                found_student = True
                x = students[i]
                break
        else:
            found_student = False
            v= input_int("this id don't exist press another id: ")
    n = -1
    while n != 0:
        n = input_int("1. Name\n2. Age\n3. Gender\n4. Major\n5. Math\n6. English\n7. Programming\n0. Cancel\nChoose an aspect you want to change")
        if n == 1:
            x["name"] = input("change your name: ")
        elif n == 2:
            x["age"] = input_int("press age: ")
            while x["age"] < 16 or x["age"] > 100:
                x["age"] = input_int("press valid age (16 to 100): ")   
        elif n == 3:
            x["gender"] = input("press gender: ")
            while x["gender"].lower() != "male" and x["gender"].lower() != "female":
                x["gender"] = input("press valid gender(male or female): ")
        elif n == 4:
            x["major"] = input("change your major: ")
        elif n == 5:
            x["math"] = checkvalid_score(input_int("Press math score: "))
        elif n == 6:
            x["english"] = checkvalid_score(input_int("change english score: "))
        elif n == 7:
            x["programming"] = checkvalid_score(input_int("change programming score: "))
    print("update completed")
        
            
    
        


def main():
    students = []

    while True:
        show_menu()
        choice = input_int("Choose: ")

        if choice == 1:
            add_student(students)

        elif choice == 2:
            showall_student(students)

        elif choice == 3:
            update_student(students)

        elif choice == 4:
            print("Delete student: Not implemented")

        elif choice == 5:
            print("Search student: Not implemented")

        elif choice == 6:
            print("Statistics: Not implemented")

        elif choice == 0:
            print("Program ended.")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()