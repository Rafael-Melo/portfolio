import flet as ft
from partials.sidebar import sidebar
from partials.content import main_content

# xs      <576px
# sm      ≥576px
# md      ≥768px
# lg      ≥992px
# xl      ≥1200px
# xxl     ≥1400px

class AppTheme:
    dark = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.DEEP_PURPLE,
            secondary=ft.Colors.INDIGO,
            tertiary=ft.Colors.WHITE,
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
    light = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.INDIGO,
            secondary=ft.Colors.BLUE,
            tertiary='#373535',
            on_inverse_surface=ft.Colors.GREY_200,
            primary_container=ft.Colors.GREY_300
        ),
        text_theme=ft.TextTheme(
            body_large=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLACK87,
                size=14
            ),
            body_medium=ft.TextStyle(
                weight=ft.FontWeight.NORMAL,
                color=ft.Colors.BLACK54,
                size=14
            ),
            headline_large=ft.TextStyle(
                weight=ft.FontWeight.W_900,
                color=ft.Colors.WHITE,
                size=50
            ),
            label_large=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.Colors.BLACK,
                size=16
            ),
            headline_medium=ft.TextStyle(
                weight=ft.FontWeight.W_700,
                color=ft.Colors.BLACK,
                size=30
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
        saved_theme = self.page.client_storage.get("dark_mode")
        self.dark_mode = saved_theme != "False"  # padrão é True
        self.theme_toggle_btn = ft.FloatingActionButton(
            icon=ft.icons.LIGHT_MODE if self.dark_mode else ft.icons.DARK_MODE,
            on_click=self.toggle_theme,
            tooltip="Alternar tema",
            bgcolor=ft.Colors.PRIMARY,
            mini=True,
        )
        self.main()
        self.apply_theme()
        self.page.on_resized = self.show_app_bar
        self.show_app_bar()
    
    def toggle_sidebar(self, e):
        self.sidebar.col['xs'] = 12 if self.sidebar.col['xs'] == 0 else 0
        self.content.col['xs'] = 0 if self.content.col['xs'] == 12 else 12
        self.page.update()
    
    def toggle_theme(self, e):
        self.dark_mode = not self.dark_mode
        self.page.client_storage.set("dark_mode", str(self.dark_mode))
        self.apply_theme()

    def apply_theme(self):
        self.page.theme = AppTheme.dark if self.dark_mode else AppTheme.light
        self.page.bgcolor = ft.Colors.BLACK if self.dark_mode else ft.Colors.WHITE
        self.content.content = main_content(self.dark_mode)
        self.theme_toggle_btn.icon = ft.icons.LIGHT_MODE if self.dark_mode else ft.icons.DARK_MODE
        self.show_app_bar()
        self.page.update()

    def show_app_bar(self, e = None):
        if self.page.width < 768:
            self.page.appbar = ft.AppBar(
                leading=ft.IconButton(
                    icon=ft.Icons.MENU,
                    icon_color=ft.Colors.WHITE if self.dark_mode else ft.Colors.BLACK,
                    on_click=self.toggle_sidebar,
                ),
                bgcolor=ft.Colors.PRIMARY_CONTAINER,
            )
            self.layout.spacing = 0,
            self.page.bgcolor = ft.Colors.PRIMARY_CONTAINER
        else:
            self.page.appbar = None
            self.layout.spacing = 10
        
        self.page.update()

    def main(self):
        self.sidebar = ft.Container(
            # col={"sm": 12, "md": 4, "lg": 3},
            col={"xs": 0, "md": 5, "lg": 4, "xxl": 3},
            content=sidebar()
        )

        self.content = ft.Container(
            # col={"sm": 12, "md": 8, "lg": 9},
            col={"xs": 12, "md": 7, "lg": 8, "xxl": 9},
            content=main_content(self.dark_mode)
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
        self.page.floating_action_button = self.theme_toggle_btn

if __name__ == '__main__':
    ft.app(target=App, assets_dir='assets')
