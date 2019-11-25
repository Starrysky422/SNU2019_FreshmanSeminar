import os
import subprocess

path = '../FreshmanSeminar/AdjList'
path_export = '../FreshmanSeminar/Fractal'
for dirname in os.listdir(path):
	if dirname[0] == '.':
		continue
	path_spec = os.path.join(path, dirname)
	path_export_spec = os.path.join(path_export, dirname)
	for filename in os.listdir(path_spec):
		if filename.split('.')[1] != 'txt':
			continue
		filename_export = os.path.join(path_export_spec, filename)
		filename_spec = os.path.join(path_spec, filename)
		subprocess.call(['./bin/box_cover','-type=auto','-graph='+filename_spec,'-method=sketch','-random_seed=1124747'])
