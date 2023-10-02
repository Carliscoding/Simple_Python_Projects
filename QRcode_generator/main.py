import qrcode
i=0
def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1, #version controls the size of the qrcode, version 1 is the smallest (21x21 matrix). There are 40 versions
        error_correction = qrcode.constants. ERROR_CORRECT_L, #Error correction "L" stands for Low provide the least error corection ability but can store more storage
        box_size=10, # box_size is the size of each module in qrcode.
        border=4, #border of qrcode
    )

    qr.add_data(text)
    qr.make(fit=True) #fit=true hense the size of module fit the qrcode.
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("Ma_QR["+str(i)+"].png") #save it to any directory on your computer.
    
# main

while True:
    url = input("Enter your url: ")
    generate_qrcode(url)
    i+=1
    print("============================")
    print("\n\tGenerate QR picture successfully. Check the root directory of this project!\n")
    print( "============================")
    Continue = int(input("Continue?: "))
    if Continue != 1:
        break