from web_scraper import __version__
from web_scraper.web_scrapper import get_citations_needed_report,get_citations_needed_count

def test_version():
    assert __version__ == '0.1.0'

def test_count_works_correctly():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    assert get_citations_needed_count(url) == 5

def test_report_works():
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual =get_citations_needed_report(url)
    assert actual[0]=={'Citation number': 1, 'Paragraph': 'The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.'}
