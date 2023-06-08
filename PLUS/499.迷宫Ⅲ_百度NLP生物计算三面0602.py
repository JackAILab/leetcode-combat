# 由空地和墙组成的迷宫中有一个球。球可以向上（u）下（d）左（l）右（r）四个方向滚动，但在遇到墙壁前不会停止滚动。当球停下时，可以选择下一个方向。迷宫中还有一个洞，当球运动经过洞时，就会掉进洞里。

# 给定球的起始位置，目的地和迷宫，找出让球以最短距离掉进洞里的路径。 距离的定义是球从起始位置（不包括）到目的地（包括）经过的空地个数。通过'u', 'd', 'l' 和 'r'输出球的移动方向。 由于可能有多条最短路径， 请输出字典序最小的路径。如果球无法进入洞，输出"impossible"。

# 迷宫由一个0和1的二维数组表示。 1表示墙壁，0表示空地。你可以假定迷宫的边缘都是墙壁。起始位置和目的地的坐标通过行号和列号给出。

# 输入 1: 迷宫由以下二维数组表示

# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0

# 输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
# 输入 3: 洞的位置 (rowHole, colHole) = (0, 1)

# 输出: "lul"

# 解析: 有两条让球进洞的最短路径。
# 第一条路径是 左 -> 上 -> 左, 记为 "lul".
# 第二条路径是 上 -> 左, 记为 'ul'.
# 两条路径都具有最短距离6, 但'l' < 'u'，故第一条路径字典序更小。因此输出"lul"。

# 输入 1: 迷宫由以下二维数组表示

# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0

# 输入 2: 球的初始位置 (rowBall, colBall) = (4, 3)
# 输入 3: 洞的位置 (rowHole, colHole) = (3, 0)

# 输出: "impossible"

# 示例: 球无法到达洞。

# 迷宫中只有一个球和一个目的地。
# 球和洞都在空地上，且初始时它们不在同一位置。
# 给定的迷宫不包括边界 (如图中的红色矩形), 但你可以假设迷宫的边缘都是墙壁。
# 迷宫至少包括2块空地，行数和列数均不超过30。

# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/the-maze-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List # BFS广度优先搜索，双100%，大量注释


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
                                                    
        directions = [(-1,0,'u'),(0,1,'r'),(0,-1,'l'),(1,0,'d')]    
                                                    # 定义上下左右四个方向和对应字符
        m = len(maze)                               # 获取矩阵大小
        n = len(maze[0])
        queue = [(ball[0],ball[1])]                 # 构造队列，并将起始位置包含其中
                                                    # distance 保存从起点到每个点的距离
                                                    # string 保存每个点对应的字符串
        distance = [[float('inf')]*n for _ in range(m)]
        string = [["impossible"]*n for _ in range(m)]
        distance[ball[0]][ball[1]] = 0              # 对起点的distance和string进行初始化
        string[ball[0]][ball[1]] = ""

        while queue:
            i,j = queue.pop(0)                      # 弹出坐标值i,j
            
            for dx,dy,letter in directions:         # 对四个方向进行遍历，letter保存了操作对应的字符
                x,y,step,word =i+dx,j+dy,distance[i][j],string[i][j]
                while 0<=x<m and 0<=y<n and maze[x][y] == 0 and (x-dx!=hole[0] or y-dy!=hole[1]):                                      
                                                    # 当x,y坐标合法，并且对应值为0
                                                    # 且没有越过hole时
                    x = x+dx                        # 继续前进，模拟小球的滚动过程
                    y = y+dy                        
                    step += 1                       # 记录步数

                x = x - dx
                y = y - dy

                if distance[x][y] > step or (distance[x][y]==step and word+letter<string[x][y]):           
                                                    # 如果起点到该点的距离比当前距离大
                                                    # 或者相等，但是字符串的字典序大
                                                    # 更新该距离和字符串，并将坐标加入队列
                    distance[x][y] = step
                    string[x][y] = word+letter
                    print(x,y,string[x][y])   
                    if x!=hole[0] or y!=hole[1]:    # 当坐标不是hole坐标时
                        queue.append((x,y))         # 将其添加到队列中
                                           
        return string[hole[0]][hole[1]]

# 作者：heimisa000
# 链接：https://leetcode.cn/problems/the-maze-iii/solution/python3-bfsyan-du-you-xian-sou-suo-shuang-100da-li/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

slover = Solution()

maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
ball = [4,3]
hole = [0,1]
result = slover.findShortestWay(maze, ball, hole)
print(result)  # 预期输出：'dlldruld'







# 思路(广度优先搜索):
# 求到终点的步数最小, 且指令字典序最小, 可以认为节点之间是带权的, 只有可滚动到的格子视为节点,
# 所以是个带权最短路问题, 可以用Dijkstra求解, 也可以用BFS求解

# 作者：DreamerDiWu
# 链接：https://leetcode.cn/problems/the-maze-iii/solution/dijkstra-python3-dai-ma-ke-du-xing-man-f-cjst/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



# class Solution:
#     def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
#         ROWS = len(maze)
#         COLS = len(maze[0])
#         def roll(x, y):
#             def hitBoundry(x, y):
#                 if not (0 <= x < ROWS and 0 <= y < COLS):
#                     return True
#                 return maze[x][y] == 1
#             def rollBydirection(x, y, dx, dy):
#                 while not hitBoundry(x + dx, y + dy):
#                     x += dx 
#                     y += dy
#                     if [x, y] == hole:
#                         break
#                 return x, y 
#             directions = [('d', 1, 0), ('l', 0, -1), ('u', -1, 0), ('r', 0, 1)]
#             for ins, dx, dy in directions:
#                 nx, ny = rollBydirection(x, y, dx, dy)
#                 yield nx, ny, ins
#         PQ = [[0, "", ball[0], ball[1]]]
#         visited = set()
#         while PQ:
#             steps, instructions, curX, curY = heapq.heappop(PQ)
#             if [curX, curY] == hole:
#                 return instructions
#             if (curX, curY) in visited:
#                 continue
#             visited.add((curX, curY))
#             for nextX, nextY, nextIns in roll(curX, curY):
#                 # print(curX, curY, nextX, nextY, nextIns)
#                 nextInstructions = instructions + nextIns
#                 nextSteps = abs(curX-nextX) + abs(curY-nextY)
#                 heapq.heappush(PQ, [steps + nextSteps, nextInstructions, nextX, nextY])
#         return "impossible"

# 作者：DreamerDiWu
# 链接：https://leetcode.cn/problems/the-maze-iii/solution/dijkstra-python3-dai-ma-ke-du-xing-man-f-cjst/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



