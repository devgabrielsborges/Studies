import flet as ft

def app(page: ft.Page):
    # list view agrupa os elemetos em listas como containers de vários elementos
    lista = ft.ListView(spacing=2, expand=True)   # spacing é semelhante à padding no CSS

    for i in range(20):
        lista.controls.append(ft.Text(f"ITEM No {i}"))
        lista.controls.append(ft.Text(f"balacobaco"))
    page.add(lista)

ft.app(target=app)