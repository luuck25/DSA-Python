



from collections import deque
def bfs(graph, node):
    visited = set()
    qq = deque([node])
    visited.add(node)
    
    result = []

    while qq:
        curr_node = qq.popleft()
        result.append(curr_node)
        print(node,end=" ")  # for printing

        for neighbour in graph[curr_node]:
            if neighbour not in  visited:
                visited.add(neighbour)
                qq.append(neighbour)


    return list


def bfs_disconnected(graph):
    visited = set()
    result = []

    for start in graph:              # 🔁 try every node
        if start not in visited:     # 🆕 new component
            queue = deque([start])
            visited.add(start)

            component = []           # nodes in this component

            while queue:
                node = queue.popleft()
                component.append(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            result.append(component)

    return result