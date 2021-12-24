from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(r'user-data-dir=C:\Users\vynic\AppData\Local\Google\Chrome\User Data\Default')
        self.chrome = webdriver.Chrome(self.driver_path,options=self.options)

    def clica_sign_in(self):
        try:
            btn_sign = self.chrome.find_element_by_link_text('Sign in')
            btn_sign.click()
        except Exception as e:
            print('Erro ao clicar em sign in: ',e)

    def acessa(self, site):
        self.chrome.get(site)


    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login_field')
            input_password =self.chrome.find_element_by_id('password')
            bnt_sign_in = self.chrome.find_element_by_name('commit')
            input_login.send_keys('VyniciusMartorano')
            input_password.send_keys('Felipebia132')

            bnt_sign_in.click()
        except Exception as e:
            print('Erro ao fazer login: ', e)

    def clica_perfil(self):
        bnt_perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
        bnt_perfil.click()

    def deslogar(self):
        bnt_log_out = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
        bnt_log_out.click()




if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clica_sign_in()
    sleep(3)
    chrome.faz_login()
    sleep(3)
    chrome.clica_perfil()
    sleep(5)
    chrome.deslogar()
    sleep(3)
    chrome.sair()
