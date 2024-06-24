# lista de itens com gridview em linhas row

import flet as ft
import os
from time import sleep

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"   # configuração para tamanho máximo das mensagens


def main(page: ft.Page):
    linha = ft.Row(wrap=True, scroll="always", expand=True)   # wrap --> quebrar linha caso nao caiba na tela; scroll e expand permitem descer a tela
    page.add(linha)

    for i in range(11):
        linha.controls.append(
            ft.Container(    # containers são como divs em HTML
                # propriedades do container
                ft.Text(f"Esse é o item No {i}"),
                width=100,
                height=100,
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(2, ft.colors.AMBER_500),
                border_radius=ft.border_radius.all(8)
            )
        )
        sleep(0.1)
        page.update()
    page.add(ft.TextField(label="Digite oi"))

ft.app(target=main, view=ft.WEB_BROWSER)   # aplicação web

