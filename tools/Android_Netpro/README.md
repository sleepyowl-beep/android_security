# Android Network Proxy
## Description:
A Python 3 script to automate proxy configuration in Android 8+(API 24 above) environment. Since android nougat, Android has change the way it provide security in application traffic so we cannot intecept its traffic by normally install proxy certification in device CAs(user-added). In order to do that we need:  
1. Decompile the apk file  
2. Add new configuration inside the AndroidManifest.xml file  
3. Add new network security configuration file inside the apk  
4. Recompile it  
5. Signed it in order to be installed in device or emulator  

## A LOT OF WORK, RIGHT?!  
  
Thus, I create this program to automate above step using apktool and uber-signer 

### Tested .apk:
          reddit(v.2.25.0)[link] (https://www.apkmirror.com/apk/redditinc/reddit/reddit-2-26-3-release/reddit-2-26-3-android-apk-download/)
