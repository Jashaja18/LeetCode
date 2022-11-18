class Solution:
    def __init__(self):
        self.paths = None
        self.target = None
        self.graph = None

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.target = len(graph) - 1
        self.paths = []
        self.dfs(0, [])
        return self.paths

    def dfs(self, param, param1):
        pass
