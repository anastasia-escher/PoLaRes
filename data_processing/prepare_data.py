import json

def prepare_data(file_name):
    all_texts = []
    with open(file_name, "r", encoding="UTF-8") as input_file:
        blocks = input_file.read().split("\n\n")
        for block in blocks:
            lines = block.split("\n")
            if len(lines) < 4:
                continue
            author, text_id, title = lines[:3]
            text = "\n".join(lines[3:])
            all_texts.append({"author": author, "text_id": text_id, "title": title, "text": text})

    return all_texts


def tsv_to_json(file_name, output_file_name):
    with open(file_name, "r", encoding="UTF-8") as input_file:
        lines = input_file.readlines()
        headers = [i.strip() for i in lines[0].split("\t")]
        data_by_authors_and_poems = {}
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            line = line.split("\t")
            author = line[4]
            text_id = line[5]
            title = line[6]
            if author not in data_by_authors_and_poems:
                data_by_authors_and_poems[author] = {}
            if text_id not in data_by_authors_and_poems[author]:
                data_by_authors_and_poems[author][text_id] = {"title": title, "text": []}

            data_dict = dict(zip(headers, line))
            del data_dict["author"]
            del data_dict["text_id"]
            del data_dict["title"]
            data_by_authors_and_poems[author][text_id]["text"].append(data_dict )
    with open(output_file_name, "w", encoding="UTF-8") as output_file:
        json.dump(data_by_authors_and_poems, output_file, indent=4)




