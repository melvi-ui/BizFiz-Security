from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.utils import get_color_from_hex

class Dashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Main Theme: Dark Navy (McAfee/Kaspersky mix)
        root = BoxLayout(orientation='horizontal')
        
        # 1. SIDEBAR (Bitdefender/Panda style)
        sidebar = BoxLayout(orientation='vertical', size_hint_x=0.18, spacing=15, padding=10)
        sidebar.add_widget(Button(text="🛡️", size_hint_y=None, height='60dp', background_color=(0.1, 0.1, 0.2, 1)))
        sidebar.add_widget(Button(text="🔒", size_hint_y=None, height='60dp', background_color=(0.1, 0.1, 0.2, 1), on_press=self.go_premium))
        sidebar.add_widget(Button(text="🚀", size_hint_y=None, height='60dp', background_color=(0.1, 0.1, 0.2, 1)))
        root.add_widget(sidebar)

        # 2. MAIN CONTENT
        main_content = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # Glowing Status (Norton style)
        self.status_label = Label(text="SYSTEM AT RISK", font_size='28sp', bold=True, color=get_color_from_hex("#00CCFF"))
        main_content.add_widget(self.status_label)

        # Futuristic Progress Bar
        self.progress = ProgressBar(max=100, value=0, size_hint_y=None, height='20dp')
        main_content.add_widget(self.progress)

        # One-Tap Scan Button (Avast style)
        self.scan_btn = Button(
            text="START DEEP SCAN", size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5}, background_color=get_color_from_hex("#0055FF"),
            font_size='22sp', bold=True
        )
        self.scan_btn.bind(on_press=self.initiate_deep_scan)
        main_content.add_widget(self.scan_btn)

        # Optimization Cards (Avira/TotalAV style)
        cards = BoxLayout(orientation='horizontal', size_hint_y=0.25, spacing=15)
        cards.add_widget(Button(text="CLEAN JUNK", background_color=(0.2, 0.2, 0.2, 1)))
        cards.add_widget(Button(text="BOOST RAM", background_color=(0.2, 0.2, 0.2, 1)))
        main_content.add_widget(cards)

        root.add_widget(main_content)
        self.add_widget(root)

    def initiate_deep_scan(self, instance):
        self.scan_btn.disabled = True
        self.status_label.text = "DEEP SCAN IN PROGRESS..."
        self.status_label.color = get_color_from_hex("#FFCC00") # Alert Yellow
        
        # Animate the progress bar
        anim = Animation(value=100, duration=5, t='in_out_quad')
        anim.bind(on_complete=self.scan_finished)
        anim.start(self.progress)

    def scan_finished(self, *args):
        self.status_label.text = "SYSTEM SECURED"
        self.status_label.color = get_color_from_hex("#00FF66") # Success Green
        self.scan_btn.text = "SCAN AGAIN"
        self.scan_btn.disabled = False

    def go_premium(self, instance):
        self.manager.current = 'premium'

class PremiumScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        layout.add_widget(Label(text="BIZFIX PREMIUM", font_size='34sp', bold=True, color=(1, 0.8, 0, 1)))
        layout.add_widget(Label(text="Unlock All Systems:\n• Deep AI Threat Hunting\n• Anti-Phishing (MRA/MCB)\n• Identity Guard Mauritius", halign='center'))
        
        buy_btn = Button(text="UNLOCK ALL - Rs 499 / Year", size_hint_y=0.2, background_color=(0, 0.8, 0, 1))
        layout.add_widget(buy_btn)
        
        back_btn = Button(text="Back to Dashboard", size_hint_y=0.1, background_color=(0.3, 0.3, 0.3, 1))
        back_btn.bind(on_press=self.go_back)
        layout.add_widget(back_btn)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'dashboard'

class BizFixSecurity(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Dashboard(name='dashboard'))
        sm.add_widget(PremiumScreen(name='premium'))
        return sm

if __name__ == "__main__":
    BizFixSecurity().run()
