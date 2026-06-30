from config.env import ConfigReader
from pages.email_page import EmailPage
from time import sleep
import os
import glob

from pages.remove_watermark_page import RemoveWatermarkPage
from pages.video_edit_page import VideoEditPage


def test_email_creation(setup_and_teardown):
    driver = setup_and_teardown

    ep = EmailPage(driver)
    vep = VideoEditPage(driver)
    rwp = RemoveWatermarkPage(driver)

    upload_folder = os.path.join(os.getcwd(), "uploads")
    videos = glob.glob(os.path.join(upload_folder, "*.mp4"))
    if not videos:
        raise Exception("No MP4 video found inside uploads folder.")
    path = videos[0]

    print("Video Selected:", path)

    ep.click_change_email()
    # ep.click_change_email()
    sleep(5)
    # Wait until the email is generated
    while True:
        temp_email = ep.get_email_text()

        if temp_email != "Generating random email...":
            break

        sleep(2)

    print(temp_email)

    ep.click_refresh_button()

    ep.open_new_window()
    ep.latest_window()
    driver.get('https://www.media.io/ai/ai-tools/video-eraser')

    sleep(2)
    vep.click_login()
    vep.change_to_iframe()
    # vep.click_create_account()
    sleep(2)
    vep.enter_email(temp_email)
    vep.enter_password("12345qwer")
    vep.click_final_create_account_button()
    sleep(5)

    ep.switch_old_first_window()

    sleep(2)

    ep.close_banner_if_present()

    sleep(1)

    ep.click_refresh_button()
    sleep(2)
    ep.check_recent_email()
    digits = ep.get_verification_code()

    ep.latest_window()
    vep.change_to_iframe()
    sleep(2)
    vep.enter_verification_code(digits)
    vep.click_verify_code()
    vep.exit_iframe()
    sleep(5)

    # Close plan popup
    rwp.remove_plan_ads()

    # Select Basic Model
    rwp.select_model_for_watermark()
    sleep(1)

    # Scroll to upload section
    rwp.scroll_to_upload()

    # Upload video
    rwp.upload_video(path)
    sleep(10)

    # Select hand tool
    rwp.click_hand_sign()
    sleep(1)

    # Zoom in twice
    rwp.click_zoom_button()
    sleep(1)

    rwp.click_zoom_button()
    sleep(1)

    # Drag image upward
    rwp.drag_image_upward()
    sleep(5)

    # Re-select hand tool
    rwp.click_hand_sign()
    sleep(1)

    # Mark the watermark area
    rwp.click_first_point()

    rwp.click_second_point()
    sleep(10)

    rwp.click_generate_button()

    rwp.scroll_to_edit()

    print("Waiting for video generation...")

    # Wait until Video Eraser text appears
    rwp.wait_for_video_eraser()

    # Give Media.io a few more seconds
    sleep(10)

    # Click download
    rwp.click_download_button()

    print("Download started")

    sleep(10)