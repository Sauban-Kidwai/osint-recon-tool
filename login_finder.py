import requests

def find_login_portals(url):
    common_paths = [
        # WordPress
        "/wp-login.php", "/wp-admin",

        # Joomla
        "/administrator", "/index.php?option=com_users&view=login",

        # Drupal
        "/user/login", "/user/1", "/admin",

        # Magento
        "/admin", "/index.php/admin", "/downloader",

        # Shopify
        "/account/login", "/admin",

        # Wix
        "/login", "/account/login", "/user/login",

        # Ghost
        "/ghost/#/signin", "/ghost/signin",

        # Textpattern
        "/textpattern/index.php", "/textpattern/login",

        # TYPO3
        "/typo3/", "/typo3/index.php", "/typo3/login",

        # BigCommerce
        "/manage", "/login",

        # Squarespace
        "/config", "/login",

        # Weebly
        "/user/login",

        # Catch-all generics
        "/signin", "/sign-in", "/log-in", "/auth", "/dashboard", "/backend", "/cpanel",
        "/admin.php", "/users/sign_in", "/site/login", "/members", "/member/login",
        "/vendors/login"
    ]

    found = []
    for path in common_paths:
        full_url = url.rstrip("/") + path
        try:
            r = requests.get(full_url, timeout=5, allow_redirects=True)
            if r.status_code in (200, 301, 302) and (
                "login" in r.text.lower() or
                "username" in r.text.lower() or
                "password" in r.text.lower() or
                "auth" in r.text.lower()
            ):
                found.append(full_url)
        except requests.RequestException:
            continue

    return list(set(found))
