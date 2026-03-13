import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.bgcolor = ft.Colors.BLUE_100
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    USUARIO_VALIDO = "admin"
    CONTRASENA_VALIDA ="1234"
    
    def login_click(e):
        usuario = txt_usuario.value
        contrasena = txt_contrasena.value
        
        if usuario == USUARIO_VALIDO and contrasena == CONTRASENA_VALIDA:
            page.show_dialog(ft.SnackBar(ft.Text("!Inicio de secion exitoso!")))
        else: 
            page.show_dialog(ft.SnackBar(ft.Text("Usuario o Contraseña Incorrectos.")))
        
    def forgot_click(e):
        page.show_dialog(ft.SnackBar(ft.Text("se han enviado instrucciones a tu correo electronico")))
        
    txt_usuario=ft.TextField(label="Correo", autofocus=True)
    
    txt_contrasena=ft.TextField(label="Contraseña", password=True)
    
    IniciarS = ft.Button(content="iniciar Sesion",
    width=200,
        on_click=login_click,
        bgcolor=ft.Colors.GREEN_200,
    
    )
    Registrarse = ft.TextButton(
        "Olvidaste tu contraseña?",
        on_click = forgot_click,
    )
    page.add( 
        ft.Icon(ft.Icons.LOGIN, color=ft.Colors.PRIMARY, size=150),
        ft.Text(value="Inicio De Sesion",
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
        ),
        txt_usuario, txt_contrasena, IniciarS, Registrarse)
    
    def mostrar_pantalla_principal():
        page.clean()
        
        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explorar"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ],
            on_change=label e: print(f"Seleccionado: {e.control.selected_index}")
        )
    page.add(
        ft.AppBar(
            title
        )
    )
    
ft.app(target=main)