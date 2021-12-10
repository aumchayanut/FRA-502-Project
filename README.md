# FRA-502-Project
Name Chayanut Rassameecharoenchai ID: 62340500012
# Video
https://youtu.be/nq3JRK6Nn3k
# Propose
หุ่นยนต์คอยส่งยาในพื้นที่ของโรงพยาบาลสนาม โดยในตัวอย่างมีเตียงทั้งหมด 6 เตียงด้วยกัน
![alt text](https://github.com/aumchayanut/FRA-502-Project/blob/main/World.jpg?raw=true)
# Command
```
$ roslaunch [package] gazebo.launch
```
spawn หุ่นลงไปใน world พร้อมส่ง laser scan, camera

```
$ roslaunch [package] amcl_with_move_base.launch
```
localization

```
$ roslaunch [package] GoToGoal.py
```
send goal through voice command

หลังจาก compile GoToGoal.py หุ่นจะรอรับคุสั่งเสียง "Turn on" เมื่อหุ่นได้ยินจะปลุกตัวเองขึ้นมาจากโหมด Standby เพื่อรอรับคำสั่งว่าต้องไปที่เป้าหมายใดบ้าง สามารถบอกทีละหลายๆคำสั่งได้ ไม่จำเป็นต้องบอกเรียงเลข เเต่เป้าหมายของหุ่นยนต์จะเรียงจากน้อยไปมาก เช่นพูดคำสั่งว่า "Go to Bed number one six and four." หุ่นยนต์จะเดินทางไปเตียงที่ 1 4 เเละ 6 ตามลำดับ อย่างไรก็ตามหากปลุกหุ่นยนต์ขึ้นมาเเล้วไม่พูดอะไรหรือหุ่นยนต์ฟังไม่เข้าใจเกิน 16 วินาที หุ่นยนต์จะกลับสู่โหมด Standby อีกครั้งหนึ่ง
