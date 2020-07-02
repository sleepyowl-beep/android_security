# Android Network Proxy
## Description:
A Python 3 script to automate proxy configuration in Android 8+(API 24 above) environment. Since android nougat, Android has change the way it provide security in application traffic so we cannot intecept its traffic by normally install proxy certification in device CAs(user-added) and redirect the traffic to our proxy device. In order to do that we need to do this additional steps:  
1. Decompile the apk file  
2. Add new configuration inside the AndroidManifest.xml file  
3. Add new network security configuration file inside the apk  
4. Recompile it  
5. Signed it in order to be installed in device or emulator  

## A LOT OF WORK, RIGHT?!    
Thus, I create this program to automate above step using apktool and uber-signer  
More Details can be checked at: [Blogpost](https://android-developers.googleblog.com/2016/07/changes-to-trusted-certificate.html)

## Prerequisite
1. Install python-magic library: pip3 install python-magic  
2. Make sure you have python version 3
3. Make sure that apktool is installed in your machine, you can follow this step to do this: [Install](https://ibotpeaches.github.io/Apktool/install/)
4. Make sure you install Java in your machine, Originally when I created this script I used Java 1.8.0_201
5. Once you install above tools, check the absolute path, by typing: which apktool & which java
6. The result of the command will be put inside the program source code  

APKTOOL_PATH = "/usr/local/bin/apktool"  
UBERSIGNER_JAR = "./uber-apk-signer-1.1.0.jar"  
JAVA_PATH = "/usr/bin/java"  

## How to use it?
~# python3 android_netpro.py apkfile.apk  

## Tested .apk:
  reddit(v.2.25.0) [link](https://www.apkmirror.com/apk/redditinc/reddit/reddit-2-26-3-release/reddit-2-26-3-android-apk-download/)
