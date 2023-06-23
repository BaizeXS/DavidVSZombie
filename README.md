# README

> 本项目为北京理工大学(BIT)计算机学院Python小学期项目。

## 1. 整体设计目标

### 1.1 简介

我小组以经典游戏《植物大战僵尸》为主题，以戴夫为主人公，重新调整游戏背景与游戏形式，进行小游戏制作。

### 1.2 游戏背景

在一个凄凉的屋子里，早已没有人生活了，只有一群僵尸相依为命，他们在等待坟墓里的同伴，和他们一起去撕咬人类。在一个午夜前，坟墓“崩”一声炸开了，紧接着从墓碑下，一个人手张了出来，从土堆里又相继出现了几个身体，没有脑袋，但是却能动。他们来到了人类世界，将路障、铁桶，戴在脑袋上，有的跑的快的僵尸，将橄榄球运动员吃掉，穿上了好看的橄榄服。也有的冲进别人家门，把铁纱窗戴在身上当防御盾牌。

幸存的人们也陷入了恐慌，直到他们发现了一些植物的神奇能力，于是人们开始使用植物保护自己。

但是由于地球环境的恶化和僵尸的无限泛滥，土地被僵尸的尸毒所污染而无所再继续种植，戴夫失去了植物的保护，但由于打僵尸变得多财多亿的戴夫决定拿起他唯一的武器——金币来捍卫自己，而且他偶然间发现了这片土地在发生了某种特殊的变化后，居然可以出产能让金币进化的金坷垃，于是他走上了戴夫大战僵尸之旅。

### 1.3 游戏整体设计

本游戏以戴夫为主人公，玩家通过对戴夫进行与攻击操作，消灭屏幕上出现的僵尸，从而抵御僵尸的进攻。该游戏作为一款2D设计类益智游戏，一方面沿用了部分《植物大战僵尸》的设定，比如“战场设置在后院”、“僵尸种类丰富”等；另一方面，我们对玩家防御僵尸的方法进行了改变，从固定植物只能攻击一行的僵尸改变为可移动的戴夫来攻击僵尸，使游戏拥有更强的灵活性，不用看着某一行有僵尸而没钱种植植物而干着急。当然，与此同时我们对僵尸的行为也重新进行调整，从而匹配游戏难度，通过设置不同种类僵尸的血量，移动速度，出现频率等属性提升游戏相对难度，从而使得玩家拥有良好的用户体验。此外，我们还采用了积分制，在消灭僵尸的同时，玩家可以获得一定积分，从而对“闯关是否成功”以及游戏难度进行调整。最后，我们添加了一项特殊技能：草坪上会随机出现金坷垃，玩家通过收集金坷垃可以使用特殊技能，也就是我们平时说的“大招”。该技能可以帮助玩家在“危机时刻”扭转乾坤，力挽狂澜，但是也十分考验玩家对“大招”使用时机的把握，不仅提升了游戏趣味性，而且使得游戏拥有一定“刺激性”！

## 2. 分工说明

### 2.1 个人分工：

- 王晨屹同学：

  负责总体程序框架设计与戴夫类编写

- 许宗嗣同学

  负责僵尸类编写与素材拼接

### 2.2 共同工作：

- PPT制作
- 文档编写
- 事件处理类代码

## 3. 代码总体框架

- 第一部分：抽象类的确定

  首先确定了类的种类，其中最主要的三类为戴夫类，僵尸类和子弹类。

  关系如下：

  僵尸——>攻击——>戴夫

  戴夫——>发射——>子弹

  子弹——>攻击——>僵尸

  因此，逻辑如下：

  僵尸入侵后院，若僵尸到达房屋，即窗口最左侧，则判定玩家输。故玩家操控戴夫在草坪上四处移动的同时，攻击来自四面八方的僵尸，并且要避免与僵尸接触，否侧判定玩家输。当玩家清理完全部僵尸，即积分到达一定值之后，玩家取得胜利。

- 第二部分：主体结构

  - 首先对窗口进行相关设置并对窗口进行初始化

    ```
     # 对窗口进行设置
     WIDTH = 1400
     HEIGHT = 800
     screen = pygame.display.set_mode((WIDTH, HEIGHT))
     background_image = pygame.image.load('images/beijing.png')
     background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
     # 创建时钟
     clock = pygame.time.Clock();
    ```

  - 初始化结束后进入循环，设置flag来决定游戏状态

    flag为0时，游戏继续进行；flag为1时，游戏结束，判定玩家为输；flag为2时，判定玩家获得胜利

  - 进入循环后，在一定范围内随机生成不同种类的僵尸

  - 进入循环后，通过对键盘事件的监听实现戴夫的移动（W、A、S、D）与攻击（Space）

  - 进入循环后，通过对碰撞的检测，实现僵尸的“消灭”以及戴夫是否存活：

    子弹与僵尸发生碰撞则进行计数，当计数到达僵尸被消灭的阈值时，将改僵尸移除；

    戴夫与僵尸发生碰撞，则判定玩家为输，设置flag为1并结束游戏

  主程序结构与部分代码如下：

  ```
   if __name__ == '__main__':
       # 初始化窗口
       screen = pygame.display.set_mode((WIDTH, HEIGHT))
       background_image = pygame.image.load('images/beijing.png')
       background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
       # 创建时钟
       clock = pygame.time.Clock();
       # 创建一个对象
       peas = peas()
       # 进入循环
       while gameover.flag == 0:
           screen.fill((0, 0, 0))
           screen.blit(background_image, (0, 0))  
           peas.display()
           # 键盘输入
           key_control()
           # 移动判断——if结构+peas移动方法
           # 创建僵尸
           Zombie.interval += 1
           if Zombie.interval >= 200:
               Zombie.interval = 0
               zombie = Zombie()
               Zombie.zombie_list.append(zombie)
           # 显示所有炮弹
           for bullet in Bullet.bullet_list:
               # 炮弹显示
               bullet.display()
               # 炮弹移动
               bullet.move()
           # 显示所有僵尸
           for zombie2 in Zombie2.zombie2_list:
               # 僵尸显示
               zombie2.display()
               # 僵尸移动
               zombie2.move()
           # 分数到达500分就结束
           if Zombie.score + Zombie1.score + Zombie2.score + Zombie3.score >= 500:  
               gameover.flag = 2
           clock.tick(60)
           pygame.font.init()
           # 金币显示
           myfont = pygame.font.Font(None, 50)
           textImage = myfont.render("Your coins:" + str(Zombie.score + Zombie1.score + Zombie2.score + Zombie3.score), True, (255, 215, 0))
           screen.blit(textImage, (1150, 10))
           # 特殊金币显示
           myfont = pygame.font.Font(None, 50)
           textImage = myfont.render("Your NBcoins:" + str(peas.cishu), True, (255, 215, 0))
           screen.blit(textImage, (1110, 50))
           pygame.display.update()
       # 玩家输了
       while gameover.flag == 1:
           screen = pygame.display.set_mode((WIDTH, HEIGHT))
           jieshuhuamian = pygame.image.load('images/youxijieshu.png')
           screen.blit(jieshuhuamian, (0, 0))
           key_control()
           pygame.display.update()
       # 玩家取得胜利
       while gameover.flag == 2:
           screen = pygame.display.set_mode((WIDTH, HEIGHT))
           jieshuhuamian = pygame.image.load('images/chuangguanchenggong.png')
           screen.blit(jieshuhuamian, (0, 0))
           key_control()
           pygame.display.update()
  ```

## 4. 第三方库介绍（下载地址）

- pygame

  - 简介：

    - Pygame是一组跨平台的Python模块, 用于创建视频游戏。
    - 它由旨在与Python编程语言一起使用的计算机图形和声音库组成。
    - Pygame由Pete Shinners正式编写, 以取代PySDL。
    - Pygame适合于创建客户端应用程序, 这些应用程序可以包装在独立的可执行文件中。

  - 下载方式:

    ```
     pip3 install pygame
    ```

  - 载入方式：

    ```
     import pygame
    ```

- random

  - 简介：

    用于生成随机数字的Python模块。

  - 下载方式：

    Python自带库，无需额外安装

  - 载入方式：

    ```
     import random
    ```

## 5. 软件环境配置及运行指导说明

### 5.1 环境配置

- Windows：
  - Windows 10 Professional 64位
  - Python 3.9.7
  - pygame库
  - PyCharm 2021.2.1
- macOS：
  - macOS 11.5.2
  - Python 3.9.7
  - pygame库
  - VisualStudioCode

### 5.2 运行指导说明

1. 法一：在终端/CMD/Powershell下切换至游戏目录，输入如下命令即可运行：

   ```
    python3 戴夫大战僵尸.py
   ```

2. 法二：在IDE下运行

   点击图中按钮或使用快捷键<ctrl>+<R>
