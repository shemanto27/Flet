import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Learn NumPy with Game!"
    page.theme_mode = "light"

    title = ft.Text("NumPY Game by Shemanto Sharkar")
    
    first_number = ft.TextField(label="1st", width= 100)
    second_number = ft.TextField(label="2nd", width= 100 )
    third_number = ft.TextField(label="3rd", width= 100)
    
    row = ft.Row(controls=[first_number,second_number,third_number])
    user_list = ft.Row()

    def list_function(e):
        a = int(first_number.value)
        b = int(second_number.value)
        c = int(third_number.value)
        list = [a,b,c]
        user_list.controls.append(ft.Text(f"This is your List: {list}"))
        page.update()
        

    def array_converter(e):
        a = int(first_number.value)
        b = int(second_number.value)
        c = int(third_number.value)
        list = [a,b,c]
        Numpy_array = np.array(list)
        user_list.controls.append(ft.Text(f"This is your Numpy Array: {Numpy_array}"))
        page.update()


    submit_button = ft.ElevatedButton(text = "Submit", on_click = list_function)
    array_converter_button = ft.ElevatedButton(text="Convert to Numpy Array", on_click= array_converter)
    

    page.add(
        title,
        row,
        submit_button,
        user_list,
        array_converter_button
        
    )


ft.app(target=main)