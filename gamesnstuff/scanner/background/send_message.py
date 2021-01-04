from django.contrib import messages


successfulMessages = ["Success"]
neutralMessages = ["Returned"]
badMessages = ["Invalid student ID", "Invalid item"]
warningMessages = ["Already borrowed something"]


def make_toast(request, message, student_name, item):
    message_texts = {"Success": f"{student_name} successfully borrowed item: {item}",
                     "Returned": f"{student_name} successfully returned item: {item}",
                     "Invalid student ID": "Your student ID was not recognized!",
                     "Invalid item": "The item you tried to borrow doesn't exist!",
                     "Already borrowed something": f"WARNING: Please {student_name }, remember to also return the "
                                                   f"things you have already borrowed!"}
    if message in successfulMessages:
        messages.success(request, f"{message_texts[message]}")
    if message in badMessages:
        messages.error(request, f"{message_texts[message]}")
    if message in neutralMessages:
        messages.info(request, f"{message_texts[message]}")
    if message in warningMessages:
        messages.warning(request, f"{message_texts[message]}")
