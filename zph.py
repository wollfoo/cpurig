import subprocess
import os
import requests
import tempfile
import tarfile
import shutil

def install_xmrig():
    # Tạo thư mục tạm để giải nén xmrig
    temp_dir = tempfile.mkdtemp()
    xmrig_path = os.path.join(temp_dir, "xmrig")

    try:
        # Tải xuống và giải nén xmrig từ kho lưu trữ GitHub chính thức
        url = "https://github.com/xmrig/xmrig/releases/latest/download/xmrig-linux-x64.tar.gz"
        response = requests.get(url)
        tar_filename = os.path.join(temp_dir, "xmrig.tar.gz")

        with open(tar_filename, "wb") as f:
            f.write(response.content)

        with tarfile.open(tar_filename, "r:gz") as tar:
            tar.extractall(path=temp_dir)

        # Di chuyển xmrig đến thư mục hiện tại
        shutil.move(os.path.join(temp_dir, "xmrig"), xmrig_path)

    except Exception as e:
        print(f"Lỗi khi tải xuống và cài đặt xmrig: {e}")
        return None

    finally:
        # Xóa thư mục tạm sau khi cài đặt
        shutil.rmtree(temp_dir)

    return xmrig_path

def start_mining():
    # Cài đặt xmrig nếu chưa có
    xmrig_path = install_xmrig()
    if not xmrig_path:
        print("Không thể cài đặt xmrig. Vui lòng kiểm tra lại.")
        return

    # Cấu hình đào coin Zephyr trên CPU và GPU với Mining Ocean
    command = [
        xmrig_path,
        "--algo=zephyr",
        "--url=stratum+tcp://zephyr.miningocean.org:6666",  # Thay thế bằng địa chỉ và cổng của Mining Ocean
        "--user=your_wallet_address",  # Thay thế bằng địa chỉ ví của bạn trên Mining Ocean
        "--pass=your_password",  # Thay thế bằng mật khẩu (nếu có)
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
