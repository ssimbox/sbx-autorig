import maya.cmds as cmds


# This is the controller library where I save curves' coordinates I make
# One day I'll import curves from this file 


# Cube form
def createCube(nome):
    crvCube = cmds.curve(d=1, p=[(-1, 1, -1), (1, 1, -1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (-1, 1, -1),
    (-1, 1, 1),
    (-1, -1, 1),
    (1, -1, 1), 
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1)], k=[0 , 1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 1.0 , 1.1, 1.2 , 1.3 , 1.4 , 1.5], n=nome )

# Sphere
def createSphere(nome):
    crvSphere = cmds.curve(n=nome, d=1, p=[( 0, 1, 0 ), ( 0, 0.92388, 0.382683 ), ( 0, 0.707107, 0.707107 ), 
                                            ( 0, 0.382683, 0.92388 ), ( 0, 0, 1 ), ( 0, -0.382683, 0.92388 ), ( 0, -0.707107, 0.707107 ), ( 0, -0.92388, 0.382683 ), 
                                            ( 0, -1, 0 ), ( 0, -0.92388, -0.382683 ), ( 0, -0.707107, -0.707107 ), ( 0, -0.382683, -0.92388 ), 
                                            ( 0, 0, -1 ), ( 0, 0.382683, -0.92388 ), ( 0, 0.707107, -0.707107 ), ( 0, 0.92388, -0.382683 ), ( 0, 1, 0 ), 
                                            ( 0.382683, 0.92388, 0 ), ( 0.707107, 0.707107, 0 ), ( 0.92388, 0.382683, 0 ), ( 1, 0, 0 ), ( 0.92388, -0.382683, 0 ), 
                                            ( 0.707107, -0.707107, 0 ), ( 0.382683, -0.92388, 0 ), ( 0, -1, 0 ), ( -0.382683, -0.92388, 0 ), ( -0.707107, -0.707107, 0 ), 
                                            ( -0.92388, -0.382683, 0 ), ( -1, 0, 0 ), ( -0.92388, 0.382683, 0 ), ( -0.707107, 0.707107, 0 ), ( -0.382683, 0.92388, 0 ), 
                                            ( 0, 1, 0 ), ( 0, 0.92388, -0.382683, ), ( 0, 0.707107, -0.707107, ), ( 0, 0.382683, -0.92388, ), ( 0, 0, -1 ), 
                                            ( -0.382683, 0, -0.92388 ), ( -0.707107, 0, -0.707107 ), ( -0.92388, 0, -0.382683 ), ( -1, 0, 0 ), ( -0.92388, 0, 0.382683 ), 
                                            ( -0.707107, 0, 0.707107 ), ( -0.382683, 0, 0.92388 ), ( 0, 0, 1 ), ( 0.382683, 0, 0.92388 ), ( 0.707107, 0, 0.707107 ), 
                                            ( 0.92388, 0, 0.382683 ), ( 1, 0, 0 ), ( 0.92388, 0, -0.382683 ), ( 0.707107, 0, -0.707107 ), ( 0.382683, 0, -0.92388 ), 
                                            ( 0, 0, -1)], 
                                            k= [0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 
                                            25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 
                                            48 , 49 , 50 , 51 , 52])

# Hand controller. Simil pyramid
def createHandCtrl(nome):
    attributeController = cmds.curve(d=1, p=[(-1.6691866981302321, -0.8320895690179206, -4.590263419858138),
                                            (1.6691866981302317, -0.8320895690179206, -4.590263419858138),
                                            (1.6691866981302317, -0.8320895690179206, 4.590263419858138),
                                            (-1.6691866981302321, -0.8320895690179206, 4.590263419858138),
                                            (0.0, 0.8318404710680585, 4.590263419858138),
                                            (1.6691866981302317, -0.8320895690179206, 4.590263419858138),
                                            (1.6691866981302317, -0.8320895690179206, -4.590263419858138),
                                            (0.0, 0.8320895690179206, -4.590263419858138),
                                            (-1.6691866981302321, -0.8320895690179206, -4.590263419858138),
                                            (-1.6691866981302321, -0.8320895690179206, 4.590263419858138),
                                            (-1.6691866981302321, -0.8320895690179206, -4.590263419858138),
                                            (-1.6691866981302321, -0.8320895690179206, -4.590263419858138),
                                            (0.0, 0.8320895690179206, -4.590263419858138),
                                            (0.0, 0.8318404710680585, 4.590263419858138)], 
                                            k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13], n=nome)