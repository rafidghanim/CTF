
class AlcoholShelf:
    def __init__(self):
        self._alcohol_shelf = [
            'vodka', 'schnapps', 'rakia', 'beer :3', 'gurktaler', 
            'sturm', 'riesling', 'jägermeister', 'rum', 'gin',
            'limoncello', 'grappa', 'prosecco', 'amarone', 'aperol',
            'sangria', 'rioja', 'sherry', 'horchata', 'cava',
            'porto', 'vinho verde', 'ginjinha', 'madeira',
            'ouzo', 'metaxa', 'retsina', 'tsipouro',
            'champagne', 'cognac', 'pastis', 'calvados', 'beaujolais'
        ]
        
        for beverage in self._alcohol_shelf:
            setattr(self, beverage, str(beverage))
    

    def add_beverage(self, beverage: str):
        self._alcohol_shelf.append(beverage)


    def get_all_beverages(self):
        return self._alcohol_shelf


class PreferenceConfig(AlcoholShelf):
    _all_instances = []
    
    def __init__(self, preferred_beverage: str):
        super().__init__()
        self.preferred_beverage = preferred_beverage
        self.alcohol_shelf = AlcoholShelf()
        self.blood_alcohol_level = 1.0
        BeverageConfig._all_instances.append(self)


    def empty_alcohol_shelf(self):
        
        if hasattr(self.alcohol_shelf, "_alcohol_shelf"):
            self.alcohol_shelf._alcohol_shelf = [self.alcohol_shelf._alcohol_shelf[0]]
        else:
            self.alcohol_shelf = self.alcohol_shelf[0]


class BeverageConfig(PreferenceConfig):
    """
    User Config 
    """

    def __init__(self, preferred_beverage: str):
        super().__init__(preferred_beverage)
        self.preferred_beverage = preferred_beverage
        self.blood_alcohol_level = 1.0


    def get_config(self):
        return {
            'preferred_beverage': self.get_property('preferred_beverage'),
            'alcohol_shelf': self.get_beverages()
        }


    def get_property(self, val):
        try:
            if hasattr(self.alcohol_shelf, val):
                return getattr(self.alcohol_shelf, val)

            return getattr(self, val)
        except:
            return
    

    def update_property(self, key: str, val: str):
        attr = self.get_property(val)
        print(attr)
        print(key, val)
        if attr:
            setattr(self, key, attr)
            return
        
        return { 'error': 'property doesn\'t exist!' }

    
    def get_beverages(self):
        try:
            return self.alcohol_shelf.get_all_beverages()
        except:
            return self.alcohol_shelf        
    

    def add_beverage(self, beverage: str):
        self.alcohol_shelf._alcohol_shelf.append(beverage)


