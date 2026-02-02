def test_homepage_title(homepage):
    assert homepage.get_title() == "Example Domain"


def test_homepage_heading_text(homepage):
    assert homepage.get_heading_text() == "Example Domain"


def test_more_information_link_is_visible(homepage):
    assert homepage.more_info_link_is_visible()


def test_more_information_link_navigation(homepage):
    homepage.click_more_info()
    assert "iana.org" in homepage.driver.current_url
