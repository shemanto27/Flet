import flet as ft 

def main(page: ft.Page):
    page.title = "Typewriter Effect"
    page.window_width = 400
    page.window_height = 500
    page.bgcolor = "#FA897B"
    page.theme_mode = "light"
    page.window_center()
    page.scroll = 'always'
    page.update()

    text = ft.Text("My Name is Shemanto Sharkar")


    page.add(
        text

    )


ft.app(target=main)    