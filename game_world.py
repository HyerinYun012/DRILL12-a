#객체로 구성된 게임 월드
# world = [] # 게임 월드에 존재하는 모든 객체를 담는 리스트

# 계층적 구조를 갖는 게임월드
world = [ [], [] ]  # layer 계층이 들어감 계층 안에 객체가 들어감

num = 0

# 게임 월드에 객체를 담는 함수
def add_object(o, depth = 0): # depth: 0(배경), 1(캐릭터)
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 이미 찾아서 제거했기 때문에 더이상 찾기 위해서 탐색할 필요가 없다(낭비를 막기 위해 return을 함)

# 게임 로직
def update():
    for layer in world:
        for o in layer:
            o.update()

# 게임 월드 렌더링

def render():
    for layer in world:
        for o in layer:
            o.draw()
            
