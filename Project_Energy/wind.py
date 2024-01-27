import flet as ft 
import math

def main(page: ft.Page):
    page.theme_mode = "light"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    png = "H:\Flet\Project_Energy\Wind turbine, work in progress.png"
    gif = "H:\Flet\Project_Energy\Wind turbine, work in progress.gif"
    
    img = ft.Image(
        src= png,
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    
    def start(e):
        img.src = gif
        page.update()

    def stop(e):
        img.src = png
        page.update()



    start_button = ft.ElevatedButton(text="start",on_click= start)
    stop_button = ft.ElevatedButton(text="stop",on_click= stop)

    c1 = ft.Container(
        content= img,
        border_radius=10,
        width=200,
        height=200,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.colors.BLUE_GREY_300,
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,)
        )
    
    r1 = ft.Row(controls=[c1],)

    L = 10
    V = 10
    roh = 1.2
    A = math.pi*L**2
    P = .5*roh*A*V**3
    print(P)
    
    
    page.add(
        r1,
        start_button,
        stop_button
    )

ft.app(target=main)