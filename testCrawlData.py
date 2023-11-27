from bs4 import BeautifulSoup
# requests để lấy info page riêng lẻ
import requests
# thư viện để xuất ra file
import io

# Get content web với input ng dùng nhập
class WebScraper:
    def __init__(self, url):
        self.url = url
        response = requests.get(url)
        self.soup = BeautifulSoup(response.content, "html.parser")

    def get_tags(self, tag_names):
        tags = []
        for tag_name in tag_names:
            tags.extend(self.soup.select(tag_name))
        return tags


def main():
    # Nhập URL từ người dùng
    url = input("Nhập URL: ")

    # Tạo đối tượng WebScraper
    scraper = WebScraper(url)

    # Lấy tất cả các thẻ h1 tới h6
    tags = scraper.get_tags(["h1", "h2", "h3", "h4", "h5", "h6"])

    # Tạo file html
    file = io.open("testGetTags.html", mode="w", encoding="utf8")

    # Ghi dữ liệu vào file html
    file.writelines([f"<{tag.name}>{tag.text}</{tag.name}>\n" for tag in tags])

    file.close()

if __name__ == "__main__":
    main()

