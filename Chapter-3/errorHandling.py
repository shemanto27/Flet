import flet as ft

def main(page: ft.Page):

    #Page Essentials
    page.title = "Error Handing and Page Cleaning"
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    user_name = ft.TextField(label="Enter Name", width=300)
    print_name = ft.Column()


    #Call_hello Function
    def call_hello(e):
        if not user_name.value: #if user_name is Empty/has no value
            user_name.error_text = "Please Enter Your Name" #Error Handing Part
            page.update()
        else:
            page.clean()
            print_name.controls.append(ft.Text(f"Hello {user_name.value}"))
            page.add(print_name)
            


    page.add(
    user_name,
    ft.ElevatedButton("Say Hello!", on_click= call_hello)
    )

ft.app(target=main)    


