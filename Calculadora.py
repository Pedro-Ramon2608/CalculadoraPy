import flet as ft

botoes = [
    {"operador": "AC", "fonte": "black", "fundo": "grey"},
    {"operador": "+-", "fonte": "black", "fundo": "grey"},
    {"operador": "%", "fonte": "black", "fundo": "grey"},
    {"operador": "/", "fonte": "white", "fundo": "purple"},
    {"operador": "7", "fonte": "white", "fundo": "blue"},
    {"operador": "8", "fonte": "white", "fundo": "blue"},
    {"operador": "9", "fonte": "white", "fundo": "blue"},
    {"operador": "*", "fonte": "white", "fundo": "purple"},
    {"operador": "4", "fonte": "white", "fundo": "blue"},
    {"operador": "5", "fonte": "white", "fundo": "blue"},
    {"operador": "6", "fonte": "white", "fundo": "blue"},
    {"operador": "-", "fonte": "white", "fundo": "purple"},
    {"operador": "1", "fonte": "white", "fundo": "blue"},
    {"operador": "2", "fonte": "white", "fundo": "blue"},
    {"operador": "3", "fonte": "white", "fundo": "blue"},
    {"operador": "+", "fonte": "white", "fundo": "purple"},
    {"operador": "0", "fonte": "white", "fundo": "blue"},
    {"operador": ".", "fonte": "white", "fundo": "blue"},
    {"operador": "=", "fonte": "white", "fundo": "purple"},
]

def main(page: ft.Page):
    page.bgcolor = "black"
    page.window.resizable = False
    page.window.width = 270
    page.window.height = 390
    page.title = "Calculadora"
    page.window.always_on_top = True

    result = ft.Text(value = "0", color = "white", size = 20)

    def calcule():
        pass

    def select(e):
        value_at = result.value if result.value != "0" else ""
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == "AC":
            value = "0"
        else:
            if value_at and value_at[-1] in ("/", "*", "-", "+", "."):
                value_at = value_at[-1]
            
            value = value_at + value

            if value[-1] in ("=", "%", "+-"):
                value = calcule
        
        result.value = value
        result.update()

    display = ft.Row(
        width=250,
        controls=[result],
        alignment= "end"
    )

    btns = [ft.Container(
            content=ft.Text(value=btn["operador"], color=btn["fonte"]),
            width=50,
            height=50,
            bgcolor=btn["fundo"],
            border_radius=100,
            alignment=ft.Alignment.CENTER,
            on_click=select
        ) for btn in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=btns,
        alignment="end"
    )

    page.add(display, keyboard)



ft.app(target = main)
