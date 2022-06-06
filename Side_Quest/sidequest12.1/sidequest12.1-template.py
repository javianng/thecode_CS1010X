#
# CS1010X --- Programming Methodology
#
# Sidequest 12.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

import json

# Reading json file
def read_json(filename):
    """
    Reads a json file and returns a list of modules
    To find out more about json, please google ;)

    For example, cs1010x-fbdata.json contains:

    {
       "members": {
          "data": [
             {
                "name": "Aadit Kamat",
                "id": "1003982836283025"
             },
             {
                "name": "Rakshit Gogia",
                "id": "10204299775189027"
             },
             ...
          ]
       },
       "description": "This is the official FB Group for ...",
       "name": "CS1010X",
       "feed": {
          "data": [
             {
                "message": "Might be useful for the business analytics ...",
                "from": {
                   "name": "Ben Leong",
                   "id": "10152805891837166"
                },
                "name": "Machine Learning with Python - BDU"
                "id": "409054432560329_1002582839874149",
                "likes": {
                   "data": [
                      {
                         "id": "10208170707289199",
                         "name": "Lim Kian Hwee"
                      },
                      {
                         "id": "10204292869386114",
                         "name": "Siidheesh Theivasigamani"
                      },
                      ...
                   ]
                },
                ...
             },
             ...
          ]
       },
       "id": "409054432560329"
    }

    """
    datafile = open(filename, 'r',  encoding='utf-8')
    return json.loads(datafile.read())

# CS1010X Facebook Group Data as a dictionary object
fb_data = read_json('cs1010x-fbdata.json')

##########
# Task a #
##########

def count_comments(data):
    counter = 0
    for data_type in data['feed']['data']:
        if "comments" in data_type:
            for comments in data_type['comments']['data']:
                counter+=1
    return counter

# print("Number of Comments in CS1010X: ", count_comments(fb_data))

##########
# Task b #
##########

def count_likes(data):
    counter = 0
    for data_type in data["feed"]["data"]:
        if "likes" in data_type:
            for i in data_type["likes"]["data"]:
                counter += 1
        if "comments" in data_type:
            for comment_data_type in data_type["comments"]["data"]:
                counter += comment_data_type["like_count"]
    return counter

# print("Number of Likes in CS1010X: ", count_likes(fb_data))

##########
# Task c #
##########

def create_member_dict(data):
    member_dict = {}
    for i in data["members"]["data"]:
        if not "gender" in i:
            member_dict[i["id"]] = {"name": i["name"]}
        else:
            member_dict[i["id"]] = {"gender": i["gender"], "name": i["name"]}
    return member_dict

# member_dict = create_member_dict(fb_data)
# print(member_dict["10205702832196255"])

# Q: Why did we choose the id of the member data object to be the key?
# A: This allows us to find the member using the id that is shared to the social media account. There would 
# not be the same index used to represent different members, making it suitable as a unique identifier.

# Q: It is inappropriate to use the name as the key. What will happen if we use the name as the key of member_dict?
# A: This would cause issues when two people have the exact same name. There would be an overide of dictionary values
# and the very first imput will be overide by the next one.

##########
# Task d #
##########

def posts_freq(data):
    freq_dict = {}
    for i in data["feed"]["data"]:
        if "from" in i:
            if i["from"]["id"] not in freq_dict:
                freq_dict[i["from"]["id"]] = 1
            else:
                freq_dict[i["from"]["id"]] += 1
    return freq_dict

# print("Posts Frequency: ", posts_freq(fb_data))

##########
# Task e #
##########

def comments_freq(data):
    freq_dict = {}
    for i in data["feed"]["data"]:
        if "comments" in i:
            for j in i["comments"]["data"]:
                if j["from"]["id"] not in freq_dict:
                    freq_dict[j["from"]["id"]] = 1
                else:
                    freq_dict[j["from"]["id"]] += 1
    return freq_dict

# print("Comments Frequency: ", comments_freq(fb_data))

##########
# Task f #
##########

def likes_freq(data):
    freq_dict = {}
    for i in data["feed"]["data"]:
        if "likes" in i:
            for j in i["likes"]["data"]:
                if j["id"] not in freq_dict:
                    freq_dict[j["id"]] = 1
                else:
                    freq_dict[j["id"]] += 1
                    
    return freq_dict

# print("Likes Frequency: ", likes_freq(fb_data))

##########
# Task g #
##########

def popularity_score(data):
    score_dict = {}
    score = 0
    for i in data["feed"]["data"]:
        if "from" in i and "likes" in i:
            if i["from"]["id"] not in score_dict:
                score_dict[i["from"]["id"]] = len(i["likes"]["data"])
            else:
                score_dict[i["from"]["id"]] += len(i["likes"]["data"])
        if "comments" in i:
            for j in i["comments"]["data"]:
                if j["like_count"] > 0:
                    if j["from"]["id"] not in score_dict:
                        score_dict[j["from"]["id"]] = j["like_count"]
                    else:
                        score_dict[j["from"]["id"]] += j["like_count"]
    return score_dict

# print("Popularity Score: ", popularity_score(fb_data))

##########
# Task h #
##########

def member_stats(data):
    member_dict = create_member_dict(data)
    for i in member_dict:
        if i in posts_freq(data):
            member_dict[i]["posts_count"] = posts_freq(data)[i]
        else:
            member_dict[i]["posts_count"] = 0
        if i in comments_freq(data): 
            member_dict[i]["comments_count"] = comments_freq(data)[i]
        else:
            member_dict[i]["comments_count"] = 0
        if i in likes_freq(data):
            member_dict[i]["likes_count"] = likes_freq(data)[i]
        else:
            member_dict[i]["likes_count"] = 0
    return member_dict

stats = member_stats(fb_data)
# print(stats["10152805891837166"])

##########
# Task i #
##########

def activity_score(data):
    score_dict = {}
    score_stats = member_stats(data)
    for i in score_stats:
        score_dict[i] = (score_stats[i]['posts_count'] * 3) + (score_stats[i]['comments_count'] * 2) + (score_stats[i]['likes_count'])       
    return score_dict

scores = activity_score(fb_data)
# print(scores["10153020766393769"]) # => 30
# print(scores["857756387629369"]) # => 8

##########
# Task j #
##########

def active_members_of_type(data, k, type_fn):
    member_dict = create_member_dict(data)
    freq_dict = type_fn(data)
    final_list = []
    for i in member_dict:
        if i in freq_dict:
            if freq_dict[i] >= k:
                final_list.append([member_dict[i]['name'], freq_dict[i]])

    final_list.sort(key=lambda x: x[0])                
    final_list.sort(key=lambda x: x[1], reverse=True)

    return final_list

# print(active_members_of_type(fb_data, 2, posts_freq))

# print(active_members_of_type(fb_data, 20, comments_freq))

# print(active_members_of_type(fb_data, 40, likes_freq))

# print(active_members_of_type(fb_data, 20, popularity_score))

# print(active_members_of_type(fb_data, 80, activity_score))


########### DO NOT REMOVE THE TEST BELOW ###########

def gradeit():
    print("\n*** Facebook Stalker Autograding ***")
    print('==================')
    answers = json.loads(open('grading.json', 'r',  encoding='utf-8').read())
    total, correct = 0, 0
    def pass_or_fail(code, answer):
        nonlocal total
        total += 1
        if code == answer:
            nonlocal correct
            correct += 1
            return 'Passed!'
        else:
            return 'Failed.'
            
    print('Testing count_comments... ', pass_or_fail(count_comments(fb_data), answers['count_comments']))
    print('Testing count_likes... ', pass_or_fail(count_likes(fb_data), answers['count_likes']))
    print('Testing create_member_dict... ', pass_or_fail(create_member_dict(fb_data), answers['create_member_dict']))
    print('Testing posts_freq... ', pass_or_fail(posts_freq(fb_data), answers['posts_freq']))
    print('Testing comments_freq... ', pass_or_fail(comments_freq(fb_data), answers['comments_freq']))
    print('Testing likes_freq... ', pass_or_fail(likes_freq(fb_data), answers['likes_freq']))
    print('Testing popularity_score... ', pass_or_fail(popularity_score(fb_data), answers['popularity_score']))
    print('Testing member_stats... ', pass_or_fail(member_stats(fb_data), answers['member_stats']))
    print('Testing activity_score... ', pass_or_fail(activity_score(fb_data), answers['activity_score']))
    print('Testing members with >= 1 posts... ', pass_or_fail(active_members_of_type(fb_data, 1, posts_freq), answers['active_posters']))
    print('Testing members with >= 4 comments... ', pass_or_fail(active_members_of_type(fb_data, 4, comments_freq), answers['active_commenters']))
    print('Testing members with >= 4 likes... ', pass_or_fail(active_members_of_type(fb_data, 4, likes_freq), answers['active_likers']))
    print('Testing members who have >= 3 likes... ', pass_or_fail(active_members_of_type(fb_data, 3, popularity_score), answers['popular']))
    print('Testing members with an activity score of >= 10... ', pass_or_fail(active_members_of_type(fb_data, 10, activity_score), answers['overall_active']))
    print('==================')
    print('Grades: ' + str(correct) + '/' + str(total) + '\n')

gradeit()
