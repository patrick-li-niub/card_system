card_list = []
def show_menu():

    print('welcome ')
    print("*" * 50)
    print("press 1 to add new cards")
    print("press 2 to show all the cards")
    print("press 3 to search cards")
    print("")
    print("press 0 to exit the system")
    print("*" * 50)

def new_card():
    name = input("please enter the name")
    phone = input("please enter the phone number")
    qq = input("please enter the qq number")
    email = input("please enter the email address")
    information = {"name" : name,
                   "phone" : phone,
                   "qq": qq,
                   "email": email}
    card_list.append(information)
    print("successfully add %s's card" %name)

def show_all():
    if len(card_list) == 0:
        print("cannot find any cards")
        return
    else:
        for i in card_list:
            print(i)

def search_cards():
    search_name = input("please enter the name you are searching for")
    for i in card_list:
        if i["name"] == search_name:
            print(i)
        else:
            print("cannot find the name you are looking for")
def remove_card():
    remove = input("please enter the name you are about to remove")
    for i in card_list:
        if remove == i["name"]:
            card_list.remove(i)
            print("successfully remove %s's card" %remove)
        else:
            print('can not find the card you are about to remove')

def fix_card():
    fix = "please enter the name of the card"
    for i in card_list:
        if i["name"] == fix:
            i["name"] = input("please enter the name you are about to fix")
            i["phone"] = input("please enter the phone number you are about to fix")
            i["qq"] = input("please enter the qq number you are about to fix")
            i["email"] = input("please enter the email address you are about to fix")
            print("successfully fix %s's card" %fix)
            print(i)






