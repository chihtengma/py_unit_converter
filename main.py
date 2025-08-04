"""Main application file"""

import tkinter as tk
import customtkinter as ctk
from config.settings import AppConfig
from data.units_data import UnitsData
from utils.converter import UnitConverter
from components.header import HeaderComponent
from components.category_selector import CategorySelector
from components.unit_input import UnitInputComponent
from components.swap_button import SwapButton
from components.result_display import ResultDisplay


class UnitConverterApp(ctk.CTk):
    """Main application class"""

    def __init__(self):
        super().__init__()

        # Configure window
        self.title(AppConfig.WINDOW_TITLE)
        self.geometry(AppConfig.WINDOW_SIZE)
        self.resizable(AppConfig.WINDOW_RESIZABLE, AppConfig.WINDOW_RESIZABLE)
        self.configure(fg_color=AppConfig.BG_COLOR)

        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface"""
        # Header
        self.header = HeaderComponent(self)

        # Main container
        self.main_frame = ctk.CTkFrame(
            self, fg_color=AppConfig.CARD_COLOR, corner_radius=20
        )
        self.main_frame.pack(padx=40, pady=(0, 40), fill="both", expand=True)

        # Category selector
        self.category_selector = CategorySelector(
            self.main_frame, self.on_category_change
        )

        # From unit input
        self.from_input = UnitInputComponent(
            self.main_frame,
            "From",
            "Meter",
            self.convert_units,
            is_readonly=False,
            placeholder="Enter value",
        )

        # Swap button
        self.swap_button = SwapButton(self.main_frame, self.swap_units)

        # To unit input
        self.to_input = UnitInputComponent(
            self.main_frame, "To", "Kilometer", self.convert_units, is_readonly=True
        )

        # Result display
        self.result_display = ResultDisplay(self.main_frame)

        # Initialize with default category
        self.on_category_change("Length")

    def on_category_change(self, category):
        """Handle category change"""
        unit_options = UnitsData.get_units_for_category(category)

        # Update unit dropdowns
        self.from_input.update_units(unit_options, unit_options[0])
        self.to_input.update_units(
            unit_options, unit_options[1] if len(unit_options) > 1 else unit_options[0]
        )

        # Clear inputs and results
        self.from_input.clear_value()
        self.to_input.clear_value()
        self.result_display.clear_result()

    def convert_units(self):
        """Perform unit conversion"""
        try:
            value = float(self.from_input.get_value())
            category = self.category_selector.get_selected_category()
            from_unit = self.from_input.get_unit()
            to_unit = self.to_input.get_unit()

            # Perform conversion
            result = UnitConverter.convert_units(value, category, from_unit, to_unit)
            result_text = UnitConverter.format_result(result)

            # Update UI
            self.to_input.set_value(result_text)
            self.result_display.update_result(
                f"{value} {from_unit} = {result_text} {to_unit}"
            )

        except ValueError:
            # Clear results on invalid input
            self.to_input.clear_value()
            self.result_display.clear_result()

    def swap_units(self):
        """Swap from and to units"""
        from_unit = self.from_input.get_unit()
        to_unit = self.to_input.get_unit()

        self.from_input.set_unit(to_unit)
        self.to_input.set_unit(from_unit)

        self.convert_units()


if __name__ == "__main__":
    # Note: This requires customtkinter to be installed
    # Install with: pip install customtkinter pillow
    app = UnitConverterApp()
    app.mainloop()
