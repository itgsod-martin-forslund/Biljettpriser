__author__ = 'martin.forslund'


def price(age):
    """

    :param age:  passenger age as integer
    :return: price in SEK
    """


    if age < 18 :
        if age > 0 :
            print "kostar 10 kr"
    elif age < 65 :
        if age >17 :
            print "kostar 20kr"
    elif age > 65 :
        print "kostar 15kr"


