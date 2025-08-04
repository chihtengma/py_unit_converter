"""Conversion logic utilities"""

from data.units_data import UnitsData


class UnitConverter:
    """Handles unit conversion calculations"""

    @staticmethod
    def convert_units(value, category, from_unit, to_unit):
        """Convert between units in the same category"""
        if category == "Temperature":
            return UnitConverter.convert_temperature(value, from_unit, to_unit)
        else:
            return UnitConverter.convert_standard_units(
                value, category, from_unit, to_unit
            )

    @staticmethod
    def convert_standard_units(value, category, from_unit, to_unit):
        """Convert between standard units using conversion factors"""
        from_factor = UnitsData.get_conversion_factor(category, from_unit)
        to_factor = UnitsData.get_conversion_factor(category, to_unit)
        return value * from_factor / to_factor

    @staticmethod
    def convert_temperature(value, from_unit, to_unit):
        """Convert temperature units with special logic"""
        if from_unit == to_unit:
            return value

        # Convert to Celsius first
        if from_unit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9
        elif from_unit == "Kelvin":
            celsius = value - 273.15
        else:
            celsius = value

        # Convert from Celsius to target unit
        if to_unit == "Fahrenheit":
            return celsius * 9 / 5 + 32
        elif to_unit == "Kelvin":
            return celsius + 273.15
        else:
            return celsius

    @staticmethod
    def format_result(result):
        """Format the conversion result for display"""
        if result.is_integer():
            return f"{int(result)}"
        elif result < 0.01 or result > 1000000:
            return f"{result:.2e}"
        else:
            return f"{result:.6g}"
