#Ander Varuskin IS22
import pygame #impordib pygame








pygame.init() #pygame käivitamine








screen=pygame.display.set_mode([300,300]) #määrab akna suuruse
pygame.display.set_caption("Lumememm - Varuskin") #paneb aknale/tööle nime








pygame.draw.circle(screen, [255, 255, 255], [150,53], 35, 0) #joonistab lumememme ülemise palli ehk pea
pygame.draw.circle(screen, [255, 255, 255], [150,115], 40, 0) #joonistab lumememme keskmise palli ehk kõhu
pygame.draw.circle(screen, [255, 255, 255], [150,180], 45, 0) #joonistab lumememme alumise palli ehk jala(d)
pygame.draw.circle(screen, [0, 0, 0], [134,37], 4, 0) #joonistab vasakpoolse silma
pygame.draw.circle(screen, [0, 0, 0], [165,37], 4, 0) #joonistab parempoolse silma




pygame.draw.polygon(screen, [228, 114, 0], [[145,44],[155,44],[150,65]]) #joonistab porgandi ehk nina




pygame.draw.circle(screen, [255, 255, 255], [105,100], 15, 0) #joonistab vasaku käe
pygame.draw.circle(screen, [255, 255, 255], [194,100], 15, 0) #joonistab parema käe




pygame.draw.circle(screen, [0, 0, 0], [150,100], 5, 0)
pygame.draw.circle(screen, [0, 0, 0], [150,120], 5, 0) #joonistab nööbid
pygame.draw.circle(screen, [0, 0, 0], [150,140], 5, 0)




pygame.draw.rect(screen, [0, 0, 0], [50, 80, 200, 300], 0)
pygame.draw.rect(screen, [0, 0, 0], [50, 80, 200, 300], 0)
pygame.draw.rect(screen, [255, 0, 0], [50, 200, 200, 300], 0)




pygame.display.flip()








run = True
while run:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         run = False








 pygame.display.update()








pygame.quit()