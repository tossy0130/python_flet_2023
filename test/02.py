import time
import flet as ft

# =========== # ０～９　まで、１秒ごとにテキストが更新する


def main(page: ft.Page):
    t = ft.Text()
    page.add(t)

    for i in range(10):
        t.value = f"step{i}" + '個'
        page.update()
        time.sleep(1)


ft.app(target=main)
