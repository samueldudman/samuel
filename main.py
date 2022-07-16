def on_gesture_shake():
    basic.show_number(1)
    basic.show_string("")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_number(1)