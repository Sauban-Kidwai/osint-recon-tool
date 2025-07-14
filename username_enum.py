import requests
import re
from bs4 import BeautifulSoup

def enumerate_users_wordpress(url):
    usernames = []
    try:
        for i in range(1, 11):
            test_url = f"{url}/?author={i}"
            response = requests.get(test_url, allow_redirects=True, timeout=5)

            # Try classic redirect technique
            match = re.search(r"/author/([^/]+)/", response.url)
            if match:
                username = match.group(1)
                if username.isnumeric():
                    continue
                if username not in usernames:
                    usernames.append(username)
                continue

            # If no redirect, parse <body> for class="author-USERNAME"
            soup = BeautifulSoup(response.text, "html.parser")
            body_tag = soup.find("body")
            if body_tag and "class" in body_tag.attrs:
                body_classes = body_tag["class"]
                for cls in body_classes:
                    if cls.startswith("author-") and not cls.startswith("author-id"):
                        username = cls.replace("author-", "")
                        if not username.isnumeric() and username not in usernames:
                            usernames.append(username)

    except Exception as e:
        usernames.append(f"Error: {str(e)}")

    return usernames




# Generic fallback user enumeration (scrapes visible names from HTML)
def enumerate_users_generic(url):
    usernames = set()
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")

        # Look for common author or comment patterns
        selectors = [
            {"tag": "span", "class": "author"},
            {"tag": "a", "class": "author"},
            {"tag": "div", "class": "username"},
            {"tag": "p", "class": "user"},
            {"tag": "a", "rel": "author"},
        ]

        for sel in selectors:
            elements = soup.find_all(sel.get("tag"), class_=sel.get("class")) if "class" in sel else soup.find_all(sel.get("tag"), rel=sel.get("rel"))
            for el in elements:
                text = el.get_text(strip=True)
                if text:
                    usernames.add(text)

        # Fallback: look for usernames in meta tags
        meta_users = re.findall(r'@([a-zA-Z0-9_]+)', response.text)
        for user in meta_users:
            usernames.add(user)

    except Exception as e:
        return [f"Error: {str(e)}"]

    return list(usernames) if usernames else ["(No usernames found)"]
