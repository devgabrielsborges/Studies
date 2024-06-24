import flet as ft

def app(page: ft.Page):
    titulo = ft.Container(
        ft.Text("Conversor de moedas", color=ft.colors.AMBER_100, size=50),
        alignment=ft.alignment.center
    )
    lista1 = ft.ListView(
        spacing=2, expand=True
    )
    lista1.controls.append(
        ft.Container(
            ft.TextField(label="Valor inicial",color=ft.colors.BLACK87, bgcolor=ft.colors.BLUE_100),
            width=100,
            height=80,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE_100,
            border=ft.border.all(2, ft.colors.BLUE_500),
            border_radius=ft.border_radius.all(8)
        )
    )
    lista1.controls.append(
        ft.Container(
            ft.TextField(label="Valor final",color=ft.colors.WHITE70, bgcolor=ft.colors.BLUE_100, border_color=ft.colors.BLUE_100),
            width=100,
            height=80,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE_100,
            border=ft.border.all(2, ft.colors.BLUE_500),
            border_radius=ft.border_radius.all(8)
        )
    )

    page.add(
        titulo, lista1
    )


ft.app(target=app)