from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.graphics import Color, Line
from kivy.animation import Animation
import os

class BizFixSecurity(App):
    def build(self):
        self.title = "BIZFIX-SECURITY: NEON"
        
        # Dark Background Layout
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Futuristic Header
        self.header = Label(
            text="[ BIZFIX // SECURITY ]", 
            font_size='32sp', 
            color=(0, 0.8, 1, 1), # Neon Blue
            bold=True
        )
        self.layout.add_widget(self.header)

        # Status with a pulsing effect
        self.status = Label(text="SYSTEM: STANDBY", color=(0.5, 0.5, 0.5, 1))
        self.layout.add_widget(self.status)
        
        # Futuristic Scan Button
        self.scan_btn = Button(
            text="INITIALIZE SCAN",
            size_hint_y=None, height='80dp',
            background_color=(0, 0.4, 0.6, 1),
            color=(1, 1, 1, 1),
            background_normal='' # Removes the default grey look
        )
        self.scan_btn.bind(on_press=self.start_scan_animation)
        self.layout.add_widget(self.scan_btn)

        # Results Console
        self.scroll = ScrollView()
        self.console = Label(
            text="> Waiting for user input...", 
            size_hint_y=None, 
            halign='left', 
            color=(0, 1, 0.3, 1), # Matrix Green
            font_name='Roboto' # Or a monospaced font if available
        )
        self.console.bind(texture_size=self.console.setter('size'))
        self.scroll.add_widget(self.console)
        self.layout.add_widget(self.scroll)
        
        return self.layout

    def start_scan_animation(self, instance):
        self.console.text = "> Booting scan engine...\n> Accessing local storage..."
        self.status.text = "SCANNING..."
        self.status.color = (1, 0.8, 0, 1) # Alert Yellow
        
        # Animate the header to pulse
        anim = Animation(color=(1, 1, 1, 1), duration=0.5) + Animation(color=(0, 0.8, 1, 1), duration=0.5)
        anim.repeat = True
        anim.start(self.header)
        
        # Schedule the actual scan logic after 2 seconds to simulate "thinking"
        Clock.schedule_once(self.run_actual_scan, 2)

    def run_actual_scan(self, dt):
        path = "/sdcard/Download" if os.path.exists("/sdcard/Download") else "."
        found_issues = []
        
        # Logic to simulate "deep" scanning
        for root, _, files in os.walk(path):
            for file in files:
                self.console.text += f"\n> Checking: {file[:20]}..."
                if file.endswith(('.apk', '.exe', '.sh')):
                    found_issues.append(file)

        Animation.stop_all(self.header) # Stop the pulse
        
        if not found_issues:
            self.status.text = "SYSTEM: CLEAN"
            self.status.color = (0, 1, 0, 1) # Safe Green
            self.console.text += "\n\n> SCAN COMPLETE: 0 THREATS DETECTED."
        else:
            self.status.text = "SYSTEM: COMPROMISED"
            self.status.color = (1, 0, 0, 1) # Danger Red
            self.console.text += f"\n\n> WARNING: {len(found_issues)} SUSPICIOUS FILES FOUND."

if __name__ == "__main__":
    BizFixSecurity().run()
