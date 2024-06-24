import flet as ft

# app deve estar contido na função main
def main(page: ft.Page):

    def mostrar_senha(event):
        if entrada_idade.value and entrada_nome.value:
             nome = str(entrada_nome.value)
             idade = int(entrada_idade.value)
             senha = f"{nome}{idade}2024"
             
             page.clean()   # função para limpar a página
             resultado = ft.Text(value=f"Olá {nome},\nSua senha padrão é:\n {senha}", size=40)
             page.controls.append(resultado)
             page.update()   # função para atualizar a página
        else:   # caso em que os campos não forem preenchido
            entrada_nome.error_text = "Por favor preencha o campo"
            entrada_idade.error_text = "Por favor preencha o campo"
            page.update()


    entrada_nome = ft.TextField(label="Digite o seu nome")    # input para dados, nesse caso --> nome
    entrada_idade = ft.TextField(label="Digite sua idade")   # input para idade
    
    # adicionando elementos à página base
    page.add(
        entrada_nome,
        entrada_idade,
        ft.ElevatedButton("Clique aqui", on_click=mostrar_senha)   # botao que executa a funcão mostrar_senha
    )

ft.app(target=main)
    