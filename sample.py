#sample


def sample(l):

    ll = []

    for item in l:

        ll.append(sum(item))
    return ll


l = [1,2,[3,4],5,6,[7,8],9]

sample(l)
