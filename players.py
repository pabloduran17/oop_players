class Player():
    def __init__(self, p_first_name, p_last_name, p_height_cm, p_weight_kg):
        self.first_name = p_first_name
        self.last_name = p_last_name
        self.height_cm = p_height_cm
        self.weight_kg = p_weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(p_first_name=first_name, p_last_name=last_name, p_height_cm=height_cm, p_weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(p_first_name=first_name, p_last_name=last_name, p_height_cm=height_cm, p_weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cars = red_cards


print("Enter players info")

f_name = input("Player's first name: ")
l_name = input("Player's last name: ")
heightcm = input("player's height: ")
weightkg = input("Player's weight: ")
n_goals = input("Player's goals scored: ")
y_cards = input("Player's yellow cards: ")
r_cards = input("Player's red cards: ")

new_player = FootballPlayer(first_name=f_name,
                            last_name=l_name,
                            height_cm=heightcm,
                            weight_kg=weightkg,
                            goals=n_goals,
                            yellow_cards=y_cards,
                            red_cards=r_cards)

with open("footballplayer_dict.txt", "w") as footballplayer_file:
    footballplayer_file.write(str(new_player.__dict__))

print("You got it!")
print("Player's info: {0}".format(new_player.__dict__))
