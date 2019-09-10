# x = "x"
# y = "y"
# z = "z"
# b = [0, "Berhasil"
# contoh = (0,{"test_1" : [0,[0,[0,b]]]})
# def fungsi(x):
#     if x == "x":
#         return 1
# def fungsi2(x,y):
#     if x == "x" and y == "y":
#         return 1
# def fungsi3(z):
#     if z == "z":
#         return "b"
# def fungsi4():
#     1
# contoh[fungsi(x)]["test_1"][fungsi2(x,y)][fungsi3(z)[fungsi4()]]

m = 1
def register():
    user = input("User: ")
    password = input("Password: ")
    userlogin_dict[user] = password
    print("Succesfully registered")

def login():
    user1 = input("User: ")
    password1 = input("Passowrd: ")  
    if user1 not in userlogin_dict.keys() and password1 not in userlogin_dict.values():
        print("Welcome {}".format(user1))
        userlogin.append(user1)
    else:
        print("User/Password salah")

def classregist(x):
    if x == 1:
        classregistt.append("Data Science")
    elif x == 2:
        classregistt.append("Web & App Developer")
    elif x == 3:
        classregistt.append("Digital Marketing")
    elif x == 4:
        classregistt.append("UI/UX")
    else:
        print("Class is not available")
userlogin = []
classregistt = []
classregisttt = {}  
while (m==1):
    userlogin_dict = {}
    print("Welcome to Purwadhika Class Registeration! Please Choose your selection")
    print("1.Register")
    print("2.Login")
    print("3.Class Registeration")
    print("4.History")
    print("5.Logout")
    print("6.Exit")
    choose = int(input("Choose: "))
    if choose == 1:
        register()
    elif choose == 2:
        login()
    elif choose == 3:
        print("1. Data Science")
        print("2. Web & App Developer")
        print("3. Digital Marketing")
        print("4. UI/UX")
        classregist_input = int(input("Choose your class: "))
        classregist(classregist_input)
    elif choose == 4:
        if len(classregistt) == 1:
            print("{} Class is {}".format(userlogin[0],classregistt[0]))
        if len(classregistt) == 0:
            print("Select your class first")
        else:
            print("{} classes are ".format(userlogin[0]))
    elif choose == 5:
        userlogin = []
        classregistt = []
    else:
        break
