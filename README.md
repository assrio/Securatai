# Securatai
Securatai is a security system that can be installed in numerous locations, primarily houses, and schools, and which analyzes a card to determine whether a door unlocks or not. We can build this project together using the Rasberry Pi Pico, an LCD, a servo, and an MFRC522 module.

The Securatai system utilizes RFID to collect a card's data, which it then communicates to the Pico to determine if the card's ID is permitted access to the building. Since each card has a unique ID, the system can distinguish between various cards, which is useful if a card is only permitted to enter a certain area of the building while the others parts of the building prevent entry. A display will read "Access granted" and play a high-pitched sound [^1] if a card has permission to enter. If not, a low-pitched sound [^2] will be played along with the message "Access denied" on display. A servo will be used to rotate to open a latch lock to unlock. This mechanism works by attaching a metal wire to the servo and connecting it to the latch so that whenever the Servo rotates, the latch will move [^3]. After a few seconds, the servo is programmed to return the latch to the lock position to get you inside and lock the door for you.

Main parts and use:

- Raspberry Pi Pico W

Microcontroller board used to control electric modules/components.

- MFRC522 module

MFRC522 is a highly integrated read-and-write card chip that receives and sends information over to the Pico to decide what to execute.

 
 - 2x Keycards

With each having its ID, the keycards are used to communicate with the MFRC522.


- Servo

Servos are devices that precisely rotate and push machine components.


- LCD

A liquid-crystal display is a flat-panel display that outputs text from the Pico.


- Passive buzzer


Used to create sounds based on frequency.


- Jumper cables

Used to connect 2 points in a circuit together.


- Electrical components (resistors, transistors, etc)

Used to limit electrical power or transfer data.


[System Demonstration](https://drive.google.com/file/d/1oIGaEGvSoh4MSxkQakfPgsSyz11fmO0A/view?usp=sharing)


[^1]: [Accepted Noise](https://drive.google.com/file/d/1fP1Ql4AOzntfi96F1mzlT5g32qhO07m_/view?usp=sharing)


[^2]: [Denied Noise](https://drive.google.com/file/d/1bduRGhVk7ZkQljy3RiV1hSeuDZixzJTc/view?usp=sharing)

[^3]: [Servo Example](https://drive.google.com/file/d/1EUGehfnb2psePgyM2nRL77taewNKoMna/view?usp=sharing)



