import flet as ft
import asyncio

GREETINGS = [
    "--- Olá ----", "--- Ey ---", "--- Hello ---",
    "--- Ciao ---", "--- Bonjour ---", "--- Hoi ---",
    "--- 嘿 ---", "--- おい ---", "--- 여기요 ---",
    "--- يا ---", "--- Привет ---", "--- Hey ---"
    ]

def welcome_screen(page: ft.Page, on_finish):
    text = ft.Text(
        value="",
        size=50,
        color=ft.Colors.WHITE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    container = ft.Container(
        bgcolor=ft.Colors.BLACK,
        content=ft.Row(
            [ft.Column(
                [text],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            )],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        ),
        expand=True,
        scale=ft.transform.Scale(1.0),
        animate_opacity=300,
        animate_scale=400,
    )

    page.clean()
    page.add(container)

    async def animate_greetings():
        for i, greeting in enumerate(GREETINGS):
            text.value = greeting
            page.update()
            
            delay = max(0.6 - (i * 0.1), 0.2)
            await asyncio.sleep(delay)

        await asyncio.sleep(0.4)
        container.scale = ft.transform.Scale(0.85)
        container.opacity = 0
        page.update()
        await asyncio.sleep(0.5)

        page.controls.clear()
        page.update()

        on_finish()

    page.run_task(animate_greetings)
