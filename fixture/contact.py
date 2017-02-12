from model.contact import Contact


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
        self.contact_cache = None

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
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@title='Details']").click()
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//input[@name = 'selected[]']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for elem in wd.find_elements_by_name("entry"):
                last_name = elem.find_elements_by_css_selector("td")[1].text
                name = elem.find_elements_by_css_selector("td")[2].text
                id = elem.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, last_name=last_name, name=name))
        return self.contact_cache



