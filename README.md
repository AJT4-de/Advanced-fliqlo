# Advanced Fliqlo 🕰️

A modern, highly customizable web-based flip clock inspired by the classic Fliqlo design. This project offers an elegant, responsive time display with advanced dual-time support and dynamic layout options, perfect for use as a browser-based screensaver or a stylish desk clock.

## ✨ Features

- **Classic Flip Clock Aesthetic**: Experience the iconic retro-modern flip animation.
- **Dual-Time Display**: Support for "up and down" orientation to display two different time zones simultaneously.
- **Customizable Day & Date**: Dynamically toggle and format the day and date display through an intuitive settings panel.
- **Fully Responsive**: Flawlessly scales to fit any screen size or window dimension without losing structural integrity.
- **Settings Dashboard**: An interactive UI to customize formatting, positioning, and other visual preferences on the fly.
- **Zero Dependencies**: Built entirely with Vanilla HTML, CSS, and JavaScript for maximum performance and portability.

## 🚀 Getting Started

### Running the Clock

Since this is a client-side web application, no build tools or servers are required!

1. Clone the repository:
   ```bash
   git clone https://github.com/AJT4-de/Advanced-fliqlo.git
   ```
2. Navigate to the project directory and simply open `index.html` in your preferred web browser.
3. Use the settings panel to configure your preferred layout, timezone, and date format.

### Running the Automated UI Tests

This project includes a Python-based testing suite using Selenium to ensure the settings panel and DOM updates function correctly.

1. Ensure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install selenium webdriver-manager
   ```
3. Run the test script:
   ```bash
   python test_ui.py
   ```
   *The script runs a headless Chrome browser to validate DOM interactions and settings application.*

## 🛠️ Built With

- **HTML5 / CSS3 / JavaScript (Vanilla)**: For the core structure, styling, and clock logic.
- **Python / Selenium**: For automated UI testing and validation.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/AJT4-de/Advanced-fliqlo/issues).

## 📝 License

This project is open-source and available under the MIT License.
