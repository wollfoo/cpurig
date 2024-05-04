import subprocess
import os

# Cài đặt Xmrig (phiên bản mới nhất)
subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "install", "xmrig"])

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
