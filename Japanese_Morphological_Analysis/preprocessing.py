import re

some_tokens = []


def remove_emoji(a_tweet):
    with open('emoji_list.txt') as emoji_file:
        emoji_regex = ''.join(emoji_file.readlines()).strip()
    emoji_finder = re.compile(emoji_regex)
    some_emoji = emoji_finder.findall(a_tweet)
    for an_emoji in some_emoji:
        some_tokens.append((an_emoji, 'EMOJI'))
        a_tweet = a_tweet.replace(an_emoji, ' ')
    return a_tweet


def remove_usernames(a_tweet):
    some_usernames = re.findall('@([a-z0-9_]+)', a_tweet, re.I)
    for an_username in some_usernames:
        some_tokens.append((an_username, 'USERNAMES'))
        a_tweet = a_tweet.replace(an_username, ' ')
    return a_tweet


def remove_hashtags(a_tweet):
    some_hashtags = re.findall("#([a-z0-9_]+)", a_tweet, re.I)
    for a_hashtag in some_hashtags:
        some_tokens.append((a_hashtag, 'HASHTAGS'))
        a_tweet = a_tweet.replace(a_hashtag, ' ')
    return a_tweet


def remove_urls(a_tweet):
    url_finder = re.compile(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+'
                            r'|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?'
                            r'\xab\xbb\u201c\u201d\u2018\u2019]))')
    some_urls = url_finder.findall(a_tweet)
    for an_url in some_urls:
        an_url = ''.join(an_url)
        some_tokens.append((an_url, 'URLS'))
        a_tweet = a_tweet.replace(an_url, ' ')
    return a_tweet


def remove_brackets(a_tweet):
    re_text = '[0-9A-Za-zぁ-ヶ一-龠]'
    bracket_finder = re.compile(r'[\(（]' + re_text + r'[\)）]')
    some_brackets = bracket_finder.findall(a_tweet)
    for a_bracket in some_brackets:
        some_tokens.append((a_bracket, 'BRACKETS'))
        a_tweet = a_tweet.replace(a_bracket, ' ')
    return a_tweet


def kaomoji_find(teststring, kao_finder, re_text, face_list=None):
    if face_list is None: face_list = []
    faces = kao_finder.findall(teststring)
    for kao in faces:
        if len(kao) > 10:
            if len(re.findall(re_text, kao)) > 4:
                first_third = kao_finder.match(kao[:int(len(kao) / 3)])
                if firstthird is not None:
                    face_list.append(firstthird.group())
                    face_list = kaomoji_find(teststring.replace(firstthird.group(), ''), kao_finder, re_text, face_list)
                else:
                    first_half = kao_finder.match(kao[:int(len(kao) / 2)])
                    if first_half is not None:
                        face_list.append(firsthalf.group())
                        face_list = kaomoji_find(teststring.replace(firsthalf.group(), ''), kao_finder, re_text, face_list)
            else:
                face_list.append(kao)
        else:
            face_list.append(kao)
    return face_list


def remove_kaomoji(a_tweet):
    re_text = '[0-9A-Za-zぁ-ヶ一-龠]'
    re_nontext = '[^0-9A-Za-zぁ-ヶ一-龠]'
    re_allowtext = '[ovっつ゜ニノ三二]'
    re_hwkana = '[ｦ-ﾟ]'
    re_openbracket = r'[\(∩꒰（]'
    re_closebracket = r'[\)∩꒱）]'
    re_aroundface = '(?:' + re_nontext + '|' + re_allowtext + ')*'
    re_face = '(?!(?:' + re_text + '|' + re_hwkana + '){3,}).{3,}'
    kao_finder = re.compile(re_aroundface + re_openbracket + re_face + re_closebracket + re_aroundface)
    some_kaomoji = kaomoji_find(a_tweet, kao_finder, re_text)
    for an_kaomoji in some_kaomoji:
        an_kaomoji = ''.join(an_kaomoji)
        some_tokens.append((an_kaomoji, 'KAOMOJI'))
        a_tweet = a_tweet.replace(an_kaomoji, ' ')
    return a_tweet