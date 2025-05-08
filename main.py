def on_bluetooth_connected():
    basic.show_icon(IconNames.YES)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.NO)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    bt_log("INFO", "Button A pressed")
input.on_button_pressed(Button.A, on_button_pressed_a)

def bt_log(level: str, message: str):
    bluetooth.uart_write_line(get_log_string(level, message))

def on_uart_data_received():
    global last_message_received
    # receive a string and shot it.
    last_message_received = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
    basic.show_string(last_message_received)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

def get_log_string(level2: str, message2: str):
    return "[" + control.device_name() + "@" + ("" + str(control.millis())) + "ms]" + " " + level2 + ":" + message2
last_message_received = ""
basic.show_icon(IconNames.SMALL_SQUARE)
bluetooth.start_uart_service()
basic.show_icon(IconNames.SQUARE)