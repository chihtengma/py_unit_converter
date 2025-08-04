"""Swap button component"""

import customtkinter as ctk
from config.settings import AppConfig


class SwapButton:
    """Swap button for switching from/to units"""

    def __init__(self, parent, on_swap_callback):
        self.parent = parent
        self.on_swap_callback = on_swap_callback
        self.setup_swap_button()

    def setup_swap_button(self):
        """Create swap button"""
        self.swap_button = ctk.CTkButton(
            self.parent,
            text="⇅",
            width=AppConfig.SWAP_BUTTON_SIZE,
            height=AppConfig.SWAP_BUTTON_SIZE,
            font=ctk.CTkFont(size=AppConfig.SWAP_BUTTON_FONT_SIZE),
            command=self.on_swap_callback,
            fg_color=AppConfig.ACCENT_COLOR,
            hover_color=AppConfig.HOVER_COLOR,
        )
        self.swap_button.pack(pady=10)
