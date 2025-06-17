from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

# 🔍 30 two-word search terms
search_terms = [
    "bamboo furniture", "crystal pendant", "organic farming", "lunar eclipse", "cyber ethics",
    "desert safari", "time capsule", "forest therapy", "vintage cameras", "cloud painting",
    "marble sculpture", "hidden waterfalls", "paper origami", "stone temple", "abstract thoughts",
    "ice hotels", "coral reefs", "nature reserves", "green architecture", "retro gadgets",
    "global cuisine", "silent retreat", "neon lights", "street musicians", "arctic wildlife",
    "mythical beasts", "ancient maps", "wind energy", "bubble tea", "fire dancers"
]

# 🛠 WebDriver path setup
driver_path = "msedgedriver.exe"
if not os.path.exists(driver_path):
    print("❌ 'msedgedriver.exe' not found! Please place it in the same folder.")
    exit()

# 🔧 Edge options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

# 🚗 Launch browser
service = Service(executable_path=driver_path)
driver = webdriver.Edge(service=service, options=options)

# 🔁 Perform searches
for term in search_terms:
    driver.get("https://www.bing.com")
    time.sleep(2)

    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(term)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        for _ in range(3):
            driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")

driver.quit()
print("✅ All searches completed.")