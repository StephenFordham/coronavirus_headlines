from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# headless implementation has not been added via Options class

class CoronaVirusHeadlines(object):
	def __init__(self):
		headless_options = Options()
		headless_options.add_argument('--headless')

		self._driver = webdriver.Chrome(options=headless_options)

	def get_headlines(self):

		self._driver.get('https://www.bbc.co.uk/news')

		search_box = self._driver.find_element_by_css_selector('input[id="orb-search-q"]')

		ActionChains(self._driver).move_to_element(search_box).click() \
			.send_keys('Global coronavirus updates').key_down(Keys.ENTER).perform()

		top_titles = self._driver.find_elements_by_css_selector('div[class="css-14rwwjy-Promo ett16tt11"]')

		with open('Coronavirus_headlines.txt', 'w') as cor_virus:
			for title in top_titles:
				headline = title.find_element_by_css_selector('p[class="css-1aofmbn-PromoHeadline ett16tt4"]').text
				cor_virus.write(headline)
				cor_virus.write('\n')

		self._driver.quit()


virus_data = CoronaVirusHeadlines()
virus_data.get_headlines()

