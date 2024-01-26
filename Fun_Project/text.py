import flet as ft

t1= """Hi Guys,
Welcome to the NumPy Essentials lecture part 1.As a fundamental package for scientific computing, NumPy provides the foundations of mathematical, scientific, engineering and data science programming within the Python Echo-system. NumPy’s main object is the homogeneous multidimensional array.
**NumPY stands for? Ans: Numerical Python  
Numpy developed by? Ans: Travis Oliphant**"""

t2 = """# Numpy Arrays

NumPy arrays will be the main concept that we will be using in this course. These arrays essentially come in two flavors: <br>
* **Vectors:** Vectors are strictly 1-dimensional array
*  **Matrices:** Matrices are 2-dimensional (matrix can still have only one row or one column)."""

text_1 = ft.Text(t1,size=15,font_family="RobotoSlab",text_align = "CENTER")
text_2 = ft.Text(t2,size=15,font_family="RobotoSlab",text_align = "CENTER")