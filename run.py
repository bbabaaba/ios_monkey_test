import os

cmd = "instruments -w 4394a67923a9f3b8a89ae424b461f8901258fe70 \
-t /Applications/Xcode.app/Contents/Applications/Instruments.app/Contents/PlugIns/AutomationInstrument.xrplugin/Contents/Resources/Automation.tracetemplate  com.ximalaya.iting \
-e UIASCRIPT /Users/nali/Git/ui-auto-monkey/UIAutoMonkey.js -e UIARESULTSPATH /Users/nali/Git/ui-auto-monkey/"

os.system(cmd)
