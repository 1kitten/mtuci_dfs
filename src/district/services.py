from district.schemas import DisctrictSearchResponse, DistrictSearchIn


def can_reach(total_districts, tunnels, district_a, district_b):
    graph = {}
    for i in range(1, total_districts+1):
        graph[i] = []

    for u, v in tunnels:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()

    def dfs(node):
        if node == district_b:
            return True
        
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        
        return False
    
    return "YES" if dfs(district_a) else "NO"


async def search_path(search_params: DistrictSearchIn):
    return DisctrictSearchResponse(result=can_reach(
        total_districts=search_params.total_districts,
        tunnels=search_params.tunnels,
        district_a=search_params.district_a,
        district_b=search_params.district_b,
    ))
