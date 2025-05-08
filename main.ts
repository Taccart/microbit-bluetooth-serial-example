bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showIcon(IconNames.Yes)
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    basic.showIcon(IconNames.No)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    bt_log("INFO", "Button A pressed")
})
function bt_log(level: string, message: string) {
    bluetooth.uartWriteLine(get_log_string(level, message))
}

bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function on_uart_data_received() {
    
    //  receive a string and shot it.
    last_message_received = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
    basic.showString(last_message_received)
})
function get_log_string(level2: string, message2: string): string {
    return "[" + control.deviceName() + "@" + ("" + ("" + control.millis())) + "ms]" + " " + level2 + ":" + message2
}

let last_message_received = ""
basic.showIcon(IconNames.SmallSquare)
bluetooth.startUartService()
basic.showIcon(IconNames.Square)
