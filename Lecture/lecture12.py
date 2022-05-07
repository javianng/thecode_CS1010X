##############
# Question 1 #
##############
class Mammal(object):
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    def say(self):
        return "What does the " + self.name + " say"

# print(Mammal("Dog").get_name())
# print(Mammal("Dog").say())

##############
# Question 2 #
##############

# You DO NOT NEED TO DEFINE Mammal class here!
class Dog(Mammal):
    def __init__(self):
        self.name = 'Dog'
        super().__init__('Dog')

# Cat definition should go here

class Cat(Mammal):
    def __init__(self):
        self.name = 'Cat'
        super().__init__('Cat')
        
# Fox definition should go here

class Fox(Mammal):
    def __init__(self):
        self.name = 'Fox'
        super().__init__('Fox')

# print(Dog().get_name())

##############
# Question 3 #
##############

# You DO NOT NEED TO DEFINE Mammal class here!

# Implement additional methods to your Dog, Cat and Fox subclasses to modify what they say.

class Dog(Mammal):
    def __init__(self):
        self.name = 'Dog'
        super().__init__('Dog')
    def say(self):
        return "Woof"
        
# Cat definition should go here

class Cat(Mammal):
    def __init__(self):
        self.name = 'Cat'
        super().__init__('Cat')
    def say(self):
        return "Meow"
        
# Fox definition should go here

class Fox(Mammal):
    def __init__(self):
        self.name = 'Fox'
        super().__init__('Fox')
    def say(self):
        return "Ring-ding-ding-ding-dingeringeding"
        
# print(Dog().say())
# print(Mammal("Dog").say())

######################
# Question 4: Artist #
######################

class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def get_name(self):
        return self.name
        
    def get_dob(self):
        return self.dob
        
# Used for public test cases.
# You DO NOT have to include this in your submission.
jt = Artist("Justin Timberlake", (1981, 1, 31))

# print(jt.get_name())
# print(jt.get_dob())
# print(Artist("JC Chasez", (1976, 8, 8)).get_name())

##########################
# Question 5: Artist Age #
##########################

def get_date_today():
    return (2014, 11, 27)

class Artist(object):
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    
    # 24 if 'today' is >= (2012, 12, 27) and < (2013, 12, 27) ; 
    # 25 if 'today' is >= (2013, 12, 27) and < (2014, 12, 27)
    # today is 2013, 10, 30
    
    def age(self):
        list_dob = list(self.dob) # dob is in yyyy, m, dd format
        
        # default age based only on year
        age_higher_est = get_date_today()[0] - list_dob[0]
        
        lower_bound_date = (get_date_today()[0]-1, list_dob[1], list_dob[2])
        middle_bound_date = (get_date_today()[0], list_dob[1], list_dob[2])
        upper_bound_date = (get_date_today()[0]+1, list_dob[1], list_dob[2])
        
        if get_date_today() >= lower_bound_date and get_date_today() < middle_bound_date:
            return age_higher_est-1
        elif get_date_today() >= middle_bound_date and get_date_today() < upper_bound_date:
            return age_higher_est

# Used for public test cases.
# You DO NOT have to include this in your submission
# jt = Artist("Justin Timberlake", (1981, 1, 31))

# print(jt.age())
# print(Artist("Hayley Williams", (1988, 12, 27)).age())

########################
# Question 6: Duration #
########################

class Duration(object):
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = seconds + minutes * 60
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        
    def get_minutes(self):
        return self.minutes
    
    def get_seconds(self):
        return self.seconds

# print((Duration(3, 30)).total_seconds)
# print((Duration(3, 30)).get_minutes())
# print((Duration(3, 30)).get_seconds())
# print((Duration(5, 80)).get_minutes())
# print((Duration(5, 80)).get_seconds())

##############################################
# Question 7: Duration String Representation #
##############################################

class Duration(object):
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = seconds + minutes * 60
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        
    def get_minutes(self):
        return self.minutes
    
    def get_seconds(self):
        return self.seconds
    
    def __str__(self):
        return str("%02d" % self.minutes) + ':' + str("%02d" % self.seconds)

# print(Duration(103,20))
# print(str(Duration(0,0)))

##################################
# Question 8: Duration Operators #
##################################

class Duration(object):
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds
        self.total_seconds = seconds + minutes * 60
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        
    def get_minutes(self):
        return self.minutes
    
    def get_seconds(self):
        return self.seconds
    
    def __str__(self):
        return str("%02d" % self.minutes) + ':' + str("%02d" % self.seconds)

    def __add__(self, duration_2):
        combined_seconds = self.total_seconds + duration_2.total_seconds
        return Duration(combined_seconds//60, combined_seconds%60)
        
    # def __add__(self, duration_2):
    #     combined_minutes = self.minutes + duration_2.minutes
    #     combined_seconds = self.seconds + duration_2.seconds
    #     return Duration(combined_minutes, combined_seconds)

# print(str(Duration(23,59) + Duration(12,59)))

####################
# Question 9: Song #
####################

# NOTE: You DO NOT have to include the definitions of the
#       Artist and Duration classes here.

class Song(object):
    def __init__(self, artist, title, duration):
        self.artist = artist
        self.title = title
        self.duration = duration
        
    def get_artist(self):
        return self.artist
    
    def get_title(self):
        return self.title
        
    def get_duration(self):
        return self.duration

######################
# Question 10: Album #
######################

# NOTE: You DO NOT have to include the definitions of the
#       Artist, Duration, Song and Band classes here.

class Album(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        
    def total_runtime(self):
        total_runtime = 0
        for songs in self.songs:
            total_runtime += songs.get_duration()
        return total_runtime

test_album = Album(artist, title)
test_album.name