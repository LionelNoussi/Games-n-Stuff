from . import create_entry, DBcommands, check
from scanner.models import Item, Student


def process_form(student_id, item):
    create_entry.create_log_entry(student_id, item)


def create_overview():
    missing = DBcommands.filter_missing()
    cleanList = []
    for entry in missing:
        cleanList.append((entry[1], entry[2], entry[3]))
    return cleanList


def create_history():
    entries = DBcommands.select_all()
    reverseList = []
    for index in range(len(entries)-1, 0, -1):
        reverseList.append(entries[index])
    return reverseList

def reload():
    check.itemList = [f"{i.item_name}" for i in Item.objects.all()]
    check.names = {f"{n.student_id}": f"{n.student_name}" for n in Student.objects.all()}
