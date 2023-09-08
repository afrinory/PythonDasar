import turtle

# Buat objek Turtle
t = turtle.Turtle()
t.speed("fastest")
# Pindahkan Turtle ke tengah jendela
t.penup()
t.goto(0, -200)  # Ubah angka sesuai dengan ukuran jendela Anda

# Gambar lingkaran besar
t.pensize(5)
t.pendown()
t.circle(200)  # Ubah angka sesuai dengan radius yang Anda inginkan
t.penup()
t.goto(2, -150)  # Kembali ke titik tengah

# Gambar lingkaran kecil di tengah
t.pendown()
t.color("blue")
t.fillcolor("blue")
t.begin_fill()
t.circle(150)  # Ubah angka sesuai dengan radius yang Anda inginkan
t.end_fill()

# Gambar persegi kecil
t.penup()
t.goto(-20, -130)
t.pendown()
t.color("white")
t.fillcolor("red")
t.begin_fill()
for _ in range(4):
    t.forward(50)  # Panjang sisi persegi
    t.left(90)  # Sudut putaran
t.end_fill()

# Gambar Lingkaran
# Gambar lingkaran kecil di tengah
t.penup()
t.goto(5, -110)
t.pendown()
t.color("white")
t.fillcolor("red")
t.begin_fill()
t.circle(85)  # Ubah angka sesuai dengan radius yang Anda inginkan
t.end_fill()

# Gambar persegi panjang dengan orientasi vertikal
#t.penup()
#t.goto(-50, 50)
#t.pendown()
#for _ in range(2):
#    t.forward(100)  # Panjang sisi vertikal
#    t.left(90)  # Putar 90 derajat ke kiri
#    t.forward(50)  # Panjang sisi horizontal
#    t.left(90)  # Putar 90 derajat ke kiri

t.penup()
t.goto(38, 12)
t.pendown()
t.color("white")
t.fillcolor("red")
t.begin_fill()
lebar = 30
panjang = 70
# Gambar persegi panjang dengan orientasi vertikal
t.forward(lebar)  # Panjang sisi vertikal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(panjang)  # Panjang sisi horizontal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(lebar)  # Panjang sisi vertikal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(panjang)  # Panjang sisi horizontal
t.end_fill()

t.penup()
t.goto(-39, 82)  # Pindahkan ke posisi yang sesuai
t.pendown()
t.color("white")
t.fillcolor("red")
t.begin_fill()
t.forward(panjang)  # Panjang sisi horizontal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(lebar)  # Panjang sisi vertikal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(panjang)  # Panjang sisi horizontal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(lebar)  # Panjang sisi vertikal
t.end_fill()

t.penup()
t.goto(-0, 82)  # Pindahkan ke posisi yang sesuai
t.pendown()
t.color("white")
t.fillcolor("red")
t.begin_fill()
t.setheading(270)
t.forward(panjang)  # Panjang sisi horizontal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(lebar)  # Panjang sisi vertikal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(panjang)  # Panjang sisi horizontal
t.left(90)  # Putar 90 derajat ke kiri
t.forward(lebar)  # Panjang sisi vertikal
t.end_fill()


# Tunggu jendela ditutup
turtle.mainloop()
