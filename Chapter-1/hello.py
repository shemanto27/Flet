import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    page.title = "Hello World"

    t = ft.Text(value= "My First App", color="Red")
    page.controls.append(t)
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)