# Android Network Proxy
## Description:
A Python 3 script to automate proxy configuration in Android 8+(API 24 above) environment.  
Since android nougat, Android has change the way it provide security in application traffic  
so we cannot intecept its traffic by normally install proxy certification in device CAs(user-added)  
In order to do that we need to decompile the apk file to add new configuration inside the AndroidManifest.xml file 
and next we need to recompile it and signed it in order to be installed in device or emulator  

### Tested .apk:
          reddit(v.2.25.0)[link] (https://www.apkmirror.com/apk/redditinc/reddit/reddit-2-26-3-release/reddit-2-26-3-android-apk-download/)
