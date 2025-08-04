# Unit Converter

A modern unit converter app with dark theme built using Python and CustomTkinter.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Features

- Convert between 7 categories: Length, Weight, Temperature, Area, Volume, Speed, Data
- Dark modern UI with real-time conversion
- Quick unit swapping
- Smart number formatting

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/unit-converter.git
cd unit-converter

# Install dependencies
pip install customtkinter pillow

# Run app
python main.py
```

## Usage

1. Select category (Length, Weight, etc.)
2. Enter value in "From" field
3. Choose source and target units
4. Result appears instantly
5. Use ⇅ button to swap units

## Supported Units

**Length**: Meter, Kilometer, Mile, Foot, Inch, etc.  
**Weight**: Kilogram, Pound, Ounce, Gram, etc.  
**Temperature**: Celsius, Fahrenheit, Kelvin  
**Area**: Square Meter, Acre, Square Mile, etc.  
**Volume**: Liter, Gallon, Cup, Milliliter, etc.  
**Speed**: m/s, km/h, mph, knots, etc.  
**Data**: Byte, KB, MB, GB, TB, etc.

## Project Structure

```
unit_converter/
├── main.py              # Main app
├── config/settings.py   # Configuration
├── data/units_data.py   # Unit data
├── utils/converter.py   # Conversion logic
└── components/          # UI components
```

## License

MIT License - feel free to use and modify!
