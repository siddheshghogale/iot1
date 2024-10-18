graph={'Devgad':['Malvan','kankavali'],
       'Malvan':['Devgad','kankavali','vengurla','kudal'],
       'vengurla':['Malvan','sawantawadi','kudal'],
       'sawantawadi':['kudal','vengurla','Dodamarg'],
       'Dodamarg':['sawantawadi'],
       'kudal':['sawantawadi','vengurla','Malvan','kankavali'],
       'kankavali':['kudal','Malvan','Devgad','vaibhavwadi'],
       'vaibhavwadi':['kankavali']}
visited=[]
node='Devgad'
def dfs(node,visited,graph):
    if node not in visited:
        print(node)
        visited.append(node)
        for i in graph[node]:
            dfs(i,visited,graph)
dfs(node,visited,graph)       






graph={'Devgad':['Malvan','kankavali'],
       'Malvan':['Devgad','kankavali','vengurla','kudal'],
       'vengurla':['Malvan','sawantawadi','kudal'],
       'sawantawadi':['kudal','vengurla','Dodamarg'],
       'Dodamarg':['sawantawadi'],
       'kudal':['sawantawadi','vengurla','Malvan','kankavali'],
       'kankavali':['kudal','Malvan','Devgad','vaibhavwadi'],
       'vaibhavwadi':['kankavali']}
visited=[]
node='Devgad'
queue=[]
def bfs(node,visited,graph):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=' ')
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
bfs(node,visited,graph)                
