from model.contact import Contact
import re


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

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(contact, 0)

    def modify_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        self.fill_contact_data(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

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
                cells = elem.find_elements_by_css_selector("td")
                last_name = cells[1].text
                name = cells[2].text
                address = cells[3].text
                id = elem.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(id=id, last_name=last_name, name=name, address=address,
                                                  all_phones_from_home_page=all_phones, all_mails_from_home_page=all_mails))
        return self.contact_cache

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        phone = wd.find_element_by_name("home").get_attribute("value")
        phone_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        phone_work = wd.find_element_by_name("work").get_attribute("value")
        phone_second = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email_second = wd.find_element_by_name("email2").get_attribute("value")
        email_third = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name=name, last_name=last_name, id=id, phone=phone, phone_mobile=phone_mobile, address=address,
                       phone_work=phone_work, phone_second=phone_second, email=email, email_second=email_second,
                       email_third=email_third)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        phone = re.search("H: (.*)", text).group(1)
        phone_mobile = re.search("M: (.*)", text).group(1)
        phone_work = re.search("W: (.*)", text).group(1)
        phone_second = re.search("P: (.*)", text).group(1)
        return Contact(phone=phone, phone_mobile=phone_mobile, phone_work=phone_work, phone_second=phone_second)

    def get_contact_body_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        return text

# consider deleting this
    @staticmethod
    def clear(s):
        return re.sub("[() -]]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.phone, contact.phone_mobile, contact.phone_work,
                                            contact.phone_second]))))

    def merge_phones_like_on_view_page(self, contact):
        contact.phone = "H: " + contact.phone
        contact.phone_mobile = "M: " + contact.phone_mobile
        contact.phone_work = "W: " + contact.phone_work
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.phone, contact.phone_mobile, contact.phone_work]))))

    def merge_mails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email_second, contact.email_third]))))
