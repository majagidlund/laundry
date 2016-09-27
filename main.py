#importt...

#seb checkar in. testing testing

import calendar

SLOT_01 = "8"
SLOT_02 = "12"
SLOT_03 = "15"
slots = [SLOT_01, SLOT_02, SLOT_03]
booked_slots = [None, None, None]
name_slots = []
date = str



class_name = 'name'
class_appointment_info = 'appointment_info'

class User(object):

    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.user_name = f_name + " " + l_name
        self.booked_slot = None

    def book(self):
        date = str(input("Nar vill du boka? "))

        print(date)

        if date in slots:
            x = slots.index(date)
            if(booked_slots[x]== None):
                booked_slots[x] = date
                print ("Du har bokat " + date)
                return booked_slots
            else:
                print ("Denna tid ar redan bokad")
        else:
            print ("Denna slots finns ej")

        for i in booked_slots:
            if booked_slots[i] != None:
                print (slots[i])

    def cancel(self):
        c = str(input("Vilken tid vill du avboka?"))
        if c in booked_slots:
            booked_slots[booked_slots.index(c)] = None
            print ("Du har tagit bort " + c + " ur listan")

        else:
            print ("Du hade ej bokat denna tid")

        print(booked_slots)

        for i in xrange(0,len(booked_slots)):
            if booked_slots[i-1] == None:
                print("Tiden " + slots[i] + " is available")
            else:
                print("Tiden is available")


Maja = User('Maja', 'Gidlund')
Maja.book()
Maja.cancel()

