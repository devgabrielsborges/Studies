import flet as ft


def app(page: ft.Page):
    def teclas(e: ft.KeyboardEvent):
        print(e.key)
        page.add(
            ft.Text(f"Tecla pressionada: {e.key}")
        )
    
    page.on_keyboard_event = teclas
    page.add(
        ft.Text("Digite qualquer tecla")
    )


ft.app(target=app)
