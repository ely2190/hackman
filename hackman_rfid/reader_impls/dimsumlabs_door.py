from django.conf import settings
import serial


def get_cards():
    '''Yields raw card ids from usb reader at DSL door'''

    conn = serial.Serial(settings.RFID_READER['CONFIG']['serial_port'],
                         settings.RFID_READER['CONFIG']['baud_rate'],
                         timeout=settings.RFID_READER['CONFIG']['timeout'])
    while True:
        card = conn.read(10)
        if not card:
            continue

        card = card[0:len(card)-1]  # Skip checksum byte
        card = bytes(reversed(card))  # Correct endianness
        yield card
