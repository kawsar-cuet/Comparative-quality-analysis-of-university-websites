
def text_extaction(webdriver,links):
    
    with webdriver as driver:
        # Set timeout time 
        # retrive url in headless browser
        for l in links:
            print(l)
            wait = WebDriverWait(driver, 10)
            driver.get(l)
            nxt_lnks = driver.find_elements_by_tag_name('a')
        
            for ln in nxt_lnks:
                links.add(ln)

        driver.close()