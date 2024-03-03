import re
from html.parser import HTMLParser

def trying_to_parse_html_or_xml_using_regex():
    html = """
    <html>
    <body>
    <a href="https://mcoding.io">Great website</a>
    </body>
    </html>
    """

    links_regex = '<a href="(.*?)"'
    for match in re.finditer(links_regex, html):
        print(f"Found link: {match.group(1)}")

    class UrlParser(HTMLParser):
        def handle_starttag(self, tag: str, attrs):
            if tag != "a":
                return

            for attr, val in attrs:
                if attr == "href":
                    print(f"Found link: {val}")
                    break

    UrlParser().feed(html)
    # or use BeautifulSoup...