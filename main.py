import argparse
import os
from cms_detector import detect_cms
from username_enum import enumerate_users_wordpress, enumerate_users_generic
from login_finder import find_login_portals
from report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="Custom Python OSINT Recon Tool")
    parser.add_argument("url", help="Target URL (e.g. https://example.com)")
    parser.add_argument("-o", "--output", default="output", help="Output directory for report (default: output/)")
    parser.add_argument("--no-report", action="store_true", help="Skip HTML report generation")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    url = args.url.rstrip("/")
    output_dir = args.output

    if args.verbose:
        print(f"[+] Target URL: {url}")
        print(f"[+] Output Directory: {output_dir}")
        print("[*] Starting CMS detection...")

    cms_info = detect_cms(url)

    if args.verbose:
        print(f"[+] CMS Detected: {cms_info['name']}")

    # Conditional username enumeration based on CMS
    if "wordpress" in cms_info["name"].lower():
        if args.verbose:
            print("[*] WordPress detected — using /?author=ID enumeration...")
        users = enumerate_users_wordpress(url)
    else:
        if args.verbose:
            print("[*] Non-WordPress CMS — using generic user scraping...")
        users = enumerate_users_generic(url)

    if args.verbose:
        print(f"[+] Usernames Found: {users}")

    # Export usernames to usernames.txt if valid ones are found
    os.makedirs(output_dir, exist_ok=True)
    if users and not all(u.startswith("Error") or u.startswith("(") for u in users):
        with open(os.path.join(output_dir, "usernames.txt"), "w") as f:
            for user in users:
                f.write(f"{user}\n")
        if args.verbose:
            print(f"[+] Usernames written to: {output_dir}/usernames.txt")

    # Find login portals
    login_pages = find_login_portals(url)
    if args.verbose:
        print(f"[+] Login Portals Found: {login_pages}")

    # Generate report unless --no-report
    if not args.no_report:
        if args.verbose:
            print("[*] Generating HTML report...")
        generate_report(url, cms_info, users, login_pages, output_dir)
        print(f"[+] Report saved to: {output_dir}/report.html")
    else:
        print("[*] Report generation skipped (--no-report)")

if __name__ == "__main__":
    main()
