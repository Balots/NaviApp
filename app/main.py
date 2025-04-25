import flet as ft
import requests


def main(page: ft.Page):
    page.title = "Emaps"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Адрес назначения', width=400)

    def get_map(e):
        API = 'a6537930-af5c-4936-b1cf-a331eac60e1d'
        URL = f'https://api-maps.yandex.ru/v3/?apikey=<{API}>&lang=en_US'
        response = requests.get(URL)
        return response.json()

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Куда вы хотите попасть?')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([ft.ElevatedButton(text='Построить маршрут', on_click=get_map)], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)

