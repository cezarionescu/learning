def match(template, candidate):
    """
    Given a template string containing 0, 1 or ?(which could be either 0 or 1) characters,
    determine whether a candidate string matches the template
    :param template: template to match with
    :param candidate: candidate to assess the match for
    :return: candidate matches the template

    Google interview March 2019
    """
    if len(template) != len(candidate):
        return False

    for i in xrange(len(template)):
        if candidate[i] not in ["0", "1"]:
            return False   # candidate must contain only decoded characters

        if not (candidate[i] == template[i] or template[i] == "?"):
            return False

    return True


def generate_matches(template):
    """
    Given a template string containing 0, 1 or ?(which could be either 0 or 1) characters,
    generate and print all possible matches for it
    :param template: template to generate all matches for

    Google interview March 2019
    """
    if "?" not in template:
        print template
        return

    decode_1 = decode_0 = template
    generate_matches(decode_0.replace("?", "0", 1))
    generate_matches(decode_1.replace("?", "1", 1))


def test():
    """
    Test routine for the code in this file
    """
    print match("????", "0?01")
    generate_matches("0??")


test()