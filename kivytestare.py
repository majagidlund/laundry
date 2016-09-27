import kivy
kivy.require('1.4.0')
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

from datetime import date, timedelta

class DatePicker(BoxLayout):

    def __init__(self, **kwargs):
        super(DatePicker, self).__init__(**kwargs)
        self.date = date.today()
        self.orientation = "vertical"

        self.header = BoxLayout(orientation = 'horizontal',
                                size_hint = (1, 0.2))
        self.body = GridLayout(cols = 7)
        self.add_widget(self.header)
        self.add_widget(self.body)

        self.populate_body()
        self.populate_header()

    def populate_header(self):
        self.header.clear_widgets()
        self.previous_month = Button(text = "<")
        self.next_month = Button(text = ">")
        self.current_month = Label(text = repr(self.date),
                                   size_hint = (2, 1))

        self.header.add_widget(self.previous_month)
        self.header.add_widget(self.current_month)
        self.header.add_widget(self.next_month)

    def populate_body(self):
        self.body.clear_widgets()
        date_cursor = date(self.date.year, self.date.month, 1)
        while date_cursor.month == self.date.month:
            self.date_label = Label(text = str(date_cursor.day))
            self.body.add_widget(self.date_label)
            date_cursor += timedelta(days = 1)



class MyApp(App):

    def build(self):
        return DatePicker()

if __name__ == '__main__':
    MyApp().run()