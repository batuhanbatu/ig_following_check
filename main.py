from os import path

# Opening and reading a saved html file
if path.exists('followers.html') & path.exists ('following.html') == False:
    print("Please make sure that you have followers.html and following.html in this directory")
    exit()
followersFile = open("followers.html", "r")
followingFile = open("following.html", "r")
followersHtmlString = followersFile.read()
followingHtmlString = followingFile.read()

# Splitting that file for each user
splittedHtml = followersHtmlString.split('PZuss')
eachFollowersHtml = splittedHtml[1].split('<li class="', 999999999)

# Deleting first element (Because it does not keep account list)
eachFollowersHtml.pop(0)
followers = []

# Making a trim operation for each follower and add it to followers array
for i in eachFollowersHtml:
    followers.append(((i.split('FPmhX'))[1].split("</a>")[0]).split(' tabindex="0">')[1])

# Doing same operations for following list
splittedHtml = followingHtmlString.split('PZuss')
eachFollowingHtml = splittedHtml[1].split('<li class="', 999999999)
eachFollowingHtml.pop(0)
following = []

for i in eachFollowingHtml:
    following.append(((i.split('FPmhX'))[1].split("</a>")[0]).split(' tabindex="0">')[1])

# Controlling each followers whether we follow that account or no and adding it to not
# following list according to the result
counter = 0
notFollowingList = []
for i in followers:
    for j in following:
        if i == j: break
        else:
            counter += 1
            if counter == len(following): notFollowingList.append(i)
    counter = 0

# Controlling each following whether that follows our account or no and adding it to not
# followers list according to the result
counter = 0
notFollowersList = []
for i in following:
    for j in followers:
        if i == j: break
        else:
            counter += 1
            if counter == len(followers): notFollowersList.append(i)
    counter = 0

# Printing results to the python terminal
print("\nHere is the accounts which you do not follow (" + str(len(notFollowingList)) + ") accounts:\n")
for i in notFollowingList: print(i)
print("\n************************************************")
print("\nHere is the accounts which do not follow you (" + str(len(notFollowersList)) + ") accounts:\n")
for i in notFollowersList: print(i)

# Author: Batuhan Batu
# https://github.com/batuhanbatu/ig_following_check