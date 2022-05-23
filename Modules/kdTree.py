from operator import itemgetter
import math

class Node:
    def __init__(self, location, left_child=None, right_child=None):
        self.location = location
        self.left_child = left_child
        self.right_child = right_child

class KDTree:
    def __init__(self, points):
        self.tree = self._make_kdtree(points)
        if len(points) > 0:
            self.k = len(points[0]) # 維度，已這題來說就是 X Y 兩維
        else:
            self.k = None
 
    def _make_kdtree(self, points, depth=0):
        if not points:
            return None
 
        k = len(points[0])
        axis = depth % k

        # 這邊偷懶，不根據變異數來決定取哪一個維度，直接X -> Y -> X -> Y...
        points.sort(key=itemgetter(axis))
        median = len(points) // 2
 
        return Node(
            location=points[median],
            left_child=self._make_kdtree(points[:median], depth + 1),
            right_child=self._make_kdtree(points[median + 1:], depth + 1))
 
    def find_nearest(self,
                     point,
                     k = 1,
                     root=None,
                     axis=0,
                     dist_func=lambda p1, p2: math.fabs(p1[0] - p2[0]) + math.fabs(p1[1] - p2[1])):
        '''
        查詢最接近 point 的點

        Args:
            point ([x, y]): 欲搜尋的點
            k (int): 欲搜尋的點數量
            root ([x, y]): 當前樹根
            axis (int): 維度
            dist_func (func): 距離計算函式
        
        Returns:
            (dist, location): 最接近點距離, 點座標
        '''

        if root is None:
            root = self.tree
            self._best = []
 
        # 若不是葉節點，則繼續向下走
        if root.left_child or root.right_child:
            new_axis = (axis + 1) % self.k
            if point[axis] < root.location[axis] and root.left_child:
                self.find_nearest(point, k, root.left_child, new_axis)
            elif root.right_child:
                self.find_nearest(point, k, root.right_child, new_axis)
 
        # 回溯：嘗試更新最短距離
        dist = dist_func(root.location, point)
        if len(self._best) < k or dist < self._best[-1][0]:
            self._best.append((dist, root.location))
            self._best.sort(key=itemgetter(0))
            self._best = self._best[:k]
 
        # 若超球與另一邊超矩形相交
        if len(self._best) < k or abs(point[axis] - root.location[axis]) < self._best[-1][0]:
            new_axis = (axis + 1) % self.k
            if root.left_child and point[axis] >= root.location[axis]:
                self.find_nearest(point, k, root.left_child, new_axis)
            elif root.right_child and point[axis] < root.location[axis]:
                self.find_nearest(point, k, root.right_child, new_axis)
 
        return self._best

if __name__ == "__main__":
    points = [[0,0],[1,1],[3.5,3.5],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]]
    kdtree = KDTree(points)
    print(kdtree.find_nearest([1.5, 1.5], 2))