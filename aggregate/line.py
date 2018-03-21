from pyspark import SparkConf
from pyspark import SparkContext


def aggregate(target):
    conf = SparkConf()
    conf.setAppName('example')
    sc = SparkContext(conf=conf)

    log_data = sc.textFile('data/crino-r')
    lines = log_data.filter(lambda s: target in s)
    with open('output/line.metrics', 'w') as fw:
        fw.write(f'●{target}：{num}\n')
        fw.writelines('\n'.join(lines.collect()))

