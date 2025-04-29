import flet as ft
from partials.sidebar import sidebar
from partials.content import main_content

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.bgcolor = ft.Colors.BLACK
        self.main()

    def main(self):
        self.sidebar = sidebar()

        self.content = main_content()

        layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Column(col={"sm": 12, "md": 4, "lg": 3}, controls=[self.sidebar]),
                ft.Column(col={"sm": 12, "md": 8, "lg": 9}, controls=[self.content]),
            ],
            expand=True,
        )

        self.page.add(layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
