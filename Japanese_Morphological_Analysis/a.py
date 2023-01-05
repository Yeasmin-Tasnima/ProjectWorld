import matplotlib.pyplot as plt
import MeCab


def analyze(text):
    parsed = mt.parseToNode(text)
    res = []
    while parsed:
        if parsed.surface != '' and parsed.feature.split(',')[0] != "記号":
            res.append((parsed.surface, parsed.feature.split(',')[0]))
        parsed = parsed.next

    return res

import time
from multiprocessing import Pool
lens = [25, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
times = []

mt = MeCab.Tagger('-r /dev/null /usr/local/lib/mecab/dic/mydic')
mt.parse('')

num_runs = 10
num_cpu = 4
for x in lens:
    t = 0
    for k in range(num_runs):
        fname = 'texts/' + str(x) + '_' + str(k%5)
        with open(fname, 'r', encoding='utf-8') as f:
            text = f.read()
            text_list = [text] * num_cpu
            ts = time.time_ns() 
            with Pool(num_cpu) as p:
                res = p.map(analyze, text_list)
            dt = time.time_ns() - ts
            t += dt / 1000000
    t /= (num_runs*num_cpu)
    times.append(t)
