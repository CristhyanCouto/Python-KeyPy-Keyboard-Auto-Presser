import time
from pynput import keyboard
from pynput.keyboard import KeyCode, Listener, Key, Controller

class KeyboardPresser():

    def __init__(self, page):
        self.page = page
        self.key_pressed = Key.enter
        self.toggle_key = Key.f2
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.mili_seconds = 0
        self.time_to_wait = 0.5
        self.clicking = False
        self.keyboard_controller = Controller()

    def clicker(self): 
        while True:
            if self.clicking:
                self.keyboard_controller.press(self.key_pressed)
                self.keyboard_controller.release(self.key_pressed)
            time.sleep(self.time_to_wait)
            self.page.update()

    def toggle_event(self, key):

        if key == self.toggle_key:
            self.clicking = not self.clicking
            self.page.update()

    def convert_to_miliseconds(self):
        hours_in_ms = self.hours * 60 * 60 * 1000
        minutes_in_ms = self.minutes * 60 * 1000
        seconds_in_ms = self.seconds * 1000
        total_miliseconds = hours_in_ms + minutes_in_ms + seconds_in_ms + self.mili_seconds
        return total_miliseconds / 1000
    
        # Getters
    def get_hours(self):
        return self.hours
    
    def set_hours(self, hours):
        self.hours = hours

    def get_minutes(self):
        return self.minutes
    
    def set_minutes(self, minutes):
        self.minutes = minutes

    def get_seconds(self):
        return self.seconds
    
    def set_seconds(self, seconds):
        self.seconds = seconds

    def get_mili_seconds(self):
        return self.mili_seconds
    
    def set_mili_seconds(self, mili_seconds):
        self.mili_seconds = mili_seconds

    def get_page(self):
        return self.page
    
    def get_key_pressed(self):
        return self.key_pressed
    
    def get_toggle_key(self):
        return self.toggle_key
    
    def get_time_to_wait(self):
        return self.time_to_wait
    
    def get_clicking(self):
        return self.clicking
    
    def get_keyboard_controller(self):
        return self.keyboard_controller
    
        # Setters
    def set_page(self, page):
        self.page = page
    
    def set_key_pressed(self, key_pressed):
        self.key_pressed = key_pressed
    
    def set_toggle_key(self, toggle_key):
        self.toggle_key = toggle_key
    
    def set_time_to_wait(self, time_to_wait):
        self.time_to_wait = time_to_wait
    
    def set_clicking(self, clicking):
        self.clicking = clicking
    
    def set_keyboard_controller(self, keyboard_controller):
        self.keyboard_controller = keyboard_controller