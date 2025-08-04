"""Category selection component"""

import tkinter as tk
import customtkinter as ctk

from config.settings import AppConfig
from data.units_data import UnitsData


class CategorySelector:
    """Handles category selection UI and logic"""

    def __init__(self, parent, on_change_callback):
        self.parent = parent
        self.on_change_callback = on_change_callback
        self.setup_category_selector()

    def setup_category_selector(self):
        """Create category selection elements"""
        # Category label
        self.category_label = ctk.CTkLabel(
            self.parent,
            text="Category",
            font=ctk.CTkFont(size=AppConfig.SECTION_FONT_SIZE, weight="bold"),
            text_color=AppConfig.TEXT_COLOR,
        )
        self.category_label.pack(pady=(30, 10))

        # Category dropdown
        self.category_var = tk.StringVar(value="Length")
        self.category_menu = ctk.CTkOptionMenu(
            self.parent,
            values=UnitsData.get_categories(),
            variable=self.category_var,
            command=self.on_category_change,
            width=AppConfig.DROPDOWN_WIDTH,
            height=AppConfig.DROPDOWN_HEIGHT,
            font=ctk.CTkFont(size=AppConfig.DEFAULT_FONT_SIZE),
            dropdown_font=ctk.CTkFont(size=AppConfig.DEFAULT_FONT_SIZE),
        )
        self.category_menu.pack(pady=(0, 20))

    def on_category_change(self, category):
        """Handle category change event"""
        self.on_change_callback(category)

    def get_selected_category(self):
        """Get currently selected category"""
        return self.category_var.get()
