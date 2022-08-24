import math

class MyVector:
  def __init__(self, dim, x, y, z):
    self.x = x
    self.y = y
    self.z = z
    self.dim = -1
    self.dist = 0

  def normalize(self):
    # norm 구하기
    mag = self.getMagnitude()
    # 각 성분 나누기
    self.x /= mag
    self.y /= mag
    self.z /= mag

  def getMagnitude(self):
    mag = math.sqrt(math.pow(self.x,2)
    + math.pow(self.y,2)
    + math.pow(self.z,2))
    return mag

  def getState(self):
    return self.x, self.y, self.z

  '''스칼라량의 곱'''
  def scalarMulti(self, scalar):
    return (self.x * scalar, self.y * scalar, self.z * scalar)

  '''객체간 +, - 연산'''
  def minus(self, MyVector):
    p = []
    m = []

    # 더하기
    p.append(self.x + MyVector[0])
    p.append(self.y + MyVector[1])
    p.append(self.z + MyVector[2])

    # 빼기
    m.append(self.x - MyVector[0])
    m.append(self.y - MyVector[1])
    m.append(self.z - MyVector[2])

    return p, m

# 아래와 같은 방식으로 활용가능
## vec = MyVector(3, 0, 0, 0)
## print(vec.getState())

# 빌더 패턴: 순전히 argument에 대한 것
class VectorBuilder:

  def __init__(self):
    self.x = None
    self.y = None
    self.z = None
    self.dim = None

  def setDim(self, dim):
    self.dim = dim
    return self

  def setX(self, x):
    self.x = x
    return self

  def setY(self, y):
    self.y = y
    return self

  def setZ(self, z):
    self.z = z
    return self

  def build(self):
    vector = MyVector(self.dim, self.x, self.y, self.z)
    return vector

# 빌더를 이용한 객체 생성
## vec = VectorBuilder().setDim(3).setX(50).setY(100).setZ(10).build()
## print(vec.getState())

# want to create 2D vector or 3D vector using presets
class VectorBuilder2D(VectorBuilder):
  def __init__(self):
    super().__init__()
    self.setZ(0)
    self.setDim(2)

class VectorBuilder3D(VectorBuilder):
  def __init__(self):
    super().__init__()
    self.setDim(3)

vec2D = VectorBuilder2D().setX(50).setY(50).build()
print(vec2D.getState())
vec2D.normalize() # -> mag = 1
print(vec2D.getState())
print(vec2D.getMagnitude())

vec3D = VectorBuilder3D().setX(50).setY(50).setZ(100).build()
print(vec3D.getState())
vec3D.normalize() # -> mag = 1
print(vec3D.getState())
print(vec3D.getMagnitude())

class Director:
  def vectorZeros(builder:VectorBuilder):
    builder.setX(0)
    builder.setY(0)
    builder.setZ(0)

  def vectorOnes(builder:VectorBuilder):
    builder.setX(1)
    builder.setY(1)
    builder.setZ(1)

builder3D = VectorBuilder3D()
Director.vectorOnes(builder3D)
vec3D = builder3D.build()
print(vec3D.getState())


'''스칼라량의 곱'''
a = VectorBuilder3D().setX(50).setY(60).setZ(70).build()
a.normalize()
b = a.scalarMulti(3)
print("스칼라량의 곱",b)

'''객체간 +, - 연산'''
c = a.minus(b)
print("객체간 +, - 연산",c)