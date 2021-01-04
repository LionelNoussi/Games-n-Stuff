# Games-n-Stuff
Games 'n Stuff is an online webapp which allows borrowing items through a barcode scanner. Django + Python

This site was designed for my school, in order for the students to borrow games like Frisbees, UNO cards, chess boards and card decks by just scanning their student ID and the barcode located on the item.

The site is supposed to be used with an HID barcode scanner (basically a scanner that acts as a keyboard) and a desktop without keyboard access for the students.

I programmed this because I came to see the lack of systems to process data input from a barcode scanner. If you want to use the concept of the site for one of your own projects, feel free to copy any section you like and Please! contact me if you have any questions. 

I would also love to know what you think about it and if you feel that the site would benefit a more broad solution applicable for costum needs of a certain user.

MyEmail: lio.noussi@gmail.com

To visit the site, go to: http://lionel17.eu.pythonanywhere.com

You can log in with the guest user to get a feel for the site:

username: guest

password: thepsswd

To borrow an item I recommend using the manuel mode if you don't randomly have a scanner lying around at home.

An example student ID is: 90001234


Items which you can borrow are: UNO, Schachbrett, Kartendeck 1 (the items are written in German)

To borrow an item, just type in the ID and than write down the item.
To return an item, just write down the item in the field for the student ID.

To add or delete items I made use of the Django admin site. The admin site is also used to manage student ID's.
I still need to write code to make the migration of more, multiple student ID's easier.

The code was written in Python using Django as a framework and 'pythonanywhere' as the hosting platform/server.

Feel free to look through the code and to offer any suggestions or issues.

