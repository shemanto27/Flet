import flet as ft
import numpy as np
import text

def main(page: ft.Page):
    page.title = "Learn NumPy with Game!"
    page.theme_mode = "light"
    page.fonts = {
        "RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"
    }
    page.horizontal_alignment = "CENTER"
    
    
    first_number = ft.TextField(label="1st", width= 100)
    second_number = ft.TextField(label="2nd", width= 100 )
    third_number = ft.TextField(label="3rd", width= 100)
    fourth_number = ft.TextField(label="4th", width= 100)
    
    
    user_list = ft.Column()

    def list_function(e):
        a = int(first_number.value)
        b = int(second_number.value)
        c = int(third_number.value)
        d = int(fourth_number.value)
        list = [a,b,c,d]
        list_of_list = [[a,b],[c,d]]
        Numpy_array_1D = np.array(list)
        Numpy_array_2D = np.array(list_of_list)
        user_list.controls.append(ft.Text(f"This is your List: {list}"))
        user_list.controls.append(ft.Text(f"This is your List of Lists: {list}"))
        user_list.controls.append(ft.Text(f"This is your 1D Numpy Array/Vector: {Numpy_array_1D}"))
        user_list.controls.append(ft.Text(f"This is your 2D Numpy Array/Matrix:"))
        user_list.controls.append(ft.Text(Numpy_array_2D))
        page.update()
        


    submit_button = ft.ElevatedButton(text = "Submit", on_click = list_function)
    row = ft.Row(controls=[first_number,second_number,third_number,fourth_number,submit_button],alignment="CENTER")
    

    page.add(
        text.text_1,
        row,
        user_list,
        text.text_2
        
        
    )


ft.app(target=main)