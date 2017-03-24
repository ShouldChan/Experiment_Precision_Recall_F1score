import time

test_dir = "./test/"
topk_dir = "./4.1.4/"
test_file = "test_list_t+d"
file_name = "top5_t+d"
file_suffix = ".txt"

K = 5


def read_list():
    with open(test_dir + test_file + file_suffix, "r") as f:
        lines = f.readlines()
        testdata = []
        for line in lines:
            data = line.split("\t")
            value = []
            for d in data:
                if len(d) != 0:
                    value.append(d.replace("\r\n", ""))
            testdata.append(value)

    with open(topk_dir + file_name + file_suffix, "r") as f:
        lines = f.readlines()
        topdata = []
        for line in lines:
            data = line.split("\t")
            value = []
            for d in data:
                if len(d) != 0:
                    value.append(d.replace("\n", ""))
            topdata.append(value)
    newTestData = []
    for test in testdata:
        test = map(lambda x: int(x), test)
        newTestData.append(test)
        # print newTestData

    newTopData = []
    for t in topdata:
        top = map(lambda x: int(x), t)
        newTopData.append(top)
    # print newTopData
    # print len(newTopData), len(newTestData)
    return newTestData, newTopData


def born_to_be_free(testData, topData):
    precision, recall = 0.0, 0.0
    for each_test, each_top in zip(testData, topData):
        intsec = list(set(each_test).intersection(set(each_top)))
        precision += (1.0 * len(intsec)) / (1.0 * K)
        recall += (1.0 * len(intsec)) / (1.0 * len(each_test))
        # print len(intsec)
    return precision / 1082, recall / 1082


def main():
    t = time.time()
    testData, topData = read_list()
    print "read elapsed:   %f" % (time.time() - t)
    precision, recall = born_to_be_free(testData, topData)
    print "calc elapsed:   %f" % (time.time() - t)

    print "precision:   %f" % precision
    print "recall:  %f" % recall
    # print testData, "\n"
    # print topData


if __name__ == '__main__':
    main()
