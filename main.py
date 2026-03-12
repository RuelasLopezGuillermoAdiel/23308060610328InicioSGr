import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.bgcolor = ft.Colors.BLUE_100
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    CorreoUS = ft.TextField(
        label = "Escribe Tu Correo Gmail",
        hint_text = "Escribe Tu Correo Gmail"
    )
    
    ContraseñaUS = ft.TextField(
        label = "Escribe Tu Contraseña",
        hint_text = "Escribe Tu Contraseña"
    )
    IniciarS = ft.Button(content="iniciar Sesion",
    width=200,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.GREEN_200,
    
    )
    Registrarse = ft.Button(content="Registrate!",
    width=150,
        color=ft.Colors.BLACK,
        bgcolor=ft.Colors.BLUE_600,
    )
    page.add( 
        ft.Icon(ft.Icons.LOGIN, color=ft.Colors.PRIMARY, size=150),
        ft.Text(value="Inicio De Sesion",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        ),
        CorreoUS, ContraseñaUS, IniciarS, Registrarse)
ft.app(target=main)