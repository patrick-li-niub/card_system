# 根据用户输入决定后续的操作
import card_tools_rep

while True:

    card_tools_rep.show_menu()
    action = input("please input your choice")

    if action in ["1", "2", "3","4", "5"]:
        if action == "1":
            card_tools_rep.new_card()
        elif action == "2":
            card_tools_rep.show_all()
        elif action == "4":
            card_tools_rep.remove_card()
        elif action == "5":
            card_tools_rep.fix_card()
        else:
            card_tools_rep.search_cards()
    elif action == "0":
        print("exiting the system")
        break
    else:
        print("please re-enter your choice")