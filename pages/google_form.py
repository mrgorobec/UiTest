from pages.basic_page import BasicPage


class GoogleForm(BasicPage):
    """Google form page contains page elements locator """

    def google_email_field(self):
        return self.driver.find_element_by_xpath('//input[@type = "email"]')

    def email_exception_field(self):
        return self.driver.find_element_by_xpath('//div[@role="alert"][1]')

    def day_field(self):
        return self.driver.find_element_by_xpath('//div[contains(@class,'
                                                 ' "quantumWizTextinputPaperinputInputArea")]/input[@type="date"]')

    def date_exception_field(self):
        return self.driver.find_element_by_xpath('//*[@id="i.err.1236342938"]')
