import cmath
import math
import matplotlib.pyplot as plt

# ฟังก์ชันคำนวณรากที่ n ของจำนวนเชิงซ้อน
def complex_root(z, n):
    # แปลงจำนวนเชิงซ้อนให้อยู่ใน Polar form
    r = abs(z)  # ขนาดของจำนวนเชิงซ้อน
    theta = cmath.phase(z)  # มุมของจำนวนเชิงซ้อน
    
    roots = []
    for k in range(n):
        # คำนวณมุมใหม่
        angle = (theta + 2 * math.pi * k) / n
        # คำนวณราก
        root = r**(1/n) * (cmath.cos(angle) + 1j * cmath.sin(angle))
        roots.append(root)
    return roots

# ฟังก์ชันแปลงค่าทศนิยมเป็นรูท
def format_real_part(real_part):
    if abs(real_part - 2 * math.sqrt(3)) < 0.1:
        return "2√3"
    elif abs(real_part - math.sqrt(3)) < 0.1:
        return "√3"
    elif abs(real_part - 2) < 0.1:
        return "2"
    elif abs(real_part + 2) < 0.1:
        return "-2"
    elif abs(real_part - 3) < 0.1:
        return "3"
    elif abs(real_part + 3) < 0.1:
        return "-3"
    else:
        return f"{real_part:.2f}"

# ฟังก์ชันแปลงค่าทศนิยมเป็นรูทสำหรับส่วนจินตภาพ
def format_imaginary_part(imag_part):
    if abs(imag_part - 2*math.sqrt(3)) < 0.1:
        return "2√3i"
    elif abs(imag_part + 2*math.sqrt(3)) < 0.1:
        return "-2√3i"
    elif abs(imag_part - math.sqrt(3)) < 0.1:
        return "√3i"
    elif abs(imag_part + math.sqrt(3)) < 0.1:
        return "-√3i"
    elif abs(imag_part - 1) < 0.1:
        return "i"
    elif abs(imag_part + 1) < 0.1:
        return "-i"
    elif abs(imag_part - 3) < 0.1:
        return "3i"
    elif abs(imag_part + 3) < 0.1:
        return "-3i"
    else:
        return f"{imag_part:.2f}i"

# ฟังก์ชันแสดงผลในรูปแบบที่ต้องการ
def format_root(root):
    real_part = root.real
    imag_part = root.imag
    
    # แสดงส่วนจริง
    real_str = format_real_part(real_part)
    
    # แสดงผลลัพธ์ในรูปแบบ 2 + 2√3i
    imag_str = format_imaginary_part(imag_part)
    
    if imag_part >= 0:
        return f"{real_str}+{imag_str}"
    else:
        return f"{real_str}{imag_str}"

# ฟังก์ชันหลักสำหรับรับอินพุตและคำนวณราก
def main():
    # รับอินพุตจำนวนเชิงซ้อนและจำนวนรากที่ต้องการ
    real = float(input("Enter the real part of the complex number: "))
    imag = float(input("Enter the imaginary part of the complex number: "))
    z = complex(real, imag)
    n = int(input("Enter the number of roots to find: "))
    
    # คำนวณราก
    roots = complex_root(z, n)
    
    # แสดงผลรากที่คำนวณได้ในรูป Polar form
    print(f"Roots of {z}:")
    for i, root in enumerate(roots):
        # แสดงผลในรูปแบบที่ต้องการ
        print(f"{i+1}). {abs(root):.2f}(cos {cmath.phase(root)/math.pi:.3f}π + i sin {cmath.phase(root)/math.pi:.3f}π) = {format_root(root)}")
    
    # แสดงกราฟเวกเตอร์
    plt.figure(figsize=(6, 6))
    ax = plt.gca()

    # วาดกราฟรากที่ได้
    for root in roots:
        ax.quiver(0, 0, root.real, root.imag, angles='xy', scale_units='xy', scale=1, color='r')
    
    # ตั้งค่ากราฟ
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f'Roots of {z}')
    
    # แสดงกราฟ
    plt.show()

# เรียกใช้ฟังก์ชันหลัก
main()
