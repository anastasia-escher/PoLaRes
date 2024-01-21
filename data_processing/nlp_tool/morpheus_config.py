import subprocess
import xml.etree.ElementTree as ET
import re


def clean_text(output):
    cleaned_output = re.sub(r"[?!.,:;\'\"]", "", output)
    return cleaned_output

def shorten_name(name):
    # Dictionary for shortening names
    shortenings = {
        'nominative': 'nom.',
        'accusative': 'acc.',
        'ablative': 'abl.',
        'dative': 'dat.',
        'genitive': 'gen.',
        'vocative': 'voc.',
        'masculine': 'masc.',
        'feminine': 'fem.',
        'neuter': 'neut.',
        'singular': 'sg.',
        'plural': 'pl.',
        'verb': 'vrb.',
        'noun': 'noun',
        'adjective': 'adj.',
        'indicative': 'ind.',
        'subjunctive': 'subj.',
        'imperative': 'imp.',
        'active': 'act.',
        'passive': 'pass.',
        'participle': 'part.',
        'infinitive': 'inf.',
        'supine': 'sup.',
        'perfect': 'perf.',
        'imperfect': 'impf.',
        'future': 'fut.',
        'present': 'pres.'
    }
    return shortenings.get(name, name)


def analyze_text(_text):
    text = clean_text(_text)
    text = text.replace("apollo", "Apollo")
    try:
        command = f"docker run -i --rm perseidsproject/morpheus-perseids sh -c \"echo '{text}' | MORPHLIB=stemlib bin/morpheus -L\""
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr.decode('utf-8')}")
        return None


def parse_morpheus_output(output, output_format="list"):
    print(output)
    root = ET.fromstring(output)
    parsed_data = {}

    for unknown in root.findall('.//unknown'):
        unknown_form = unknown.text
        if unknown_form not in parsed_data:
            default_message = "Not able to recognize automatically"
            parsed_data[unknown_form] = [default_message] if output_format == "list" else default_message

    for word in root.findall('.//word'):
        form = word.find('form').text
        if word.find('.//unknown') is not None:
            if output_format == "list":
                parsed_data[form] = ["Unknown"]
            else:
                parsed_data[form] = "Not able to automatically parse this word. Please check manually."


        if form not in parsed_data:
            interpretations = [] if output_format == "list" else ""

            for entry in word.findall('.//entry'):
                lemma = entry.find('.//dict/hdwd').text if entry.find('.//dict/hdwd') is not None else None
                pos = entry.find('.//pofs').text if entry.find('.//pofs') is not None else None

                for infl in entry.findall('.//infl'):
                    interpretation_parts = [f"<b>{lemma} ({shorten_name(pos)})</b>:"]

                    # Tense, mood, voice for verbs
                    if pos == 'verb':
                        if infl.find('tense') is not None:
                            interpretation_parts.append(shorten_name(infl.find('tense').text))
                        if infl.find('mood') is not None:
                            interpretation_parts.append(shorten_name(infl.find('mood').text))
                        if infl.find('voice') is not None:
                            interpretation_parts.append(shorten_name(infl.find('voice').text))

                    # Other characteristics
                    if infl.find('case') is not None:
                        interpretation_parts.append(shorten_name(infl.find('case').text))
                    if infl.find('gender') is not None:
                        interpretation_parts.append(shorten_name(infl.find('gender').text))
                    if infl.find('number') is not None:
                        interpretation_parts.append(shorten_name(infl.find('number').text))

                    interpretation = ', '.join(filter(None, interpretation_parts))

                    if output_format == "list":
                        interpretations.append(interpretation)
                    else:
                        interpretations += interpretation + "; "

            if output_format == "string":
                interpretations = interpretations.rstrip("; ")

            parsed_data[form] = interpretations

    return parsed_data

# output = analyze_text("cacti pulchri sunt")
# parsed_output = parse_morpheus_output(output)
# print(parsed_output)
