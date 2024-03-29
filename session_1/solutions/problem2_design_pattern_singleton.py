# -*- coding: utf-8 -*-
import logging
logging.getLogger().setLevel(logging.DEBUG)


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

if __name__ == '__main__':
    logging.info("*" * 20)
    logging.info("""
            Let's try our singleton with these 2 objects:
            obj1 = Singleton.getInstance()
            obj2 = Singleton.getInstance()""")
    obj1 = Singleton.getInstance()
    obj2 = Singleton.getInstance()
    total_score = 0
    # Test 1
    logging.info("*" * 20)
    logging.info("1st Test obj1 == obj2 ? : let's see if we get the same instance for both our objects:")
    result = obj1 == obj2
    if result is True:
        logging.info("Test succeeded obj1 == obj2 with obj1 =  {} and obj2 =  {}".format(obj1, obj2))
        total_score += 1
    else:
        logging.error("Test failed obj1 == obj2 with obj1 =  {} and obj2 =  {}".format(obj1, obj2))
    # Test 2
    logging.info("*" * 20)
    logging.info("2nd Test: let's try changing the Singleton instance with obj1 and see what happens to obj2")
    logging.info("""
                obj1.test = 1
                obj2.test ? """)
    obj1.test = 1
    if obj2.test == 1:
        logging.info("Test succeeded obj1.test == obj2.test with obj1.test =  {} and obj2.test =  {}".format(obj1.test, obj2.test))
        total_score += 1
    else:
        logging.error("Test failed obj1.test == obj2.test with obj1.test =  {} and obj2.test =  {}".format(obj1.test, obj2.test))
    logging.info("Your score is {}/{}, {}% success rate"
            .format(total_score, 2, 100 * float(total_score)/2))


