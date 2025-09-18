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
# import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}  
        self.cuisine_heaps = {}  

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        # Python heaps sort based on the tuple indexes, if there is a tie with the nth index, it will look for the
        # next index, in this case, on a tie on ratings, it will sort based on the food str value lexicographically.
        # the str class __gt__ (greather than >) and __lt__ (less than <) methods sort lexicographically by default
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine] # get the current cuisine heap
        while heap: # traverse the heap
            rating_neg, food = heap[0] # get the heap top element
            if self.food_info[food][1] == -rating_neg: # if the rating on the heap top element matches the food info
                return food # return the food name
            heapq.heappop(heap)  # else, the heap value is outdated (this food ratin was lowered and the heap doesnt know)
            # simply remove the item and keep iterating the heap.
        return ""  