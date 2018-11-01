"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3, 4, 5, 6, 7],
            "answer": [1, 2, 2, 3, 4, 5, 6]
        },
        {
            "input": [1],
            "answer": [1]
        }
    ],
    "Extra": [
        {
            "input": [5, 2, 9, 1, 7, 4, 6, 3, 8],
            "answer": [5, 2, 5, 2, 7, 4, 6, 4, 6]
        },
        {
            "input": [6, 7],
            "answer": [6, 7]
        }
    ]
}
