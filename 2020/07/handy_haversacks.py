#!/usr/bin/env python3


def read_rules(rules_file):
    ruleset = {}
    with open(rules_file, 'r') as f:
        for line in f:
            rule = line.strip().rstrip('.')
            bag, contents = rule.split(' contain ')
            bag = bag.rstrip('bags').strip()
            contents = contents.split(', ')
            contents = [c.rstrip('bags').strip() for c in contents]
            ruleset[bag] = contents
    return ruleset


def traverse_subtree(ruleset, root, target):
    if 'no other' in ruleset[root]:
        return False
    children = [''.join(list(r)[1:]).strip() for r in ruleset[root]]
    if target in children:
        return True
    else:
        results = []
        for c in children:
            results.append(traverse_subtree(
                ruleset,
                c,
                target))
        return True in results


def count_subtree(ruleset, root):
    if 'no other' in ruleset[root]:
        return 0
    children = [
        (int(list(r)[:1][0]), ''.join(list(r)[1:]).strip())
        for r in ruleset[root]]
    bag_count = 0
    for c in children:
        bag_count = bag_count + c[0] + c[0] * count_subtree(ruleset, c[1])
    return bag_count


def main(rules_file):
    rules = read_rules(rules_file)
    options = []
    for k in rules.keys():
        if traverse_subtree(rules, k, 'shiny gold'):
            options.append(k)

    print(len(options))

    total = count_subtree(rules, 'shiny gold')
    print(total)


if __name__ == '__main__':
    rules_file = 'input.dat'
    main(rules_file)
