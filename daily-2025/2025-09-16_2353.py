"""
Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

 

Example 1:

Input
["FoodRatings", "highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

"""
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.food_map = {}
        for i, food in enumerate(foods):
            self.food_map[food] = i
        self.max_rating_by_cuisine = {}
        for i, rating in enumerate(ratings):
            if cuisines[i] not in self.max_rating_by_cuisine:
                self.max_rating_by_cuisine[cuisines[i]] = (rating, foods[i])
            else:
                r, f = self.max_rating_by_cuisine[cuisines[i]]
                if ratings[i] > r:
                    self.max_rating_by_cuisine[cuisines[i]] = (rating, foods[i])
        print("foods: ", self.foods)
        print("ratings: ", self.ratings)
        print("cuisines: ", self.cuisines)
        print("food_map: ", self.food_map)
        print("max_rating_by_cuisine: ", self.max_rating_by_cuisine)


    def changeRating(self, food: str, newRating: int) -> None:
        #TODO: If the biggest rated food for x cuisine gets its rating reduced, the max_rating_by_cuisine needs to be recalculated.
        i = self.food_map[food]
        print("updating self.ratings for food=", food, " on i=", i, "from", self.ratings[i], " to ", newRating)
        print("after: ", self.ratings)
        self.ratings[i] = newRating
        print("before: ", self.ratings)
        # currentRating = self.highestRated(self.cuisines[i])
        old_rating, old_food = self.max_rating_by_cuisine[self.cuisines[i]]
        print(f"if ({newRating} > {old_rating}) or ({newRating} == {old_rating} and {food} < {old_food}):")
        if (newRating > old_rating) or (newRating == old_rating and food < old_food):
            print("updating max_rating_by_cuisine, before: ", self.max_rating_by_cuisine)
            self.max_rating_by_cuisine[self.cuisines[i]] = (newRating, food)
            print("after: ", self.max_rating_by_cuisine)


    def highestRated(self, cuisine: str) -> str:
        rating, food = self.max_rating_by_cuisine[cuisine]
        return food

