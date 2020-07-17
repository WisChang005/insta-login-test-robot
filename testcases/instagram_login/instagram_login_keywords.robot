*** Settings ***
Library  instagram_login_steps.py
Library  insta_utils.robot_data.RobotDataStore


*** Keywords ***

Setup Steps
    Set Log Level                         Trace

Teardown Steps
    close_instagram_login_page
    del_all_vars


user use "${browser_type}" browser to Instagram login page
    setup_instagram_login_page  ${browser_type}
    get_instagram_login_page


user type correct Instagram username and password
    type_correct_login_info
    click_login_button


user will login successful
    check_login_succeed


user click login with Facebook link
    click_login_with_fb


check the page is "${exp_title}"
    check_page_title  ${exp_title}


user type incorrect Instagram "${incorrect_field}"
    type_incorrect_login_info  ${incorrect_field}
    click_login_button


the login error "${incorrect_field}" warning message will show up
    check_login_error_alert_msg  ${incorrect_field}
