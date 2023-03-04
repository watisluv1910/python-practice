def main(tree, it=0):

    dep = {
        "2019": 0,
        "2017": 1,
        "IOKE": 2
    }

    mult = {
        "COBOL": 0,
        "IOKE": 0,
        "SASS": 1
    }

    if tree[3] == 1968:
        if tree[0] == 2019:
            dep = {
                "QMAKE": 5,
                "COOL": 6,
                "TWIG": 7
            }
        else:
            dep = {
                "COBOL": 8,
                "IOKE": 9,
                "SASS": 10
            }

    curr = str(tree[it])

    if curr in dep:
        return dep.get(curr) + 3 * (0, mult.get(str(tree[1])))[tree[3] == 1980]

    return main(tree, it + 1)


if __name__ == "__main__":
    print(main([2017, 'IOKE', 'QMAKE', 1968]))
    print(main([2017, 'COBOL', 'TWIG', 1980]))
    print(main([2017, 'SASS', 'QMAKE', 1980]))
    print(main([2019, 'SASS', 'QMAKE', 1968]))
    print(main([2019, 'SASS', 'COOL', 1968]))
