from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

options = Options()
options.headless = True  # Run in headless mode
driver = webdriver.Chrome(options=options)

maps_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps'  # Update this path
output_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps_merged'  # Update this path
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(maps_dir):
    if filename.endswith(".html"):
        file_path = f'file:///{os.path.join(maps_dir, filename)}'
        driver.get(file_path)

        # Wait for the map to be loaded
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'leaflet-pane'))
            # Adjust this selector based on your map's HTML structure
        )

        # Optionally, resize window to ensure the map is fully visible
        driver.set_window_size(1200, 800)  # Adjust as needed

        # Take screenshot
        output_filepath = os.path.join(output_dir, filename.replace('.html', '.png'))
        driver.save_screenshot(output_filepath)
        print(f'Screenshot saved for {filename}')

driver.quit()
