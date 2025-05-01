import flet as ft
from partials.sidebar import sidebar
from partials.content import main_content

class AppTheme:
    theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.DEEP_PURPLE,
            on_inverse_surface='#2d2d3a',
            primary_container='#20202a'
        ),
        text_theme=ft.TextTheme(
            body_large=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
                size=14,
            ),
            body_medium=ft.TextStyle(
                weight=ft.FontWeight.NORMAL,
                color=ft.Colors.GREY,
                size=14,
            ),
            headline_large=ft.TextStyle(
                weight=ft.FontWeight.W_900,
                color=ft.Colors.WHITE,
                size=50,
            ),
            label_large=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.Colors.WHITE,
                size=16,
            ),
            headline_medium=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.Colors.WHITE,
                size=30,
            ),
        ),
        scrollbar_theme=ft.ScrollbarTheme(
            track_visibility=False,
            thumb_visibility=False,
            track_color={
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
            },
            thumb_color={
                ft.ControlState.DEFAULT: ft.Colors.TRANSPARENT,
                ft.ControlState.HOVERED: ft.Colors.TRANSPARENT,
            }
        )
    )

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme = AppTheme.theme
        self.page.on_resized = self.show_app_bar
        self.page.bgcolor = ft.Colors.BLACK
        self.main()
        self.show_app_bar()
    
    def toggle_sidebar(self, e):
        self.sidebar.col['xs'] = 12 if self.sidebar.col['xs'] == 0 else 0
        self.content.col['xs'] = 0 if self.content.col['xs'] == 12 else 12
        self.page.update()

    def show_app_bar(self, e = None):
        if self.page.width < 768:
            self.page.appbar = ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_color=ft.Colors.WHITE,
                    on_click=self.toggle_sidebar,
                ),
                bgcolor=ft.Colors.PRIMARY_CONTAINER,
            )
            self.layout.spacing = 0,
            self.page.bgcolor = ft.Colors.PRIMARY_CONTAINER
        else:
            self.page.appbar = None
            self.layout.spacing = 10
            self.page.bgcolor = ft.Colors.BLACK
        
        self.page.update()

    def main(self):
        self.sidebar = ft.Container(
            col={'xs': 12, 'md': 5, 'xxl': 3},
            content=sidebar()
        )

        self.content = ft.Container(
            col={'xs': 0, 'md': 7, 'xxl': 9},
            content=main_content()
        )

        self.layout = ft.ResponsiveRow(
            columns=12,
            controls=[
                self.sidebar,
                self.content,
            ],
            expand=True,
        )

        self.page.add(self.layout)

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
