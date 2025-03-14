from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def read_first_line(file_path):
    """Read the first line from the text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines[0].strip() if lines else None

def remove_first_line(file_path):
    """Remove the first line from the text file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    if lines:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines[1:])

def main():
    # Path to the text file
    file_path = "shiyakusyo.txt"
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: {file_path} does not exist.")
        return
    
    # Read the first line
    city_name = read_first_line(file_path)
    if not city_name:
        print(f"Error: {file_path} is empty.")
        return
    
    # Set up Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Step 1: Open Google Maps
        driver.get("https://www.google.com/maps")
        driver.maximize_window()
        
        # Wait for the page to load
        wait = WebDriverWait(driver, 20)
        
        # Step 3: Enter search query (city name + 市役所)
        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))
        search_query = f"{city_name} 市役所"
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
        
        # Wait for search results and pin to appear
        time.sleep(5)  # Give extra time for map to load and pin to appear
        
        # Step 4: Right-click on the pinned location
        # First find the main map element
        map_element = wait.until(EC.presence_of_element_located((By.ID, "map")))
        
        # Find the pin (usually the first element with role="main")
        main_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[role='main']")))
        
        # Move to the main result area and right-click
        actions = ActionChains(driver)
        actions.move_to_element(main_result).context_click().perform()
        
        # Step 5: Click on "Nearby Search" option
        # The exact selector might vary depending on Google Maps UI
        time.sleep(2)  # Wait for context menu to appear
        nearby_search = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(text(), '付近を検索') or contains(text(), 'Search nearby')]")))
        nearby_search.click()
        
        # Step 6: Enter "B型事業所" in the search box
        search_box = wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))
        search_box.clear()
        search_box.send_keys("B型事業所")
        search_box.send_keys(Keys.ENTER)
        
        # Wait for results to load
        time.sleep(5)
        
        # Step 7: Remove the first line from the text file
        remove_first_line(file_path)
        
        # Goal achieved: displaying B型事業所 near the city hall
        print(f"Successfully searched for B型事業所 near {city_name} 市役所")
        
        # Keep the browser open for viewing results
        input("Press Enter to close the browser...")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
