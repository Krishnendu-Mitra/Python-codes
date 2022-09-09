myDicti = {
    "fast": "In a quick manner",
    "krish": "A coder",
    "light": "Electromagenetic wave",
    "yourDicti": {'earth': 'A planet name',
    'marks': [1, 5, 2, 7, 100, 98, 46]
    },
    "tom": "Name of a cat",
    "subDicti": {
        'gta': '90s famuse game',
        'computer': 'me',
        'dicti': {
            'array': (5,9,8,3,10,7,49,34,12),
            'jarry': 'name of a rat'
        }
    }
}
print(myDicti)
print(myDicti['krish'])
print(myDicti['yourDicti'])
print(myDicti['yourDicti']['marks'])
print(myDicti['subDicti']['dicti']['array'])
print(myDicti.keys())
print(type(myDicti.keys()))
print(list(myDicti.keys())) #put in a listformat
print("\n",myDicti.items())
print("\n",myDicti.values())
updateDicti = {
    "python": "A good code lang",
    "html": "hihi"
}
myDicti.update(updateDicti)
print("\n",myDicti)

#important to job & exam ------
print("\n\n",myDicti.get("krish2")) #return none to not found
print(myDicti["krish2"]) #throws error to not found
