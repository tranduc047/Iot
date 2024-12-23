from flask import Flask, render_template
from sense_emu import SenseHat
import time

app = Flask(__name__)

# Khởi tạo Sense HAT (mô phỏng)
sense = SenseHat()

# Tên hiển thị trên LED Matrix
name = "Anh/Chị"
color = (255, 0, 0)  # Màu đỏ

def display_name_on_led(name, color):
    """
    Hiển thị tên trên LED Matrix.
    """
    sense.show_message(name, text_colour=color, scroll_speed=0.1)

# Hàm để lấy thông tin nhiệt độ, độ ẩm và trạng thái joystick
def get_sensor_data():
    # Đọc nhiệt độ và độ ẩm
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    # Lấy trạng thái joystick
    joystick_events = sense.stick.get_events()

    # Trả về dữ liệu dưới dạng dictionary
    return {
        "temperature": temp,
        "humidity": humidity,
        "joystick_events": joystick_events
    }

@app.route('/')
def index():
    # Lấy thông tin từ cảm biến
    sensor_data = get_sensor_data()

    # Hiển thị tên trên LED Matrix
    display_name_on_led(name, color)

    # Render template với dữ liệu cảm biến
    return render_template('index.html', sensor_data=sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
path_cer='tranduck57kmt-firebase-adminsdk-v9pi3-f7170b1af7.json'
path_data_url='https://tranduck57kmt-default-rtdb.asia-southeast1.firebasedatabase.app/'