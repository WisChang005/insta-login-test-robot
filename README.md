# Instagram Login Test
Instagram login UI test, only support on Windows and I choice the `Robot framework` to run the tests.


## Requirements

1. cd to the project
2. set the environment variable `CONFIG_FILE=config.yaml` and `PYTHONPATH` to the project
>> if you use `git-bash.exe` or `cmder.exe` terminal, you just need to source the env_script.sh
```bash
source env_script.sh
```
3. run the following command
```bash
pip install -r requirements.txt
```
4. Download the `chromedriver.exe` (Chrome) and `geckodriver.exe` (Firefox) into path `project/insta_utils/browser_drivers/*`


## Config Settings

Please modify the `config.yaml` to setup the Instagram username, password and firefox binary path
* Examples
```yaml
instagram_user: my_user@gmail.com
instagram_pwd: my_password
firefox_binary: C:\Program Files\Mozilla Firefox\firefox.exe
```


## Run test

```bash
robot testcases/instagram_login/instagram_login_features.robot
```

## Test Report
The test report will generated in the project path `log.html`, `report.html` and `output.xml`
