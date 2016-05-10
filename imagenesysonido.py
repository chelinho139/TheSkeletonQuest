import pygame
class Imagenes(object):
    def __init__(self):
        self.nombre="Unknown"
pygame.init()
pygame.display.set_mode((0,0))

attack=pygame.mixer.Sound("ChelinsWorld/atack.wav")
attack.set_volume(0.4)
hited=pygame.mixer.Sound("ChelinsWorld/hited.wav")
levelup=pygame.mixer.Sound("ChelinsWorld/levelup.wav")
gameoversound=pygame.mixer.Sound("ChelinsWorld/gameover.wav") 
fireballsound=pygame.mixer.Sound("ChelinsWorld/fireball.wav")
fireballsound.set_volume(0.3)
snowballsound=pygame.mixer.Sound("ChelinsWorld/snowball.wav")
snowballsound.set_volume(0.3)


imagen1=pygame.image.load("ChelinsWorld/knightr1.png").convert_alpha()
imagen2=pygame.image.load("ChelinsWorld/knightr2.png").convert_alpha()
imagen1l=pygame.image.load("ChelinsWorld/knightl1.png").convert_alpha()
imagen2l=pygame.image.load("ChelinsWorld/knightl2.png").convert_alpha()    
imagen1t=pygame.image.load("ChelinsWorld/knightt1.png").convert_alpha()
imagen2t=pygame.image.load("ChelinsWorld/knightt2.png").convert_alpha()
imagen1b=pygame.image.load("ChelinsWorld/knightb1.png").convert_alpha()
imagen2b=pygame.image.load("ChelinsWorld/knightb2.png").convert_alpha()

ianciano= Imagenes()
ianciano.iancianor1=pygame.image.load("ChelinsWorld/ancianor1.png").convert_alpha()
ianciano.iancianor2=pygame.image.load("ChelinsWorld/ancianor2.png").convert_alpha()
ianciano.iancianol1=pygame.image.load("ChelinsWorld/ancianol1.png").convert_alpha()
ianciano.iancianol2=pygame.image.load("ChelinsWorld/ancianol2.png").convert_alpha()
ianciano.lista=[[ianciano.iancianor1,ianciano.iancianor2],[ianciano.iancianol1,ianciano.iancianol2],
                [],[]]

iimpaciente= Imagenes()
iimpaciente.iimpaciente1=pygame.image.load("ChelinsWorld/impaciente1.png").convert_alpha()
iimpaciente.iimpaciente2=pygame.image.load("ChelinsWorld/impaciente2.png").convert_alpha()

iimpaciente.lista=[[iimpaciente.iimpaciente1,iimpaciente.iimpaciente2],[iimpaciente.iimpaciente1,iimpaciente.iimpaciente2],
                [],[]]


iportal= Imagenes()
iportal.iportal1=pygame.image.load("ChelinsWorld/portal1.png").convert_alpha()
iportal.iportal2=pygame.image.load("ChelinsWorld/portal2.png").convert_alpha()

iportal.lista=[[iportal.iportal1,iportal.iportal2],[iportal.iportal1,iportal.iportal2],
                [],[]]

ientradaice= Imagenes()
ientradaice.ientradaice1=pygame.image.load("ChelinsWorld/entradaice.png").convert_alpha()
ientradaice.ientradaice2=pygame.image.load("ChelinsWorld/entradaice.png").convert_alpha()

ientradaice.lista=[[ientradaice.ientradaice1,ientradaice.ientradaice2],[ientradaice.ientradaice1,ientradaice.ientradaice2],
                [],[]]

iguardia= Imagenes()
iguardia.iguardiar1=pygame.image.load("ChelinsWorld/guardiar1.png").convert_alpha()
iguardia.iguardiar2=pygame.image.load("ChelinsWorld/guardiar2.png").convert_alpha()
iguardia.iguardial1=pygame.image.load("ChelinsWorld/guardial1.png").convert_alpha()
iguardia.iguardial2=pygame.image.load("ChelinsWorld/guardial2.png").convert_alpha()
iguardia.lista=[[iguardia.iguardiar1,iguardia.iguardiar2],[iguardia.iguardial1,iguardia.iguardial2],
                [],[]]    

imajor= Imagenes()
imajor.imajorr1=pygame.image.load("ChelinsWorld/majorr1.png").convert_alpha()
imajor.imajorr2=pygame.image.load("ChelinsWorld/majorr2.png").convert_alpha()
imajor.imajorl1=pygame.image.load("ChelinsWorld/majorl1.png").convert_alpha()
imajor.imajorl2=pygame.image.load("ChelinsWorld/majorl2.png").convert_alpha()
imajor.lista=[[imajor.imajorr1,imajor.imajorr2],[imajor.imajorl1,imajor.imajorl2],
                [],[]]   


ialdeano= Imagenes()
ialdeano.ialdeanob1=pygame.image.load("ChelinsWorld/aldeanob1.png").convert_alpha()
ialdeano.ialdeanob2=pygame.image.load("ChelinsWorld/aldeanob2.png").convert_alpha()
ialdeano.ialdeanot1=pygame.image.load("ChelinsWorld/aldeanot1.png").convert_alpha()
ialdeano.ialdeanot2=pygame.image.load("ChelinsWorld/aldeanot2.png").convert_alpha()
ialdeano.lista=[[ialdeano.ialdeanob1,ialdeano.ialdeanob2],[],[ialdeano.ialdeanob1,ialdeano.ialdeanob2],[ialdeano.ialdeanot1,ialdeano.ialdeanot2]
                ]  

icangrejo= Imagenes()
icangrejo.icangrejob1=pygame.image.load("ChelinsWorld/cangrejob1.png").convert_alpha()
icangrejo.icangrejob2=pygame.image.load("ChelinsWorld/cangrejob2.png").convert_alpha()
icangrejo.icangrejot1=pygame.image.load("ChelinsWorld/cangrejob1.png").convert_alpha()
icangrejo.icangrejot2=pygame.image.load("ChelinsWorld/cangrejob2.png").convert_alpha()
icangrejo.lista=[[icangrejo.icangrejob1,icangrejo.icangrejob2],[],[icangrejo.icangrejob1,icangrejo.icangrejob2],[icangrejo.icangrejot1,icangrejo.icangrejot2]
                ]      

ianimacion=Imagenes()
ianimacion.ianimacionr1=pygame.image.load("ChelinsWorld/animacion1.png").convert_alpha()
ianimacion.ianimacionl1=pygame.image.load("ChelinsWorld/animacion1l.png").convert_alpha()
ianimacion.ianimacionb1=pygame.image.load("ChelinsWorld/animacion1b.png").convert_alpha()
ianimacion.ianimaciont1=pygame.image.load("ChelinsWorld/animacion1t.png").convert_alpha()    
ianimacion.ianimacionr2=pygame.image.load("ChelinsWorld/animacion2.png").convert_alpha()
ianimacion.ianimacionl2=pygame.image.load("ChelinsWorld/animacion2l.png").convert_alpha()
ianimacion.ianimacionb2=pygame.image.load("ChelinsWorld/animacion2b.png").convert_alpha()
ianimacion.ianimaciont2=pygame.image.load("ChelinsWorld/animacion2t.png").convert_alpha()   
ianimacion.lista=[[ianimacion.ianimacionr1,ianimacion.ianimacionr2],
                    [ianimacion.ianimacionl1,ianimacion.ianimacionl2],
                    [ianimacion.ianimacionb1,ianimacion.ianimacionb2],
                    [ ianimacion.ianimaciont1,ianimacion.ianimaciont2]]


ifuryorc=Imagenes()
ifuryorc.ifuryorcr1=pygame.image.load("ChelinsWorld/furyorcr1.png").convert_alpha()
ifuryorc.ifuryorcl1=pygame.image.load("ChelinsWorld/furyorcl1.png").convert_alpha()
ifuryorc.ifuryorcb1=pygame.image.load("ChelinsWorld/furyorcb1.png").convert_alpha()
ifuryorc.ifuryorct1=pygame.image.load("ChelinsWorld/furyorct1.png").convert_alpha()    
ifuryorc.ifuryorcr2=pygame.image.load("ChelinsWorld/furyorcr2.png").convert_alpha()
ifuryorc.ifuryorcl2=pygame.image.load("ChelinsWorld/furyorcl2.png").convert_alpha()
ifuryorc.ifuryorcb2=pygame.image.load("ChelinsWorld/furyorcb2.png").convert_alpha()
ifuryorc.ifuryorct2=pygame.image.load("ChelinsWorld/furyorct2.png").convert_alpha()   
ifuryorc.lista=[[ifuryorc.ifuryorcr1,ifuryorc.ifuryorcr2],
                    [ifuryorc.ifuryorcl1,ifuryorc.ifuryorcl2],
                    [ifuryorc.ifuryorcb1,ifuryorc.ifuryorcb2],
                    [ ifuryorc.ifuryorct1,ifuryorc.ifuryorct2]]


iOrco=Imagenes()
iOrco.iOrcor1=pygame.image.load("ChelinsWorld/Orcor1.png").convert_alpha()
iOrco.iOrcol1=pygame.image.load("ChelinsWorld/Orcol1.png").convert_alpha()
iOrco.iOrcob1=pygame.image.load("ChelinsWorld/Orcob1.png").convert_alpha()
iOrco.iOrcot1=pygame.image.load("ChelinsWorld/Orcot1.png").convert_alpha()    
iOrco.iOrcor2=pygame.image.load("ChelinsWorld/Orcor2.png").convert_alpha()
iOrco.iOrcol2=pygame.image.load("ChelinsWorld/Orcol2.png").convert_alpha()
iOrco.iOrcob2=pygame.image.load("ChelinsWorld/Orcob2.png").convert_alpha()
iOrco.iOrcot2=pygame.image.load("ChelinsWorld/Orcot2.png").convert_alpha()   
iOrco.lista=[[iOrco.iOrcor1,iOrco.iOrcor2],
                    [iOrco.iOrcol1,iOrco.iOrcol2],
                    [iOrco.iOrcob1,iOrco.iOrcob2],
                    [ iOrco.iOrcot1,iOrco.iOrcot2]]




iali=Imagenes()
iali.ialir1=pygame.image.load("ChelinsWorld/alir1.png").convert_alpha()
iali.ialil1=pygame.image.load("ChelinsWorld/alil1.png").convert_alpha()
iali.ialib1=pygame.image.load("ChelinsWorld/alib1.png").convert_alpha()
iali.ialit1=pygame.image.load("ChelinsWorld/alit1.png").convert_alpha()    
iali.ialir2=pygame.image.load("ChelinsWorld/alir2.png").convert_alpha()
iali.ialil2=pygame.image.load("ChelinsWorld/alil2.png").convert_alpha()
iali.ialib2=pygame.image.load("ChelinsWorld/alib2.png").convert_alpha()
iali.ialit2=pygame.image.load("ChelinsWorld/alit2.png").convert_alpha()   
iali.lista=[[iali.ialir1,iali.ialir2],
                    [iali.ialil1,iali.ialil2],
                    [iali.ialib1,iali.ialib2],
                    [ iali.ialit1,iali.ialit2]]


iskeletongreen=Imagenes()
iskeletongreen.iskeletonr1=pygame.image.load("ChelinsWorld/skeletongreenr1.png").convert_alpha()
iskeletongreen.iskeletonl1=pygame.image.load("ChelinsWorld/skeletongreenl1.png").convert_alpha()
iskeletongreen.iskeletonb1=pygame.image.load("ChelinsWorld/skeletongreenb1.png").convert_alpha()
iskeletongreen.iskeletont1=pygame.image.load("ChelinsWorld/skeletongreent1.png").convert_alpha()    
iskeletongreen.iskeletonr2=pygame.image.load("ChelinsWorld/skeletongreenr2.png").convert_alpha()
iskeletongreen.iskeletonl2=pygame.image.load("ChelinsWorld/skeletongreenl2.png").convert_alpha()
iskeletongreen.iskeletonb2=pygame.image.load("ChelinsWorld/skeletongreenb2.png").convert_alpha()
iskeletongreen.iskeletont2=pygame.image.load("ChelinsWorld/skeletongreent2.png").convert_alpha()   
iskeletongreen.lista=[[iskeletongreen.iskeletonr1,iskeletongreen.iskeletonr2],
					[iskeletongreen.iskeletonl1,iskeletongreen.iskeletonl2],
					[iskeletongreen.iskeletonb1,iskeletongreen.iskeletonb2],
					[ iskeletongreen.iskeletont1,iskeletongreen.iskeletont2]]




iskeletonred=Imagenes()
iskeletonred.iskeletonr1=pygame.image.load("ChelinsWorld/skeletonredr1.png").convert_alpha()
iskeletonred.iskeletonl1=pygame.image.load("ChelinsWorld/skeletonredl1.png").convert_alpha()
iskeletonred.iskeletonb1=pygame.image.load("ChelinsWorld/skeletonredb1.png").convert_alpha()
iskeletonred.iskeletont1=pygame.image.load("ChelinsWorld/skeletonredt1.png").convert_alpha()    
iskeletonred.iskeletonr2=pygame.image.load("ChelinsWorld/skeletonredr2.png").convert_alpha()
iskeletonred.iskeletonl2=pygame.image.load("ChelinsWorld/skeletonredl2.png").convert_alpha()
iskeletonred.iskeletonb2=pygame.image.load("ChelinsWorld/skeletonredb2.png").convert_alpha()
iskeletonred.iskeletont2=pygame.image.load("ChelinsWorld/skeletonredt2.png").convert_alpha()   
iskeletonred.lista=[[iskeletonred.iskeletonr1,iskeletonred.iskeletonr2],
                    [iskeletonred.iskeletonl1,iskeletonred.iskeletonl2],
                    [iskeletonred.iskeletonb1,iskeletonred.iskeletonb2],
                    [ iskeletonred.iskeletont1,iskeletonred.iskeletont2]]

iskeleton=Imagenes()
iskeleton.iskeletonr1=pygame.image.load("ChelinsWorld/skeletonr1.png").convert_alpha()
iskeleton.iskeletonl1=pygame.image.load("ChelinsWorld/skeletonl1.png").convert_alpha()
iskeleton.iskeletonb1=pygame.image.load("ChelinsWorld/skeletonb1.png").convert_alpha()
iskeleton.iskeletont1=pygame.image.load("ChelinsWorld/skeletont1.png").convert_alpha()    
iskeleton.iskeletonr2=pygame.image.load("ChelinsWorld/skeletonr2.png").convert_alpha()
iskeleton.iskeletonl2=pygame.image.load("ChelinsWorld/skeletonl2.png").convert_alpha()
iskeleton.iskeletonb2=pygame.image.load("ChelinsWorld/skeletonb2.png").convert_alpha()
iskeleton.iskeletont2=pygame.image.load("ChelinsWorld/skeletont2.png").convert_alpha()   
iskeleton.lista=[[iskeleton.iskeletonr1,iskeleton.iskeletonr2],
				[iskeleton.iskeletonl1,iskeleton.iskeletonl2],
				[iskeleton.iskeletonb1,iskeleton.iskeletonb2],
				[ iskeleton.iskeletont1,iskeleton.iskeletont2]]


ibarbarian=Imagenes()
ibarbarian.barbarianr1=pygame.image.load("ChelinsWorld/barbarian8.png").convert_alpha()
ibarbarian.barbarianl1=pygame.image.load("ChelinsWorld/barbarian10.png").convert_alpha()
ibarbarian.barbarianb1=pygame.image.load("ChelinsWorld/barbarian2.png").convert_alpha()
ibarbarian.barbariant1=pygame.image.load("ChelinsWorld/barbarian5.png").convert_alpha()    
ibarbarian.barbarianr2=pygame.image.load("ChelinsWorld/barbarian9.png").convert_alpha()
ibarbarian.barbarianl2=pygame.image.load("ChelinsWorld/barbarian11.png").convert_alpha()
ibarbarian.barbarianb2=pygame.image.load("ChelinsWorld/barbarian3.png").convert_alpha()
ibarbarian.barbariant2=pygame.image.load("ChelinsWorld/barbarian6.png").convert_alpha()   
ibarbarian.lista=[[ibarbarian.barbarianr1,ibarbarian.barbarianr2],
                [ibarbarian.barbarianl1,ibarbarian.barbarianl2],
                [ibarbarian.barbarianb1,ibarbarian.barbarianb2],
                [ ibarbarian.barbariant1,ibarbarian.barbariant2]]

iespada=pygame.image.load("ChelinsWorld/espada.png").convert_alpha()
iespadal=pygame.image.load("ChelinsWorld/espadal.png").convert_alpha()
iespadat=pygame.image.load("ChelinsWorld/espadat.png").convert_alpha()
iespadab=pygame.image.load("ChelinsWorld/espadab.png").convert_alpha()

iespada2=pygame.image.load("ChelinsWorld/espada2.png").convert_alpha()
iespadal2=pygame.image.load("ChelinsWorld/espadal2.png").convert_alpha()
iespadat2=pygame.image.load("ChelinsWorld/espadat2.png").convert_alpha()
iespadab2=pygame.image.load("ChelinsWorld/espadab2.png").convert_alpha()


iespadaacrono=pygame.image.load("ChelinsWorld/espadaacrono.png").convert_alpha()
iespadaacronol=pygame.image.load("ChelinsWorld/espadaacronol.png").convert_alpha()
iespadaacronot=pygame.image.load("ChelinsWorld/espadaacronot.png").convert_alpha()
iespadaacronob=pygame.image.load("ChelinsWorld/espadaacronob.png").convert_alpha()

iespadaacrono2=pygame.image.load("ChelinsWorld/espadaacrono2.png").convert_alpha()
iespadaacronol2=pygame.image.load("ChelinsWorld/espadaacronol2.png").convert_alpha()
iespadaacronot2=pygame.image.load("ChelinsWorld/espadaacronot2.png").convert_alpha()
iespadaacronob2=pygame.image.load("ChelinsWorld/espadaacronob2.png").convert_alpha()

icastingr=pygame.image.load("ChelinsWorld/castingr.png").convert_alpha()
icastingl=pygame.image.load("ChelinsWorld/castingl.png").convert_alpha()
icastingb=pygame.image.load("ChelinsWorld/castingb.png").convert_alpha()
icastingt=pygame.image.load("ChelinsWorld/castingt.png").convert_alpha()


icastingacronor=pygame.image.load("ChelinsWorld/castingacronor.png").convert_alpha()
icastingacronol=pygame.image.load("ChelinsWorld/castingacronol.png").convert_alpha()
icastingacronob=pygame.image.load("ChelinsWorld/castingacronob.png").convert_alpha()
icastingacronot=pygame.image.load("ChelinsWorld/castingacronot.png").convert_alpha()

ifireballr=pygame.image.load("ChelinsWorld/fireballr.png").convert_alpha()
ifireballl=pygame.image.load("ChelinsWorld/fireballl.png").convert_alpha()
ifireballt=pygame.image.load("ChelinsWorld/fireballt.png").convert_alpha()
ifireballb=pygame.image.load("ChelinsWorld/fireballb.png").convert_alpha()
ifireballr2=pygame.image.load("ChelinsWorld/fireballr2.png").convert_alpha()
ifireballl2=pygame.image.load("ChelinsWorld/fireballl2.png").convert_alpha()
ifireballt2=pygame.image.load("ChelinsWorld/fireballt2.png").convert_alpha()
ifireballb2=pygame.image.load("ChelinsWorld/fireballb2.png").convert_alpha()

isnowballr=pygame.image.load("ChelinsWorld/snowballr.png").convert_alpha()
isnowballl=pygame.image.load("ChelinsWorld/snowballr.png").convert_alpha()
isnowballt=pygame.image.load("ChelinsWorld/snowballr.png").convert_alpha()
isnowballb=pygame.image.load("ChelinsWorld/snowballr.png").convert_alpha()
isnowballr2=pygame.image.load("ChelinsWorld/snowballr2.png").convert_alpha()
isnowballl2=pygame.image.load("ChelinsWorld/snowballr2.png").convert_alpha()
isnowballt2=pygame.image.load("ChelinsWorld/snowballr2.png").convert_alpha()
isnowballb2=pygame.image.load("ChelinsWorld/snowballr2.png").convert_alpha()



icasa1=pygame.image.load("ChelinsWorld/casa1.png").convert_alpha()   
icasa2=pygame.image.load("ChelinsWorld/casa2.png").convert_alpha()
iarbol=pygame.image.load("ChelinsWorld/arbol.png").convert_alpha()
iarbol2=pygame.image.load("ChelinsWorld/arbol2.png").convert_alpha()

ipozo=pygame.image.load("ChelinsWorld/pozo.png").convert_alpha()
ishop=pygame.image.load("ChelinsWorld/shop1.png").convert_alpha()
ishop2=pygame.image.load("ChelinsWorld/shop2.png").convert_alpha()
ishop3=pygame.image.load("ChelinsWorld/shop3.png").convert_alpha()
ishop4=pygame.image.load("ChelinsWorld/shop4.png").convert_alpha() 
ishop5=pygame.image.load("ChelinsWorld/shop5.png").convert_alpha() 
ishop6=pygame.image.load("ChelinsWorld/shop6.png").convert_alpha() 
igameover=pygame.image.load("ChelinsWorld/gameover.png").convert_alpha()                                                                      
