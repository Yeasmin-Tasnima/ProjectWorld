import MeCab


def find_tokens(tweet, keywords=None):
    if keywords is None: keywords = []
    mt = MeCab.Tagger()
    mt.parse('')
    parsed = mt.parseToNode(tweet)
    components = []
    while parsed:
        if parsed.surface != '' and parsed.feature.split(',')[0] != "記号":
            components.append((parsed.surface, parsed.feature.split(',')[0]))
        parsed = parsed.next
    """for a_keyword in keywords:
        cindex = 0
        while True:
            if cindex >= len(components):
                break
            temp_key = a_keyword
            if components[cindex][0] == temp_key:
                cindex += 1
                continue
            elif components[cindex][0] == temp_key[:len(components[cindex][0])]:
                match = False
                temp_index = cindex
                temp_key = temp_key.replace(components[temp_index][0], '', 1)
                while True:
                    temp_index += 1
                    if temp_index >= len(components):
                        break
                    else:
                        if components[temp_index][0] == temp_key[:len(components[temp_index][0])]:
                            temp_key = temp_key.replace(components[temp_index][0], '', 1)
                            if temp_key == '':
                                match = True
                                break
                            else:
                                continue
                        else:
                            break
                if match:
                    components[cindex] = (a_keyword, 'PROJECT_KEYWORD')
                    del components[cindex+1:temp_index+1]
                cindex += 1
                continue
            else:
                cindex += 1
                continue"""

    return components
# '表', '戦', 'だっ', 'た', 'が', '国民', 'の', '関心', 'も', '薄く', '…', '…', '。', '惨敗', 'を', '喫し', 'た', '2'
# 表 戦 だっ た が 国民 の 関心 も 薄く … … 。 惨敗 を 喫し た