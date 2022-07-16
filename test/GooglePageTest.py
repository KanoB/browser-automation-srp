import pytest

from webtester.GooglePages import GoogleMainPage 

#@pytest.mark.parametrize("keyword,index", [("passion fitness", 3), ("robot", 6), ("lizzard", 8)])
def test_GoogleWorkflow(driver, keyword="robot", index=3):

    google_main_page = GoogleMainPage(driver)
    google_main_page.go()
    assert "Google" in driver.title

    google_main_page.getSearchWidget().enter(keyword)
    suggestions = google_main_page.getSearchSuggestions().text()
    print("Suggestions found")
    for idx, ln in enumerate(suggestions, start=1):
        if idx == index:
            print(f"\t- '{ln}'", "*")
        else:
            print(f"\t- '{ln}'")

    assert len(suggestions) > 2, "No suggestions found"
    
