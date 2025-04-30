import flet as ft
from typing import List

scroll_row_ref = ft.Ref[ft.Row]()

def move_backward(e):
    scroll_row_ref.current.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)

def move_forward(e):
    scroll_row_ref.current.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)

def carousel(controls: List[ft.Control], height: int = 250):
    return ft.Column(
        controls=[
            ft.Row(
                ref=scroll_row_ref,
                height=height,
                scroll=ft.ScrollMode.HIDDEN,
                controls=controls,
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.END,
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.KEYBOARD_ARROW_LEFT,
                        on_click=move_backward,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.KEYBOARD_ARROW_RIGHT,
                        on_click=move_forward,
                    ),
                ]
            )
        ]
    )