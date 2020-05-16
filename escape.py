"""
 program title: Escape the House
 program description: text based game in python
 author: steve
"""

def gameloop(r):
    print(map[r]["room_name"]);
    print(map[r]["room_description"]);
    print(map[r]["exits"]);
    dir = input("Which way do you want to move?\n");
    flag = 0;
    while(flag != 1):
        if dir == "n" or \
        dir == "s" or \
        dir == "e" or \
        dir == "w":
            print("\nYou move {}\n".format(compass[dir]));
            break;
        else:
            print("\nInvalid entry, try again");
            dir = input("Which way do you want to move?\n");
    return map[r][dir];


compass = {"n": "north", "s": "south", "e": "east", "w": "west"};
map = [];
map.extend([
    #room_name, room_description, room_exits_desc, to_north, to_east, to_south, to_west
    {"room_name": "Porch", "room_description": "The brick walls and black and white tileing tell you your are in the porch.\nThere is no one around.\nYou look though the open door into the hall.", "exits": "\nYou can move North", "n": 1, "s": 11, "e": 10, "w": 10},
    {"room_name": "Hall", "room_description": "The house is still silent, you see some dirt on the carpet from an earler escapade.", "exits": "\nYou can move North, East, South or West", "n": 6, "s": 0, "e": 2, "w": 3},
    {"room_name": "Toilet", "room_description": "The toilet and sink gleam the unintresting hostility of cold, white porcelin.", "exits": "\nYou can move West", "n": 10, "s": 10, "e": 10, "w": 1},
    {"room_name": "Lounge", "room_description": "You enter the lounge timmidly, your not usually allowed in here becuase of the orniments.\nYou better slink out quickly.", "exits": "\nYou can move North or East", "n": 5, "s": 10, "e": 1, "w": 10},
    {"room_name": "Dining Room", "room_description": "A veritable forist of chair and table legs in here.", "exits": "\nYou can move East", "n": 10, "s": 10, "e": 5, "w": 10},
    {"room_name": "Play Room", "room_description": "You step over the toys strewn on the floor. A squeeky one tempts you but you resist.\nYou must continue your quest to get out.", "exits": "\nYou can move East, South, or West", "n": 10, "s": 3, "e": 6, "w": 4},
    {"room_name": "Kitchen", "room_description": "Your faviorit room! The food is hidden away but you can smell something nice brewing.", "exits": "\nYou can move North, South, East, or West", "n": 8, "s": 1, "e": 7, "w": 5},
    {"room_name": "Stairs", "room_description": "You know the garden cant be upstairs but you go up anyway.", "exits": "\nYou can move West", "n": 10, "s": 10, "e": 10, "w": 6},
    {"room_name": "Back Porch", "room_description": "The back pourch, and what luck, the garage door is open too", "exits": "\nYou can move East or South", "n": 10, "s": 6, "e": 9, "w": 10},
    {"room_name": "Garage", "room_description": "This rooms packed, bikes, cars, boxes, its a bit dark though.\nThere is a shaft of light comming from the back door though!\nCould this be it?", "exits": "\nYou can move North or West", "n": 11, "s": 10, "e": 10, "w": 8},
    {"room_name": "There is no room there!", "room_description": "You cannot move that way\n", "exits": "", "n": 10, "s": 10, "e": 10, "w": 10},
    {"room_name": "Garden", "room_description": "SCUCESS! You mannage to escape the building\nYou let out a exultent WOOF and get ready for a happy romp!", "exits": "\nCongratulations, You have finished the game", "n": 10, "s": 10, "e": 10, "w": 10},
]);

print("\n****************");
print("Escape the House");
print("****************");
print("The object of the game is to find your way out of the hosue in as few moves as possible\n" \
"To move enter n, s, e, or w\n");

print("You open your eyes and stand up.\nDespite your happy dream of the outside world you realise you are still inside.\n");

r = 0; #set the starting room
count = 0;

while(r != 11): #break if final room reached
    r_temp = gameloop(r);

    #reset if you go wrong
    if r_temp == 10:
        print(map[r_temp]["room_name"]);
        print(map[r_temp]["room_description"]);
    else:
        r = r_temp;

    #count your turns
    count += 1;

print(map[r]["room_name"]);
print(map[r]["room_description"]);
print(map[r]["exits"]);
print();
print("Your score is {}".format(count));
print("Smaller is better");
print();
