from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = False          # Reserves the driver session even after the function is dead.


def webscraper(search_query, platform_name="youtube"):
    
    new_window = False                   # This is an indicator within the function to signal whether to use any pre-existing windows or create new.
    

    def Create_driver_session():          # This function will create a new session.
        global driver
        nonlocal new_window

        edge_options = Options()
        edge_options.add_experimental_option("detach", True)
        driver = Edge("edgedriver_win64\msedgedriver.exe", options=edge_options)
        new_window = True       


    if driver == False:            # If there is no existing session , then call the above function.
        Create_driver_session()

    platform_url = {"youtube":["https://www.youtube.com/results?search_query=", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button"],
    "zee5": ["https://www.zee5.com/search?q=", "/html/body/div[1]/div/div/div[2]/div[3]/div/div[4]/div/div/div[1]/div/div/div[1]/div/h3/a", ""],
    "hotstar":["https://www.hotstar.com/in/search?q=", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div/div/article/a/div[2]/div[2]", "/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div/a/article/div[1]/div/img"]}

    
    for platform in platform_url.keys():
        if platform == platform_name:
            complete_search = platform_url[platform_name][0] + search_query.replace(" ", "%20")
            if new_window:
                driver.get(complete_search)

            else:
                try:
                    driver.execute_script(f'window.open("{complete_search}");')
                    driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1])
                except:
                    Create_driver_session()       
                    driver.get(complete_search)

            for i in range(1, len(platform_url[platform_name])-1):
                try:
                    clicker = ActionChains(driver=driver)
                    element = WebDriverWait(driver, 10).until(presence_of_element_located((By.XPATH, platform_url[platform_name][i])))
                    clicker.click(element)
                    clicker.perform()
                except: 
                    pass
            break

