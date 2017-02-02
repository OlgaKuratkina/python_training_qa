class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_text_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_data(self, contact):
        wd = self.app.wd
        self.fill_text_field("firstname", contact.name)
        self.fill_text_field("middlename", contact.second_name)
        self.fill_text_field("lastname", contact.last_name)
        self.fill_text_field("nickname", contact.nickname)
        self.fill_text_field("title", contact.position)
        self.fill_text_field("company", contact.company)
        self.fill_text_field("address", contact.address)
        self.fill_text_field("home", contact.phone)
        self.fill_text_field("email", contact.email)

    def delete_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@title='Details']").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()



