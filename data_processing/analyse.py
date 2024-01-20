from data_processing.nlp_tool.nlp_config import cltk_nlp
from data_processing.prepare_data import prepare_data, tsv_to_json

data = prepare_data("data/demo.txt")
out_file_name = "data/demo_output.tsv"


def analyse_texts(data_texts):
    with open(out_file_name, "a", encoding='UTF-8') as output_file:
        output_file.write("token\tlemma\tpos\tmorphosyntactic_features\tauthor\ttext_id\ttitle\tline_number\n")
        for text in data_texts:
            doc = cltk_nlp.analyze(text=text["text"])
            line_number = 1
            for i in range(len(doc.tokens)):
                if doc.tokens[i] == "\n":
                    line_number += 1
                    continue
                print(doc.tokens[i], doc.lemmata[i], doc.pos[i], doc.morphosyntactic_features[i], text["author"],
                        text["text_id"], text["title"], line_number, sep="\t", file=output_file)


analyse_texts(data)

tsv_to_json(out_file_name, "data/demo_output.json")
