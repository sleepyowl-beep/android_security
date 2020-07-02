import os
import magic
import logging
import sys
import xml.etree.ElementTree as ET
import shutil

APKTOOL_PATH = "/usr/local/bin/apktool"
UBERSIGNER_JAR = "./uber-apk-signer-1.1.0.jar"
JAVA_PATH = "/usr/bin/java" #originally I used Java 1.8.0_201
logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.INFO)

def signing_new_apk(apk_file_path):
	global UBERSIGNER_JAR
	global JAVA_PATH

	new_file_signed_apk = os.path.splitext(apk_file_path)[0] + "_signed"
	command = "{} -jar {} -a {} --out {}".format(JAVA_PATH, UBERSIGNER_JAR, apk_file_path, new_file_signed_apk)
	logging.info(command)
	os.system(command)
	if os.system(command) != 0:
		logging.info("Something is wrong with the uber-apk-signer make sure you put the correct path in this program")
		sys.exit(1)
	else:
		logging.info("Generate new signed apk file {}".format(new_file_signed_apk))
		logging.info("All set! you can install it to your device or emulator :)")


def check_file_apk(apk_file_path):
	filetype = magic.from_file(apk_file_path,mime=True)
	if filetype == "application/zip":
		return True
	else:
		return False

def decompile_to_smali(apk_file_path):
	global APKTOOL_PATH
	logging.info("Decompile apk file")
	dir_output = "./" + os.path.basename(apk_file_path) + "_smali"
	command = "{} d {} -o {}".format(APKTOOL_PATH, apk_file_path, dir_output)
	logging.info(command)
	if os.system(command) != 0:
		logging.info("Something is wrong with the apktool make sure you put the correct path in this program")
		sys.exit(1)
	else:
		return dir_output

def rebuild_to_apk(dir_output):
	global APKTOOL_PATH
	logging.info("Decompile apk file")
	file_output = "./" + os.path.basename(dir_output) + "_new.apk"
	command = "{} b {} -o {}".format(APKTOOL_PATH, dir_output, file_output)
	logging.info(command)
	os.system(command)
	if os.system(command) != 0:
		logging.info("Something is wrong with the apktool make sure you put the correct path in this program")
		sys.exit(1)
	else:
		logging.info("Generate new apk file {}".format(file_output))
		return file_output

def copied_configuration_file(dir_output):
	xml_folder = "res/xml/"
	network_security_config_file = "./network_security_config.xml"
	path_config_file = os.path.join(dir_output,xml_folder)

	if os.path.isfile(network_security_config_file):
		if os.path.isdir(path_config_file):
			logging.info("copied the network_security_config.xml file to the app")
			shutil.copy(network_security_config_file,path_config_file)
		else:
			logging.info("I couldn't find the /res/xml directory, try it again please")
	else:
		logging.info("I couldn't find the network_security_config.xml file, try it again please :)")

def edit_manifest_xml(dir_output):
	#'{http://schemas.android.com/apk/res/android}networkSecurityConfig': '@xml/network_security_config'
	ET.register_namespace("android", "http://schemas.android.com/apk/res/android")
	filename = "AndroidManifest.xml"
	logging.info("Result is stored in {}".format(dir_output))
	path_manifest = os.path.join(dir_output,filename)
	if os.path.isfile(path_manifest):
		logging.info("Manifest file:{}".format(path_manifest))
		xml_file = ET.parse(path_manifest)
		root = xml_file.getroot()
		application_tag = root.find("application").attrib
		application_tag['{http://schemas.android.com/apk/res/android}networkSecurityConfig'] = '@xml/network_security_config'
		xml_file.write(path_manifest)	
		logging.info("Edit the AndroidManifest.xml file")		
	else:
		logging.info("I couldn't find the manifest file, try it again please :)")	
		sys.exit(1)

def main():
	print("##############################################################################")
	print("                    _           _     _        _   _      _   _____           ")
	print("    /\             | |         (_)   | |      | \ | |    | | |  __ \          ")
	print("   /  \   _ __   __| |_ __ ___  _  __| |______|  \| | ___| |_| |__) | __ ___  ")
	print("  / /\ \ | '_ \ / _` | '__/ _ \| |/ _` |______| . ` |/ _ \ __|  ___/ '__/ _ \ ")
	print(" / ____ \| | | | (_| | | | (_) | | (_| |      | |\  |  __/ |_| |   | | | (_) |")
	print("/_/    \_\_| |_|\__,_|_|  \___/|_|\__,_|      |_| \_|\___|\__|_|   |_|  \___/ ")
	print("")
	print("by sleepyowl")
	print("##############################################################################")
	if len(sys.argv) == 2:
		logging.info('apk file: {}'.format(sys.argv[1]))
		apk_file_path = sys.argv[1]	
		if os.path.isfile(apk_file_path):	
			if check_file_apk(apk_file_path):
				output = decompile_to_smali(apk_file_path)
				#output="reddit.apk_smali"
				edit_manifest_xml(output)
				copied_configuration_file(output)
				file_apk_new = rebuild_to_apk(output)
				signing_new_apk(file_apk_new)
			else:
				logging.info('Please provide an apk file')
		else:
			logging.info('File is not exist')
	else:
		logging.info('Usage: python android_netpro.py [apkfile]')

main()
