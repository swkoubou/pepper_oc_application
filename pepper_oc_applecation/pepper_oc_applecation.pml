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
    </Resources>
    <Topics>
        <Topic name="main_response_jpj" src="main_response/main_response_jpj.top" topicName="main_response" language="ja_JP" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="ja_JP">
        <Translation name="translation_ja_JP" src="translations/translation_ja_JP.ts" language="ja_JP" />
    </Translations>
</Package>
