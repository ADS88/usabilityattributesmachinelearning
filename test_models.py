import spacy
from main import convert_to_spacy_format, get_specific_attribute_data, get_training_data


def test_data_accuracy(filename, attribute):
    nlp = spacy.load("accessoutput/model-best")
    test_data = get_specific_attribute_data(filename, attribute)
    num_matching_attribute = 0
    num_not_matching_attribute = 0
    right = 0
    wrong = 0
    false_positives = 0
    false_negatives = 0
    thought_matched_attribute = 0
    thought_didnt_match_attribute = 0
    for story, is_attribute in test_data:
        if is_attribute:
            num_matching_attribute += 1
        else:
            num_not_matching_attribute += 1
        classification = nlp(story)
        if classification.cats['usability_attribute'] >= 0.5:
            print(story)
            thought_matched_attribute += 1
        else:
            thought_didnt_match_attribute += 1
        if is_classification_right(classification, is_attribute):
            right += 1
        else:
            wrong += 1
            if is_attribute:
                false_negatives += 1
            else:
                false_positives += 1
    print("matching attribute", num_matching_attribute)
    print("not matching attribute", num_not_matching_attribute)
    print("right", right)
    print("wrong", wrong)
    print("false positives", false_positives)
    print("false negatives", false_negatives)
    print("thought matched attribute", thought_matched_attribute)
    print("thought didnt match attribute", thought_didnt_match_attribute)


def is_classification_right(classification, expected):
    if classification.cats['usability_attribute'] >= 0.5:
        return expected
    else:
        return not expected


test_data_accuracy("test_data.csv", "accessibility")
