import flet as ft
import speedtest
from time import sleep


def main(page: ft.Page):
    page.title = "Internet Speed Test App"
    page.theme_mode = "light"
    page.padding = 5
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_bgcolor = "#19BDFF"
    page.auto_scroll = True
    page.fonts = {
        "Daggersquare" : "fonts/DAGGERSQUARE.otf",
        "Poppins" : "fonts/Poppins-Black.ttf"
    }


    #initializing speed test variable
    st = speedtest.Speedtest()



    #page Components
    # Title
    app_title = ft.Row(controls=[
        ft.Text(value="Internet", color="#19BDFF", size= 30, font_family= "Daggersquare" ),
        ft.Text(value="Tester", color="#1C1C1C", size= 30, font_family= "Daggersquare")
    ], alignment= "center")
    


    #defining container lines
    line_01 = ft.Text(value="> click button to start!", font_family= "Poppins", color = "#FFFFFF", size= 15)
    line_02 = ft.Text(value="", font_family= "Poppins", color = "#1cab55", size= 15)
    line_03 = ft.Text(value="", font_family= "Poppins", color = "#1cab55", size= 15)
    progessbar_01 = ft.ProgressBar(width= 500, color="#19BDFF", bgcolor="#FFFFFF", opacity=0)
    line_04 = ft.Text(value="", font_family= "Poppins", color = "#19BDFF", size= 25)
    line_05 = ft.Text(value="", font_family= "Poppins", color = "#1cab55", size= 15)
    line_06 = ft.Text(value="", font_family= "Poppins", color = "#1cab55", size= 15)
    progessbar_02 = ft.ProgressBar(width= 500, color="#19BDFF", bgcolor="#FFFFFF", opacity=0)
    line_07 = ft.Text(value="", font_family= "Poppins", color = "#19BDFF", size= 25)
    line_08 = ft.Text(value="", font_family= "Poppins", color = "#FFFFFF",size= 30)

    all_text = ft.Column(controls=[
        line_01,line_02,line_03,progessbar_01,line_04,
        line_05,line_06,progessbar_02,line_07,line_08
    ],alignment = "center")



    # Container
    speed_container = ft.Container(
        content= all_text,
        width= 200,
        height= 100,
        bgcolor= "#1C1C1C",
        border_radius= 30,
        padding= 40,
        animate = ft.animation.Animation(1000,"bounceout"),
        alignment=ft.alignment.center


    )


    def animate_speed_container(e):
        speed_container.update()
        line_01.value = "Calculating Internet speed,please wait!"
        speed_container.width = 1000
        speed_container.height = 600
        speed_container.update()
        sleep(1)

        ideal_server = st.get_best_server()  #this will findout best/nearest server,connect to that server and calculate speed by uploading and downloading data
        city = ideal_server["name"] #ideal_server will give us dictionary
        country = ideal_server["country"]
        country_code = ideal_server["cc"]
        line_02.value = f">>Searching the best possible server in {city}, {country} ({country_code})"
        speed_container.update()
        sleep(2)

        line_03.value = ">>Great! Connection successfull, status OK, fetching DOWNLOAD speed"
        progessbar_01.opacity = 1
        speed_container.update()

        download_speed = st.download()/1024/1024 #calculating downloadspeed,it will give in bits per sec than we need to convert it to Mbps
        progessbar_01.value = 1
        line_04.value = f">>DOWNLOAD speed is {str(round(download_speed,2))} Mbps"
        speed_container.update()

        line_05.value = ">>Calculating UPLOAD speed, please wait...."
        speed_container.update()
        sleep(1)

        line_06.value = ">>Almost there! Please hold on"
        progessbar_02.opacity = 1
        speed_container.update()

        upload_speed = st.upload()/1024/1024
        progessbar_02.value = 1
        line_07.value = f">>UPLOAD speed is {str(round(upload_speed,2))} Mbps"
        speed_container.update()
        sleep(1)

        line_08.value = "Task Completed Successfully!\n\n App Developed by Bidut Sharkar Shemanto"
        speed_container.update()




    # Button
    go_icon_button = ft.IconButton(icon= ft.icons.RESTART_ALT_ROUNDED, icon_color = "#19BDFF", icon_size= 40, on_click=animate_speed_container)
    
    




    page.add(
        app_title,
        speed_container,
        go_icon_button
    
    )


ft.app(target=main, assets_dir= "assets")    