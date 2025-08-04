"""Application configuration and constants"""

import customtkinter as ctk

# Set global appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AppConfig:
    """Application configuration constants"""

    WINDOW_TITLE = "Unit Converter"
    WINDOW_SIZE = "500x600"
    WINDOW_RESIZABLE = False

    # Color scheme
    BG_COLOR = "#1a1a1a"
    CARD_COLOR = "#2b2b2b"
    ACCENT_COLOR = "#3b82f6"
    TEXT_COLOR = "#ffffff"
    SECONDARY_TEXT = "#a0a0a0"
    HOVER_COLOR = "#2563eb"

    # Font sizes
    TITLE_FONT_SIZE = 32
    SUBTITLE_FONT_SIZE = 14
    SECTION_FONT_SIZE = 16
    DEFAULT_FONT_SIZE = 14
    SMALL_FONT_SIZE = 12
    SWAP_BUTTON_FONT_SIZE = 20

    # Component dimensions
    DROPDOWN_WIDTH = 300
    DROPDOWN_HEIGHT = 40
    ENTRY_WIDTH = 200
    ENTRY_HEIGHT = 40
    SMALL_DROPDOWN_WIDTH = 100
    SWAP_BUTTON_SIZE = 40
