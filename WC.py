import cv2

# Kích thước của ảnh (32, 32)
image_size = (32, 32)

# Khởi tạo thiết bị webcam
camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()  # Đọc một khung hình từ webcam

    if ret:
        # Resize ảnh thành kích thước mong muốn
        resized_frame = cv2.resize(frame, image_size)

        # Hiển thị ảnh đã chụp
        cv2.imshow('Resized Image', resized_frame)

    # Đợi một phím được nhấn và kiểm tra nếu phím là 'q' (thoát)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên của camera và đóng cửa sổ hiển thị
camera.release()
cv2.destroyAllWindows()
