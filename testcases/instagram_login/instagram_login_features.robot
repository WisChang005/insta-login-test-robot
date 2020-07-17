*** Settings ***
Resource  instagram_login_keywords.robot

Test Setup       Setup Steps
Test Teardown    Teardown Steps


*** Test Cases ***

Login Instagram with Chrome Browser
    Given user use "chrome" browser to Instagram login page
    When user type correct Instagram username and password
    Then user will login successful


Login Instagram with Firefox Browser
    Given user use "firefox" browser to Instagram login page
    When user type correct Instagram username and password
    Then user will login successful


Redirect to Facebook Login Page
    Given user use "chrome" browser to Instagram login page
    When user click login with Facebook link
    Then check the page is "Facebook"


Login by Incorrect Username
    Given user use "chrome" browser to Instagram login page
    When user type incorrect Instagram "username"
    Then the login error "username" warning message will show up


Login by Incorrect Password
    Given user use "chrome" browser to Instagram login page
    When user type incorrect Instagram "password"
    Then the login error "password" warning message will show up





