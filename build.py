import os, sys, multiprocessing, subprocess

def exec_command_line(content):
	p = subprocess.Popen(content, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		str_line = line.decode("utf-8")
		sys.stdout.write("	" + line)

try:
	import build_cfg
except:
	print("Generating build_cfg.py ...")
	import shutil
	shutil.copyfile("build_cfg_default.py", "build_cfg.py")
	import build_cfg

print("Starting build project: " + build_cfg.project_name + " ...")
print("Downloading dependents ...")

if not os.path.isdir(build_cfg.dependent_path):
	print("Making directory: " + build_cfg.dependent_path + " ...")
	os.makedirs(build_cfg.dependent_path)

curdir = os.path.abspath(os.curdir)

for dependent in build_cfg.dependent_list:
	if os.path.isdir(build_cfg.dependent_path + "/" + dependent[0]):
		os.chdir(curdir + "/" + build_cfg.dependent_path + "/" + dependent[0])
		print("pull " + dependent[0] + ":")
		exec_command_line("git pull")
	else:
		os.chdir(curdir + "/" + build_cfg.dependent_path)
		print("clone " + dependent[0] + ":")
		exec_command_line("git clone " + dependent[1] + " " + dependent[0])
	os.chdir(curdir)

