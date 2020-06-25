# QR-code-to-track-Covid-19-patients
QR code that can be used to track Covid-19 tested patients by scanning them at every checkpoints to control the spread of corona virus

QR code that should be generated and attached with every report of the corona virus, Also a digital copy can be given so that they can carry it with them, the basic idea here is, to generate a QR code for every person who tested them at the hospital.
This QR code when scanned gives a particulara ID(We can use AADHAR Number as it is unique and nation-wide recognize). This id is then matched with the database available, and it provides necessary details such as name, age, address, is he tested, if yes what was the result(result can be positive, negative, NA - NA is for people who are not yet tested).
this can be used by shop owners, police department at every checkpoint(to ensure no paitent travels to different state when asked to quarantine themself).

QR_generator_final. py is the main file to generate QR Code, when all the details are entered, press generate QR, and it will ask you to select an image, select an image of the person, so that it can be embeded at the very center of the QR code, this is done to ensure authenticity and integrity of the QR code. It will also connect to SQLITE3, and create a table if it is not present in the database.

read.py is the file that scans the QR code, currently i have done is the name of the QR code has to be passed, then it will decode, trim and match the output with the database and then display the fields.( this can be modified to taking the input from a camera, and live decoding and output display can be achieved).
