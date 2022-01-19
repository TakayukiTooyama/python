# 特殊メソッド

class Word:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'word!!!!'

    def __len__(self):
        return len(self.text)

    def __eq__(self, word):
        return self.text.lower() == word.lower()

w = Word('text')
print(w) # word!!!
print(len(w)) # 4
print(w == 'text') # True
print(w == 'txt') # False

"""
他にも
__eq__( self, other ) self == other
__ne__( self, other ) self != other
__lt__( self, other ) self < other
__gt__( self, other ) self > other
__le__( self, other ) self <= other
__ge__( self, other ) self >= other

__add__( self, other ) self + other
__sub__( self, other ) self - other
__mul__( self, other ) self * other
__floordiv__( self, other ) self // other
__truediv__( self, other ) self / other
__mod__( self, other ) self % other
__pow__( self, other ) self ** other

__str__( self ) str( self )⭐️
__len__( self ) len( self )

"""
