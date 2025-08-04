"""Unit input component for from/to conversion inputs"""

import tkinter as tk
import customtkinter as ctk
from config.settings import AppConfig
from data.units_data import UnitsData


class UnitInputComponent:
    """Reusable component for unit input (from/to)"""

    def __init__(
        self,
        parent,
        label_text,
        initial_unit,
        on_change_callback,
        is_readonly=False,
        placeholder="Enter value",
    ):
        self.parent = parent
        self.label_text = label_text
        self.on_change_callback = on_change_callback
        self.is_readonly = is_readonly
        self.placeholder = placeholder

        self.setup_unit_input(initial_unit)

    def setup_unit_input(self, initial_unit):
        """Create unit input elements"""
        # Label
        self.label = ctk.CTkLabel(
            self.parent,
            text=self.label_text,
            font=ctk.CTkFont(size=AppConfig.DEFAULT_FONT_SIZE),
            text_color=AppConfig.SECONDARY_TEXT,
        )
        self.label.pack(pady=(10, 5))

        # Input frame
        self.input_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        self.input_frame.pack(pady=(0, 20))

        # Entry field
        entry_state = "readonly" if self.is_readonly else "normal"
        self.entry = ctk.CTkEntry(
            self.input_frame,
            width=AppConfig.ENTRY_WIDTH,
            height=AppConfig.ENTRY_HEIGHT,
            font=ctk.CTkFont(size=AppConfig.DEFAULT_FONT_SIZE),
            placeholder_text=self.placeholder,
            state=entry_state,
        )
        self.entry.pack(side="left", padx=(0, 10))

        if not self.is_readonly:
            self.entry.bind("<KeyRelease>", self.on_value_change)

        # Unit dropdown
        self.unit_var = tk.StringVar(value=initial_unit)
        self.unit_menu = ctk.CTkOptionMenu(
            self.input_frame,
            values=[initial_unit],  # Will be updated by parent
            variable=self.unit_var,
            command=self.on_unit_change,
            width=AppConfig.SMALL_DROPDOWN_WIDTH,
            height=AppConfig.ENTRY_HEIGHT,
            font=ctk.CTkFont(size=AppConfig.SMALL_FONT_SIZE),
        )
        self.unit_menu.pack(side="left")

    def on_value_change(self, event=None):
        """Handle value change in entry field"""
        self.on_change_callback()

    def on_unit_change(self, unit):
        """Handle unit selection change"""
        self.on_change_callback()

    def update_units(self, units, selected_unit=None):
        """Update available units in dropdown"""
        self.unit_menu.configure(values=units)
        if selected_unit:
            self.unit_var.set(selected_unit)

    def get_value(self):
        """Get current entry value"""
        return self.entry.get()

    def set_value(self, value):
        """Set entry value"""
        if self.is_readonly:
            self.entry.configure(state="normal")
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(value))
        if self.is_readonly:
            self.entry.configure(state="readonly")

    def clear_value(self):
        """Clear entry value"""
        if self.is_readonly:
            self.entry.configure(state="normal")
        self.entry.delete(0, tk.END)
        if self.is_readonly:
            self.entry.configure(state="readonly")

    def get_unit(self):
        """Get currently selected unit"""
        return self.unit_var.get()

    def set_unit(self, unit):
        """Set selected unit"""
        self.unit_var.set(unit)
