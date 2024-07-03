class LayoutControl():

    def __init__(self, page):
        self.page = page
        self.page.title = "KeyPy Auto Presser"
        self.page.theme_mode = 'dark'
        self.page.window_height = 500
        self.page.window_width = 500
        self.page.window_max_width = 500
        self.page.window_max_height = 500
        self.page.window_min_width = 500
        self.page.window_min_height = 500

    def change_to_dark_mode(self, e):
        self.page.theme_mode = 'dark'
        self.page.update()
    def change_to_light_mode(self, e):
        self.page.theme_mode = 'light'
        self.page.update()
