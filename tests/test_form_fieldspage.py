from pages.page_locators.FormFieldsPage import FormFieldsPage
from pages.page_locators.BasePage import HomePage

def test_form_fields_page(driver, configure):
    driver.get(configure["base_url"])
    home_page = HomePage(driver)
    formfield_page = FormFieldsPage(driver)

    home_page.open_javascript_delays_page()
    formfield_page.click_start_timer_liftoff_btn()
    formfield_page.wait_for_liftoff()



