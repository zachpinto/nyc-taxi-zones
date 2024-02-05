from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def generate_missing_screenshots(html_dir, png_dir, start_year, end_year):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Set window size to match the size used in maps_screenshots_selenium.py
    driver.set_window_size(1200, 800)  # Adjust this size to match your requirements

    for year in range(start_year, end_year + 1):
        for week in range(1, 53):
            png_filename = f'week_{year}-{week}.png'
            png_filepath = os.path.join(png_dir, png_filename)

            if not os.path.exists(png_filepath):
                print(f"{png_filename} is missing, attempting to regenerate...")

                html_filename = f'week_{year}-{week}.html'
                html_filepath = os.path.join(html_dir, html_filename)

                if os.path.exists(html_filepath):
                    file_url = f'file:///{html_filepath}'
                    driver.get(file_url)

                    # Take screenshot
                    driver.save_screenshot(png_filepath)
                    print(f"Regenerated: {png_filename}")
                else:
                    print(f"HTML file not found: {html_filename}")

    driver.quit()
    print("Finished regenerating missing screenshots.")

# Paths to your directories
html_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps'
png_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps_merged'

# Define the range of years you're working with
start_year = 2018
end_year = 2022

generate_missing_screenshots(html_dir, png_dir, start_year, end_year)