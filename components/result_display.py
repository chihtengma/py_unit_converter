"""Result display component"""

import customtkinter as ctk
from config.settings import AppConfig


class ResultDisplay:
    """Displays conversion results"""

    def __init__(self, parent):
        self.parent = parent
        self.setup_result_display()

    def setup_result_display(self):
        """Create result display elements"""
        self.result_label = ctk.CTkLabel(
            self.parent,
            text="",
            font=ctk.CTkFont(size=AppConfig.DEFAULT_FONT_SIZE),
            text_color=AppConfig.ACCENT_COLOR,
            wraplength=300,
        )
        self.result_label.pack(pady=(20, 30))

    def update_result(self, text):
        """Update result text"""
        self.result_label.configure(text=text)

    def clear_result(self):
        """Clear result text"""
        self.result_label.configure(text="")
