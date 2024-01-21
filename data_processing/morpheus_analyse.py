from data_processing.nlp_tool.morpheus_config import analyze_text, parse_morpheus_output
import json

with open("data/demo.txt", "r", encoding="UTF-8") as input_file:
    text = input_file.read()
    output = analyze_text(text)
    parsed_output = parse_morpheus_output(output, output_format="string")
    with open("data/demo_output_morpheus_strings.json", "w", encoding="UTF-8") as output_file:
        json.dump(parsed_output, output_file, indent=4)

