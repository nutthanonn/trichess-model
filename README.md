# Idea
เราวางแผนโดยการใช้ minimax แต่ทำได้เพียงเอาแนวคิดของ minimax มาประยุกต์ใช้ในช่วงเวลาปัจจุบันเท่านั้น และแนวคิดเพิ่มเติมเป็น Boost force & DP & Heap
# Work process
1. เช็คกินตัวไหนได้ เก็บ Max priority (Queen ไม่กิน Pawn ใน 20 turn แรก) </br>
2. ถ้ากินอะไรไม่ได้เดินที่ปลอดภัย</br>
2.1. เดินหลบ (ถ้าจะโดนกินจะเดินหลบโดยหากตัวที่จะโดนกินมีหลายตัวให้เดินหลบตามค่า Priority มากสุดก่อน)</br>
2.2. เดินที่ที่ศัตรูกินไม่ได้ (เก็บตำแหน่งที่ศัตรูเดินได้ intersect ตำแหน่งทั้งหมดบนกระดานปัจจุบันของเรา)</br>
3. ถ้ากินได้และกำลังจะโดนกินตัวไหนมี Priority สูงกว่าหากตัวที่เราจะถูกกินมี Priority สูงกว่าจะเดินหลบไปที่ปลอดภัย หากตัวที่เราจะถูกกินมี Priority ต่ำกว่าหรือเท่ากับตัวที่เราสามารถกินได้จะทำการกิน</br>

### Priority
```
    "King": 1000,
    "Queen": 9,
    "Rook": 5,
    "Knight": 3,
    "Bishop": 3,
    "Pawn": 1
```

# Usage

- เปลี่ยน `url` ในไฟล์ `main.py` ให้เป็น url ของเกม
  <img src='./assets/url.png'>

- รันไฟล์ `main.py` โดยใช้คำสั่ง `python main.py or python3 main.py`

_IMPORTANT NOTE:_ ใส่จำนวน Player ที่ต้องการ
<img src='./assets/player.png'>

## Bug Fix

- เปลี่ยน Import test เป็น import algorithm ด้วยครับบ
  <img src="./assets/fix-import.png">
  <img src="./assets/fix-import2.png">

`อาจจะมี bug อยู่นะเพราะไม่ได้ handle ทุก case`
