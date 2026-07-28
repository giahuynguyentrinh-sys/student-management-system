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
    student["programming"] = checkvalid_score(input_int("Press programming score: "))
    students.append(student)
    print("add student successfully")
    return

def showall_student(students):
    if(len(students)) == 0:
        print("no students")
        return 
    for i in range(len(students)):
        print(students[i])
        
def update_student(students):
    v = input_int("press to find student id: ")
    found_student = False
    while found_student == False:
        if v < 0:
            print("error: id < 0")    
            v =input_int("press a positive interger id: ")
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
        n = input_int("1. Name\n2. Age\n3. Gender\n4. Major\n5. Math\n6. English\n7. Programming\n0. Cancel\nChoose an aspect you want to change: ")
        while n < 0 or n >7:
            print("1. Name\n2. Age\n3. Gender\n4. Major\n5. Math\n6. English\n7. Programming\n0. Cancel")
            n=input_int("press valid number (0 to 7)")
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
        
def delete_student(students):
    n = input_int("press id to delete: ")
    v = False
    while v == False:
            if n < 0:
                print("error: id < 0")    
                n=input_int("press a positive interger")
                continue
            for i in range (len(students)):
                        if n == students[i]["id"]:
                            v = True
                            del students[i]
                            break
            else:
                v = False
                n= input_int("this id don't exist press another id: ")
            

def search_student(students):
    choice = input_int("1. Search by ID\n2. Search by Name\n3. Search by Major")
    if choice == 1:
        myid = input_int("press id to search student: ")
        foundid = False
        while foundid == False:
                    if myid < 0:
                        print("error: id < 0")    
                        myid=input_int("press a positive interger")
                        continue
                    for i in range (len(students)):
                                if myid == students[i]["id"]:
                                    foundid = True
                                    print(students[i])
                                    break
                    else:
                        foundid= True
                        print("this id don't exist")
    elif choice == 2:
        myname = input("press name: ")
        foundname = False
        while foundname == False:
            listname = []
            for i in range (len(students)):
                if myname == students[i]["name"]:
                    listname.append(students[i])
                    foundname = True
            if len(listname) == 0:
                print("no name found")
                break
            print(listname)
    elif choice == 3:
    mymajor = input("press major: ")
    foundmajor = False
    while foundmajor == False:
        listmajor = []
        for i in range(len(students)):
            if mymajor == students[i]["major"]:
                listmajor.append(students[i])
                foundmajor = True
        if len(listmajor) == 0:
            print("no major found")
            break
        print(listmajor)
    
                
            
    
        

