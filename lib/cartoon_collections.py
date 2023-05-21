def roll_call_dwarves(self):
    for i in range(len(self)):
        print(f"{i + 1}. {self[i]}")
    pass

def summon_captain_planet(planteers):
    new_planteers = []
    for planteer in planteers:
        new_planteer = planteer.capitalize() + "!"
        new_planteers.append(new_planteer)
    return new_planteers

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    for string in strings:
        if string in cheeses:
            return string

    return None
