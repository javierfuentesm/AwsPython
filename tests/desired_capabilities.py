import os


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Sony',
        'platformVersion': '5.1.1',
        'autoAcceptAlerts': 'true',
        'noReset': 'true',
        'appPackage': 'com.globalhitss.claro.pay.uat',
        'appActivity': '.com.globalhitss.claro.pay.ui.activities.SplashScreen',
        #'app': '/Users/venkateshakula/Desktop/ios/sample-code-master/sample-code/apps/ContactManager/ContactManager.apk',

    }
    return desired_caps
