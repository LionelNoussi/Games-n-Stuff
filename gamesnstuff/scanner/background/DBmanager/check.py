from . import DBcommands
from scanner.models import Item, Student

itemList = [f"{i.item_name}" for i in Item.objects.all()]

names = {f"{n.student_id}": f"{n.student_name}" for n in Student.objects.all()}

clear = "78903"

messageList = []


def get_name(student_id):
    name = names[student_id]
    return name


def check_if_returning(student_id):
    if student_id in itemList:
        if DBcommands.check_exist("Item", student_id):
            name = DBcommands.return_item(student_id)
            messageList.append(("Returned", name, student_id))
            return "Return"
        messageList.append(("Invalid student ID", "----", "----"))
        return "Invalid student ID"
    return clear


def already_borrowed_check(student_id, item):
    name = get_name(student_id)
    my_cursor = DBcommands.connect_to_db()
    my_cursor.execute(f"SELECT EXISTS(SELECT * FROM GnS_table WHERE (`Name`='{name}' AND `Status`='missing' "
                      f"AND `Item`!='{item}'))")
    result = my_cursor.fetchall()
    if result[0][0] == 1:
        messageList.append(("Already borrowed something", name, "----"))
    my_cursor.close()


def check_if_student(student_id):
    try:
        names[student_id]
    except KeyError:
        messageList.append(("Invalid student ID", "----", "----"))
        return "Invalid student ID"
    else:
        return clear


def check_if_item(item):
    if item in itemList:
        if DBcommands.check_exist("Item", item):
            check_if_returning(item)
        return clear
    messageList.append(("Invalid item", "----", "----"))
    return "Invalid item"


def check_input(student_id, item):
    result = check_if_returning(student_id)
    if result != clear:
        return

    result = check_if_student(student_id)
    if result != clear:
        return

    result = check_if_item(item)
    if result != clear:
        return False

    already_borrowed_check(student_id, item)
    return True
