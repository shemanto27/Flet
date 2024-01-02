import flet as ft

def main(page: ft.Page):
    page.title = "Guess Me Game"
    page.theme_mode = "light"
    page.padding = 20
    page.fonts = {
        "DAGGERSQUARE" : "fonts/DAGGERSQUARE.otf",
        "Poppins-SemiBold" : "fonts/Poppins-SemiBold.ttf"
    }
    
    
    heading_text = ft.Text(value = "GUESS ME!", font_family= "DAGGERSQUARE", size= 50, color="#FFFFFF")

    #players
    player_1 = ft.TextField(label= "Player 1", hint_text= "Give number between 1-10", password= True, width= 500)
    player_2 = ft.TextField(label= "Player 2", hint_text= "Guess what Player 1 is giving (Number between 1-10)", width= 500)
    
    result = ft.Text("Result will be showed here!", color= "#d92121", size= 30, font_family= "DAGGERSQUARE")

    #check_answer_function
    def check_answer(e):
        if not player_1.value: #error handling
            player_1.error_text= "Player 1!! You haven't give your number"

        elif not player_2.value:
            player_2.error_text= "Player 2!! you are being lazy,give your number hurry"

        elif int(player_1.value) > 11:  #finding player 1 is cheating or not
            result.value = "Player 1 is Cheating!"
        elif int(player_1.value) == int(player_2.value):
            result.value = "Player 2 is Correct!!"
            result.color = "#008000" 
        else:
            result.value = "Player is Wrong!!"
            result.color = "#d92121"

        page.update()

    
    page.add(
        ft.Card(
            ft.Container(
            content= ft.Row(controls=[heading_text],alignment= "center"),
            padding = 20
        ),
        color = "#87CEEB"
        
        ),

        

        ft.Column(
            controls = [
                ft.Row(controls = [player_1], alignment= "center"),
                ft.Row(controls = [player_2],alignment= "center"),
                ft.Row(controls = [ft.ElevatedButton("Check if Player 2 is Right or Wrong!", on_click= check_answer)],alignment= "center"),
                ft.Row(controls=[result],alignment="center")
            ]
        )
    
    
    )

ft.app(target=main, assets_dir= "assets")    




