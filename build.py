import os, sys, multiprocessing, subprocess
import build_cfg

print("Starting build project: " + build_cfg.project_name + " ...")
print("Downloading dependents ...")

if not os.path.isdir(build_cfg.dependent_path):
	print("Making directory: " + build_cfg.dependent_path + " ...")
	os.makedirs(build_cfg.dependent_path)

print(build_cfg.dependent_list)