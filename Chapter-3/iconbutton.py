#import the library
import flet as ft

#defining the main function
def main(page: ft.Page):
    page.title = "Icon Button"
    page.theme_mode = "light"
    page.vertical_alignment="center"
    txt_number = ft.TextField(value=0,text_align="center", width=100)


    def minus_click(e):
        txt_number.value = int(txt_number.value) -1
        page.update()


    def plus_click(e):
        txt_number.value = int(txt_number.value) +1
        page.update()
    page.add(
      ft.Row(
          controls=[
              ft.IconButton(ft.icons.REMOVE_CIRCLE_ROUNDED,on_click= minus_click),
              txt_number,
              ft.IconButton(ft.icons.ADD_CIRCLE_ROUNDED,on_click= plus_click)
          ],
          alignment="center",

      )  
    )

ft.app(target=main)    