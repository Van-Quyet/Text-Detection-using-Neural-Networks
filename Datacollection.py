import cv2
import os

# Đường dẫn thư mục để lưu các ảnh chụp
output_dir = '9'

# Tạo thư mục nếu nó chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Số lượng ảnh muốn chụp
num_images = 1000

# Kích thước của ảnh (32, 32, 3)
image_size = (32, 32)
channels = 3

# Khởi tạo thiết bị chụp ảnh (camera)
camera = cv2.VideoCapture(0)

# Lặp để chụp các ảnh
for i in range(num_images):
    ret, frame = camera.read()  # Đọc một khung hình từ camera

    if ret:
        # Resize ảnh thành kích thước mong muốn
        resized_frame = cv2.resize(frame, image_size)

        # Lưu ảnh đã chụp vào thư mục đích
        image_path = os.path.join(output_dir, f'image_{i}.jpg')
        cv2.imwrite(image_path, resized_frame)

        print(f'Captured image {i+1}/{num_images}')
    else:
        print(f'Error capturing image {i+1}')

# Giải phóng tài nguyên của camera
camera.release()

print('Capture process complete.')
