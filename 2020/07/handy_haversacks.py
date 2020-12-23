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


def main(rules_file):
    rules = read_rules(rules_file)
    options = []
    for k in rules.keys():
        if traverse_subtree(rules, k, 'shiny gold'):
            options.append(k)

    print(len(options))


if __name__ == '__main__':
    rules_file = 'input.dat'
    main(rules_file)
