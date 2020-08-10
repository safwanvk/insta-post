from selenium import webdriver
from config import USERNAME, PASSWORD
import time

users = ['cristiano', 'dqsalmaan']

browser = webdriver.Chrome(executable_path='/home/safwan/chromedriver_linux64/chromedriver')

browser.maximize_window()
browser.get('https://www.instagram.com')

time.sleep(2)

username = browser.find_element_by_name('username')
username.send_keys(USERNAME)

password = browser.find_element_by_name('password')
password.send_keys(PASSWORD)

login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(5)

for user in users:
    browser.get(f"https://www.instagram.com/{user}/")

    time.sleep(2)

    number_of_posts, followers, following = browser.find_elements_by_css_selector(
        '.g47SY')
    print('Number of Posts:', number_of_posts.text, 'Followers:', followers.text, 'Following:', following.text)
    

    bio = browser.find_element_by_css_selector(
        '.-vDIg')
    print('Bio:', bio.text, sep='\n')

    with open(f"{user}.txt", "w") as file:
        file.write(
            f"Number of Posts: {number_of_posts.text}\nFollowers: {followers.text}\nFollowing: {following.text}\n\nBio:\n{bio.text}")

    time.sleep(1)
