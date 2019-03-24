<?xml version="1.0" encoding="UTF-8" ?>
<Package name="pepper_oc_applecation" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="main_response" src="main_response/main_response.dlg" />
    </Dialogs>
    <Resources>
        <File name="golia" src="html/images/gorilla.png" />
        <File name="clock" src="icons/clock.png" />
        <File name="gorila" src="icons/gorilla.png" />
        <File name="welcome_new" src="html/images/welcome_new.png" />
        <File name="under_construction" src="html/images/under_construction.png" />
        <File name="scanar" src="icons/scanar.png" />
        <File name="QRCode" src="html/debugMode/img/QRCode.png" />
        <File name="pepper" src="html/debugMode/img/pepper.png" />
        <File name="welcome_new" src="html/debugMode/img/welcome_new.png" />
        <File name="index" src="html/debugMode/index.html" />
        <File name="jquery.min" src="html/debugMode/libs/qimessaging/1.0/jquery.min.js" />
        <File name="qimessaging" src="html/debugMode/libs/qimessaging/1.0/qimessaging.js" />
        <File name="socket.io.min" src="html/debugMode/libs/qimessaging/1.0/socket.io.min.js" />
        <File name="main" src="html/debugMode/scripts/main.js" />
        <File name="mode" src="html/debugMode/scripts/mode.js" />
        <File name="speak" src="html/debugMode/scripts/speak.js" />
        <File name="main" src="html/debugMode/styles/main.css" />
    </Resources>
    <Topics>
        <Topic name="main_response_jpj" src="main_response/main_response_jpj.top" topicName="main_response" language="ja_JP" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="ja_JP">
        <Translation name="translation_ja_JP" src="translations/translation_ja_JP.ts" language="ja_JP" />
    </Translations>
</Package>
