from kivy.app import App
from kivy.uix.button import Button
from plyer import gps

class GPSApp(App):
    def build(self):
        return Button(text='Get GPS', on_press=self.get_gps)

    def get_gps(self, *args):
        gps.configure(on_location=self.on_location)
        gps.start()

    def on_location(self, **kwargs):
        print(f"GPS: {kwargs}")

GPSApp().run()