"""Unit conversion data and constants"""


class UnitsData:
    """Container for all unit conversion data"""

    UNITS = {
        "Length": {
            "Meter": 1.0,
            "Kilometer": 0.001,
            "Centimeter": 100.0,
            "Millimeter": 1000.0,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701,
        },
        "Weight": {
            "Kilogram": 1.0,
            "Gram": 1000.0,
            "Milligram": 1000000.0,
            "Pound": 2.20462,
            "Ounce": 35.274,
            "Ton": 0.001,
        },
        "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"},
        "Area": {
            "Square Meter": 1.0,
            "Square Kilometer": 0.000001,
            "Square Mile": 3.861e-7,
            "Square Yard": 1.19599,
            "Square Foot": 10.7639,
            "Acre": 0.000247105,
            "Hectare": 0.0001,
        },
        "Volume": {
            "Liter": 1.0,
            "Milliliter": 1000.0,
            "Gallon (US)": 0.264172,
            "Quart": 1.05669,
            "Pint": 2.11338,
            "Cup": 4.22675,
            "Fluid Ounce": 33.814,
            "Cubic Meter": 0.001,
        },
        "Speed": {
            "Meter/Second": 1.0,
            "Kilometer/Hour": 3.6,
            "Mile/Hour": 2.23694,
            "Foot/Second": 3.28084,
            "Knot": 1.94384,
        },
        "Data": {
            "Byte": 1.0,
            "Kilobyte": 0.001,
            "Megabyte": 0.000001,
            "Gigabyte": 1e-9,
            "Terabyte": 1e-12,
            "Bit": 8.0,
            "Kilobit": 0.008,
            "Megabit": 0.000008,
        },
    }

    @classmethod
    def get_categories(cls):
        """Get list of available categories"""
        return list(cls.UNITS.keys())

    @classmethod
    def get_units_for_category(cls, category):
        """Get list of units for a specific category"""
        return list(cls.UNITS.get(category, {}).keys())

    @classmethod
    def get_conversion_factor(cls, category, unit):
        """Get conversion factor for a unit in a category"""
        return cls.UNITS.get(category, {}).get(unit, 1.0)
