A, B, C, D, E, F, G, H, I, J, K, L, M, N, O = 150, 105, 120, 6.50, 20, 10, 18, 10.25, 120.25, 21.50, 29.50, 15.75, 19, 15.15, 10
print('ฉันพกเงินออกไป 1000 บาท เพื่อซื้อของ 15 รายการ ดังนี้') 
print('หมูสับ 1 กิโลกรัม : 150.00 บาท')
print('เนื้ออกไก่ : 105.00 บาท')
print('ไก่บ้าน 1 ตัว : 120.00 บาท')
print('มาม่าต้มยำ : 6.50 บาท')
print('น้ำตาล : 20.00 บาท')
print('ปลากระป๋องสามแม่ครัว : 10.00 บาท')
print('ซอสน้ำมันหอย : 18.00 บาท')
print('ผงชูรส : 10.25 บาท')
print('ไข่แผงคละเบอร์ : 120.25 บาท')
print('ชาเขียว : 21.50 บาท')
print('Pepsi : 29.50 บาท')
print('กาแฟ : 15.75 บาท')
print('ขนมปังอบเนย : 19.00 บาท')
print('น้ำเปล่า : 15.15 บาท')
print('น้ำแข็ง : 10.00 บาท')

เงินที่ต้องจ่าย = A + B + C + D + E + F + G + H + I + J + K + L + M + N + O
print('รวมมูลค่าทั้งสิ้น:', เงินที่ต้องจ่าย, 'บาท')

while True:
    Money = input("คุณจ่ายเงินจำนวน (ตอนนี้มีธนบัตร 1000 บาท 1 ใบ และไม่ต้องพิมพ์หน่วยบาทหรือเว้นวรรค): ")
    try:
        Money = float(Money)
        if Money == 1000.0:
            เงินทอน = Money - เงินที่ต้องจ่าย
            print('<<<<<คุณได้รับเงินทอนทั้งสิ้น:' , round(เงินทอน, 329.10), 'บาท', ">>>>>")
            print('<<<<<สรุปคุณใช้จ่ายไปทั้งสิ้น:' , เงินที่ต้องจ่าย, 'บาท' , ">>>>>")
            break
        else:
            print('>>>> คุณไม่สามารถจ่ายด้วยจำนวนเงินอื่นๆ ได้นอกจาก 1000 บาท เพราะตอนนี้คุณมีแค่ธนบัตรหนึ่งพัน 1 ใบเท่านั้น')
    except ValueError:
        print('>>> คุณต้องกรอกจำนวนเงินเป็นตัวเลขเท่านั้น')