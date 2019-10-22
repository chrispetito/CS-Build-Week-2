import requests

node = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'

post_data = {
    "direction": "n"
}

r = requests.post(url=node + "/move", json=post_data, Authorization='Token fe3abb92210f3b857851c6abe756d336a12a6e4f')
data = r.json()

room_id = data['room_id']
room_exits = data['exits']


def getOpposite(direction):
    if direction is 'n':
        return 's' 
    elif direction is 's':
        return 'n'
    elif direction is 'e':
        return 'w'
    elif direction is 'w':
        return 'e'

# visited rooms dict
visited = {}
# initilize rooms dict with current room exits
visited[room_id] = room_exits
# checked rooms list
checked_rooms = []
# moves count
moves_count = []

while len(list(visited)) < 499:
    # if current room is not in visited...
    if room_id not in visited:
        # add room to visited
        visited[room_id] = room_exits
        visited[room_id].remove(checked_rooms[-1])
    # If there aren't any rooms to travel, back track until there is
    while len(visited[room_id]) is 0 and len(checked_rooms) > 0:
        path = checked_rooms.pop()
        moves_count.append(path)
        # player.travel(path)
    # move player
    move = visited[room_id].pop(0)
    # add move to count and reverse path
    checked_rooms.append(getOpposite(move))
    moves_count.append(move)
    # player.travel(move)