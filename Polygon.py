

class Matrix:
    
    def __init__(self,lst):
        self.list = lst[:]
        self.dim = (len(self.list) ,len(self.list[0]))
        for row in self.list:
            if not self.dim[1] == len(row):
                raise ValueError("not all lines are of same length")
            
    def __repr__(self):
        return str(self.list)
    
    def get(self,i,j):
        if self.dim[0]>= i and self.dim[1]>=j:
            return self.list[i][j]
        else:
            raise IndexError ("matrix index out of range") 

    def transpose(self):
        trans = []
        for i in range(self.dim[1]):
            trans_row = []
            for j in range(self.dim[0]):
                trans_row.append(self.get(j,i))
            trans.append(trans_row)
            trans_row = []
        return Matrix(trans)

    def __add__(self,other):
        if self.dim == other.dim:
            new_matrix = []
            new_row = []
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    new_row.append(self.get(i, j) + other.get(i, j))
                new_matrix.append(new_row)
                new_row = []
            return Matrix(new_matrix)
        else:
            raise ValueError ("dims do not match")
        

    def __mul__(self,other):
        if self.dim == other.dim:
            new_matrix = []
            new_row = []
            for i in range(self.dim[0]):
                for j in range(self.dim[1]):
                    new_row.append(self.get(i, j) * other.get(i, j))
                new_matrix.append(new_row)
                new_row = []
            return Matrix(new_matrix)
        
        else:
            raise ValueError ("dims do not match")

    def dot(self,other):
        if self.dim[1] == other.dim[0]:
            new_matrix = []
            new_row = []
            new_dig = 0
            for i in range(self.dim[0]):
                for j in range(other.dim[1]):
                    for s in range(self.dim[1]):
                        new_dig += (self.get(i,s) * other.get(s,j))
                    new_row.append(new_dig)
                    new_dig = 0
                new_matrix.append(new_row)
                new_row = []
            return Matrix(new_matrix)
        
        else:
            raise ValueError ("dims do not match")

 ##########################################
class Point: 
    def __init__(self,x,y):
        ''' x and y are int or float '''
        self.x = x
        self.y = y
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def shift(self,dx,dy):
        self.x += dx
        self.y += dy
###########################################
        

class Polygon:

    def __init__(self,points):
        self.vertices = points
        if len(self.vertices) < 3:
            raise ValueError ("not enough vertices")

    def __repr__(self):
        return str(self.vertices)

    def shift(self,dx,dy):
        for point in self.vertices:
            point.shift(dx, dy)

    def circumference(self):
        circ = 0
        n = 0
        for point in self.vertices:
            while n <= len(self.vertices)-2:
                circ += self.vertices[n].distance(self.vertices[n+1])
                n += 1
        circ += self.vertices[-1].distance(self.vertices[0])
        return circ
                           

class Square(Polygon):

    def __init__(self, points):
        Polygon.__init__(self,points)
        self.edge = self.vertices[0].distance(self.vertices[1])
        dist_list = []
        n = 0
        for point in self.vertices:
            while n <= len(self.vertices)-2:
                dist_list.append(self.vertices[n].distance(self.vertices[n+1]))
                n += 1
        dist_list.append(self.vertices[-1].distance(self.vertices[0]))
        for i in range(len(dist_list)-1):
            if dist_list[i]!=dist_list[i+1]:
                equal_distance = False
            else:
                equal_distance = True
        if len(self.vertices) != 4 or (self.vertices[0].distance(self.vertices[2])) != (self.vertices[1].distance(self.vertices[3])) or equal_distance == False:
            raise ValueError ("the given vertices don't form a square")

    def __repr__(self):
        result = "Square - "
        result += Polygon.__repr__(self)
        return result

    def shift(self, dx, dy):
        return Polygon.shift(self,dx,dy)

    def circumference(self):
        return self.edge*4

    def area(self):
        return self.edge**2

        
class Triangle(Polygon):

    def __init__(self, points):
        Polygon.__init__(self, points)
        if len(self.vertices)!=3:
            raise ValueError ('triangle must have 3 vertices')
                         
    def __repr__(self):
            result = "Triangle - "
            result += Polygon.__repr__(self)
            return result

    def shift(self, dx, dy):
            return Polygon.shift(self,dx,dy)

    def circumference(self):
        return Polygon.circumference(self)

    def area(self):
        s = (self.circumference())
        s = s/2
        a = self.vertices[0].distance(self.vertices[1])
        b = self.vertices[1].distance(self.vertices[2])
        c = self.vertices[2].distance(self.vertices[0])
        area = s*(s-a)*(s-b)*(s-c)
        area = area**0.5
        return area
        
                         
                        

