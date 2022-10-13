# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'background',
        'directory': 'nazuna/Background',
        'required': True,
        'rarity_weights': [60,55,50,45,30,20,10,5],
    },
    {
        'id': 2,
        'name': 'face',
        'directory': 'nazuna/Face',
        'required': True,
        'rarity_weights': [60,40,20,10],
    },
    {
        'id': 3,
        'name': 'facewitharm',
        'directory': 'nazuna/FacewithArm',
        'required': True,
        'rarity_weights': [60,55,50,45,40,35,30,25,20,15,10,9,8,7,6,5,4,3,2,1,1,1,1,1],
    },
    {
        'id': 4,
        'name': 'armdecro',
        'directory': 'nazuna/ArmDecro',
        'required': True,
        'rarity_weights': [80,20],
    },
    {
        'id': 5,
        'name': 'clothes',
        'directory': 'nazuna/Clothes',
        'required': True,
        'rarity_weights': [60,50,40,30,20,10,9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
    },
    {
        'id': 6,
        'name': 'eyes',
        'directory': 'nazuna/Eyes',
        'required': True,
        'rarity_weights': [80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,2,1,1],
    },
    {
        'id': 7,
        'name': 'mouth',
        'directory': 'nazuna/Mouth',
        'required': True,
        'rarity_weights': [60,50,45,40,35,30,25,20,15,10,5],
    },
    {
        'id': 8,
        'name': 'hairw/outbang',
        'directory': 'nazuna/HairwithoutBang',
        'required': True,
        'rarity_weights': [80,70,60,50,40,30,20,10,9,8,7,6,5,4,3,3,2,1],
    },
    {
        'id': 9,
        'name': 'eardecro',
        'directory': 'nazuna/EarDecro',
        'required': True,
        'rarity_weights': [60,50,40,30,20,10,5,1],
    },
    {
        'id': 10,
        'name': 'headdecro',
        'directory': 'nazuna/HeadDecro',
        'required': True,
        'rarity_weights': [50,40,30,20,10],
    },
    {
        'id': 11,
        'name': 'glasses',
        'directory': 'nazuna/Glasses',
        'required': True,
        'rarity_weights': [60,50,40,30,20],
    },
    # {
    #     'id': 12,
    #     'name': 'hairw/bang',
    #     'directory': 'nazuna/HairwithBang',
    #     'required': True,
    #     'rarity_weights': [80,20],
    # },
    {
        'id':13,
        'name': 'neckdecro',
        'directory': 'nazuna/NeckDecro',
        'required': True,
        'rarity_weights': [60,40,30,10],

    },

]
