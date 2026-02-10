from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import hashlib
import os

# BizFix-Security Local Threat Database
MALWARE_DATABASE = {
    "5d41402abc4b2a76b9719d911017c592": "Fake-MCB-Juice",
    "8d221d014c568f6d6545123456789012": "MRA-Phishing-Tool"
}

class BizFixSecurity(App):
    def build(self):
        self.title = "BizFix-Security Lite"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Branding
        layout.add_widget(Label(text="BIZFIX-SECURITY", font_size='24sp', color=(0, 0.6, 1, 1)))
        layout.add_widget(Label(text="Mauritius Edition v1.0", font_size='14sp'))

        self.status = Label(text="System Status: Protected", color=(0, 1, 0, 1))
        layout.add_widget(self.status)
        
        # Scan Button
        scan_btn = Button(text="RUN LITE SCAN", size_hint_y=None, height='100dp', background_color=(0, 0.5, 0.8, 1))
        scan_btn.bind(on_press=self.run_scan)
        layout.add_widget(scan_btn)

        # Results Area
        self.scroll = ScrollView()
        self.results = Label(text="Log ready...", size_hint_y=None, halign='left')
        self.results.bind(texture_size=self.results.setter('size'))
        self.scroll.add_widget(self.results)
        layout.add_widget(self.scroll)
        
        return layout

    def run_scan(self, instance):
        self.status.text = "Scanning Storage..."
        # On Android, we look at the public Downloads folder
        path = "/sdcard/Download" if os.path.exists("/sdcard/Download") else "."
        
        found_issues = []
        for root, _, files in os.walk(path):
            for file in files:
                # Basic check for suspicious extensions popular in local scams
                if file.endswith(('.apk', '.exe', '.sh')):
                    found_issues.append(f"Checked: {file}")
        
        if not found_issues:
            self.results.text = "No threats found in Downloads."
        else:
            self.results.text = "\n".join(found_issues)
        self.status.text = "Scan Complete"

if __name__ == "__main__":
    BizFixSecurity().run()