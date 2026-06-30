import os
import pytest
from selenium.webdriver import Chrome, ChromeOptions
from config.env import ConfigReader


@pytest.fixture(scope="session")
def setup_and_teardown():
    ## Read env and config file
    config = ConfigReader.read_config()
    env = config["qa"]
    base_url = env["base_url"]

    # Download folder inside project
    download_path = os.path.join(os.getcwd(), "downloads")

    # Create folder if it doesn't exist
    os.makedirs(download_path, exist_ok=True)

    # Chrome options
    o = ChromeOptions()

    o.add_experimental_option("detach", True)
    o.add_argument("--no-sandbox")
    o.add_argument("--disable-notifications")
    o.add_argument("--start-maximized")

    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }

    o.add_experimental_option("prefs", prefs)

    driver = Chrome(options=o)

    # Allow downloads in Chrome for Testing
    driver.execute_cdp_cmd(
        "Page.setDownloadBehavior",
        {
            "behavior": "allow",
            "downloadPath": download_path
        }
    )

    driver.implicitly_wait(10)
    driver.get(base_url)

    yield driver

    driver.quit()