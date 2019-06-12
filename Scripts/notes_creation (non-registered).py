import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def creating_notes(number_of_notes=1) -> int:
    """
    creates notes in the online notepad "aNotepad"
    at the number passed as an argument.
    Mode: non-registered user
    """
    driver = webdriver.Chrome('G:\\Selenium\\chromedriver.exe')
    driver.maximize_window()
    driver.get('https://anotepad.com/')
    counter = 0

    # a path to a folder storing notes. Rewrite if neccessary
    notes = os.listdir('G:\\Selenium\\Test_Notes')    

    assert 0 < number_of_notes <= len(notes), "The number of notes expected: from 1(min) to %s(max)" %(len(notes))
    
    for file in notes[:number_of_notes]:
        with open("G:\\Selenium\\Test_Notes\\" + file) as note:                
            driver.find_element_by_id('edit_title').send_keys(file[:-4])
            driver.find_element_by_id('edit_textarea').send_keys(note.read())
            driver.find_element_by_id('btnSaveNote').click()
            counter += 1
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Add New Note')))
            driver.find_element_by_link_text('Add New Note').click()

    num_dif = "note was" if counter == 1 else "notes were"
    print("%s %s successfully added" %(counter, num_dif))

    #driver.quit()

creating_notes(6)





