import flet as ft

def main(page: ft.Page):

    page.add(
        ft.Row(
            controls=[
                ft.Text("Talha"),
                ft.Text("Akash"),
                ft.Text("Pranto"),
                ft.Text("Shemanto")
            ]
        ),

        ft.Column(
            controls=[
                ft.Text("Talha"),
                ft.Text("Akash"),
                ft.Text("Pranto"),
                ft.Text("Shemanto")
            ]
        )

    )



ft.app(target=main)