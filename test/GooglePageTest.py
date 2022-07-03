import pytest

from webtester.GooglePages import GoogleMainPage 

def test_GoogleWorkflow(driver):
    keyword = "passion fitness"
    index = 3

    google_main_page = GoogleMainPage(driver)
    google_main_page.go()
    assert "Google" in driver.title

    google_main_page.getSearchWidget().enter(keyword)
    suggestions = google_main_page.getSearchSuggestions().text()
    for ln in suggestions:
        print(ln)

    assert len(suggestions) > 2, "No suggestions found"
    
