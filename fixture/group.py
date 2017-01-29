class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create_group(self, group):
        wd = self.app.wd
        # init new group
        self.app.goto_groups_page()
        wd.find_element_by_xpath("//input[@name='new' and @value='New group']").click()
        # fill input fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit
        wd.find_element_by_name("submit").click()
        self.app.goto_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.goto_groups_page()
        wd.find_element_by_xpath("//input[@name = 'selected[]' or @value = '32']").click()
        wd.find_element_by_name("delete").click()
        self.app.goto_groups_page()