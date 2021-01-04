import mysql.connector
import datetime

#local imports
from . import check, DBcommands

db = mysql.connector.connect(
    host="lionel17.mysql.eu.pythonanywhere-services.com",
    user="lionel17",
    passwd="LRAFPXdenP",
    database="lionel17$gamesnstuff_records",
)

my_cursor = db.cursor(buffered=True)


class LogEntry:

    def __init__(self, student_id, name, item, dateAndTime):
        self.id = student_id
        self.name = name
        self.item = item
        self.dateAndTime = dateAndTime
        self.status = "missing"


def create_log_entry(student_id, item):
    result = check.check_input(student_id, item)
    if result == True:
        name = check.get_name(student_id)
        dt = datetime.datetime.today()
        dateAndTime = "{}.{}.{}--{}:{}".format(dt.day, dt.month, dt.year, dt.hour, dt.minute)
        entry = LogEntry(student_id, name, item, dateAndTime)
        DBcommands.add_entry(entry)
        check.messageList.append(("Success", name, item))
        my_cursor.close()
        db.close()
        return
    my_cursor.close()
    db.close()
    return
