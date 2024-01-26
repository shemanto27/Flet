import flet as ft 
import time

class TypeWriterControl(ft.UserControl):
    def __init__(self,text_to_print):
        super().__init__()
        self.text_to_print = text_to_print
        
    def effect(self, e):
        for i in range(len(self.text_to_print)):
            self.my_type_writer_text.value += self.text_to_print[]


    def build(self):
        self.my_type_writer_text = ft.text("My Tupe Writer Text...\n")
        return ft.Column([self.my_type_writer_text, ft.ElevatedButton("Start",on_click= self.effect)])        