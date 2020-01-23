# some ideas from https://github.com/andyhopp/aws-transcribe-to-srt

import json

def format_mins(val):
    secs = float(val)
    hours = int(secs/3600)
    secs = secs - (hours * 3600)
    mins = int(secs/60)
    secs = secs - (mins * 60)
    m_secs = int(secs*1000)
    secs = int(secs)
    return pad_time(hours) + ':' + pad_time(mins) + ':' + pad_time(secs) + ',' + pad_time(m_secs, 3)

def pad_time(val, l= 2):
    return ('0'.join([''] * (l+1)) + str(val))[-l:]

def convert_to_srt():
    with open('input.json', encoding='utf-8') as f:
        raw = json.load(f)
        items = raw['results']['items']

        start = end = counter = index = 0
        current = float(items[0]['start_time'])
        output = next_line = ''

        for token in items:
            start = format_mins(current)
            if token['type'] == 'punctuation':
                next_line = next_line[0:-1] + token['alternatives'][0]['content']
                end = format_mins(items[counter - 1]['end_time'])
                index += 1
                output += str(index) + '\n' + str(start) + ' --> ' + str(end) + '\n' + next_line + '\n\n'
                next_line = ''
                if counter + 1 < len(items):
                    current = float(items[counter + 1]['start_time'])
            elif float(token['end_time']) - float(token['start_time']) > 5.0:
                end = format_mins(items[counter - 1]['end_time'])
                index += 1
                output += str(index) + '\n' + str(start) + ' --> ' + str(end) + '\n' + next_line + '\n\n'
                next_line = token['alternatives'][0]['content'] + ' '
                current = float(token['start_time'])
            else:
                next_line += token['alternatives'][0]['content'] + ' '
        
            start = format_mins(current)

            if items[len(items)-1]['type'] == 'punctuation':
                end = format_mins(items[len(items)-2]['end_time'])
            else:
                end = format_mins(items[len(items)-1]['end_time'])
            
            counter += 1
        
        with open('output.srt', 'w', encoding='utf-8') as f:
            f.write(output)

