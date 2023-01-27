import flet as ft


class MyControl(ft.UserControl):
    def build(self):
        return ft.Card(
            content=ft.Container(
                content=ft.Row(
                    [
                        ft.CircleAvatar(content=ft.Text("UN"),
                                        bgcolor=ft.colors.DEEP_PURPLE_300),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    "UserName", style=ft.TextThemeStyle.TITLE_MEDIUM),
                                ft.Text("email@example.com",
                                        color=ft.colors.BLACK38),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        ),
                    ]
                ),
                width=400,
                padding=16,
            )
        )


def main(page: ft.Page):
    for _ in range(4):
        page.add(MyControl())


ft.app(target=main)
