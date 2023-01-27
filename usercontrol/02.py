import flet as ft


def main(page: ft.Page):
    app_title = "カウンター出力"
    page.title = app_title

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    txt_number = ft.TextField(
        color=ft.colors.BLACK,
        border_radius=10,
        border=ft.InputBorder.NONE,
        value="0",
        text_align=ft.TextAlign.CENTER
    )

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Column(
            [
                ft.Text(
                    app_title
                )
            ]
        ),
        ft.Row(
            [
                ft.IconButton(
                    ft.icons.REMOVE,
                    bgcolor=ft.colors.CYAN_200,
                    on_click=minus_click
                ),
                ft.Container(
                    content=txt_number,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.INDIGO_50,
                    border_radius=10,
                    ink=True
                ),
                ft.IconButton(
                    ft.icons.ADD,
                    bgcolor=ft.colors.AMBER,
                    on_click=plus_click
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(target=main)
