
# คำสั่ง Git ที่สำคัญ

## การตั้งค่าเบื้องต้น
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## การสร้างและการโคลน Repository
```bash
git init                          # สร้าง repository ใหม่
git clone <url>                   # โคลน repository ที่มีอยู่
```

## การตรวจสอบสถานะ
```bash
git status                        # ตรวจสอบสถานะของไฟล์
git log                           # ดูประวัติ commit
git diff                          # ดูความแตกต่างของไฟล์
```

## การจัดการการเปลี่ยนแปลง
```bash
git add <file>                    # เพิ่มไฟล์ไปยัง staging area
git add .                         # เพิ่มทุกไฟล์
git commit -m "message"           # บันทึกการเปลี่ยนแปลง
git push                          # ส่งการเปลี่ยนแปลงไปยัง remote
git pull                          # ดึงการเปลี่ยนแปลงจาก remote
```

## การทำงานกับ Branch
```bash
git branch                        # ดูรายชื่อ branch
git branch <name>                # สร้าง branch ใหม่
git checkout <branch>            # เปลี่ยน branch
git merge <branch>               # รวม branch
```
