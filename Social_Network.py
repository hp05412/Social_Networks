"""
@author : Pandey Hitesh Shabhamuni
The overall task for this project is to design and develop a standalone application in Python for analysing
small social networks and recommending likely new friend.

"""


# The social Network class contains main file in form of dictionary in order to access it anywhere in Project
class SocialNetwork:

    def __init__(self):
        self.file = input("Enter the file name: ")
        self.user_input = input("Do you want to see network file")
        self.social_nw = {}  # File used to store Social Network data

    def open_social_network_file(self):
        show = self.file
        try:
            if self.file == show:
                file = open(self.file, 'r')
                file.readlines()
                file.close()
        except Exception as e:
            print("File not found")
            print(e)

    def get_social_data(self):  # used as to get mutual friend
        try:
            file = open(self.file, "r")
        except:
            print("Try again")
            return
        data = file.readlines()
        total_members = int(data[0])  # convert string to int and remove it
        data.pop(0)  # remove the number 0 place index for use of loop
        users = []  # Used as Keys
        for line in data:
            word = line.split()  # read as newline and split hte values by ","
            for user in word:
                if user not in users:
                    users.append(user)

        # print("Unique users are :", users)
        self.social_nw = {}  # Used as Social Network File
        for user in users:
            self.social_nw[user] = []
            for line in data:
                word = line.split()
                for user2 in word:
                    if user2 == user:
                        pos = word.index(user)
                        try:
                            if pos == 1:  # manual position for values to find friends
                                self.social_nw[user].append(word[0])
                            else:
                                self.social_nw[user].append(word[1])
                            break
                        except:
                            self.social_nw[user].append(None)
        print("Friends Representation is :\n")
        for value in self.social_nw:
            print(value, "-> ", end="")
            i = 1
            for j in self.social_nw[value]:
                if i < len(self.social_nw[value]):
                    print(j, ",", end=" ")
                else:
                    print(j, end=" ")
                i = i + 1
            print()

        return self.social_nw


class Filehandler:

    def get_common_friends(self, data):  # Getting data from class Social Media in order to process common friend
        friends = {}
        for user in data:
            friends[user] = {}
            for friend in data:
                if user != friend:
                    friends[user][friend] = len(
                        set(data[user]).intersection(data[friend]))  # find common friend by intersection method
        return friends  # return the value to its function

    def mutual_frien(self):
        mutual = {}
        global friends
        mutual_friends = fun1.get_social_data()  # calling a class Social Network, method get_social_data() to run the mutual friend data
        for friends in fun1.get_social_data():
            if friends != fun1.get_social_data():
                if friends not in mutual:
                    mutual[friends] = 1
                else:
                    mutual[friends] += 1
        if not friends:
            return None
        users = sorted(mutual.items(), key=lambda x: x[1], reverse=True)
        return users[0][0]


class Statics:

    def __init__(self, mf):
        self.mf = mf  # used as MutualFriend data

    def countfreiend(self):
        user = input(" Enter a user ID to see number of friend")  # UserId to see number of friend
        for keys in self.mf.keys():
            if keys == user:  # Itereate the keys of mutual friend to count number of user
                print("The number of friends are", len(self.mf[user]))
                break

    def userfreiend(self):
        user = input(" Enter a user ID to see the friend of the user  ")  # UserId to see friend's of the given user
        for value in self.mf.keys():
            if value == user:
                print("The friends of user are ",
                      self.mf[user])  # Itereate the value of mutual friend to see user's friend
                break

    def least_friend(self):
        user_input = input(" Enter a user ID to see least number of friend the user have")
        positions = []  # output variable
        min_value = list()
        for keys, values in self.mf.items():
            if values == min_value:
                positions.append(keys)
            if values < min_value:
                min_value = values
                positions = []  # output variable
                positions.append(keys)
                print(positions)

        return positions

    def indirectfriend(self, data):
        uncommon = {}
        for user in data:
            uncommon[user] = {}
            for friend in data:
                if user != friend:
                    uncommon[user][friend] = len(
                        set(data[user]).difference(data[friend]))  # find difference friend by intersection method
        return uncommon  # return the value to its function


# __main__program
user_input = input("Initialize the programme y/n: ") # calls the function requested by user
if user_input == "y" or "yes":
    while user_input: # Keep the programme on until the user terminate it
        choice = input("Do you want to continue y/n: ")
        if choice == "y" or "yes":
            fun1 = SocialNetwork()
            fun1.open_social_network_file()
            mutual_friends = fun1.get_social_data()
            st = Statics(mutual_friends)
            st.countfreiend()
            st.userfreiend()
            st.least_friend()
            fun1.get_social_data()
            fh = Filehandler()
            # print(mutual_friends)
            choice = input("Do you want to see common friends ")
            if choice == "y":
                print("common friend count for each member of the social network are")
                common_friends = fh.get_common_friends(mutual_friends)

                for key, value in common_friends.items():  # to find common friend and count them
                    friends = ",".join([f for f in value.keys()])  # comparing keys and counting them
                    counts = ",".join([str(c) for c in value.values()])  # comparing values and counting tem
                    print(f"{key}->[{counts}]")  # Result of the loop
            else:
                print("Exit")
        else:
            print("try again")
    else:
        print("Do you want to try again? ")
else:
    print("File terminated")
