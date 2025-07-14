import subprocess
import re

def detect_cms(url):
    try:
        result = subprocess.run(
            ["whatweb", "--user-agent", "Mozilla/5.0", url],
            capture_output=True,
            text=True,
            timeout=50
        )
        output = result.stdout

        # Remove ANSI escape sequences (color codes)
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        cleaned_output = ansi_escape.sub('', output)

        # Extract CMS name and version if available
        cms_match = re.search(r'WordPress\[(.*?)\]', cleaned_output)
        if cms_match:
            return {"name": f"WordPress {cms_match.group(1)}"}

        drupal_match = re.search(r'Drupal\[(.*?)\]', cleaned_output)
        if drupal_match:
            return {"name": f"Drupal {drupal_match.group(1)}"}

        joomla_match = re.search(r'Joomla\[(.*?)\]', cleaned_output)
        if joomla_match:
            return {"name": f"Joomla {joomla_match.group(1)}"}

        if "WordPress" in cleaned_output:
            return {"name": "WordPress (unknown version)"}
        elif "Drupal" in cleaned_output:
            return {"name": "Drupal (unknown version)"}
        elif "Joomla" in cleaned_output:
            return {"name": "Joomla (unknown version)"}
        elif cleaned_output.strip():
            return {"name": "Other CMS"}
        else:
            return {"name": "Unknown"}

    except subprocess.TimeoutExpired:
        return {"name": "Error", "detail": "Timeout from whatweb"}
    except Exception as e:
        return {"name": "Error", "detail": str(e)}
