class DiceGame:
    history = []

    @classmethod
    def roll_dice(cls, num_dice, sides):
        import random
        rolls = []
        for i in range(num_dice):
            num_sides = sides[i]
            roll = random.randint(1, num_sides)
            rolls.append(roll)
        roll_sum = sum(rolls)
        rolls.append(roll_sum)
        cls.history.append(rolls)
        if len(cls.history) > 10:
            cls.history.pop(0)
        return rolls

    @classmethod
    def get_history(cls):
        return cls.history
