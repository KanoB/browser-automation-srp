import pytest

from webtester.main.GoogleMainPage import GoogleMainPage
from webtester.result.GoogleResultPage import GoogleResultPage

@pytest.mark.parametrize("keyword,index", [("passion fitness", 3), ])
def test_GoogleWorkflow(driver, keyword, index):

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
    
def test_basicSearch(driver):
    keyword = "natural born"
    main_page = GoogleMainPage(driver)
    main_page.go()

    assert main_page.getSearchWidget().isDisplayed(), "Search widget not found"

    main_page.getSearchWidget().enter(keyword)
    suggestions = main_page.getSearchSuggestions().getSuggestions()
    assert len(suggestions) > 0, "No search suggestions found"

    main_page.getSearchWidget().search(keyword)
    result_page = GoogleResultPage(driver)
    assert result_page.getResultStat().isDisplayed(), "Result page not visible"
    assert result_page.getResultStat().text, "No result stats"
    print("Results:", result_page.getResultStat().text)
