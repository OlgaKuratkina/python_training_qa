class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        # init new group
        self.app.goto_groups_page()
        wd.find_element_by_xpath("//input[@name='new' and @value='New group']").click()
        # fill input fields
        self.fill_group_info(group)
        # submit
        wd.find_element_by_name("submit").click()
        self.app.goto_groups_page()

    def fill_group_info(self, group):
        wd = self.app.wd
        self.fill_text_field("group_name", group.name)
        self.fill_text_field("group_header", group.header)
        self.fill_text_field("group_footer", group.footer)

    def fill_text_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.app.goto_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.app.goto_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@name = 'selected[]' or @value = '32']").click()

    def modify_group(self, group):
        wd = self.app.wd
        self.app.goto_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_info(group)
        wd.find_element_by_name("update").click()
        self.app.goto_groups_page()
