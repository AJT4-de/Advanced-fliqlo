import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

html_path = "file:///" + os.path.abspath("index.html").replace("\\", "/")

options = webdriver.ChromeOptions()
options.add_argument('--headless')

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(html_path)
    
    print("Page Loaded. Capturing initialization logs:")
    logs = driver.get_log("browser")
    for log in logs:
        print(log)
        
    print("\nOpening settings panel via DOM click...")
    # Just directly interact with the DOM via JS to avoid simulation bugs
    
    print("Finding triggers...")
    script = """
        console.log("Checking triggers:");
        let selects = document.querySelectorAll('.custom-select-container');
        return selects.length;
    """
    length = driver.execute_script(script)
    print(f"Found Custom Select Containers: {length}")
    
    script2 = """
        let trigger = document.querySelector('.custom-select-trigger');
        if (!trigger) return 'No trigger found';
        trigger.click();
        return 'Trigger clicked';
    """
    res = driver.execute_script(script2)
    print(res)
    time.sleep(0.5)

    script3 = """
        let opt = document.querySelector('.custom-select-option:nth-child(2)');
        if (!opt) return 'No option found';
        opt.click();
        return 'Option clicked: ' + opt.innerText;
    """
    res2 = driver.execute_script(script3)
    print(res2)
    time.sleep(0.5)

    val = driver.execute_script("return document.querySelector('select').value;")
    print(f"First select value is now: {val}")
    
    logs = driver.get_log("browser")
    for log in logs:
        print(log)
        
    driver.quit()
except Exception as e:
    print("Exception during test:", e)
