import pygame
import random
from pygame.locals import *

WIDTH = 1400
HEIGHT = 800
class gameover:
    flag = 0
class Bullet:
    bullet_list = []
    # 炮弹发射延迟
    interval = 0
    def __init__(self, pea):
        self.image = pygame.image.load('images/bullet.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = pea.image_rect.centery - 90
        self.image_rect.left = pea.image_rect.right - 50
    # 炮弹显示
    def display(self):
        screen.blit(self.image, self.image_rect)
    # 炮弹移动
    def move(self):
        self.image_rect.move_ip(6, 0)
        # 如果炮弹越界就删除
        if self.image_rect.left > WIDTH:
            Bullet.bullet_list.remove(self)
class Bullet1:
    bullet_list = []
    # 炮弹发射延迟
    interval = 0
    def __init__(self, pea):
        self.image = pygame.image.load('images/bullet1.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = pea.image_rect.centery - 90
        self.image_rect.left = pea.image_rect.right - 50
    # 炮弹显示
    def display(self):
        screen.blit(self.image, self.image_rect)
    # 炮弹移动
    def move(self):
        self.image_rect.move_ip(10, 0)
        # 如果炮弹越界就删除
        if self.image_rect.left > WIDTH:
            Bullet1.bullet_list.remove(self)
class Prop:
    interval = 0
    prop_list = []

    def __init__(self):
        self.image = pygame.image.load('images/prop.png')
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = random.randint(350, 700)
        self.image_rect.centerx = random.randint(400, 760)
        self.image = pygame.transform.scale(self.image, (50, 80))

    def display(self):
        screen.blit(self.image, self.image_rect)
        if self.image_rect.colliderect(peas.image_rect):
            Prop.prop_list.remove(self)
            peas.cishu+=1


class peas:
    cishu = 0

    def __init__(self):
        self.image = pygame.image.load('images/daifu.png')
        self.image_rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (80, 150))
        self.image_rect.centery = 400
        self.image_rect.centerx = 400
        # 定义移动状态
        self.moveup = False
        self.movedown = False
        self.moveleft = False
        self.moveright = False
        self.shoot = False

    def move_up(self):
        self.image_rect.move_ip(0, -5)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                gameover.flag = 1
        for z1 in Zombie1.zombie1_list:
            if self.image_rect.colliderect(z1.image_rect):
                gameover.flag = 1
# 这里新添了代码
        for z2 in Zombie2.zombie2_list:
                    if self.image_rect.colliderect(z2.image_rect):
                        gameover.flag = 1


    def move_down(self):
        self.image_rect.move_ip(0, 5)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                gameover.flag = 1
        for z1 in Zombie1.zombie1_list:
            if self.image_rect.colliderect(z1.image_rect):
                gameover.flag = 1

# 这里新添了代码
        for z2 in Zombie2.zombie2_list:
            if self.image_rect.colliderect(z2.image_rect):
                gameover.flag = 1

    def move_left(self):
        self.image_rect.move_ip(-5, 0)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                gameover.flag = 1
        for z1 in Zombie1.zombie1_list:
            if self.image_rect.colliderect(z1.image_rect):
                gameover.flag = 1

# 这里新添了代码
        for z2 in Zombie2.zombie2_list:
            if self.image_rect.colliderect(z2.image_rect):
                gameover.flag = 1



    def move_right(self):
        self.image_rect.move_ip(5, 0)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                gameover.flag = 1
        for z1 in Zombie1.zombie1_list:
            if self.image_rect.colliderect(z1.image_rect):
                gameover.flag = 1

# 这里新添了代码
        for z2 in Zombie2.zombie2_list:
            if self.image_rect.colliderect(z2.image_rect):
                gameover.flag = 1



    def display(self):
        screen.blit(self.image, self.image_rect)

    def shoot_bullet(self):
        # 创建炮弹
        bullet = Bullet(self)
        bullet.bullet_list.append(bullet)

    def shoot_bullet1(self):
        # 创建炮弹
        bullet1 = Bullet1(self)
        bullet1.bullet_list.append(bullet1)


class Zombie:
    score = 15
    # 创建频率
    interval = 0
    # 保存多个僵尸
    zombie_list = []

    def __init__(self):
        self.image = pygame.image.load('images/zombie.gif')
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = random.randint(300, 700)
        self.image_rect.centerx = 1300
        self.count = 0

    def display(self):
        screen.blit(self.image, self.image_rect)

    def move(self):
        self.image_rect.move_ip(-1, 0)
        # 如果僵尸越界就删除
        if self.image_rect.left < 200:
            Zombie.zombie_list.remove(self)
        # 三颗子弹打死一只小僵尸
        for b in Bullet.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                self.count = self.count + 1
                if self.count == 4:
                    Zombie.zombie_list.remove(self)
                    Bullet.bullet_list.remove(b)
                    self.count = 0
                    Zombie.score += 5
                else:
                    Bullet.bullet_list.remove(b)
        for b in Bullet1.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                Zombie.zombie_list.remove(self)
                Zombie.score += 5

        if self.image_rect.colliderect(peas.image_rect):
            gameover.flag = 1


class Zombie1:
    # 创建频率
    score = 0
    interval = 0
    # 保存多个僵尸
    zombie1_list = []

    def __init__(self):
        self.image = pygame.image.load('images/zombie1.gif')
        self.image_rect = self.image.get_rect()

        self.image_rect.centery = random.randint(300, 700)
        self.image_rect.centerx = 1300
        self.count = 0

    def display(self):
        screen.blit(self.image, self.image_rect)

    def move(self):
        self.image_rect.move_ip(-1, 0)
        # 如果僵尸越界就删除
        if self.image_rect.left < 200:
            Zombie1.zombie1_list.remove(self)
        # 三颗子弹打死一只小僵尸
        for b in Bullet.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                self.count = self.count + 1

                if self.count == 6:
                    Zombie1.zombie1_list.remove(self)
                    Bullet.bullet_list.remove(b)
                    self.count = 0
                    Zombie1.score += 10
                else:
                    Bullet.bullet_list.remove(b)

        for b in Bullet1.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                Zombie1.zombie1_list.remove(self)

                Zombie1.score += 15
        if self.image_rect.colliderect(peas.image_rect):
            gameover.flag = 1

# 这里新添了代码

class Zombie2:
    # 创建频率
    score = 0
    interval = 0
    # 保存多个僵尸
    zombie2_list = []
    def __init__(self):
        self.image = pygame.image.load('images/zombie2.png')
        self.image_rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (150, 200))
        self.image_rect.centery = random.randint(400, 700)
        self.image_rect.centerx = 1300
        self.count = 0

    def display(self):
        screen.blit(self.image, self.image_rect)

    def move(self):
        self.image_rect.move_ip(-1, 0)
        # 如果僵尸越界就删除
        if self.image_rect.left < 200:
            Zombie2.zombie2_list.remove(self)
        # 三颗子弹打死一只小僵尸
        for b in Bullet.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                self.count = self.count + 1

                if self.count == 7:
                    Zombie2.zombie2_list.remove(self)
                    Bullet.bullet_list.remove(b)
                    self.count = 0
                    Zombie2.score += 15
                else:
                    Bullet.bullet_list.remove(b)

        for b in Bullet1.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                Zombie2.zombie2_list.remove(self)

                Zombie2.score += 15
        if self.image_rect.colliderect(peas.image_rect):
            gameover.flag = 1


def key_control():
    for event in pygame.event.get():
        # 事件类型
        if event.type == QUIT:
            pygame.quit()
            exit()
        # 判断键盘输入
        elif event.type == KEYDOWN:
            if event.key == (K_w or K_UP):
                peas.moveup = True
            elif event.key == (K_s or K_DOWN):
                peas.movedown = True
            elif event.key == (K_a or K_LEFT):
                peas.moveleft = True
            elif event.key == (K_d or K_RIGHT):
                peas.moveright = True
            elif event.key == K_SPACE:
                peas.shoot = True
            elif event.key == K_n and peas.cishu > 0:
                peas.shoot_bullet1()
                peas.cishu -= 1
        elif event.type == KEYUP:
            if event.key == (K_w or K_UP):
                peas.moveup = False
            elif event.key == (K_s or K_DOWN):
                peas.movedown = False
            elif event.key == (K_a or K_LEFT):
                peas.moveleft = False
            elif event.key == (K_d or K_RIGHT):
                peas.moveright = False
            elif event.key == K_SPACE:
                peas.shoot = False


if __name__ == '__main__':
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background_image = pygame.image.load('images/beijing.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    # 创建时钟
    clock = pygame.time.Clock();
    # 创建一个对象
    peas = peas()

    while gameover.flag == 0:

        screen.fill((0, 0, 0))
        screen.blit(background_image, (0, 0))  # 背景显示
        peas.display()
        # 键盘输入
        key_control()
        # 移动判断
        if peas.moveup == True and peas.image_rect.top > 150:
            peas.move_up()
        if peas.movedown == True and peas.image_rect.bottom < 900:
            peas.move_down()
        if peas.moveleft == True and peas.image_rect.centerx > 350:
            peas.move_left()
        if peas.moveright == True and peas.image_rect.centerx < 960:
            peas.move_right()
        Bullet.interval += 1
        if peas.shoot == True and Bullet.interval >= 20 and Zombie.score + Zombie1.score + Zombie2.score > 0:
            peas.shoot_bullet()
            Bullet.interval = 0
            Zombie.score -= 1
        # 创建僵尸
        Zombie.interval += 1
        if Zombie.interval >= 250:
            Zombie.interval = 0
            zombie = Zombie()
            Zombie.zombie_list.append(zombie)
        Zombie1.interval += 1
        if Zombie1.interval >= 300:
            Zombie1.interval = 0
            zombie1 = Zombie1()
            Zombie1.zombie1_list.append(zombie1)

        Zombie2.interval += 1
        if Zombie2.interval >= 350:
            Zombie2.interval = 0
            zombie2 = Zombie2()
            Zombie2.zombie2_list.append(zombie2)
            Zombie2.interval += 1


        Prop.interval += 1
        if Prop.interval >= 800:

            prop = Prop()
            Prop.prop_list.append(prop)
            Prop.interval = 0

        # 显示所有炮弹
        for bullet in Bullet.bullet_list:
            # 炮弹显示
            bullet.display()
            # 炮弹移动
            bullet.move()
        for bullet in Bullet1.bullet_list:
            # 炮弹显示
            bullet.display()
            # 炮弹移动
            bullet.move()
        # 显示所有僵尸
        for zombie in Zombie.zombie_list:
            # 僵尸显示
            zombie.display()
            # 僵尸移动
            zombie.move()
        for zombie1 in Zombie1.zombie1_list:
            # 僵尸显示
            zombie1.display()
            # 僵尸移动
            zombie1.move()


        for zombie2 in Zombie2.zombie2_list:
            # 僵尸显示
            zombie2.display()
            # 僵尸移动
            zombie2.move()

        for prop in Prop.prop_list:
            prop.display()

        if Zombie.score + Zombie1.score + Zombie2.score  >=200:  # 分数到达200分就结束
            gameover.flag = 2
        clock.tick(60)

        pygame.font.init()
        # 金币显示
        myfont = pygame.font.Font(None, 50)
        textImage = myfont.render("Your coins:" + str(Zombie.score + Zombie1.score + Zombie2.score ), True, (255, 215, 0))
        screen.blit(textImage, (1150, 10))
        # 特殊金币显示
        myfont = pygame.font.Font(None, 50)
        textImage = myfont.render("Your NBcoins:" + str(peas.cishu), True, (255, 215, 0))
        screen.blit(textImage, (1110, 50))

        pygame.display.update()

    while gameover.flag == 1:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        jieshuhuamian = pygame.image.load('images/youxijieshu.png')
        screen.blit(jieshuhuamian, (0, 0))
        key_control()
        pygame.display.update()
    while gameover.flag == 2:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        jieshuhuamian = pygame.image.load('images/chuangguanchenggong.png')
        screen.blit(jieshuhuamian, (0, 0))
        key_control()
        pygame.display.update()
