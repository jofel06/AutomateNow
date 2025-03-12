from pages.page_locators.BasePage import HomePage


def test_homepage(driver, configure):
    driver.get(configure["base_url"])
    home_page = HomePage(driver)

    home_page.open_javascript_delays_page()
    home_page.click_homepage_icon()
    home_page.open_form_fields_page()
    home_page.click_homepage_icon()
    home_page.open_popups_link_page()
    home_page.click_homepage_icon()
