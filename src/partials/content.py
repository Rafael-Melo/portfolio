import flet as ft
from typing import List, Dict, Union
import math
from components.carousel import carousel

def project_item(title, description, url):
    return ft.Container(
        col={'xs': 12, 'md': 6, 'lg': 4},
        padding=ft.padding.all(30),
        bgcolor=ft.Colors.ON_INVERSE_SURFACE,
        content=ft.Column(
            controls=[
                ft.Text(value=title, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ft.Text(value=description),
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(value='VER PROJETO', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.PRIMARY),
                            ft.Icon(name=ft.Icons.ARROW_FORWARD_IOS, size=14, color=ft.Colors.PRIMARY)
                        ],
                        tight=True,
                    ),
                    url=url
                )
            ]
        )
    )

def price_item(price: int, url: str, items_included: List[Dict[str, bool]]):
    return ft.Container(
        col={'xs': 12, 'md': 6, 'lg': 4},
        bgcolor=ft.Colors.ON_INVERSE_SURFACE,
        padding=ft.padding.symmetric(vertical=20, horizontal=50),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
            controls=[
                ft.Text(value='Pagamento por hora', theme_style=ft.TextThemeStyle.LABEL_LARGE),
                ft.Text(
                    spans=[
                        ft.TextSpan(text='R$', style=ft.TextStyle(color=ft.Colors.WHITE)),
                        ft.TextSpan(text=f' {price} ', style=ft.TextStyle(color=ft.Colors.PRIMARY, weight=ft.FontWeight.BOLD, size=50)),
                        ft.TextSpan(text='/hora', style=ft.TextStyle(color=ft.Colors.WHITE)),
                    ]
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                               ft.Icon(
                                    name=ft.Icons.CHECK if item['is_included'] else ft.Icons.CLOSE,
                                    color=ft.Colors.PRIMARY,
                                ),
                                ft.Text(value=item['title']),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ) for item in items_included 
                    ]
                ),
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Text(value='QUERO ESTE', theme_style=ft.TextThemeStyle.BODY_LARGE, color=ft.Colors.PRIMARY),
                            ft.Icon(name=ft.Icons.ARROW_FORWARD_IOS, size=14, color=ft.Colors.PRIMARY),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    url=url,
                )
            ]
        )
    )

def testimonial_item(user: str, job: str, testimonial: str, image_src: str = 'img/testimonial-default.jpg'):
    return ft.Container(
        bgcolor=ft.Colors.ON_INVERSE_SURFACE,
        padding=ft.padding.all(30),
        margin=ft.margin.only(top=20),
        width=400,
        content=ft.Stack(
            controls=[
                ft.Column(
                    spacing=0,
                    controls=[
                        ft.Text(value=user, theme_style=ft.TextThemeStyle.LABEL_LARGE),
                        ft.Text(value=job, theme_style=ft.TextThemeStyle.LABEL_MEDIUM, italic=True),

                        ft.Container(height=20),
                        ft.Text(
                            value=testimonial,
                            theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                        ),

                        ft.Container(height=20),
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=16),
                                    ft.Icon(name=ft.Icons.STAR, color=ft.Colors.PRIMARY, size=16),
                                ],
                                tight=True,
                            ),
                            bgcolor=ft.Colors.BLACK54,
                            padding=ft.padding.symmetric(vertical=5, horizontal=10),
                            border_radius=ft.border_radius.all(50),
                        )
                    ]
                ),

                ft.Image(
                    src=image_src,
                    border_radius=ft.border_radius.all(100),
                    width=100,
                    top=0,
                    right=0,
                    offset=ft.Offset(x=0, y=-0.5)
                )
            ]
        )
    )

def main_content():
    banner = ft.Container(
        shadow=ft.BoxShadow(
            color=ft.Colors.ON_SURFACE,
            offset=ft.Offset(x=0, y=-60),
            spread_radius=-30,
        ),
        image=ft.DecorationImage(
            src='img/bg.jpg',
            fit=ft.ImageFit.COVER,
            repeat=ft.ImageRepeat.NO_REPEAT,
            opacity=0.5,
        ),
        margin=ft.margin.only(top=30),
        bgcolor=ft.Colors.BLACK,
        content=ft.ResponsiveRow(
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.END,
            controls=[
                ft.Container(
                    col={'md': 12, 'lg':8},
                    padding=ft.padding.all(50),
                    content=ft.Column(
                        controls=[
                            ft.Text(value='Transformando código em soluções reais', theme_style=ft.TextThemeStyle.HEADLINE_LARGE),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(text='<'),
                                    ft.TextSpan(text='code', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                    ft.TextSpan(text='> '),

                                    ft.TextSpan(
                                        text='Apaixonado por tecnologia e resolução de problemas. Com experiência em automações em Python, criação de APIs, desenvolvimento de apps iOS e Android, softwares para macOS, Windows e Linux, além de websites responsivos. Transformo desafios em soluções simples e eficientes.',
                                        style=ft.TextStyle(color=ft.Colors.WHITE),
                                    ),
                                    ft.TextSpan(text=' </'),
                                    ft.TextSpan(text='code', style=ft.TextStyle(color=ft.Colors.PRIMARY)),
                                    ft.TextSpan(text='> '),
                                ],
                                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                            ),
                            ft.ElevatedButton(
                                bgcolor=ft.Colors.PRIMARY,
                                content=ft.Text(value='Explore agora', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                                url='#',
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                            )
                        ],
                        spacing=30,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),
                ft.Container(
                    col={'md': 12, 'lg':4},
                    content=ft.Image(
                        src='img/face-2.png',
                        width=200,
                        scale=ft.Scale(scale=1.8)
                    )
                )
            ]
        )
    )

    experience = ft.Container(
        padding=ft.padding.symmetric(vertical=20),
        content=ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Text(
                    col={'xs': 6, 'md': 3},
                    spans=[
                        ft.TextSpan(
                            text='3 + ',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                        ft.TextSpan(
                            text=' Anos de experiência',
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                size=16,
                            )
                        ),
                    ]
                ),

                ft.Text(
                    col={'xs': 6, 'md': 3},
                    spans=[
                        ft.TextSpan(
                            text='10 + ',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                        ft.TextSpan(
                            text=' Automações criadas',
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                size=16,
                            )
                        ),
                    ]
                ),

                ft.Text(
                    col={'xs': 6, 'md': 3},
                    spans=[
                        ft.TextSpan(
                            text='3 + ',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                        ft.TextSpan(
                            text=' Sistemas internos ativos',
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                size=16,
                            )
                        ),
                    ]
                ),

                ft.Text(
                    col={'xs': 6, 'md': 3},
                    spans=[
                        ft.TextSpan(
                            text='6 + ',
                            style=ft.TextStyle(
                                color=ft.Colors.PRIMARY,
                                weight=ft.FontWeight.W_900,
                                size=20,
                            )
                        ),
                        ft.TextSpan(
                            text=' Stacks dominadas',
                            style=ft.TextStyle(
                                color=ft.Colors.WHITE,
                                size=16,
                            )
                        ),
                    ]
                ),
            ]
        )
    )

    projects = ft.ResponsiveRow(
        columns=12,
        controls=[
            project_item(title='Calculadora do iPhone', description='Calculadora com o mesmo design do App do iPhone', url=''),
            project_item(title='ToDo App', description='Aplicativo para gerenciamento de tarefas com integração com banco de dados', url=''),
            project_item(title='Sistema de Login', description='Sistema completo de autenticação de usuário com suporte a recuperação de senha e cadastro de novos usuários', url=''),
            project_item(title='Contador', description='Aplicativo que contabiliza os cliques de um botão', url=''),
        ],
        spacing=30,
        run_spacing=30,
    )

    prices = ft.ResponsiveRow(
        columns=12,
        spacing=30,
        run_spacing=30,
        controls=[
            price_item(
                price=100,
                url='',
                items_included=[
                    {'title':'Prototipagem', 'is_included': True},
                    {'title':'Desenvolvimento WEB', 'is_included': True},
                    {'title':'Aplicativo multiplataforma', 'is_included': False},
                    {'title':'Manutenção por 12 meses', 'is_included': False},
                ]
            ),
            ft.Stack(
                col={'xs': 12, 'md': 6, 'lg': 4},
                controls=[
                    price_item(
                        price=150,
                        url='',
                        items_included=[
                            {'title':'Prototipagem', 'is_included': True},
                            {'title':'Desenvolvimento WEB', 'is_included': True},
                            {'title':'Aplicativo multiplataforma', 'is_included': True},
                            {'title':'Manutenção por 12 meses', 'is_included': False},
                        ]
                    ),
                    ft.Container(
                        bgcolor=ft.Colors.PRIMARY,
                        content=ft.Text(value='Popular', color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                        padding=ft.padding.symmetric(vertical=5, horizontal=50),
                        right=-40,
                        top=15,
                        rotate=ft.Rotate(angle=math.radians(40)),
                    )
                ]
            ),
            price_item(
                price=200,
                url='',
                items_included=[
                    {'title':'Prototipagem', 'is_included': True},
                    {'title':'Desenvolvimento WEB', 'is_included': True},
                    {'title':'Aplicativo multiplataforma', 'is_included': True},
                    {'title':'Manutenção por 12 meses', 'is_included': True},
                ]
            ),
        ]
    )

    testimonials = carousel(
        controls=[
            testimonial_item(
                user='Paula Rocha',
                job='Desenvolvedora júnior',
                testimonial='O trabalho do Rafael é realmente muito incrível, seus projetos são muito bonitos! Nunca pensei que desse pra clonar um site inteiro apenas com Python',
                image_src='img/testimonial-1-280x280.jpg'
            ),
            testimonial_item(
                user='Paula Rocha',
                job='Desenvolvedora júnior',
                testimonial='O trabalho do Rafael é realmente muito incrível, seus projetos são muito bonitos! Nunca pensei que desse pra clonar um site inteiro apenas com Python',
                image_src='img/testimonial-2-280x280.jpg'
            ),
            testimonial_item(
                user='Paula Rocha',
                job='Desenvolvedora júnior',
                testimonial='O trabalho do Rafael é realmente muito incrível, seus projetos são muito bonitos! Nunca pensei que desse pra clonar um site inteiro apenas com Python',
                image_src='img/testimonial-3-280x280.jpg'
            ),
            testimonial_item(
                user='Paula Rocha',
                job='Desenvolvedora júnior',
                testimonial='O trabalho do Rafael é realmente muito incrível, seus projetos são muito bonitos! Nunca pensei que desse pra clonar um site inteiro apenas com Python',
                image_src='img/testimonial-4-280x280.jpg'
            ),
        ]
    )

    logos = ft.Container(
        padding=ft.padding.all(30),
        opacity=0.6,
        content=ft.ResponsiveRow(
            controls=[
                ft.Image(
                    src='img/brand-1-464x512.png',
                    col={'xs': 6, 'lg': 3, 'xl': 2},
                ),
                ft.Image(
                    src='img/brand-2-458x512.png',
                    col={'xs': 6, 'lg': 3, 'xl': 2},
                ),
                ft.Image(
                    src='img/brand-3-456x512.png',
                    col={'xs': 6, 'lg': 3, 'xl': 2},
                ),
                ft.Image(
                    src='img/brand-1-464x512.png',
                    col={'xs': 6, 'lg': 3, 'xl': 2},
                ),
            ],
            spacing=30,
            run_spacing=30,
        )
    )

    footer = ft.Container(
        bgcolor=ft.Colors.ON_INVERSE_SURFACE,
        padding=ft.padding.all(30),
        content=ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Text(
                    col={'xs': 12, 'md': 6},
                    value='© 2025 Todos os direitos reservados.',
                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                ),
                ft.Text(
                    col={'xs': 12, 'md': 6},
                    spans=[
                        ft.TextSpan(text='Email: '),
                        ft.TextSpan(
                            text='rafael.vilas@gmail.com',
                            url='mailto:rafael.vilas@gmail.com'
                        )
                    ],
                    theme_style=ft.TextThemeStyle.BODY_MEDIUM,
                    text_align=ft.TextAlign.END,
                )
            ]
        )
    )

    def sections_title(title: str):
        return ft.Container(
            padding=ft.padding.symmetric(vertical=20),
            content=ft.Text(value=title, theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)
        )

    return ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                banner,
                experience,
                sections_title(title='Projetos'),
                projects,
                sections_title(title='Preços'),
                prices,
                sections_title(title='Recomendações'),
                testimonials,
                logos,
                footer,
            ],
            scroll=ft.ScrollMode.HIDDEN,
        ),
        bgcolor=ft.Colors.BLACK87,
        padding=ft.padding.all(30),
    )