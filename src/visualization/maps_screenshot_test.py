from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

options = Options()
options.headless = True  # Run in headless mode
driver = webdriver.Chrome(options=options)

# Path to your HTML file
html_file_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps/week_2018-1.html'
output_screenshot_path = '/reports/maps_merged/week_2018-1.png'

# Use the file:// protocol to open local HTML files
file_url = f'file:///{html_file_path}'
driver.get(file_url)

# Wait for the map to be loaded. Adjust the timeout and condition based on your map's specifics.
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'leaflet-pane'))  # This assumes your map has a 'leaflet-pane' class. Adjust if necessary.
)

# Optionally, resize window to ensure the map is fully visible
driver.set_window_size(1200, 800)  # Adjust as needed

# Take screenshot
driver.save_screenshot(output_screenshot_path)
print(f'Screenshot saved: {output_screenshot_path}')

driver.quit()
