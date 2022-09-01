import serial
import csv

if __name__ == "__main__":
    serialConnection = serial.Serial('COM5', 115200, timeout=1)

    serialConnection.reset_input_buffer()

    user = []

    with open('users.csv', newline='') as csvfile:
        users = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in users:
            user.append(row)
            print(', '.join(row))

    while True:
        if serialConnection.in_waiting > 0:
            uid = serialConnection.readline().decode('utf8').rstrip()
            print(uid)
            userFound = False
            for item in user:
                if item[1] == uid:
                    userFound = True
                    serialConnection.write(b'0')
                    print("Access granted\nHello, " + item[0])
                    continue

            if not userFound:
                print("Access denied")
                serialConnection.write(b'1')