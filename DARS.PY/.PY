# import pygame
# import sys

# # Pygame kutubxonasini boshlash
# pygame.init()

# # Ekran o'lchamlari
# ekran_kengligi = 800
# ekran_balandligi = 600

# # Ekran yaratish
# ekran = pygame.display.set_mode((ekran_kengligi, ekran_balandligi))
# pygame.display.set_caption("Pygame Animatsiya")

# # Ranglar
# oq = (255, 255, 255)
# qora = (0, 0, 0)
# qizil = (255, 0, 0)

# # To'p xususiyatlari
# top_radius = 20
# top_x = ekran_kengligi // 2
# top_y = ekran_balandligi // 2
# top_velocity_x = 3
# top_velocity_y = 3

# # Asosiy o'yin sikli
# while True:
#     # Hodisalarni tekshirish
#     for hodisa in pygame.event.get():
#         if hodisa.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     # Ekranni tozalash
#     ekran.fill(qora)

#     # To'pni harakatlantirish
#     top_x += top_velocity_x
#     top_y += top_velocity_y

#     # To'p chegarasiga to'qnashganida yo'nalishini o'zgartirish
#     if top_x - top_radius <= 0 or top_x + top_radius >= ekran_kengligi:
#         top_velocity_x = -top_velocity_x
#     if top_y - top_radius <= 0 or top_y + top_radius >= ekran_balandligi:
#         top_velocity_y = -top_velocity_y

#     # To'pni chizish
#     pygame.draw.circle(ekran, qizil, (top_x, top_y), top_radius)

#     # Ekranni yangilash
#     pygame.display.update()

#     # FPS (Frame per second) boshqarish
#     pygame.time.Clock().tick(60)

"""1-mashq"""
# import math
# print(round(math.sqrt(round(67365/32, 2)**3) ,3))


"""2mashq"""

# bozorlik = []
# bozorlik.append("olma")
# bozorlik.append("anjir")
# bozorlik.append('anor')
# bozorlik.insert(0, 'qovoq')
# bozorlik.insert(4,'bodiring')
# print(bozorlik)



"""3-maswhq"""
sonlar = [-34,45,0,65.3,3.6,2,62]
import math
print(sonlar[2]+sonlar[4])
print(sonlar[-6] / sonlar[-2])
print(math.sqrt(sonlar[1]))


"""4-mashq"""

# kitoblar = []
# kitoblar.append(input("kitob kirit"))
# kitoblar.append(input("kitob kirit"))
# kitoblar.append(input("kitob kirit"))
# kitoblar.append(input("kitob kirit"))
# kitoblar.append(input("kitob kirit"))
# print(f'sen oqigan kitoblar : {kitoblar}')


"""5-mashq"""









