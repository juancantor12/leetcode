"""
You are given an integer numberOfUsers representing the total number of users and an array events of size n x 3.
Each events[i] can be either of the following two types:
Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
This event indicates that a set of users was mentioned in a message at timestampi.
The mentions_stringi string can contain one of the following tokens:
id<number>: where <number> is an integer in range [0,numberOfUsers - 1]. There can be multiple ids separated by a single whitespace and may contain duplicates. This can mention even the offline users.
ALL: mentions all users.
HERE: mentions all online users.
Offline Event: ["OFFLINE", "timestampi", "idi"]
This event indicates that the user idi had become offline at timestampi for 60 time units. The user will automatically be online again at time timestampi + 60.
Return an array mentions where mentions[i] represents the number of mentions the user with id i has across all MESSAGE events.
All users are initially online, and if a user goes offline or comes back online, their status change is processed before handling any message event that occurs at the same timestamp.
Note that a user can be mentioned multiple times in a single message event, and each mention should be counted separately.
"""
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        users = { str(n) : {"online": True, "back_online": None} for n in range(numberOfUsers)}
        sorted_events = sorted(events, key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        mentions = [0]*numberOfUsers
        for event, timestamp, arg in sorted_events:
            timestamp = int(timestamp)
            if event == "OFFLINE":
                users[arg]["online"] = False
                users[arg]["back_online"] = timestamp + 60
            else: # message
                if arg == "ALL":
                    mentions = [ x + 1 for x in mentions]
                else:
                    mentioned = []
                    if arg == "HERE":
                        mentioned = [str(i) for i in range(numberOfUsers)]
                        for i in mentioned:
                            if users[i]["online"] or users[i]["back_online"] <= timestamp:
                                mentions[int(i)] += 1
                                users[i]["online"] = True
                                users[i]["back_online"] = None
                    else:
                        mentioned = [ x[2:] for x in arg.split(" ")]
                        for i in mentioned:
                            mentions[int(i)] += 1
        return mentions

        