import pygame as py
import numpy as np

def n(x,y):
    return np.sqrt(x*x+y*y) 

class particule(object):
    SURFACE = py.Surface((10,10))  # pylint: disable=too-many-function-args
    ARRAY=[]
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0
        self.color=(42, 180, 235)
        self.radius=5
        self.maxspeed=1
        self.shape="line"
    
    def apply(self):
        self.vx+=np.random.random_integers(-1*self.maxspeed,self.maxspeed)
        self.vy+=np.random.random_integers(-1*self.maxspeed,self.maxspeed)
        self.x+=self.vx
        self.y+=self.vy
        (w, h) = particule.SURFACE.get_size()
        self.x=(self.x+w)%w
        self.y=(self.y+h)%h

    def draw(self):
        if self.shape == "circle":
            py.draw.circle(particule.SURFACE,self.color,(int(self.x),int(self.y)),int(self.radius))
        if self.shape == "line":
            nn=n(self.vx,self.vy)/4
            if nn>0:
                py.draw.line(particule.SURFACE,self.color,(int(self.x),int(self.y)),(int(self.x+self.vx/nn),int(self.y+self.vy/nn)))
            else:
                py.draw.circle(particule.SURFACE,self.color,(int(self.x),int(self.y)),1)
                
    @staticmethod
    def generaterandompos(quantity):
        (w, h) = particule.SURFACE.get_size()
        for _ in range(quantity):
            particule.ARRAY.append(particule(np.random.random_integers(0,w),np.random.random_integers(0,h)))
    @staticmethod 
    def drawall():
        for i in particule.ARRAY:
            i.apply()
            i.draw()