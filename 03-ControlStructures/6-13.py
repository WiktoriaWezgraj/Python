'''13. An influencer is a person who can influence other people\'s behaviour. An influencer communicates with other people using social networking sites. 
Write a program that checks whether a given person is a good influencer, that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram. 
Use logical type variables: facebook, twitter, instagram, the value of which indicates whether the person has an account on the social networking site. Sample result:

    facebook = True\
    twitter = False\
    instagram = True\
    You are a good influencer!'''

facebook = True
twitter = False
instagram = True

if (facebook+twitter+instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")