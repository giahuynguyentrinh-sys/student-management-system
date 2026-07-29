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
    return

def satistics(students):
    if len(students) == 0:
        print ("no students stat to calculate please return to menu to add more students")
        return
    else: 
        stat = -1
        while stat != 0:
            stat = input_int("""
========== Statistics ==========
1. Total students
2. GPA of each student
3. Highest GPA student(s)
4. Students by major
5. Average score of each subject
6. Students by classification
0. Back
===============================
""")
            if stat < 0 or stat > 6:
                print("press 0 to 6")
                continue
            elif stat == 1:
                print(f"total students: {len(students)}")
            elif stat == 2:
                for i in range (len(students)):
                    x = (students[i]["math"]+students[i]["english"]+students[i]["programming"]) /3
                    print(f"{students[i]["name"]}: {round(x,2)}")
            elif stat == 3:
                highest = []
                for i in range (len(students)):
                    x = (students[i]["math"]+students[i]["english"]+students[i]["programming"]) /3
                    highest.append(x)
                for i in range (len(students)):
                    if (students[i]["math"]+students[i]["english"]+students[i]["programming"]) /3 == max(highest):
                        print(f"{students[i]["name"]} highest gpa:  {max(highest)}")
                        break
            elif stat == 4:
                category = {}
                for i in range(len(students)):
                    x = students[i]["major"]
                    if x not in category:
                        category[x] = []
                        category[x].append(students[i])

                for major, list_sv in category.items():
                    print(f"major: {major}, students: {len(list_sv)}")
            elif stat == 5:
                math = 0
                english = 0
                programming = 0
                for i in range (len(students)):
                    math += students[i]["math"]
                    english += students[i]["english"]
                    programming += students[i]["programming"]
                print(f"Average Math Score: {math / len(students):.2f}")
                print(f"Average English Score: {english / len(students):.2f}")
                print(f"Average Programming Score: {programming / len(students):.2f}")
            elif stat == 6:
                exce = []
                good = []
                average = []
                poor = []
                for i in range (len(students)):
                    gpa = (students[i]["math"]+students[i]["english"]+students[i]["programming"]) /3
                    if gpa >= 9.0:
                        exce.append(students[i])
                    elif gpa >= 8.0:
                        good.append(students[i])
                    elif gpa >= 6.5:
                        average.append(students[i])
                    else:
                        poor.append(students[i])
                print("===== Student Classification =====")
                print(f"Excellent : {len(exce)}")
                print(f"Good      : {len(good)}")
                print(f"Average   : {len(average)}")
                print(f"Poor      : {len(poor)}")
        print("exit successfully")
        return    
choice = -1
students = []
while choice != 0:
    choice = input_int("""
========== Student Management ==========
1. Add student
2. Show all students
3. Update student
4. Delete student
5. Search student
6. Statistics
7. Top 3 GPA
0. Exit
========================================
""")
    if choice < 0 or choice > 7:
        print("choose 0 to 7: ")
        continue
    elif choice == 1:
        add_student(students)
    elif choice == 2:
        showall_student(students)
    elif choice == 3:
        update_student(students)
    elif choice == 4:
        delete_student(students)
    elif choice == 5:
        search_student(students)
    elif choice == 6:
        satistics(students)
    elif choice == 7:
        
                
        
            
            
        
print("Program exited successfully.")


        

"""Cú pháp for x in một_thứ_gì_đó: luôn tự động 
duyệt qua từng phần tử của "thứ đó" theo thứ tự, 
không cần bạn tự quản lý index. range(n) sinh ra chuỗi số, 
category.items() sinh ra chuỗi tuple — cơ chế lặp 
giống hệt nhau, chỉ khác loại dữ liệu được sinh ra thôi."""    
        

