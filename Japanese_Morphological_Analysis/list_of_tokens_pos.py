from preprocessing import *
from create_token import *


def token_list(str):
    """str = remove_emoji(str)
    str = remove_usernames(str)
    str = remove_hashtags(str)
    str = remove_urls(str)
    str = remove_brackets(str)
    str = remove_kaomoji(str)"""
    comp = find_tokens(str)
    """temp = []
    for word in comp:
        temp.append(word[0])
    components.append(temp)
    text.append(df['text'][i])"""
    return comp


if __name__ == '__main__':
    # s = 'Nice editing is 値段 から して hello こんな もん でしょう か ねぇ 可 も なく 不可 も なし です ね'
    # s = '彼は新しい仕事できっと成功するだろう。'
    s = '値段からしてこんなもんでしょうかねぇ可もなく不可もなしですね who are you.'
    lst = token_list(s)
    print(lst)
    """for i in range(len(lst)):
        print(lst[i][0])"""

# [('彼', '代名詞'), ('は', '助詞'), ('新しい', '形容詞'), ('仕事', '名詞'), ('で', '助動詞'), ('きっと', '副詞'), ('成功', '名詞'), ('する', '動詞'), ('だろう', '助動詞'), ('。', '補助記号')]
