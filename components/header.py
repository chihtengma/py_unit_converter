"""Header components for the application"""

import customtkinter as ctk
from config.settings import AppConfig


class HeaderComponent:
    """Creates and manages the header section"""

    def __init__(self, parent):
        self.parent = parent
        self.setup_header()

    def setup_header(self):
        """Creates header elements"""
        # Title
        self.title_label = ctk.CTkLabel(
            self.parent,
            text="Unit Converter",
            font=ctk.CTkFont(size=AppConfig.TITLE_FONT_SIZE, weight="bold"),
            text_color=AppConfig.TEXT_COLOR,
        )
        self.title_label.pack(pady=(30, 10))

        # Sbutitle
        self.subtitle_label = ctk.CTkLabel(
            self.parent,
            text="Convert between different units easily",
            font=ctk.CTkFont(size=AppConfig.SUBTITLE_FONT_SIZE),
            text_color=AppConfig.SECONDARY_TEXT,
        )
        self.subtitle_label.pack(pady=(0, 30))
