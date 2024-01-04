'''
User Controls: Controls that are made by user
by combining default controls

1) why we need user Controls?
user controls allows building isolated re-usable components
by combining the existing Flet controls

2)UserControl must implement build() that is called
to build the control's UI

3) build() function should return a single control instance or
a list of controls

'''

import flet as ft

class GreetingsControl(ft.UserControl):  # GreetingsControl is an user control and ft.UserControl as made by flet team.In here GreetingsControl is inherited from UserControl
    def build(self):
        text = ft.Text("Hello World")
        button = ft.ElevatedButton("hi")
        row = ft.Row(controls=[text,button])
        return row

def main(page: ft.Page):
    
    page.add(GreetingsControl(),
             GreetingsControl())




ft.app(target = main)    