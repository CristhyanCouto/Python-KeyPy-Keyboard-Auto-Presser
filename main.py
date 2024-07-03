import flet as ft
from flet import *

# pynput
import threading
from pynput import keyboard
from pynput.keyboard import KeyCode, Listener, Key, Controller

# my imports
from src.services.KeyboardPresser import KeyboardPresser
from src.services.LayoutControl import LayoutControl

def main(page: ft.Page):
    # Page Settings
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_center()

    #Class Instances
    keyboard_presser = KeyboardPresser(page)
    layout_control = LayoutControl(page)

    t3 = ft.Text()

    # Toggle Key
    def drop_down_toggle_key_changed(e):
        toggle_key = getattr(Key, drop_down_toggle_key.value, KeyCode.from_char(drop_down_toggle_key.value))
        keyboard_presser.set_toggle_key(toggle_key)
        t.value = f"Toggle Key is set to:  {toggle_key}"
        page.update()

    t = ft.Text()

    # Generate options for all keys
    key_options = [ft.dropdown.Option(key.name) for key in list(Key)]
    key_options += [ft.dropdown.Option(str(chr(kc))) for kc in range(32, 127)]  # Adding printable ASCII characters

    drop_down_toggle_key = ft.Dropdown(
        width=200,
        options=key_options,
        label="Toggle Key",
        on_change=drop_down_toggle_key_changed
    )

    # Key to be auto pressed
    def drop_down_pressed_key_changed(e):
        key_pressed = getattr(Key, drop_down_pressed_key.value, KeyCode.from_char(drop_down_pressed_key.value))
        keyboard_presser.set_key_pressed(key_pressed)
        t2.value = f"Key to be pressed is:  {key_pressed}"
        page.update()

    t2 = ft.Text()

    drop_down_pressed_key = ft.Dropdown(
        width=200,
        options=key_options,
        label="Pressed Key",
        on_change=drop_down_pressed_key_changed,
    )
    
    def on_hour_change(e):
        if e.control.value == "":
            e.control.value = 0
        keyboard_presser.set_hours(int(e.control.value))
        keyboard_presser.set_time_to_wait(keyboard_presser.convert_to_miliseconds())
        time_to_wait_text.value = f"Time to wait: {keyboard_presser.get_time_to_wait()}"
        page.update()
    
    def on_minute_change(e):
        if e.control.value == "":
            e.control.value = 0
        keyboard_presser.set_minutes(int(e.control.value))
        keyboard_presser.set_time_to_wait(keyboard_presser.convert_to_miliseconds())
        time_to_wait_text.value = f"Time to wait: {keyboard_presser.get_time_to_wait()}"
        page.update()
    
    def on_second_change(e):
        if e.control.value == "":
            e.control.value = 0
        keyboard_presser.set_seconds(int(e.control.value))
        keyboard_presser.set_time_to_wait(keyboard_presser.convert_to_miliseconds())
        time_to_wait_text.value = f"Time to wait: {keyboard_presser.get_time_to_wait()}"
        page.update()
    
    def on_milisecond_change(e):
        if e.control.value == "":
            e.control.value = 0
        keyboard_presser.set_mili_seconds(int(e.control.value))
        keyboard_presser.set_time_to_wait(keyboard_presser.convert_to_miliseconds())
        time_to_wait_text.value = f"Time to wait: {keyboard_presser.get_time_to_wait()}"
        page.update()

    hour_value = ft.TextField(label="Hour", width=75, value=0, on_change=on_hour_change, text_align="center", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]"))
    minute_value = ft.TextField(label="Min", width=75, value=0, on_change=on_minute_change, text_align="center", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]"))
    second_value = ft.TextField(label="Sec", width=75, value=0, on_change=on_second_change, text_align="center", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]"))
    milisecond_value = ft.TextField(label="Milisec", width=75, value=0, on_change=on_milisecond_change, text_align="center", input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]"))
    time_to_wait_text = ft.Text(f"Time to wait: {keyboard_presser.get_time_to_wait()}")

    # Page Adds
    page.add(
        ft.Row(
            [
            time_to_wait_text
            ], alignment="center"
        ),
        ft.Row(
            [
            hour_value,
            minute_value,
            second_value,
            milisecond_value,
            ], alignment="center"
        ),
        ft.Row(
            [
            drop_down_toggle_key,
            drop_down_pressed_key
            ], alignment="center"
        )
    )

    #App Bar
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.KEYBOARD),
        leading_width=40,
        title=ft.Text("KeyPy Auto Presser"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.LIGHT_MODE_OUTLINED, on_click=layout_control.change_to_light_mode),
            ft.IconButton(ft.icons.DARK_MODE, on_click=layout_control.change_to_dark_mode),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="About", icon=ft.icons.INFO),
                ]
            ),
        ],
    )

    click_thread = threading.Thread(target=keyboard_presser.clicker)
    click_thread.start()

    with Listener(on_press=keyboard_presser.toggle_event) as listener:
        listener.join()

ft.app(target=main)
