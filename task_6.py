def main(tree, it=0):

    dep = {
        "CIRRU": 0,
        "1968": 1,
        "1976": 2,
        "2010": 3,
        "1988": 10
    }

    mult = {
        "1964": 1,
        "1958": 2
    }

    curr = str(tree[it])

    if curr in dep:
        if (tree[2] == "TCL" or tree[2] == "CIRRU") and tree[1] != "P4":
            return dep.get(curr)
        elif it > 2:
            return dep.get(curr) + 3 * mult.get(str(tree[4]))

    return main(tree, it + 1)


if __name__ == "__main__":
    print(main([1988, 'HTML', 'CIRRU', 2010, 1958]))
