import spacy
import random
from spacy.tokens import DocBin


def convert_to_spacy_format(data):
    nlp = spacy.load("en_core_web_sm")
    docs = []
    for story, is_quality_attribute in nlp.pipe(data, as_tuples=True):
        if is_quality_attribute:
            story.cats["usability_attribute"] = 1
            story.cats["not_usability_attribute"] = 0
        else:
            story.cats["usability_attribute"] = 0
            story.cats["not_usability_attribute"] = 1
        docs.append(story)
    return docs


def get_training_data(filename):
    """Takes CSV file delimeted by double quote characters"""
    with open(filename) as stories:
        lines = stories.readlines()
    data = []
    for line in reversed(lines):
        line = line.strip()
        usability_attribute, story = line.split('"')
        if usability_attribute == "":
            data.append((story, False))
        else:
            data.append((story, True))
    return data


def get_specific_attribute_data(filename, attribute):
    with open(filename) as stories:
        lines = stories.readlines()
    data = []
    count = 0
    for line in lines:
        line = line.strip()
        usability_attributes, story = line.split('"')
        usability_attributes = usability_attributes.split(',')
        usability_attributes = [attribute.strip().lower() for attribute in usability_attributes]
        if attribute in usability_attributes:
            data.append((story, True))
            count += 1
        else:
            data.append((story, False))
    print(count)
    return data


if __name__ == "__main__":
    data = get_specific_attribute_data("test_data.csv", "efficiency")
    data = convert_to_spacy_format(data)
    random.shuffle(data)

    training_data = data[:len(data) // 2]
    validation_data = data[len(data) // 2:]

    doc_bin = DocBin(docs=training_data)
    doc_bin.to_disk("./data/train_access.spacy")

    doc_bin = DocBin(docs=validation_data)
    doc_bin.to_disk("./data/valid_access.spacy")
