import subprocess
import random
import os
import shutil
import urllib.request
import tarfile

def update_system():
    # Update system and set vm.nr_hugepages
    subprocess.run(['sudo', 'apt-get', 'update'])
    subprocess.run(['sudo', 'sysctl', '-w', 'vm.nr_hugepages=1280'])
    subprocess.run(['sudo', 'bash', '-c', 'echo vm.nr_hugepages=1280 >> /etc/sysctl.conf'])

def install_packages():
    # Install necessary packages
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'git', 'wget', 'screen'])

def setup_directories():
    # Set up directories
    work_dir = '/usr/share/work'
    subprocess.run(['sudo', 'mkdir', '-p', work_dir])  # Create directory under sudo
    return work_dir

def download_and_extract_xmrig(version, work_dir):
    # Download and extract xmrig
    tar_url = f'https://github.com/xmrig/xmrig/releases/download/v{version}/xmrig-{version}-linux-x64.tar.gz'
    tar_file = f'xmrig-{version}-linux-x64.tar.gz'
    download_path = os.path.join(work_dir, tar_file)

    urllib.request.urlretrieve(tar_url, download_path)

    with tarfile.open(download_path, 'r:gz') as tar:
        tar.extractall(path=work_dir)

    # Rename xmrig binary
    xmrig_dir = os.path.join(work_dir, f'xmrig-{version}')
    xmrig_path = os.path.join(xmrig_dir, 'xmrig')
    renamed_path = os.path.join(xmrig_dir, 'xmrig_renamed')  # Renaming to a visible name
    subprocess.run(['sudo', 'mv', xmrig_path, renamed_path])  # Move and rename under sudo
    return renamed_path

def start_xmrig(pool, username, work_dir, cpu_threads=None, gpu_enabled=True, gpu_type='auto'):
    # Start xmrig
    donate_level = 1
    algo = 'rx/0'
    xmrig_path = download_and_extract_xmrig('6.21.0', work_dir)

    cmd = [f'{xmrig_path}', '--donate-level', str(donate_level), '-o', pool, '-u', f'{username}.ws-p x', '-a', algo, '-k', '--tls']

    if cpu_threads is not None:
        cmd.extend(['--cpu', str(cpu_threads)])

    if gpu_enabled:
        if gpu_type == 'auto':
            cmd.append('--opencl')  # Use auto-detection for OpenCL
        elif gpu_type == 'cuda':
            cmd.append('--cuda')  # Use NVIDIA CUDA for GPU mining

    try:
        # Run xmrig and capture output
        result = subprocess.run(['sudo'] + cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("xmrig stdout:")
        print(result.stdout)
        print("xmrig stderr:")
        print(result.stderr)
    except Exception as e:
        print(f"Error running xmrig: {e}")

if __name__ == "__main__":
    update_system()
    install_packages()
    work_dir = setup_directories()
    
    pool = 'us-zephyr.miningocean.org:5432'
    username = 'ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB'
    
    start_xmrig(pool, username, work_dir, cpu_threads=None, gpu_enabled=True, gpu_type='auto')
