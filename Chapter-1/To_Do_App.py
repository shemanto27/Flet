import flet as ft

def main(page: ft.Page):
    page.title = "To-Do App by Shemanto"
    page.theme_mode = "light"
    user_input = ft.TextField(label="Task",hint_text="Write Your Task in here....", width=350)
    
    def button_click(e):
        page.add(ft.Checkbox(label=user_input.value))
    
    page.add(
        ft.Row(
            [
                user_input,
                ft.ElevatedButton(text="Add task", on_click=button_click)
            ]
        )


    )




ft.app(target=main)