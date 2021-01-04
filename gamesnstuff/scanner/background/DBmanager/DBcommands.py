import mysql.connector
import datetime


def connect_to_db():
    global db
    db = mysql.connector.connect(
        host="lionel17.mysql.eu.pythonanywhere-services.com",
        user="lionel17",
        passwd="LRAFPXdenP",
        database="lionel17$gamesnstuff_records",
    )
    my_cursor = db.cursor(buffered=True)
    return my_cursor


def add_entry(entry):
    my_cursor = connect_to_db()
    command = "INSERT INTO GnS_table (Name, Item, Date_Time, Status) VALUES (%s, %s, %s, %s)"
    record = (entry.name, entry.item, entry.dateAndTime, entry.status)
    my_cursor.execute(command, record)
    db.commit()
    # code to properly close cursor
    try:
        my_cursor.fetchall()  # fetch (and discard) remaining rows
    except mysql.connector.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    # end of code
    my_cursor.close()
    db.close()


def return_item(item):
    my_cursor = connect_to_db()
    my_cursor.execute(
        "SELECT Name from GnS_table WHERE (`Item`='{}' AND `Status`='missing');".format(item))
    name = my_cursor.fetchall()[0][0]
    dt = datetime.datetime.today()
    dateAndTime = "{}.{}.{}--{}:{}".format(dt.day, dt.month, dt.year, dt.hour, dt.minute)
    my_cursor.execute(
        "UPDATE `GnS_table` SET Status = '{}' WHERE (`Item`='{}' AND `Status`='missing')".format(dateAndTime,
                                                                                                 item))
    db.commit()
    # code to properly close cursor
    try:
        my_cursor.fetchall()  # fetch (and discard) remaining rows
    except mysql.connector.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    # end of code
    my_cursor.close()
    db.close()
    return name


def check_exist(column, entry):
    my_cursor = connect_to_db()
    my_cursor.execute(
        f"SELECT EXISTS(SELECT * from GnS_table WHERE (`{column}`='{entry}' AND `Status`='missing'));")
    result = my_cursor.fetchall()
    # code to properly close cursor
    try:
        my_cursor.fetchall()  # fetch (and discard) remaining rows
    except mysql.connector.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    # end of code
    my_cursor.close()
    db.close()
    return True if result[0][0] == 1 else False


def filter_missing():
    my_cursor = connect_to_db()
    my_cursor.execute(
        f"SELECT * FROM GnS_table WHERE (`Status`='missing')"
    )
    # code to properly close cursor
    results = my_cursor.fetchall()
    try:
        my_cursor.fetchall()  # fetch (and discard) remaining rows
    except mysql.connector.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    # end of code
    my_cursor.close()
    db.close()
    return results


def select_all():
    my_cursor = connect_to_db()
    my_cursor.execute(
        f"SELECT * FROM GnS_table"
    )
    results = my_cursor.fetchall()
    # code to properly close cursor
    try:
        my_cursor.fetchall()  # fetch (and discard) remaining rows
    except mysql.connector.errors.InterfaceError as ie:
        if ie.msg == 'No result set to fetch from.':
            # no problem, we were just at the end of the result set
            pass
        else:
            raise
    # end of code
    my_cursor.close()
    db.close()
    return results
