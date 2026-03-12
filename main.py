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
    
    def login_click(e):
        contraseña = txt_contraseñaUS.value
        
        if usuario == USUARIO_VALIDO and contraseña == CONTRASEÑA_VALIDA:
            page.show_dialog(ft.SnackBar(ft.Text("!Inicio de secion exitoso!")))
            
        else: page.show_dialog(ft.SnackBar(ft.Text("Usuario o Contraseña Incorrectos.")))
        
    def forgot_clicl(e):
        page.show_dialog(ft.Snackbar(ft.Text("se han enviado instrucciones a tu correo electronico")))
        
    txt_usuario=ft.TextField(lavel="Usuario", autofocus=True)
    txt_contraseña=ft.TextField(label="Contraseña", password=Tr)
    
    IniciarS = ft.Button(content="iniciar Sesion",
    width=200,
        color=ft.Colors.BLACK,
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
        CorreoUS, ContraseñaUS, IniciarS, Registrarse)
ft.app(target=main)