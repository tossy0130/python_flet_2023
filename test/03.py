import flet as ft 

def main(page):
    row = ft.Row(controls=[ft.Text("A"), ft.Text("B"), ft.Text("C")])
    column = ft.Column(controls=[row, ft.Text("D")])
    page.add(column)
    
ft.app(target=main)