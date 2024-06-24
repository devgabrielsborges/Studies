import flet as ft

def main(page: ft.Page):
    ola = ft.Text(value="Hello World", size=30)
    page.controls.append(ola)
    page.update()

ft.app(target=main)