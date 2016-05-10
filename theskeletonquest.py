#This code belongs to Chelin Tutorials
#Use it for education only
#www.chelintutorials.com
#youtube.com/ChelinTutorials
#for a new cool game checkout: www.littlewaronline.com

import pygame
import random
import math
from imagenesysonido import  *  


class Snow():
    def __init__(self):
        self.list=[]
        for i in range(150):
            x=random.randrange(0,800)
            y=random.randrange(0,600)
            self.list.append([x,y])
    def update(self,pantalla):
        for i in range(len(self.list)):
            # Draw the star
            pygame.draw.circle(pantalla,(255,255,255),self.list[i],2)
             
            # Move the star down one pixel
            self.list[i][1]+=3
             
            # If the star has moved off the bottom of the screen
            if self.list[i][1] > 600:
                # Reset it just above the top
                y=random.randrange(-50,-10)
                self.list[i][1]=y
                # Give it a new x position
                x=random.randrange(0,800)
                self.list[i][0]=x   
                     
class BotonAudio(pygame.sprite.Sprite):
    def __init__(self,x,y):  
        self.imagenon=pygame.image.load("ChelinsWorld/soundon.png").convert_alpha() 
        self.imagenoff=pygame.image.load("ChelinsWorld/soundoff.png").convert_alpha() 
        self.estado="ON"
        self.imagen_actual=self.imagenon
        self.rect=  self.imagen_actual.get_rect()
        self.rect.left=x
        self.rect.top=y
    def update(self,surface):
        surface.blit(self.imagen_actual,self.rect)
    def cambiar_estado(self):
        if self.estado=="ON":
            self.estado="OFF"
            self.imagen_actual=self.imagenoff
            pygame.mixer.music.stop()
        else:
            self.estado="ON"
            self.imagen_actual=self.imagenon
            pygame.mixer.music.play(5)
class Imagenes(object):
    def __init__(self):
        self.nombre="Unknown"

class Botonskill(pygame.sprite.Sprite):
    def __init__(self,x,y):  

        self.imagensinpuntos=pygame.image.load("ChelinsWorld/skilloff.png")
        self.imagenconpuntos=pygame.image.load("ChelinsWorld/skillon.png")
        self.imagen=self.imagensinpuntos      
        self.rect= self.imagen.get_rect()
        self.rect.left=x
        self.rect.top=y
    def update(self,surface,player):
        if player.skillpoints>0:self.imagen=self.imagenconpuntos
        else:self.imagen=self.imagensinpuntos
        surface.blit(self.imagen,(self.rect.left,self.rect.top))



class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x,y):  
        self.imagen=imagen1
        self.imagennormal=imagen1
        self.imagenseleccion=imagen2
        self.rect= imagen1.get_rect()
        self.rect.left=x
        self.rect.top=y
    def setImage(self,imagen):
        self.imagen=imagen
    def pintar(self,surface,cursor):
        if cursor.colliderect(self.rect): self.setImage(self.imagenseleccion)
        else:self.setImage(self.imagennormal)
        surface.blit(self.imagen,(self.rect.left,self.rect.top))
class cursor(pygame.Rect):
    def __init__(self):
        (self.x,self.y)=pygame.mouse.get_pos()
        pygame.Rect.__init__(self,self.x,self.y,0,0)
    def updatecursor(self):
        (self.left,self.top)=pygame.mouse.get_pos()

class Times(object):
    def __init__(self):
        self.t=0
        self.tde4=0
        self.tde8=0
        self.tde40=0
        self.trespawn=[]
        self.gameover=False
        self.tiempoanterior=0
    def update_times(self):
        #nuevotiempo=pygame.time.get_ticks()
        #if nuevotiempo-self.tiempoanterior>10:
            #print "nuevo ",nuevotiempo
            #print " anterior",self.tiempoanterior
            self.t+=1
            self.tde4+=1
            self.tde8+=1
            self.tde40+=1
            if self.t>1: self.t=0
            if self.tde4>4: self.tde4=0
            if self.tde8>8: self.tde8=0
            if self.tde40>140: self.tde40=0
            for respawntimes in self.trespawn:
                respawntimes.update()

            
                



class Info(pygame.sprite.Sprite):
    def __init__(self,fps=0):
        self.listatexto=[]
        self.iconlevel=pygame.image.load("ChelinsWorld/iconlevel1.png").convert_alpha() 
        self.iconlevelup=pygame.image.load("ChelinsWorld/iconlevel.png").convert_alpha() 
        self.fondo=pygame.image.load("ChelinsWorld/infofondo.png").convert_alpha() 
        self.iconhp=pygame.image.load("ChelinsWorld/iconhp.png").convert_alpha()  
        self.icondano=pygame.image.load("ChelinsWorld/icondano.png").convert_alpha()
        self.iconmagic=pygame.image.load("ChelinsWorld/iconmagic.png").convert_alpha()
        self.iconspeed=  pygame.image.load("ChelinsWorld/iconspeed.png").convert_alpha()
        self.iconpot=pygame.image.load("ChelinsWorld/iconpot.png").convert_alpha()  
        self.icongold=pygame.image.load("ChelinsWorld/icongold.png").convert_alpha()
        self.iconskills=pygame.image.load("ChelinsWorld/skillon.png").convert_alpha()        
        self.listaimagenes=[self.iconlevel,self.iconlevelup,self.iconhp,self.icondano,self.iconmagic,self.iconspeed ,self.iconpot,self.icongold,self.iconskills]  
        self.botones=pygame.image.load("ChelinsWorld/botones.png").convert_alpha()
        self.fps=pygame.font.SysFont("Arial", 14, True, False).render("0",0,(255,255,255))
       
    def update(self,pantalla,fps,player):
        self.fps=pygame.font.SysFont("Arial", 14, True, False).render("FPS: "+str(round(fps,2)),0,(255,255,255))
        self.maketext(player,fps)
        ypad=3
        ypad2=3
        pantalla.blit(self.fondo,(-1,0))        
        for textos in self.listatexto:
            pantalla.blit(textos,(40,ypad))
            ypad+=25
        
 
        for icono in self.listaimagenes:
            pantalla.blit(icono,(7,ypad2))
            ypad2+=25
        pantalla.blit(self.botones,(10,550))
        pantalla.blit(self.fps,(650,10))
            
            
    def maketext(self,player,fps):
       
        self.text2="Level: " + str(player.level)
        self.textsurface2= pygame.font.SysFont("Arial", 14, True, False).render(self.text2,0,(255,255,255))
       
        self.text3="Xp to lvl: " + str(player.xptonextlevel-player.xp)
        self.textsurface3= pygame.font.SysFont("Arial", 14, True, False).render(self.text3,0,(255,255,255))
        
        self.text4=str(player.hp)+" / "+ str(player.hpmax)+" HP"
        self.textsurface4= pygame.font.SysFont("Arial", 14, True, False).render(self.text4,0,(255,255,255))        
        
        self.text5="Damage: " + str(player.dano)
        self.textsurface5= pygame.font.SysFont("Arial", 14, True, False).render(self.text5,0,(255,255,255))        

        self.text6="Magic: "+str(int(player.magic))
        self.textsurface6= pygame.font.SysFont("Arial", 14, True, False).render(self.text6,0,(255,255,255))        


        self.text7="Speed: "+str(int(player.velocidad*10))
        self.textsurface7= pygame.font.SysFont("Arial", 14, True, False).render(self.text7,0,(255,255,255))        

        
        self.text8="Potions: " + str(player.pots)
        self.textsurface8= pygame.font.SysFont("Arial", 14, True, False).render(self.text8,0,(255,255,255))        
        
        self.text9=str(player.gold)+" Gold"
        self.textsurface9= pygame.font.SysFont("Arial", 14, True, False).render(self.text9,0,(255,255,255))        

        self.text10="Pts Remaining: "+str(player.skillpoints)
        self.textsurface10= pygame.font.SysFont("Arial", 14, True, False).render(self.text10,0,(255,255,255))        
 

        self.listatexto=[self.textsurface2,self.textsurface3,
                         self.textsurface4,self.textsurface5,self.textsurface6,
                         self.textsurface7,self.textsurface8,self.textsurface9,self.textsurface10]                    


class Objeto(pygame.sprite.Sprite):
    def __init__(self,imagen,x=25,y=300,inflate=False):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(y,x)
        self.inflate=inflate
        self.inscreen=False
        if self.inflate:
            self.rect.inflate_ip(-self.rect.width/2,-self.rect.height/2) 

    def update(self,superficie,vx,vy):
            if (self.rect.top>=-300 and self.rect.top<=960 
                 and self.rect.left>=-400 and self.rect.left<=1060):
                self.inscreen=True
            else: self.inscreen=False            
            self.mover(-vx, -vy)
            if self.inflate and self.inscreen:
                superficie.blit(self.imagen,(self.rect.left-self.rect.width/2,self.rect.top-self.rect.height/2))
            elif self.inscreen:
                superficie.blit(self.imagen,self.rect)
              
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)


class Shop(Objeto):
    def __init__(self,imagen,x=25,y=300,tipo="Vida",inflate=False):
        Objeto.__init__(self,imagen,x,y,inflate)
        self.precio=1000
        self.tipo=tipo
        if self.tipo=="Heal":
            self.precio=100
        if self.tipo=="Pots":
            self.precio=300
        self.sound=pygame.mixer.Sound("ChelinsWorld/level.wav")
    def comprar(self,jugador):
        if self.tipo=="Dano":
            jugador.dano+=5
        elif self.tipo=="Vida":
            jugador.hpmax+=20
            jugador.hp+=20
        elif self.tipo== "Pots":
            jugador.pots+=1
        elif self.tipo== "Heal":
            jugador.hp=jugador.hpmax
        elif self.tipo=="Velocidad":
            if jugador.velocidad<=14:
                jugador.velocidad+=0.20
        elif self.tipo=="Magic":
            jugador.magic+=3
       
       
class Gold(pygame.sprite.Sprite):
    def __init__(self,x=350,y=300,cantidad=100,inflate=False):
        self.x=x
        self.y=y
        self.imagen=pygame.image.load("ChelinsWorld/gold.png").convert_alpha()
        self.sound=pygame.mixer.Sound("ChelinsWorld/gold.wav")
        self.cantidad=cantidad
        if self.cantidad>200:
            self.imagen=pygame.image.load("ChelinsWorld/tesoro.png").convert_alpha()
        self.rect=self.imagen.get_rect()
        
        self.rect.left=self.x
        self.rect.top=self.y
        self.inflate=inflate
        if self.inflate:
            self.rect.inflate_ip(-self.rect.width/2,-self.rect.height/2)
    def __str__(self):
        return  str(self.x)+" "+str(self.y)+" "+str(self.cantidad)

    def update(self,superficie,vx,vy):
            self.mover(-vx, -vy)
            if self.inflate:
                superficie.blit(self.imagen,(self.rect.left-self.rect.width/2,self.rect.top-self.rect.height/2))
            else:
                superficie.blit(self.imagen,self.rect)
              
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)    
    
    def destroy(self,listagold):
        if self in listagold:
            self.sound.play()
            listagold.remove(self)
            
                   
class Monster(pygame.sprite.Sprite):
    
    def __init__(self,imagenes,x=340,y=400,direccion=1,distancia_max=60,dano=random.randrange(3,11),hp=100,velocidad=7):
        self.imagenesinicial=imagenes
        self.imagenes=imagenes.lista
        self.imagen=self.imagenes[0][0]
        self.imagen_actual=0
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(y,x)
        self.xinicial,self.yinicial=x,y
        self.hpmax=hp
        self.hp=self.hpmax      
        self.estavivo=True
        self.direccion=direccion
        self.velocidad=velocidad
        self.vx=0
        self.vy=0
        self.distancia_max=distancia_max 
        self.distancia=0
        self.orientacion=0
        self.dano=dano
        signobool=random.randrange(2)
        self.trespawn=0
        self.trespawntotal=1700
        self.primeravez=True
        self.xp=500
        self.active=True
        self.inscreen=False
        self.human=False
        self.frozen=False
        self.tiempofrozen=0
        if signobool==1: self.signo=1
        else:self.signo=-1   
        if self.distancia_max!=0:     
            if direccion==0:
                self.vx=self.signo*self.velocidad
            if direccion == 1:
                self.vy=self.signo*self.velocidad


            
    def update(self,superficie,listamonstro,listagold,vx,vy,t,player):
        self.distancia+=1
        if self.hp<=0:
            self.estavivo=False
 
        self.mover(-vx+self.vx,-vy+self.vy,t)
        if (self.rect.top>=-60 and self.rect.top<=660 
             and self.rect.left>=-60 and self.rect.left<=860):
            self.inscreen=True
        else: self.inscreen=False
        if not self.distancia_max==0:
            if self.primeravez:distancia_max=self.distancia_max/2
            else:distancia_max=self.distancia_max
            if self.distancia>distancia_max: #cambiar de lado
                self.primeravez=False
                if self.vx!=0:self.vx=-self.vx
                elif self.vy!=0:self.vy=-self.vy
                self.distancia=0 
      
        if self.estavivo:
            
            if self.inscreen:
                if self.tiempofrozen==18: 
                    self.frozen=False   
                    self.velocidad+=3
                    self.tiempofrozen=0
                if self.frozen:
                        if self.tiempofrozen==0:
                            self.velocidad-=3
                        self.tiempofrozen+=1

        #control de relantizado

                superficie.blit(self.imagen,self.rect)
                self.printText(superficie,self.rect.left,self.rect.top)
        
        else:
            if self.trespawn==0:
                player.xp+=self.xp
                if random.randrange(2)==1:
                    listagold.append(Gold(self.rect.left+100,self.rect.top+2,25))
                    
            self.trespawn+=1
            if self.trespawn>self.trespawntotal:
                self.estavivo=True
                self.hp=self.hpmax
                self.trespawn=0
 
        if self.human and self.textactive:
            self.hablar(superficie)
            

    def nextimage(self):
        self.imagen_actual+=1
        if self.imagen_actual==len(self.imagenes[self.orientacion]):
            self.imagen_actual=0
        self.imagen=self.imagenes[self.orientacion][self.imagen_actual]            
                   
    def printText(self,surface,x,y):
        if not self.human:
            f1=pygame.font.SysFont("Terminal", 20, False, False)
            if self.estavivo: self.text=str(self.hp)+" / "+str(self.hpmax)
            else: self.text="*DEAD*"
            self.textsurface=f1.render(self.text,0,(0,0,0))
            surface.blit(self.textsurface,(x,y-10))    
                
    def destroy(self,lista):
        if self in lista:
            lista.remove(self) 
                         
    def mover(self,vx,vy,t):
        self.rect.move_ip(vx,vy)               
        if self.vx>0: self.orientacion=0
        elif self.vx<0: self.orientacion=1
        
        if self.vy>0: self.orientacion=2
        elif self.vy<0: self.orientacion=3        
        
        if  t.t==1:
            self.nextimage()          

class Monsterfollower(Monster):
    def __init__(self,imagenes,x=340,y=400,direccion=1,distancia_max=60,dano=random.randrange(3,11),hp=100,velocidad=3,xp=1000,gold=100):
        Monster.__init__(self,imagenes,x,y,direccion,distancia_max,dano,hp)
        self.active=False
        self.velocidad=velocidad
        self.xrecorrido,self.yrecorrido=0,0
        self.vx,self.vy=0,0
        self.xp=xp
        self.trespawntotal=2100
        self.inscreen=False
        self.gold=gold
    def update(self,superficie,listamonstro,listagold,vx,vy,t,player):
        if self.hp<=0:
            self.estavivo=False
        self.mover(-vx+self.vx,-vy+self.vy,t)


        if (self.rect.top>=-60 and self.rect.top<=660 
             and self.rect.left>=-60 and self.rect.left<=860):
            self.inscreen=True
        else: self.inscreen=False
        if (self.rect.top>=20 and self.rect.top<=425 
             and self.rect.left>=125 and self.rect.left<=575):
            """     
            if (self.rect.top>=0 and self.rect.top<=475 
                 and self.rect.left>=75 and self.rect.left<=625): """           
            self.active=True
        else:    self.active=False
        self.vx,self.vy=0,0
        #control de relantizado
        if self.tiempofrozen==18: 
            self.frozen=False   
            self.velocidad+=3
            self.tiempofrozen=0
        if self.active:
            if self.frozen:
                if self.tiempofrozen==0:
                    self.velocidad-=3
                self.tiempofrozen+=1

            self.vx,self.vy=0,0
            if self.rect.left>290:
                self.vx=-self.velocidad
            elif self.rect.left<=290:
                self.vx=self.velocidad
            
            if self.rect.top>270:
                self.vy=-self.velocidad
            elif self.rect.top<272:
                self.vy=self.velocidad
            if self.rect.top>269 and self.rect.top<274:
                self.vy=0  
            self.xrecorrido+=self.vx
            self.yrecorrido+=self.vy
        if self.inscreen and self.estavivo:      
                superficie.blit(self.imagen,self.rect)
                self.printText(superficie,self.rect.left,self.rect.top) 
        if not(self.estavivo):
            self.vx,self.vy=0,0
            if self.trespawn==0:
                player.xp+=self.xp                       
                self.rect.move_ip(-self.xrecorrido,-self.yrecorrido)
                if random.randrange(2)==1:
                    listagold.append(Gold(self.rect.left+10,self.rect.top+2,self.gold))
            self.trespawn+=1
            if self.trespawn>self.trespawntotal:
                self.estavivo=True
                self.hp=self.hpmax
                self.trespawn=0
                self.vx,self.vy=0,0
                self.active=False

class Boss(pygame.sprite.Sprite):
    def __init__(self,imagenes,x=340,y=400,dano=random.randrange(3,11),hp=100,velocidad=3):
        self.imagenesinicial=imagenes
        self.imagenes=imagenes.lista
        self.imagen=self.imagenes[0][0]
        self.imagen_actual=0
        self.active=False
        self.velocidad=velocidad
        self.xrecorrido,self.yrecorrido=0,0
        self.vx,self.vy=0,0
        self.xp=100000
        self.inscreen=False
 
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(y,x)
        #self.rect.inflate_ip(-self.rect.width/2,-self.rect.height/2)
        self.xinicial,self.yinicial=x,y
        self.hpmax=hp
        self.hp=self.hpmax      
        self.estavivo=True
        self.direccion=0
        self.velocidad=velocidad
        self.distancia=0
        self.orientacion=0
        self.dano=dano
        self.trespawn=0
        self.trespawntotal=100000
        self.primeravez=True
        self.xp=500
        self.human=False
        self.spawning=False
        self.spawningimage=pygame.image.load("ChelinsWorld/aliinvocando.png").convert_alpha()
        self.spawningsound=pygame.mixer.Sound("ChelinsWorld/spawn.wav")
        self.tspawnbicho=0
        self.tspawnbichototal=150
        self.frozen=False
        self.tiempofrozen=0
    def update(self,superficie,listamonstro,listagold,vx,vy,t,player):
        if self.hp<=0:
            if self.estavivo:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("ChelinsWorld/victory.mid")
                pygame.mixer.music.play()
                listamonstro.insert(0,Teleporter(iportal,300,100))
            self.estavivo=False
        self.mover(-vx+self.vx,-vy+self.vy,t)
        if (self.rect.top>=-200 and self.rect.top<=660 
             and self.rect.left>=-200 and self.rect.left<=860):
            self.inscreen=True
        else: self.inscreen=False
        if (self.rect.bottom>=20 and self.rect.bottom<=650 
             and self.rect.left>=-200 and self.rect.left<=900):
            self.active=True
        else:    self.active=False
        self.vx,self.vy=0,0
        
        if self.tiempofrozen==13: 
            self.frozen=False   
            self.velocidad+=3
            self.tiempofrozen=0
            
        if self.active:
            if self.frozen:
                if self.tiempofrozen==0:
                    self.velocidad-=3
                self.tiempofrozen+=1                      
            self.vx,self.vy=0,0
            
            
            if self.rect.left>270:
                self.vx=-self.velocidad
            elif self.rect.left<270:
                self.vx=self.velocidad
            
            if self.rect.bottom>348:
                self.vy=-self.velocidad
            elif self.rect.bottom<353:
                self.vy=self.velocidad
                
            if self.rect.bottom>348 and self.rect.bottom<353:
                self.vy=0
                
            self.xrecorrido+=self.vx
            self.yrecorrido+=self.vy
            
            if self.estavivo and (self.tspawnbicho>self.tspawnbichototal):
                self.spawn(t,listamonstro,player)
                
            self.tspawnbicho+=1
        if self.spawning and t.tde40==40:
               self.spawning=False
            
        if self.inscreen and self.estavivo:      
                superficie.blit(self.imagen,self.rect)
                self.printText(superficie,self.rect.left,self.rect.top) 
        if not(self.estavivo):
            self.vx,self.vy=0,0
            if self.trespawn==0:
                player.xp+=self.xp                       
                self.rect.move_ip(-self.xrecorrido,-self.yrecorrido)
                for x in range(30):
                    listagold.append(Gold(random.randrange(250,400),random.randrange(150,350),100))
            self.trespawn+=1
            if self.trespawn>self.trespawntotal:
                self.estavivo=True
                self.hp=self.hpmax
                self.trespawn=0
                self.vx,self.vy=0,0
                self.active=False
            
    def nextimage(self):
            if self.spawning:
                self.imagen=self.spawningimage
            else:
                self.imagen_actual+=1
                if self.imagen_actual==len(self.imagenes[self.orientacion]):
                    self.imagen_actual=0
                self.imagen=self.imagenes[self.orientacion][self.imagen_actual]            
                   
    def printText(self,surface,x,y):
        if not self.human:
            f1=pygame.font.SysFont("Terminal", 20, False, False)
            if self.estavivo: self.text=str(self.hp)+" / "+str(self.hpmax)
            else: self.text="*DEAD*"
            self.textsurface=f1.render(self.text,0,(0,0,0))
            surface.blit(self.textsurface,(x,y-10))    
                
    def destroy(self,lista):
        if self in lista:
            lista.remove(self) 
                         
    def mover(self,vx,vy,t):
        self.rect.move_ip(vx,vy)               
        if self.vx>0: self.orientacion=0
        elif self.vx<0: self.orientacion=1
        
        if self.vy>0: self.orientacion=2
        elif self.vy<0: self.orientacion=3        
        
        if  t.t==1:
            self.nextimage()          

    def spawn(self,t,listamonstro,player):
            self.spawningsound.play()
            t.tde40=0
            self.spawning=True
            self.tspawnbicho=0
            r=random.randrange(3)
            if r==0:
                listamonstro.append(Monsterfollower(iskeletonred,player.rect.left-100,player.rect.top+100,1,1,1,1000,7,1000))
            if r==1:
                listamonstro.append(Monsterfollower(iskeletongreen,player.rect.left-100,player.rect.top+110,1,1,1,1000,5,1000))
            if r==2:
                listamonstro.append(Monsterfollower(ibarbarian,player.rect.left-70,player.rect.top+70,1,1,1,1000,4,1000))

class Aldeano(Monster):
    def __init__(self,imagenes,x=340,y=400,direccion=1,distancia_max=60,
                 dano=random.randrange(3,11),hp=100,text="HOLA",textactive=False,velocidad=1):
        Monster.__init__(self,imagenes,x,y,direccion,distancia_max,dano,hp,velocidad)
        self.human=True
        self.text=self.obtenertexto(text)
        self.textactive=textactive
        self.time=0
        self.fondo=pygame.image.load("ChelinsWorld\\texto.png")
        self.sound=pygame.mixer.Sound("ChelinsWorld/text.wav")
        self.sound.set_volume(1)
    def obtenertexto(self,text):
        if text:
            if len(text)>27:   listatexto=[text[0:27],text[27:]]
            else:  listatexto=[text]
            return listatexto
            
        
    def hablar(self,surface): 
        if self.time==0:
            self.sound.play()
        self.time+=1
        f1=pygame.font.SysFont("verdana", 14, True, False)
        xpad,ypad=5,5

        if self.text:
            surface.blit(self.fondo,(self.rect.left-75,self.rect.top-55))
            for textos in self.text:
                self.textsurface=f1.render(textos,0,(255,255,255))          
                surface.blit(self.textsurface,(self.rect.left-70,self.rect.top-55+ypad))
                ypad+=15
            if self.time>150:
                self.time=0
                self.textactive=False               
           

class Teleporter(Aldeano):
    def __init__(self,imagenes,x=4189,y=538,direccion=0,distancia_max=0,
                 dano=random.randrange(3,11),hp=100,text="You are now known as        the champion of Acrono",textactive=False,velocidad=1):
       Aldeano.__init__(self, imagenes, x, y, direccion, distancia_max, dano, hp, text, textactive, velocidad)   
       self.teleporton=False
       self.zona="none"
    def teleport(self):
        self.teleporton=True
    def teleport_on_contact(self):
        pass           
class Teleporter_on_contact(Aldeano):
    def __init__(self,imagenes,x=4189,y=538,direccion=0,distancia_max=0,
                 dano=random.randrange(3,11),hp=100,text=None,textactive=False,velocidad=1):
       Aldeano.__init__(self, imagenes, x, y, direccion, distancia_max, dano, hp, text, textactive, velocidad)   
       self.teleporton=False    
       self.tipo="Teleporter_on_contact"
       self.zona="ice"
    def teleport_on_contact(self):
        if self.zona=="ice":        
            self.teleport()
    def teleport(self):
        self.teleporton=True  
                    
class fireball(pygame.sprite.Sprite):
    def __init__(self,player):
        player.casting=True
        
        self.tipo="fireball"
        self.imagenes=[[ifireballr,ifireballr2],[ifireballl,ifireballl2],[ifireballt,ifireballt2],[ifireballb,ifireballb2]]
        self.imagen_numero=0
        self.imagen=self.imagenes[player.orientacion][self.imagen_numero]
        self.rect=self.imagen.get_rect()
        self.insets=[[-5,10],[-5,-20],[-65,5],[10,5]]
        self.rect.top,self.rect.left=player.rect.top+self.insets[player.orientacion][0],player.rect.left+self.insets[player.orientacion][1]
        self.delta=0
        self.tiempototal=12
        self.velocidadtiempo=1
        self.dano=5
        self.orientacion=player.orientacion
        self.vx,self.vy=0,0
        self.sound=fireballsound
    def update(self,superficie,lista,jugador,listamonster,listashop,attack,vx,vy,t):
        self.delta+=self.velocidadtiempo
        if self.delta%3==0:
            self.imagen_numero=1
        else: self.imagen_numero=0
        jugador.estapegando=False       
        if self.orientacion==0:self.vx=20
        elif self.orientacion==1: self.vx=-20
        elif self.orientacion==2: 
            self.vy=-20
            self.velocidadtiempo=2
        elif self.orientacion==3: 
            self.vy=20
            self.velocidadtiempo=2
        self.rect.move_ip(-vx+self.vx,-vy+self.vy,)
        if self.delta>self.tiempototal:
            self.destroy(lista,jugador)
        for monster in listamonster:
            if   monster.estavivo and monster.active and self.rect.colliderect(monster.rect) and t.t==1 and not monster.human:
                monster.hp-=self.dano+(7*jugador.magic/8)
                self.sound.play()
                pygame.draw.rect(superficie,(250,0,0),monster.rect)
                self.destroy(lista,jugador)
            if monster.human and self.rect.colliderect(monster.rect):
                monster.textactive=True
                if  isinstance(monster,Teleporter):
                    monster.teleport()
                    self.destroy(lista, jugador)
        for shop in listashop:
            if self.rect.colliderect(shop.rect) and jugador.gold>=shop.precio:
                jugador.gold-=shop.precio
                shop.comprar(jugador)
                shop.sound.play()
                pygame.draw.rect(superficie,(0,255,0),shop.rect)
                self.destroy(lista,jugador)              
        self.imagen=self.imagenes[self.orientacion][self.imagen_numero]
        superficie.blit(self.imagen,self.rect)
    def destroy(self,lista,player):
        if self in lista:
            if len(lista)<=1:
                player.estapegando=False                
            lista.remove(self)
            player.casting=False
   


class Hielo(fireball):
    def __init__(self,player):
        fireball.__init__(self, player)
        self.tipo="hielo"
        self.imagenes=[[isnowballr,isnowballr2],[isnowballl,isnowballl2],[isnowballt,isnowballt2],[isnowballb,isnowballb2]]
        self.sound=snowballsound
    def update(self,superficie,lista,jugador,listamonster,listashop,attack,vx,vy,t):
        self.delta+=self.velocidadtiempo
        if self.delta%3==0:
            self.imagen_numero=1
        else: self.imagen_numero=0
        jugador.estapegando=False       
        if self.orientacion==0:self.vx=20
        elif self.orientacion==1: self.vx=-20
        elif self.orientacion==2: 
            self.vy=-20
            self.velocidadtiempo=2
        elif self.orientacion==3: 
            self.vy=20
            self.velocidadtiempo=2
        self.rect.move_ip(-vx+self.vx,-vy+self.vy,)
        if self.delta>self.tiempototal:

            self.destroy(lista,jugador)
        for monster in listamonster:
            if   monster.estavivo and monster.active and self.rect.colliderect(monster.rect)and t.t==1 and not monster.human:
                monster.hp-=self.dano+(jugador.magic)/3
                if not(monster.frozen): 
                    monster.frozen=True
                self.sound.play()
                pygame.draw.rect(superficie,(250,0,0),monster.rect)
                self.destroy(lista,jugador)
            if monster.human and self.rect.colliderect(monster.rect):
                monster.textactive=True
                if  isinstance(monster,Teleporter):

                    monster.teleport()
                    self.destroy(lista, jugador)
        for shop in listashop:
            if self.rect.colliderect(shop.rect) and jugador.gold>=shop.precio:
                jugador.gold-=shop.precio
                shop.comprar(jugador)
                shop.sound.play()
                pygame.draw.rect(superficie,(0,255,0),shop.rect)
                self.destroy(lista,jugador)              
        self.imagen=self.imagenes[self.orientacion][self.imagen_numero]
        superficie.blit(self.imagen,self.rect)

class espada(pygame.sprite.Sprite):
    def __init__(self,player):
        player.estapegando=True
        if player.acrono:self.imagenes=[[iespadaacrono,iespadaacrono2]
                                        ,[iespadaacronol,iespadaacronol2]
                                        ,[iespadaacronot,iespadaacronot2],
                                        [iespadaacronob,iespadaacronob2]]
        else: self.imagenes=[[iespada,iespada2],[iespadal,iespadal2],[iespadat,iespadat2],[iespadab,iespadab2]]
        self.orientacion=player.orientacion
        self.imagen=self.imagenes[self.orientacion][0]
        self.rect=self.imagen.get_rect()
        self.tipo="espada"
        self.insets=[[-15,15],[-15,-25],[-65,5],[10,5]]
        self.rect.top,self.rect.left=player.rect.top+self.insets[player.orientacion][0],player.rect.left+self.insets[player.orientacion][1]
        self.delta=0
        self.tiempototal=5
        self.velocidadtiempo=1
        self.dano=5
        self.numero_imagen=0
    def update(self,superficie,lista,jugador,listamonster,listashop,attack,t):
        self.delta+=self.velocidadtiempo
        if self.delta>self.tiempototal:
            self.destroy(lista,jugador)
        if self.delta%3==0: self.numero_imagen=1
        else:self.numero_imagen=0
        for monster in listamonster:
            if   monster.active and monster.estavivo and self.rect.colliderect(monster.rect) and t.tde4==2 and not monster.human:
                monster.hp-=self.dano+jugador.dano
                attack.play()
                pygame.draw.rect(superficie,(250,0,0),monster.rect)
                self.destroy(lista,jugador)
            if monster.human and self.rect.colliderect(monster.rect):
                monster.textactive=True
                if  isinstance(monster,Teleporter):
                    monster.teleport()
                    self.destroy(lista, jugador)
        for shop in listashop:
            if self.rect.colliderect(shop.rect) and jugador.gold>=shop.precio:
                jugador.gold-=shop.precio
                shop.comprar(jugador)
                shop.sound.play()
                pygame.draw.rect(superficie,(0,255,0),shop.rect)
                self.destroy(lista,jugador)              
        for spell in lista:
            if spell.tipo=="fireball" or spell.tipo=="hielo": return
        self.imagen=self.imagenes[self.orientacion][self.numero_imagen]
        superficie.blit(self.imagen,self.rect)
    def destroy(self,lista,player):
        if self in lista:
            if len(lista)<=1:
                player.estapegando=False                
            lista.remove(self)
   

class Player(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,imagen1l,imagen2l,imagen1t,imagen2t,imagen1b,imagen2b):
        self.imagenes=[[imagen1,imagen2],[imagen1l,imagen2l],[imagen1t,imagen2t],[imagen1b,imagen2b]]
        self.imagenescasting=[icastingr,icastingl,icastingt,icastingb]
        self.imagenescastingacrono=[icastingacronor,icastingacronol,icastingacronot,icastingacronob]
        self.imagendead=pygame.image.load("ChelinsWorld/dead.png").convert_alpha()        
        
        self.imagen=self.imagenes[3][0]
        self.rect=self.imagen.get_rect()
        self.rect.height=self.rect.height/2
        self.rect.top,self.rect.left=(300,330)
        self.moving=False
        self.imagen_actual=0
        self.orientacion=3
        self.xp=0
        self.xptonextlevel=1500
        self.level=1
        self.velocidad=8
        self.hpmax=100
        self.hp=100
        self.gold=0
        self.dano=5
        self.magic=5
        self.pots=1
        self.skillpoints=1
        self.estavivo=True
        self.leveledup=False
        self.enablepots=True
        self.estapegando=False
        self.casting=False
        self.acrono=0
    def mover(self,vx,vy):
        if vx == 0 and vy ==0: self.moving=False
        else: 
            self.moving=True
            if vx>0: self.orientacion=0
            else: self.orientacion=1
            if vy<0: self.orientacion=2
            elif vy>0: self.orientacion=3
        self.rect.move_ip(vx,vy)

    def update(self,listamonster,listagold,superficie,t,hited,levelup):
        if self.hp<=0:
            self.estavivo=False
        if t.tde8==8 and self.leveledup:
            self.leveledup=False
        if self.xp>=self.xptonextlevel:
            self.levelup(superficie,levelup,t)
        if self.casting and not(self.estapegando):
            self.imagen=self.imagenescasting[self.orientacion]
        elif not(self.moving):self.imagen=self.imagenes[self.orientacion][1]
        if self.moving and t.t==1:
            self.nextimage()        
        for monster in listamonster:
            if  monster.active and monster.estavivo and self.rect.colliderect(monster.rect) and t.t==1 and not(t.gameover) and not(monster.human):
                self.hp-=monster.dano
                pygame.draw.rect(superficie,(255,0,0),self.rect)
                hited.play()
            if isinstance(monster,Teleporter_on_contact):
                 if monster.rect.colliderect(self.rect):
                     monster.teleport_on_contact()
        for gold in listagold:
            if self.rect.colliderect(gold.rect):
                self.gold+=gold.cantidad
                gold.destroy(listagold)
        self.printText(superficie, self.rect.left, self.rect.top-self.rect.height)
        if not self.estapegando:
            if self.hp<=0:self.imagen=self.imagendead
            superficie.blit(self.imagen,(self.rect.left,self.rect.top-self.rect.height) )
        
    def printText(self,surface,x,y):
        f1=pygame.font.SysFont("Terminal", 20, False, False)
        if self.estavivo: self.text=str(self.hp)+" / " + str(self.hpmax)
        else: self.text="*DEAD*"
        self.textsurface=f1.render(self.text,0,(0,0,0))
        surface.blit(self.textsurface,(x,y-10))
        if self.leveledup:
            pygame.draw.rect(surface,(255,245,0),self.rect)
            self.textsurface2 = pygame.font.SysFont("Arial", 14, True, False).render("LEVEL UP!",0,(255,255,255))
            surface.blit(self.textsurface2,(x,y-30))                   
    def nextimage(self):
        if self.casting:
            self.imagen=self.imagenescasting[self.orientacion]
        else:
            self.imagen_actual+=1
            if self.imagen_actual==len(self.imagenes[self.orientacion]):
                self.imagen_actual=0
            self.imagen=self.imagenes[self.orientacion][self.imagen_actual]

    def levelup(self,superficie,levelup,t):
            self.leveledup=True
            self.level+=1
            t.tde8=0
            self.xp=0
            if self.level<=12:self.xptonextlevel=(self.level**(2))*1500
            else: 
                x=self.level**3
                self.xptonextlevel=math.log(x,2)*20000+10000
            self.xptonextlevel=(round(self.xptonextlevel,0))
            levelup.play()
            self.dano+=0
            self.magic+=0
            self.hpmax+=20
            self.skillpoints+=10
            if self.hp<=75:
                self.hp+=25          
    def usepot(self):

        if self.pots>0:
            self.pots-=1
            heal=self.hpmax/4+self.hpmax/2
            self.hp+=heal
            pygame.mixer.Sound("ChelinsWorld/pot.wav").play()
            if self.hp>self.hpmax:
                self.hp=self.hpmax
        self.lockpots()
    def lockpots(self):
        self.enablepots=False
    def unlockpots(self):
        self.enablepots=True

    def setacrono(self):
        imagen1=pygame.image.load("ChelinsWorld/acronor1.png").convert_alpha()
        imagen2=pygame.image.load("ChelinsWorld/acronor2.png").convert_alpha()
        imagen1l=pygame.image.load("ChelinsWorld/acronol1.png").convert_alpha()
        imagen2l=pygame.image.load("ChelinsWorld/acronol2.png").convert_alpha()    
        imagen1t=pygame.image.load("ChelinsWorld/acronot1.png").convert_alpha()
        imagen2t=pygame.image.load("ChelinsWorld/acronot2.png").convert_alpha()
        imagen1b=pygame.image.load("ChelinsWorld/acronob1.png").convert_alpha()
        imagen2b=pygame.image.load("ChelinsWorld/acronob2.png").convert_alpha()
        self.imagenes=[[imagen1,imagen2],[imagen1l,imagen2l],[imagen1t,imagen2t],[imagen1b,imagen2b]]
        self.imagenescasting=self.imagenescastingacrono
class Fondo(pygame.sprite.Sprite):
    def __init__(self,imagen,x=-250,y=-1370):
        self.imagen=imagen
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(x,y)
    def mover(self,vx,vy):
        self.rect.move_ip(vx,vy)
    def update(self,superficie,vx,vy):
        self.mover(-vx, -vy)
        superficie.blit(self.imagen,self.rect)        
  
  
def save(player,listagold):
        destino=open("save.data","w+")
        destinogold=open("save.data2","w+")
        listaguardar=[player.xp, player.xptonextlevel, player.level,player.hpmax,player.hp,
                      player.velocidad,player.gold,player.dano,player.magic,player.pots,player.acrono,player.skillpoints]
        for x in range(len(listaguardar)):
            destino.write(str(listaguardar[x])+"\n")


        for x in listagold:
            destinogold.write(str(x)+"\n")
        destino.close()
        destinogold.close()
def load(player,listagold):
        listagolda=[]
        origen=open("save.data","r+")
        origengold=open("save.data2","r+")
        listacargar=[]
        for linea in origen:
            linea=linea.rstrip("\n")
            try:
                linea=int(linea)
            except:
                linea=float(linea)
            
            listacargar.append(linea)
        player.xp=listacargar[0]
        player.xptonextlevel=listacargar[1]
        player.level=listacargar[2]
        player.hpmax=listacargar[3]
        player.hp=listacargar[4]
        player.velocidad=listacargar[5]
        player.gold=listacargar[6]
        player.dano=listacargar[7]
        player.magic=listacargar[8]       
        player.pots=listacargar[9]
        player.acrono=listacargar[10]
        player.skillpoints=listacargar[11]        
        if player.acrono==1:
            player.setacrono()
        for linea in origengold:
            linea=linea.rstrip("\n")
            linea= linea.split()
            for x in range(len(linea)):
                linea[x]=int(linea[x])
            listagolda.append(Gold(linea[0],linea[1],linea[2]))
        origen.close()
        origengold.close()
        return listagolda
    
def loadmusic():
    pygame.mixer.quit()
    pygame.mixer.init()
    listamusic=[
    "ChelinsWorld/melodyfire.mid"
    ,"ChelinsWorld/melodyrpg.mid"
    ,"ChelinsWorld/melodytime.mid"
    ,"ChelinsWorld/melody2.mid"
    ,"ChelinsWorld/castle2.mid"
    ,"ChelinsWorld/castle3.mid"
    ,"ChelinsWorld/castle4.mid"
    ]
    longitud=  len(listamusic) 
    r=random.randrange(longitud)  
    musica=listamusic.pop(r) 
    pygame.mixer.music.load(musica)
    longitud-=1   
    while longitud>0:
        r=random.randrange(longitud)  
        musica=listamusic.pop(r)
        pygame.mixer.music.queue(musica)
        longitud-=1
    
    
    
def movercosas(player,fondo,pantalla,listamonster,listaechizos,
               listaobjetos,listawalls,listagold,vx,vy,t,attack,hited,levelup):
        velocidad=7
        colision=False
        listashop=[]
        monstervx=vx  #auxiliares
        monstervy=vy        
        fondo.update(pantalla,vx, vy)
        #muevo las cosas
        for wall in listawalls:
            wall.move_ip(-vx,-vy)
        for objeto in listaobjetos:        
            objeto.update(pantalla,vx,vy)          
            if  isinstance(objeto, Shop):
                listashop.append(objeto)
         #con el nuevo mov evaluo q paso
        for objeto in listaobjetos:
            if objeto.rect.colliderect(player.rect): 
                vx,vy=-vx,-vy
                colision=True
                break
        for wall in listawalls:
            if wall.colliderect(player.rect):
                vx,vy=-vx,-vy
                colision=True
                break
            
        # si colisionaron entoncees volver atras   
        if colision==True:
            fondo.update(pantalla,vx, vy)
            for wall in listawalls:
                wall.move_ip(-vx,-vy)
            for objeto in listaobjetos:        
                objeto.update(pantalla,vx,vy)
            monstervx=0#uaxiliares
            monstervy=0  
            
                   
        for monster in listamonster:
            monster.update(pantalla,listamonster,listagold,monstervx,monstervy,t,player)
        for gold in listagold:
            gold.update(pantalla,monstervx,monstervy)
        player.update(listamonster,listagold,pantalla,t,hited,levelup)
        for echizo in listaechizos:
            if isinstance (echizo,fireball):echizo.update(pantalla,listaechizos,player,listamonster,listashop,attack,monstervx,monstervy,t)
            else: echizo.update(pantalla,listaechizos,player,listamonster,listashop,attack,t)
         


def bossfight(player1):
    import pygame

    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("::: The Skeleton Quest RPG v0.7 :::")
    pygame.display.set_icon(pygame.image.load("ChelinsWorld/iconlevel1.png").convert_alpha())
    pygame.mixer.music.load("ChelinsWorld/melodyboss.mid")
    reloj1= pygame.time.Clock()
    botonaudio=BotonAudio(760,5)
    fondo1=Fondo(pygame.image.load("ChelinsWorld/fondoboss.gif"),-250,-250)
    cursor1=cursor()
    botonhp=Botonskill(130,50)
    botondamage=Botonskill(130,75)
    botonmagic=Botonskill(130,100)
    botonspeed=Botonskill(130,125)    
    #player1=player1
    infotext= Info(0)
    vx,vy=0,0
    velocidad=8
    t= Times()
    listaechizos=[]
    listamonster=[ Boss(iali,1100,400,random.randrange(2, 3),20000,4)]
    listagold=[]
    listaobjetos=[]
    listawalls=[pygame.Rect(150,190,1100,3),pygame.Rect(150,210,3,700)
                ,pygame.Rect(150,700,1100,3),pygame.Rect(1260,190,3,700)]
    printsave,salir=False,False
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    pygame.mixer.music.play(10)
    termino="quit"
    pantalla.blit(player1.imagen,player1.rect)
    while salir!=True:#LOOP PRINCIPAL    
        reloj1.tick(28)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
                termino="quit"
                
            if  t.gameover:
                    if event.key==pygame.K_RETURN:
                        return "reload"
                    if event.key==pygame.K_ESCAPE:
                        return "quit"              
                
            else:    
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        if player1.skillpoints>0:
                            if cursor1.colliderect(botonhp):
                                player1.hpmax+=8
                                if player1.hp==player1.hpmax:player1.hp+=8
                                player1.skillpoints-=1
                            elif cursor1.colliderect(botondamage):
                                player1.dano+=1
                                player1.skillpoints-=1                                
                            elif cursor1.colliderect(botonmagic):
                                player1.magic+=1
                                player1.skillpoints-=1  
                            elif cursor1.colliderect(botonspeed):
                                if player1.velocidad<=14:
                                    player1.velocidad+=0.20  
                                    player1.skillpoints-=1                        
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-player1.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=player1.velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-player1.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=player1.velocidad
                    if event.key == pygame.K_d:
                        auxfireball=False
                        for spells in listaechizos:
                            if spells.tipo=="hielo": auxfireball=True
                        if not(auxfireball):listaechizos.append(Hielo(player1))                        
                    if event.key == pygame.K_s:
                        auxfireball=False
                        for spells in listaechizos:
                            if spells.tipo=="fireball": auxfireball=True
                        if not(auxfireball):listaechizos.append(fireball(player1))                       
                    if event.key == pygame.K_a:
                        listaechizos.append(espada(player1))      
                    if event.key ==pygame.K_f:
                        player1.usepot()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=player1.velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-player1.velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=player1.velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-player1.velocidad
                        else:vy=0                    
                    if event.key ==pygame.K_f:
                        player1.unlockpots()
                    if event.key==pygame.K_F1:
                        t.tde40=0
                        printsave=True
                        save(player1,listagold)
                    if event.key==pygame.K_m:
                        botonaudio.cambiar_estado()

        pantalla.fill((255,255,255))
        player1.mover(vx/1000.0, vy/1000.0) 
        movercosas(player1,fondo1,pantalla,listamonster,listaechizos,
               listaobjetos,listawalls,listagold,vx,vy,t,attack,hited,levelup)                  
        t.update_times()     
        if player1.hp<=0:
            if t.gameover==False:
                gameoversound.play()
            t.gameover=True
            vx,vy=0,0
            pygame.mixer.music.stop()
            pantalla.blit(igameover,(200,50))
            player1.imagen=pygame.image.load("ChelinsWorld/dead.png").convert_alpha()

        #for wall in listawalls:
         # pygame.draw.rect(pantalla,(255,0,0),wall)
        infotext.update(pantalla,reloj1.get_fps(),player1)
        
        if printsave:
            if t.tde40>=40:
                printsave=False
            pantalla.blit(
                          pygame.font.SysFont("Arial", 46, True, False)
                          .render("GAME SAVED..",1,(255,255,255)),(300,150)
                          )
        cursor1.updatecursor()
        botonaudio.update(pantalla)
        botonhp.update(pantalla, player1)
        botondamage.update(pantalla, player1)
        botonmagic.update(pantalla, player1)
        botonspeed.update(pantalla, player1)             
        pygame.display.update()
        if isinstance(listamonster[0],Teleporter):
            if listamonster[0].teleporton:
                listamonster[0].teleporton=False
                termino="ok"
                salir=True
                player1.vx=0
                player1.vy=0      
    return termino

def ice(player1):
    import pygame

    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("::: The Skeleton Quest RPG v0.7 :::")
    pygame.display.set_icon(pygame.image.load("ChelinsWorld/iconlevel1.png").convert_alpha())
    loadmusic()
    reloj1= pygame.time.Clock()
    botonaudio=BotonAudio(760,5)
    fondo1=Fondo(pygame.image.load("ChelinsWorld/ice.png"),-150,0)
    cursor1=cursor()
    nieve1=Snow()
    botonhp=Botonskill(130,50)
    botondamage=Botonskill(130,75)
    botonmagic=Botonskill(130,100)
    botonspeed=Botonskill(130,125)    
    #player1=player1
    infotext= Info(0)
    vx,vy=0,0
    velocidad=8
    t= Times()
    listaechizos=[]
    listamonster=[Teleporter_on_contact(ientradaice,250,200)
                  ,Monsterfollower(ifuryorc,1000,200,1,1,5,5000,5,22000,350)
                  ,Monsterfollower(ifuryorc,532,1031,1,1,5,5000,5,22000,350)
                  ,Monsterfollower(ifuryorc,1644,586,1,1,5,5000,5,22000,350)
                  ,Monsterfollower(ifuryorc,1941,1274,1,1,5,5000,5,22000,350)
                  ,Monsterfollower(ifuryorc,2576,738,1,1,5,5000,5,22000,350)
                  ,Monsterfollower(ifuryorc,2576,971,1,1,5,5000,5,22000,350)
                  ,Monsterfollower(ifuryorc,1135,1781,1,1,5,5000,5,22000,350)
                  ]
    listagold=[]
    listaobjetos=[]
    listawalls=[]
    printsave,salir=False,False
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    pygame.mixer.music.play(10)
    termino="quit"
    pantalla.blit(player1.imagen,player1.rect)
    while salir!=True:#LOOP PRINCIPAL    
        reloj1.tick(28)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
                termino="quit"
                
            if  t.gameover:
                    if event.key==pygame.K_RETURN:
                        return "reload"
                    if event.key==pygame.K_ESCAPE:
                        return "quit"              
                
            else:    
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        if player1.skillpoints>0:
                            if cursor1.colliderect(botonhp):
                                player1.hpmax+=8
                                if player1.hp==player1.hpmax:player1.hp+=8
                                player1.skillpoints-=1
                            elif cursor1.colliderect(botondamage):
                                player1.dano+=1
                                player1.skillpoints-=1                                
                            elif cursor1.colliderect(botonmagic):
                                player1.magic+=1
                                player1.skillpoints-=1  
                            elif cursor1.colliderect(botonspeed):
                                if player1.velocidad<=14:
                                    player1.velocidad+=0.20  
                                    player1.skillpoints-=1                        
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-player1.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=player1.velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-player1.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=player1.velocidad
                    if event.key == pygame.K_d:
                        auxfireball=False
                        for spells in listaechizos:
                            if spells.tipo=="hielo": auxfireball=True
                        if not(auxfireball):listaechizos.append(Hielo(player1))                        
                    if event.key == pygame.K_s:
                        auxfireball=False
                        for spells in listaechizos:
                            if spells.tipo=="fireball": auxfireball=True
                        if not(auxfireball):listaechizos.append(fireball(player1))                       
                    if event.key == pygame.K_a:
                        listaechizos.append(espada(player1))      
                    if event.key ==pygame.K_f:
                        player1.usepot()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=player1.velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-player1.velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=player1.velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-player1.velocidad
                        else:vy=0                    
                    if event.key ==pygame.K_f:
                        player1.unlockpots()
                    if event.key==pygame.K_F1:
                        t.tde40=0
                        printsave=True
                        save(player1,listagold)
                    if event.key==pygame.K_m:
                        botonaudio.cambiar_estado()

        pantalla.fill((191,255,255))
        player1.mover(vx/1000.0, vy/1000.0) 
        movercosas(player1,fondo1,pantalla,listamonster,listaechizos,
               listaobjetos,listawalls,listagold,vx,vy,t,attack,hited,levelup)                  
        t.update_times()     
        if player1.hp<=0:
            if t.gameover==False:
                gameoversound.play()
            t.gameover=True
            vx,vy=0,0
            pygame.mixer.music.stop()
            pantalla.blit(igameover,(200,50))
            player1.imagen=pygame.image.load("ChelinsWorld/dead.png").convert_alpha()

        #for wall in listawalls:
         # pygame.draw.rect(pantalla,(255,0,0),wall)
        nieve1.update(pantalla)
        infotext.update(pantalla,reloj1.get_fps(),player1)
        
        if printsave:
            if t.tde40>=40:
                printsave=False
            pantalla.blit(
                          pygame.font.SysFont("Arial", 46, True, False)
                          .render("GAME SAVED..",1,(255,255,255)),(300,150)
                          )
        cursor1.updatecursor()
        botonaudio.update(pantalla)
        botonhp.update(pantalla, player1)
        botondamage.update(pantalla, player1)
        botonmagic.update(pantalla, player1)
        botonspeed.update(pantalla, player1)             
        pygame.display.update()
        if isinstance(listamonster[0],Teleporter_on_contact):
            if listamonster[0].teleporton:
                listamonster[0].teleporton=False
                termino="ok"
                salir=True
                player1.vx=0
                player1.vy=0    
    return termino

def menu():
    import pygame
    pygame.init()

    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("::: The Skeleton Quest RPG v0.7:::")
    pygame.display.set_icon(pygame.image.load("ChelinsWorld/iconlevel1.png").convert_alpha()) 
    relojmenu= pygame.time.Clock()
    title=pygame.image.load("ChelinsWorld/title.png").convert_alpha()
    newgame=Boton(pygame.image.load("ChelinsWorld/newgame1.png").convert_alpha(),
                  pygame.image.load("ChelinsWorld/newgame2.png").convert_alpha(),250,200)
    
    loadgame=Boton(pygame.image.load("ChelinsWorld/loadgame1.png").convert_alpha(),
                  pygame.image.load("ChelinsWorld/loadgame2.png").convert_alpha(),250,400)
    
    c1=cursor()
    loadgamebool=None
    #intro=pygame.movie.Movie("ChelinsWorld/intro.mpg")
    #pygame.mixer.music.load("ChelinsWorld/introsound.mp3")
    #pygame.mixer.music.play()
    #intro.play()
    
    
    #t=0
    #while t<200:
        #relojmenu.tick(12)
        #t+=1
        #for event in pygame.event.get():
         #   if event.type==pygame.KEYDOWN:
              #  t=200
               # pygame.mixer.music.stop()
                #intro.stop()
                
    pygame.mixer.music.load("ChelinsWorld/melody2.mid")
    pygame.mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return None
            if event.type==pygame.MOUSEBUTTONDOWN:
                if c1.colliderect(newgame.rect):
                    pygame.quit()
                    return False
                elif c1.colliderect(loadgame.rect):
                    pygame.quit()
                    return True
        
        pantalla.fill((0,0,0))
        relojmenu.tick(12)
        pantalla.blit(title,(200,50))
        newgame.pintar(pantalla, c1)
        loadgame.pintar(pantalla, c1)
        c1.updatecursor()
        pygame.display.update()

            
def main(cargar=False):
    import pygame

    pygame.init()
    pantalla=pygame.display.set_mode((800,600))
    pygame.display.set_caption("::: The Skeleton Quest RPG v0.7 :::")
    pygame.display.set_icon(pygame.image.load("ChelinsWorld/iconlevel1.png").convert_alpha())
    loadmusic()
    #aver q onda


    salir=False
    collide=False
    gameover=False
    printsave=False
    cambiolista=False
    reloj1= pygame.time.Clock()
    botonaudio=BotonAudio(760,5)
  
    fondo1=Fondo(pygame.image.load("ChelinsWorld/fondo2.gif"))
    cursor1=cursor()
    botonhp=Botonskill(130,50)
    botondamage=Botonskill(130,75)
    botonmagic=Botonskill(130,100)
    botonspeed=Botonskill(130,125)
    player1=Player(imagen1,imagen2,imagen1l,imagen2l,imagen1t,imagen2t,imagen1b,imagen2b)

    infotext= Info(0)
    vx,vy=0,0
    velocidad=8
    t= Times()
    listaechizos=[]
    
    leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
    listamonster=[Teleporter(iportal),Teleporter_on_contact(ientradaice,4191,44),
                  Aldeano(imajor,590,110,0,80,0,1,"Hey! The shops are due     south of here")
                  ,Aldeano(ianimacion,243,296,0,50,0,1,"Use \" A \" to attack and to talk, BRO!!",True)
                  ,Aldeano(ialdeano,610,418,1,150,0,1,"Use f1 to save the current game, or you will lose it")
                  ,Aldeano(iimpaciente,281,571,0,0,0,1,"I heard that with \"F\" you can use potions...")
                  ,Aldeano(ianimacion,519,1107,1,250,0,1,"Use \" S\" to cast fireball or \" D\" for iceball")
                  ,Aldeano(iguardia,1006,696,0,80,0,1," Beware, monsters live     across the bridge... ")
                  ,Aldeano(ianciano,368,946,0,80,0,1,"I hate music, You can stop the music by pressing \" M\"")
                  ,Monster(iskeleton,1170,144,0,15),Monster(iskeleton,1126,278,1,50)
                  ,Monster(iskeleton,1156,1033,1,50),Monster(iskeleton,1168,1220,0,15)
                  ,Monster(iskeleton,1552,588,0,10),Monster(iskeleton,1740,717,1,20)
                  ,Monster(iskeleton,1484,459,0,20),Monster(iskeleton,1387,333,1,30)
                  ,Monster(iskeleton,1552,308,0,40),Monster(iskeleton,1630,402,1,25)
                  ,Monster(iskeleton,1677,451,0,40),Monster(iskeleton,1554,472,1,35)
                  ,Monster(iskeleton,1760,372,1,35),Monster(iskeleton,1454,82,0,15)
                  ,Monster(iskeleton,1429,101,1,35),Monster(iskeleton,1525,167,1,60)
                  ,Monster(iskeleton,2062,207,0,45),Monster(iskeleton,1859,869,0,35)
                  ,Monster(iskeleton,1628,207,0,45),Monster(iskeleton,1628,207,0,15)
                  ,Monster(iskeleton,1760,764,1,25),Monster(iskeleton,1859,683,0,25)
                  ,Monster(iskeleton,1950,1166,0,95)

                  ,Monsterfollower(iskeletongreen,1979,139,1,1,1,300)
                  ,Monsterfollower(iskeletongreen,1678,1143,0,1,2,250,4)
                  ,Monsterfollower(iskeletongreen,2310,1073,0,1,1,300,4)
                  ,Monsterfollower(iskeletongreen,2710,1073,0,1,1,300,5)
                  ,Monsterfollower(iskeletongreen,2216,1242,1,1,1,300,4)
                  ,Monsterfollower(iskeletongreen,2675,1151,1,1,2,400,4)
                  ,Monsterfollower(ibarbarian,2394,642,1,1,3,1200,5,2000)
                  ,Monsterfollower(ibarbarian,2503,141,1,1,3,1000,5,2000)
                  ,Monsterfollower(ibarbarian,2966,532,1,1,3,1000,5,8000)#
                  ,Monsterfollower(ibarbarian,2976,773,1,1,3,1000,5,2000)#
                  ,Monsterfollower(ibarbarian,3105,639,1,1,3,1000,5,2000)#
                  ,Monsterfollower(ibarbarian,3400,561,1,1,3,1000,5,2000)#
                  ,Monsterfollower(ibarbarian,3078,142,1,1,3,1000,5,2000)
                  ,Monsterfollower(ibarbarian,3138,1145,1,1,3,1000,5,2000)
                  ,Monsterfollower(iskeletonred,4028,879,1,1,5,3000,5,4000,200)
                  ,Monsterfollower(iskeletonred,3943,700,1,1,3,3000,6,4000,350)
                  ,Monsterfollower(iskeletonred,3408,125,1,1,5,3000,5,22000,200)
                  ,Monsterfollower(iskeletonred,3966,97,1,1,5,2000,6,10000,350)
                  ,Monsterfollower(iskeletonred,3826,527,1,1,3,3000,6,22000,200)
                  ,Monsterfollower(iskeletonred,3826,670,1,1,4,2000,5,10000)
                  ,Monsterfollower(iskeletonred,3896,635,1,1,5,3000,5,22000,200)
                  ,Monsterfollower(iskeletonred,4118,527,1,1,6,2000,5,22000)
                  ,Monsterfollower(iskeletonred,4118,670,1,1,7,3000,5,22000,200)
                  ,Monsterfollower(iskeletongreen,3275,1103,1,1,2,400,4)
                  ,Monsterfollower(iskeletongreen,3387,1103,1,1,2,400,4)
                  ,Monsterfollower(iskeletongreen,3353,1103,1,1,2,400,4)
                  ,Monsterfollower(iskeletongreen,3275,1220,1,1,2,400,4)
                  ,Monsterfollower(iskeletongreen,3494,1201,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,3610,1251,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,3698,1213,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,3779,1251,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,3837,1201,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,4013,1201,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,4052,1242,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,4132,1201,1,1,2,400,4)
                 ,Monsterfollower(iskeletongreen,4186,1251,1,1,2,400,4)
                 #cangrejois
                 ,Monsterfollower(icangrejo,-443,-28,1,1,4,2000,4,22000)
                 ,Monsterfollower(icangrejo,-554,434,1,1,4,2000,4,15000)
                 ,Monsterfollower(icangrejo,-886,444,1,1,4,2000,4,15000)
                 ,Monsterfollower(icangrejo,-443,1417,1,1,4,2000,4,15000)
                 ,Monsterfollower(iskeletonred,-601,1161,1,1,7,3000,7,32000,200)
                 ,Monsterfollower(iskeletonred,-891,0,1,1,7,3000,7,22000,200)
                
                 ,Monsterfollower(iskeletongreen, -739,840,1,1,3,700,4)
                 ,Monsterfollower(iskeletongreen,-739,750,1,1,3,700,4)
                 ,Monsterfollower(iskeletongreen, -810,840,1,1,3,700,4)
                 ,Monsterfollower(iskeletongreen,-810,750,1,1,3,700,4)
                 ,Monsterfollower(iskeletongreen, -870,840,1,1,3,700,4)
                 ,Monsterfollower(iskeletongreen,-870,750,1,1,3,700,4)
                 
                 ,Monsterfollower(iOrco,-4201,25,1,1,5,3000,5,22000,350)
                ,Monsterfollower(iOrco,-913,1338,1,1,5,3000,5,22000,350)
                ,Monsterfollower(iOrco,-739,63,1,1,5,3000,5,22000,350)
                ,Monsterfollower(iOrco,-330,290,1,1,5,3000,5,22000,350)
                  ]

    listaobjetos=[Objeto(icasa2,121,-131),Objeto(icasa1,669,-185)
                  ,Objeto(icasa1,363,355),Objeto(icasa1,705,434)
                  ,Objeto(icasa2,238,676),Shop(ishop,217,1034,"Dano"),
                  Shop(ishop2,217,1230,"Vida"),Shop(ishop3,743,1045,"Pots"),
                  Shop(ishop4,756,826,"Heal"),Shop(ishop5,753,1245,"Velocidad"),
                  Shop(ishop6,460,1307,"Magic")
                  ]
 
    listawalls=[pygame.Rect(88,5,1,900),pygame.Rect(88,1065,1,400),pygame.Rect(88,70,1000,2)
                ,pygame.Rect(88,1500,1000,1)#primeras 3
                ,pygame.Rect(950,50,1,625),pygame.Rect(950,800,1,700)#entrada del puente
                ,pygame.Rect(950,700,150,2),pygame.Rect(950,800,150,2)#puente
                ,pygame.Rect(1100,50,1,625),pygame.Rect(1100,800,1,1000)#salidas del pte
                ,pygame.Rect(1120,30,3400,2),pygame.Rect(1120,1350,3400,2)#arriba y abajo
                ,pygame.Rect(4322,-22,2,1400)#costado dercha
                ,pygame.Rect(1277,-32,2,680),pygame.Rect(1296,816,2,600)#primeras 2
                ,pygame.Rect(1291,594,222,50)
                ,pygame.Rect(1651,594,422,50),pygame.Rect(1301,846,422,150) # 3 horizontales
                ,pygame.Rect(2069,-83,20,260),pygame.Rect(2069,333,20,680)#2 verticales
                ,pygame.Rect(2100,340,641,70),pygame.Rect(2088,940,414,70)#2 horizontales
                ,pygame.Rect(2738,-33,20,663),pygame.Rect(2738,763,20,250),pygame.Rect(2885,931,20,527) #3 verticales
                ,pygame.Rect(2791,337,220,70),pygame.Rect(3114,337,414,70)#2 horizontales]            
                ,pygame.Rect(2671,938,222,70),pygame.Rect(3021,938,582,70) #2 mas abajo
                ,pygame.Rect(3530,262,851,170),pygame.Rect(3529,975,851,170)  #2 horizontal
                ,pygame.Rect(3549,338,20,280),pygame.Rect(3549,726,20,304)#2 verticales cueva
                #left
                ,pygame.Rect(-1048,30,1100,1),pygame.Rect(-1048,1500,1200,1)
                ,pygame.Rect(-990,5,1,1600)
                ]
    
    listagold=[Gold(150,200),Gold(650,200),Gold(1169,80,350),Gold(1217,1289,350)
               ,Gold(1361,476,450),Gold(1392,89,450),Gold(1377,1204,450),
               Gold(2780,1130,350),
               Gold(2374,568,450),Gold(2574,568,450),
               Gold(2638,181,450),
               Gold(3351,489,450),Gold(3400,489,450),Gold(3442,489,450),Gold(3493,489,450),
               Gold(4091,184,450),Gold(4140,184,450),Gold(4182,184,450),Gold(4233,184,450),
               Gold(-713,1326,550),Gold(-653,1326,550),Gold(-780,1326,550),
               Gold(-750,-18,550),Gold(-750,41,550),Gold(-840,41,550),
               ]
    
    
    if cargar==True:
        listagold=load(player1,listagold)
    
    pygame.mixer.music.play()

    while salir!=True:#LOOP PRINCIPAL
        reloj1.tick(28)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir=True
            if  t.gameover:
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        return True
                    if event.key==pygame.K_ESCAPE:
                        return False
            
            else: 
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:
                        if player1.skillpoints>0:
                            if cursor1.colliderect(botonhp):
                                player1.hpmax+=8
                                if player1.hp==player1.hpmax:player1.hp+=8
                                player1.skillpoints-=1
                            elif cursor1.colliderect(botondamage):
                                player1.dano+=1
                                player1.skillpoints-=1                                
                            elif cursor1.colliderect(botonmagic):
                                player1.magic+=1
                                player1.skillpoints-=1  
                            elif cursor1.colliderect(botonspeed):
                                if player1.velocidad<=14:
                                    player1.velocidad+=0.20  
                                    player1.skillpoints-=1                                                                                      
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        return False
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=True
                        vx=-player1.velocidad
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=True
                        vx=player1.velocidad
                    if event.key== pygame.K_UP:
                        upsigueapretada=True
                        vy=-player1.velocidad
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=True
                        vy=player1.velocidad
                    if event.key == pygame.K_d:
                        auxfireball=False
                        for spells in listaechizos:
                            if spells.tipo=="hielo" or spells.tipo=="fireball": auxfireball=True
                        if not(auxfireball):listaechizos.append(Hielo(player1))                     
                    if event.key == pygame.K_a:
                        listaechizos.append(espada(player1)) 
                    if event.key == pygame.K_s:
                        auxfireball=False
                        for spells in listaechizos:
                            if spells.tipo=="fireball" or spells.tipo=="hielo": auxfireball=True
                        if not(auxfireball):listaechizos.append(fireball(player1))      

                    if event.key ==pygame.K_f:
                        player1.usepot()
                    if event.key == pygame.K_F7:
                        player1.levelup(pantalla, levelup, t)
            
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        leftsigueapretada=False
                        if rightsigueapretada:vx=player1.velocidad
                        else:vx=0
                    if event.key == pygame.K_RIGHT:
                        rightsigueapretada=False
                        if leftsigueapretada:vx=-player1.velocidad
                        else:vx=0
                    if event.key== pygame.K_UP:
                        upsigueapretada=False
                        if downsigueapretada:vy=player1.velocidad
                        else:vy=-0
                    if event.key == pygame.K_DOWN:
                        downsigueapretada=False
                        if upsigueapretada:vy=-player1.velocidad
                        else:vy=0                    
                    if event.key ==pygame.K_f:
                        player1.unlockpots()
                    if event.key==pygame.K_F1:
                        if (player1.estavivo):
                            t.tde40=0
                            printsave=True
                        save(player1,listagold)
                    if event.key==pygame.K_m:
                        botonaudio.cambiar_estado()


        pantalla.fill((0,0,170))
        player1.mover(vx/1000.0, vy/1000.0)           
        t.update_times()     
        movercosas(player1,fondo1,pantalla,listamonster,listaechizos,
               listaobjetos,listawalls,listagold,vx,vy,t,attack,hited,levelup) 
        
        #teleportar??
        if listamonster[0].teleporton:
            listamonster[0].teleporton=False
            vx,vy=0,0
            termino=bossfight(player1)
            if termino=="quit": 
                pygame.quit()
                return      
            elif termino=="ok":
                player1.acrono=1
                player1.setacrono()
                pygame.mixer.music.stop()
                loadmusic()
                pygame.mixer.music.play()  
            elif termino=="reload":
                return True
        if listamonster[1].teleporton:
            listamonster[1].teleporton=False
            movercosas(player1,fondo1,pantalla,listamonster,listaechizos,
               listaobjetos,listawalls,listagold,-3*vx,-3*vy,t,attack,hited,levelup)             
            leftsigueapretada,rightsigueapretada,upsigueapretada,downsigueapretada=False,False,False,False
            vx,vy=0,0
            print "change map"
            termino=ice(player1)
            vx,vy=-vx,-vy
            if termino=="quit": 
                pygame.quit()
                return      
            elif termino=="ok":
                pygame.mixer.music.stop()
                loadmusic()
                pygame.mixer.music.play()  
            elif termino=="reload":
                return True
        if player1.hp<=0:
            if t.gameover==False:
                #gameoversound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("ChelinsWorld/gameover.wav")
                pygame.mixer.music.play()                
                t.gameover=True
            vx,vy=0,0
            pantalla.blit(igameover,(200,50))
            

        #for wall in listawalls:
         #   pygame.draw.rect(pantalla,(255,0,0),wall)
        cursor1.updatecursor()
        infotext.update(pantalla,reloj1.get_fps(),player1)
        botonaudio.update(pantalla)
        botonhp.update(pantalla, player1)
        botondamage.update(pantalla, player1)
        botonmagic.update(pantalla, player1)
        botonspeed.update(pantalla, player1)        
        if printsave:
            if t.tde40>=40:
                printsave=False
            pantalla.blit(
                          pygame.font.SysFont("Arial", 46, True, False)
                          .render("GAME SAVED..",1,(255,255,255)),(300,150)
                          )
        pygame.display.update()
                
    pygame.quit()

def start(loadbool=None):
    if loadbool==None:
        loadbool=menu()
    if not(loadbool==None):
        a=main(loadbool)
        if a==True:
            start(True)       
start()