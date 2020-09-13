# /*
#  * @Author: gaoyuan 
#  * @Date: 2020-07-24 21:25:38 
#  * @Last Modified by:   gaoyuan 
#  * @Last Modified time: 2020-07-24 21:25:38 
#  */
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]):
        self.res = []
        def graphDFS(graph, start, end, path):
            if start == end:
                self.res.append(path)
            for node in graph[start]:
                graphDFS(graph,node,end,path+[node])
        graphDFS(graph,0,len(graph)-1,res,[0])
        return self.res
