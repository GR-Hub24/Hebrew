# -*- coding: utf-8 -*-

def Hebrew_verbs(verb):

# Verbs to change to be past tense.

    if len(verb) == 2:
        if verb.endswith("ץ"):
            verb0 = verb.replace("ץ", "צ")
            return "ל"+verb[0]+"ו"+verb[1], \
                "אני" " " + verb0 + "תי", \
                "אתה" " " + verb0 + "ת", \
                "את" " " + verb0 + "ת", \
                "הוא" " " + verb, \
                "היא" " " + verb0 + "ה", \
                "אנחנו" " " + verb0 + "נו", \
                "אתם" " " + verb0 + "תם", \
                "אתן" " " + verb0 + "תן", \
                "הם/הן" " " + verb0 + "ו"
        # קל

        elif verb.endswith("ם"):
            verb0 = verb.replace("ם", "מ")
            return "ל"+verb[0]+"ו"+verb[1], \
                "אני" " " + verb0 + "תי", \
                "אתה" " " + verb0 + "ת", \
                "את" " " + verb0 + "ת", \
                "הוא" " " + verb, \
                "היא" " " + verb0 + "ה", \
                "אנחנו" " " + verb0 + "נו", \
                "אתם" " " + verb0 + "תם", \
                "אתן" " " + verb0 + "תן", \
                "הם/הן" " " + verb0 + "ו"
        elif verb.endswith("ף"):
            verb0 = verb.replace("ף", "פ")
            return "ל"+verb[0]+"ו"+verb[1], \
                "אני" " " + verb0 + "תי", \
                "אתה" " " + verb0 + "ת", \
                "את" " " + verb0 + "ת", \
                "הוא" " " + verb, \
                "היא" " " + verb0 + "ה", \
                "אנחנו" " " + verb0 + "נו", \
                "אתם" " " + verb0 + "תם", \
                "אתן" " " + verb0 + "תן", \
                "הם/הן" " " + verb0 + "ו"
        elif verb.endswith("ך"):
            verb0 = verb.replace("ך", "כ")
            return "ל"+verb[0]+"ו"+verb[1], \
                "אני" " " + verb0 + "תי", \
                "אתה" " " + verb0 + "ת", \
                "את" " " + verb0 + "ת", \
                "הוא" " " + verb, \
                "היא" " " + verb0 + "ה", \
                "אנחנו" " " + verb0 + "נו", \
                "אתם" " " + verb0 + "תם", \
                "אתן" " " + verb0 + "תן", \
                "הם/הן" " " + verb0 + "ו"
        elif verb.endswith("ן"):
            verb0 = verb.replace("ן", "נ")
            return "ל"+verb[0]+"ו"+verb[1], \
                "אני" " " + verb0 + "תי", \
                "אתה" " " + verb0 + "ת", \
                "את" " " + verb0 + "ת", \
                "הוא" " " + verb, \
                "היא" " " + verb0 + "ה", \
                "אנחנו" " " + verb0 + "נו", \
                "אתם" " " + verb0 + "תם", \
                "אתן" " " + verb0 + "תן", \
                "הם/הן" " " + verb0 + "ו"
        else:
            return "ל"+verb[0]+"ו"+verb[1], \
                "אני" " " + verb + "תי", \
                "אתה" " " + verb + "ת", \
                "את" " " + verb + "ת", \
                "הוא" " " + verb, \
                "היא" " " + verb + "ה", \
                "אנחנו" " " + verb + "נו", \
                "אתם" " " + verb + "תם", \
                "אתן" " " + verb + "תן", \
                "הם/הן" " " + verb + "ו"
# פועל
    elif len(verb) == 4 and verb[1] == "ו" and verb[3] == "ה":
        letter2 = verb[0] + verb[2]
        return "ל" + letter2 + "ות", \
            "אני" " " + letter2 + "יתי", \
            "אתה" " " + letter2 + "ית", \
            "את" " " + letter2 + "ית", \
            "הוא" " " + letter2 + "ה", \
            "היא" " " + letter2 + "תה", \
            "אנחנו" " " + letter2 + "ינו", \
            "אתם" " " + letter2 + "יתם", \
            "אתן" " " + letter2 + "יתן", \
            "הם/הן" " " + letter2 + "ו"

# פןעל
    elif verb[1] == "ו" and len(verb) == 4:
        if verb.endswith("ף"):
            verb0 = verb.replace("ף","פ")
            letter1 = verb0[2] + verb0[3]
            return "ל"+verb[0]+verb[2]+"ו"+verb[3], \
                "אני" " " + verb[0] + letter1 + "תי", \
                "אתה" " " + verb[0] + letter1 + "ת", \
                "את" " " + verb[0] + letter1 + "ת",\
                "הוא" " " + verb[0] + verb[2] + verb[3], \
                "היא" " " + verb[0] + letter1 + "ה", \
                "אנחנו" " " + verb[0] + letter1 + "נו", \
                "אתם" " " + verb[0] + letter1 + "תם", \
                "אתן" " " + verb[0] + letter1 + "תן", \
                "הם/הן" " "+ verb[0] + letter1 + "ו"
        elif verb.endswith("ם"):
            verb0 = verb.replace("ם","מ")
            letter1 = verb0[2] + verb0[3]
            return "ל"+verb[0]+verb[2]+"ו"+verb[3], \
                "אני" " " + verb[0] + letter1 + "תי", \
                "אתה" " " + verb[0] + letter1 + "ת", \
                "את" " " + verb[0] + letter1 + "ת",\
                "הוא" " " + verb[0] + verb[2] + verb[3], \
                "היא" " " + verb[0] + letter1 + "ה", \
                "אנחנו" " " + verb[0] + letter1 + "נו", \
                "אתם" " " + verb[0] + letter1 + "תם", \
                "אתן" " " + verb[0] + letter1 + "תן", \
                "הם/הן" " "+ verb[0] + letter1 + "ו"
        elif verb.endswith("ך"):
            verb0 = verb.replace("ך","כ")
            letter1 = verb0[2] + verb0[3]
            return "ל"+verb[0]+verb[2]+"ו"+verb[3], \
                "אני" " " + verb[0] + letter1 + "תי", \
                "אתה" " " + verb[0] + letter1 + "ת", \
                "את" " " + verb[0] + letter1 + "ת",\
                "הוא" " " + verb[0] + verb[2] + verb[3], \
                "היא" " " + verb[0] + letter1 + "ה", \
                "אנחנו" " " + verb[0] + letter1 + "נו", \
                "אתם" " " + verb[0] + letter1 + "תם", \
                "אתן" " " + verb[0] + letter1 + "תן", \
                "הם/הן" " "+ verb[0] + letter1 + "ו"
        elif verb.endswith("ץ"):
            verb0 = verb.replace("ץ","צ")
            letter1 = verb0[2] + verb0[3]
            return "ל"+verb[0]+verb[2]+"ו"+verb[3], \
                "אני" " " + verb[0] + letter1 + "תי", \
                "אתה" " " + verb[0] + letter1 + "ת", \
                "את" " " + verb[0] + letter1 + "ת",\
                "הוא" " " + verb[0] + verb[2] + verb[3], \
                "היא" " " + verb[0] + letter1 + "ה", \
                "אנחנו" " " + verb[0] + letter1 + "נו", \
                "אתם" " " + verb[0] + letter1 + "תם", \
                "אתן" " " + verb[0] + letter1 + "תן", \
                "הם/הן" " "+ verb[0] + letter1 + "ו"
        elif verb.endswith("ן"):
            verb0 = verb.replace("ן","נ")
            letter1 = verb0[2] + verb0[3]
            return "ל"+verb[0]+verb[2]+"ו"+verb[3], \
                "אני" " " + verb[0] + letter1 + "תי", \
                "אתה" " " + verb[0] + letter1 + "ת", \
                "את" " " + verb[0] + letter1 + "ת",\
                "הוא" " " + verb[0] + verb[2] + verb[3], \
                "היא" " " + verb[0] + letter1 + "ה", \
                "אנחנו" " " + verb[0] + letter1 + "נו", \
                "אתם" " " + verb[0] + letter1 + "תם", \
                "אתן" " " + verb[0] + letter1 + "תן", \
                "הם/הן" " "+ verb[0] + letter1 + "ו"
        else:
            letter1 = verb[2] + verb[3]
            return "ל"+verb[0]+verb[2]+"ו"+verb[3], \
                "אני" " " + verb[0] + letter1 + "תי", \
                "אתה" " " + verb[0] + letter1 + "ת", \
                "את" " " + verb[0] + letter1 + "ת",\
                "הוא" " " + verb[0] + letter1, \
                "היא" " " + verb[0] + letter1 + "ה", \
                "אנחנו" " " + verb[0] + letter1 + "נו", \
                "אתם" " " + verb[0] + letter1 + "תם", \
                "אתן" " " + verb[0] + letter1 + "תן", \
                "הם/הן" " "+ verb[0] + letter1 + "ו"

    elif len(verb) == 4 and verb[0] == "מ":
        if verb.endswith("ף"):
            verb0 = verb.replace("ף","פ")
            letter4 = verb0[1] + "י" + verb0[2] + verb0[3]
            return "ל" + verb[1] + verb[2] + verb[3], \
                "אני" " " + letter4 + "תי", \
                "אתה" " " + letter4 + "ת", \
                "את" " " + letter4 + "ת", \
                "הוא" " " + verb[0] + "י" + verb[2] + verb[3], \
                "היא" " " + letter4 + "ה", \
                "אנחנו" " " + letter4 + "נו", \
                "אתם" " " + letter4 + "תם", \
                "אתן" " " + letter4 + "תן", \
                "הם/הן" " " + letter4 + "ו"
        elif verb.endswith("ם"):
            verb0 = verb.replace("ם","מ")
            letter4 = verb0[1] + "י" + verb0[2] + verb0[3]
            return "ל" + verb[1] + verb[2] + verb[3], \
                "אני" " " + letter4 + "תי", \
                "אתה" " " + letter4 + "ת", \
                "את" " " + letter4 + "ת", \
                "הוא" " " + verb[0] + "י" + verb[2] + verb[3], \
                "היא" " " + letter4 + "ה", \
                "אנחנו" " " + letter4 + "נו", \
                "אתם" " " + letter4 + "תם", \
                "אתן" " " + letter4 + "תן", \
                "הם/הן" " " + letter4 + "ו"
        elif verb.endswith("ך"):
            verb0 = verb.replace("ך","כ")
            letter4 = verb0[1] + "י" + verb0[2] + verb0[3]
            return "ל" + verb[1] + verb[2] + verb[3], \
                "אני" " " + letter4 + "תי", \
                "אתה" " " + letter4 + "ת", \
                "את" " " + letter4 + "ת", \
                "הוא" " " + verb[0] + "י" + verb[2] + verb[3], \
                "היא" " " + letter4 + "ה", \
                "אנחנו" " " + letter4 + "נו", \
                "אתם" " " + letter4 + "תם", \
                "אתן" " " + letter4 + "תן", \
                "הם/הן" " " + letter4 + "ו"
        elif verb.endswith("ן"):
            verb0 = verb.replace("ן","נ")
            letter4 = verb0[1] + "י" + verb0[2] + verb0[3]
            return "ל" + verb[1] + verb[2] + verb[3], \
                "אני" " " + letter4 + "תי", \
                "אתה" " " + letter4 + "ת", \
                "את" " " + letter4 + "ת", \
                "הוא" " " + verb[0] + "י" + verb[2] + verb[3], \
                "היא" " " + letter4 + "ה", \
                "אנחנו" " " + letter4 + "נו", \
                "אתם" " " + letter4 + "תם", \
                "אתן" " " + letter4 + "תן", \
                "הם/הן" " " + letter4 + "ו"
        elif verb.endswith("ץ"):
            verb0 = verb.replace("ץ","צ")
            letter4 = verb0[1] + "י" + verb0[2] + verb0[3]
            return "ל" + verb[1] + verb[2] + verb[3], \
                "אני" " " + letter4 + "תי", \
                "אתה" " " + letter4 + "ת", \
                "את" " " + letter4 + "ת", \
                "הוא" " " + verb[0] + "י" + verb[2] + verb[3], \
                "היא" " " + letter4 + "ה", \
                "אנחנו" " " + letter4 + "נו", \
                "אתם" " " + letter4 + "תם", \
                "אתן" " " + letter4 + "תן", \
                "הם/הן" " " + letter4 + "ו"
        else:
            letter3 = verb[1] + verb[2] + verb[3]
            letter4 = verb[1] + "י" + verb[2] + verb[3]
            return "ל" + letter3, \
                "אני" " " + letter4 + "תי", \
                "אתה" " " + letter4 + "ת", \
                "את" " " + letter4 + "ת", \
                "הוא" " " + letter4, \
                "היא" " " + letter4 + "ה", \
                "אנחנו" " " + letter4 + "נו", \
                "אתם" " " + letter4 + "תם", \
                "אתן" " " + letter4 + "תן", \
                "הם/הן" " " + letter4 + "ו"

    elif verb[0] == "מ" and verb[3] == "י":
        if verb.endswith("ף"):
            verb0 = verb.replace("ף","פ")
            letter5 = "ה" + verb0[1] + verb0[2] + verb0[4]
            letter6 = verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "לה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter5 + "תי", \
                "אתה" " " + letter5 + "ת", \
                "את" " " + letter5 + "ת", \
                "הוא" " " "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " "ה" + letter6 + "ה", \
                "אנחנו" " " + letter5 + "נו", \
                "אתם" " " + letter5 + "תם", \
                "אתן" " " + letter5 + "תן", \
                "הם/הן" " " + letter6 + "ו"
        elif verb.endswith("ם"):
            verb0 = verb.replace("ם", "מ")
            letter5 = "ה" + verb0[1] + verb0[2] + verb0[4]
            letter6 = verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "לה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter5 + "תי", \
                "אתה" " " + letter5 + "ת", \
                "את" " " + letter5 + "ת", \
                "הוא" " " "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " "ה" + letter6 + "ה", \
                "אנחנו" " " + letter5 + "נו", \
                "אתם" " " + letter5 + "תם", \
                "אתן" " " + letter5 + "תן", \
                "הם/הן" " " + letter6 + "ו"
        elif verb.endswith("ך"):
            verb0 = verb.replace("ך","כ")
            letter5 = "ה" + verb0[1] + verb0[2] + verb0[4]
            letter6 = verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "לה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter5 + "תי", \
                "אתה" " " + letter5 + "ת", \
                "את" " " + letter5 + "ת", \
                "הוא" " " "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " "ה" + letter6 + "ה", \
                "אנחנו" " " + letter5 + "נו", \
                "אתם" " " + letter5 + "תם", \
                "אתן" " " + letter5 + "תן", \
                "הם/הן" " " + letter6 + "ו"
        elif verb.endswith("ן"):
            verb0 = verb.replace("ן","נ")
            letter5 = "ה" + verb0[1] + verb0[2] + verb0[4]
            letter6 = verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "לה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter5 + "תי", \
                "אתה" " " + letter5 + "ת", \
                "את" " " + letter5 + "ת", \
                "הוא" " " "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " "ה" + letter6 + "ה", \
                "אנחנו" " " + letter5 + "נו", \
                "אתם" " " + letter5 + "תם", \
                "אתן" " " + letter5 + "תן", \
                "הם/הן" " " + letter6 + "ו"
        elif verb.endswith("ץ"):
            verb0 = verb.replace("ץ","צ")
            letter5 = "ה" + verb0[1] + verb0[2] + verb0[4]
            letter6 = verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "לה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter5 + "תי", \
                "אתה" " " + letter5 + "ת", \
                "את" " " + letter5 + "ת", \
                "הוא" " " "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " "ה" + letter6 + "ה", \
                "אנחנו" " " + letter5 + "נו", \
                "אתם" " " + letter5 + "תם", \
                "אתן" " " + letter5 + "תן", \
                "הם/הן" " " + letter6 + "ו"
        else:
            letter5 = "ה" + verb[1] + verb[2] + verb[4]
            letter6 = verb[1] + verb[2] + verb[3] + verb[4]
            return "לה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter5 + "תי", \
                "אתה" " " + letter5 + "ת", \
                "את" " " + letter5 + "ת", \
                "הוא" " " "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " "ה" + letter6 + "ה", \
                "אנחנו" " " + letter5 + "נו", \
                "אתם" " " + letter5 + "תם", \
                "אתן" " " + letter5 + "תן", \
                "הם/הן" " " + letter6 + "ו"

    elif len(verb) >= 5 and verb.startswith("מת") or verb.startswith("מס"):
        if verb.endswith("ף"):
            verb0 = verb.replace("ף","פ")
            letter7 = "ה" + verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "ל" + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter7 + "תי", \
                "אתה" " " + letter7 + "ת", \
                "את" " " + letter7 + "ת", \
                "הוא" " " + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " + letter7 + "ה", \
                "אנחנו" " " + letter7 + "נו", \
                "אתם" " " + letter7 + "תם", \
                "אתן" " " + letter7 + "תן", \
                "הם/הן" " " + letter7 + "ו"
        elif verb.endswith("ם"):
            verb0 = verb.replace("ם", "מ")
            letter7 = "ה" + verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "ל" + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter7 + "תי", \
                "אתה" " " + letter7 + "ת", \
                "את" " " + letter7 + "ת", \
                "הוא" " " + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " + letter7 + "ה", \
                "אנחנו" " " + letter7 + "נו", \
                "אתם" " " + letter7 + "תם", \
                "אתן" " " + letter7 + "תן", \
                "הם/הן" " " + letter7 + "ו"
        elif verb.endswith("ך"):
            verb0 = verb.replace("ך", "כ")
            letter7 = "ה" + verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "ל" + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter7 + "תי", \
                "אתה" " " + letter7 + "ת", \
                "את" " " + letter7 + "ת", \
                "הוא" " " + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " + letter7 + "ה", \
                "אנחנו" " " + letter7 + "נו", \
                "אתם" " " + letter7 + "תם", \
                "אתן" " " + letter7 + "תן", \
                "הם/הן" " " + letter7 + "ו"
        elif verb.endswith("ן"):
            verb0 = verb.replace("ן", "נ")
            letter7 = "ה" + verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "ל" + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter7 + "תי", \
                "אתה" " " + letter7 + "ת", \
                "את" " " + letter7 + "ת", \
                "הוא" " " + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " + letter7 + "ה", \
                "אנחנו" " " + letter7 + "נו", \
                "אתם" " " + letter7 + "תם", \
                "אתן" " " + letter7 + "תן", \
                "הם/הן" " " + letter7 + "ו"
        elif verb.endswith("ץ"):
            verb0 = verb.replace("ץ", "צ")
            letter7 = "ה" + verb0[1] + verb0[2] + verb0[3] + verb0[4]
            return "ל" + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter7 + "תי", \
                "אתה" " " + letter7 + "ת", \
                "את" " " + letter7 + "ת", \
                "הוא" " " + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " + letter7 + "ה", \
                "אנחנו" " " + letter7 + "נו", \
                "אתם" " " + letter7 + "תם", \
                "אתן" " " + letter7 + "תן", \
                "הם/הן" " " + letter7 + "ו"
        else:
            letter7 = "ה" + verb[1] + verb[2] + verb[3] + verb[4]
            return "ל" + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "אני" " " + letter7 + "תי", \
                "אתה" " " + letter7 + "ת", \
                "את" " " + letter7 + "ת", \
                "הוא" " " + "ה" + verb[1] + verb[2] + verb[3] + verb[4], \
                "היא" " " + letter7 + "ה", \
                "אנחנו" " " + letter7 + "נו", \
                "אתם" " " + letter7 + "תם", \
                "אתן" " " + letter7 + "תן", \
                "הם/הן" " " + letter7 + "ו"

    else:
        return None

user_input = input("Enter a verb (male, singular): ")
verb_past_tense = Hebrew_verbs(user_input)

# here need to think how to change the last letter for further form changing.


if verb_past_tense:
    verb_past_tense_string = " ".join(verb_past_tense)
    print(f"The past tense of __'{user_input}'__ is __{verb_past_tense}__.")
else:
    print("Invalid verb input.")

#-------------------------------------------------------

quiz1 = {
    "Are these answer correct? (כן או לא)": None
}

quiz2 = {
    "אני": None,
    "אתה": None,
    "את": None,
    "הוא": None,
    "היא": None,
    "אנחנו": None,
    "אתם": None,
    "אתן": None,
    "הם/הן": None,
    "ל": None
}

correct_answers = {}

with open("Hebrew_words.txt", "a", encoding="utf-8") as file:
    for question1, answer1 in quiz1.items():
        while True:
            user_answer = input(question1 + " ")

            if user_answer == "לא":
                for question2, answer2 in quiz2.items():
                    correct_answer = input(question2 + ": ")
                    correct_answers[question2] = correct_answer
                file.write(f"\n{user_input}\nProvided answers:\n")
                for question2, answer2 in correct_answers.items():
                    file.write(f"{question2} {answer2}, ")
                break

            elif user_answer == "כן":
                print("Yaaaaaaaaaaaaaaaay!")
                file.write(f"\n'{user_input}'\n'{verb_past_tense_string}'")
                break

            else:
                print("Please write 'כן' or 'לא'.")
    file.write(f"\n")

print("תודה רבה!!")