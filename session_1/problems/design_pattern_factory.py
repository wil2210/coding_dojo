# -*- coding: utf-8 -*-
import logging
logging.getLogger().setLevel(logging.DEBUG)

### put your code here

if __name__ == '__main__':
    tests = {
        "test1":
            {
                "operation": "reverse",
                "text": "hellothere",
                "expected_result": "erehtolleh"
            },
        "test2":
            {
                "operation": "upper",
                "text": "Hi how are you",
                "expected_result": "HI HOW ARE YOU"
            },
        "test3":
            {
                "operation": "lower",
                "text": "HEY HOW DO YOU DO",
                "expected_result": "hey how do you do"
            }
    }
    total_score = 0
    for test in tests:
        logging.info("*" * 20)
        logging.info("Test name: {}".format(test))
        ### tool = [your make_tool call](tests[test]["operation"])
        result = tool.use(tests[test]["text"])
        if result == tests[test]["expected_result"]:
            logging.info("Test succeeded with text: {} and result : {}".format(tests[test]["text"], result))
            total_score += 1
        else:
            logging.error(("Test failed with text: {} and result : {} instead of expected: "
                        .format(tests[test]["text"], result, tests[test]["expected_result"])))
    logging.info("Your score is {}/{}, {}% success rate"
            .format(total_score, len(tests), 100 * float(total_score)/len(tests)))


