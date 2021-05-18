#Used to only obtain attributes stories from specific backlog.txt

def get_classification_of_backlog():
    with open("test_data.csv") as test_data:
        all_test_lines = test_data.readlines()

    with open("backlog.txt") as specific_backlog:
        specific_backlog = set(specific_backlog.read().split('\n'))

    classifications = []
    for line in all_test_lines:
        classification, story = line.split('"')
        story = story.strip()
        if story in specific_backlog:
            classifications.append((classification, story))
    for attributes, story in classifications:
        print(f'{attributes}"{story}')

get_classification_of_backlog()

