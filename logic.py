from time import sleep
from selenium import webdriver
from random import randint


class MyInstaBot_login():

    links = []

    comments = [
        'very beautiful', 'very gorgeous', 'looks grate'
    ]

    #hashtag = ['luxlife', 'bugatti']

    accounts = [
        'charlidamelio', 'dixiedamelio,'
    ]
    #'🔥🔥🔥', 'beautiful 😍😍',
    def __init__(self):
        username = str(input("enter username: "))
        password = str(input("enter password: "))
        self.login(username, password)
        self.likes_comment_and_hashtag('luxlife')
        self.comment_on_account()

    def login(self, username, password):
        PATH = "C:\Program Files (x86)\\chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get('https://www.instagram.com')
        sleep(2)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def comment_on_account(self):
        for account in self.accounts:
            #go to profile page
            self.driver.get('https://www.instagram.com/{}/'.format(account))

            # get most resent photo
            links = self.driver.find_element_by_tag_name('a')
            def condition(link):
                return '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))
            last_photo_url = valid_links[0].get_attribute('href')
            self.driver.get(last_photo_url)

            # comment on photos
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            comment_this_bitch = self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            comment_this_bitch.send_keys(self.comments[randint(0,2)])
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()

    def likes_comment_and_hashtag(self, hashtage):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtage))
        links = self.driver.find_elements_by_tag_name('a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in self.links:
            self.driver.get(link)
            # like
            sleep(3)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click() # like btw
            sleep(5)

            # comments
            self.driver.find_element_by_class_name('RxpZH').click()
            sleep(1)
            comment_this_bitch = self.driver.find_element_by_xpath("//textarea[@aria-label='Add a comment…']")
            comment_this_bitch.send_keys(self.comments[randint(0,2)])
            sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()

class testerr():
    def tester_print():
        print("printed")

