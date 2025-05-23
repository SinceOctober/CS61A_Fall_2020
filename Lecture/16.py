def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

# Also works:
def make_withdraw1(balance):
    """Return a withdraw function with a starting balance."""
    def withdraw(amount):
        # nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        # balance = balance - amount
        return balance
    return withdraw


def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
b(3) + b(4)

def profit(t):
    """Return the max profit
    
    >>> t = tree(2, [tree(3), tree(4)])
    >>> profit(t)
    4
    """
    return helper(t, False)

def helper(t, used_parent):
    if used_parent:
        return sum(map(lambda x: helper(x, False), branches(t)))
    else:
        used_label_total = label0 + sum([helper(x, True) for x in branches(t)])
        skip_label_total = sum([helper(x, False) for x in branches(t)])
        return max(used_label_total, skip_label_total)