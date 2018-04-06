import sys, getopt, os

helpmsg = "用法: pre.py [[-i <inputfile> [-o <outputfile>]] | [-a]] [-l <level>]\n" \
        "    -i|--ifile 输入文件名\n" \
        "    -o|--ofile 指定输出文件名，默认为pre-*.png\n" \
        "    -a|--all   遍历当前文件夹下所有png文件，并进行预处理，输出文件名均为默认名称\n" \
        "    -l|--level [0|1]指定颜色替换强度，默认为0，复杂计算替换为1\n" \
        "    -h|--help  帮助信息"


def main(argv):
    inputfile = ''
    outputfile = ''
    level = 0
    try:
        opts, args = getopt.getopt(argv,"ahsi:o:l:",["ifile=","ofile=","level="])
    except getopt.GetoptError:
        print('pre.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    if len(opts) == 0:
        print('pre.py -i <inputfile> -o <outputfile>')
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print(helpmsg)
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = [arg]
        elif opt in ("-o", "--ofile"):
            outputfile = [arg]
        elif opt in ("-a", "--all"):
            inputfile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.png']
        elif opt in ("-s", "--self"):
            inputfile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.png' and ('mask' in os.path.splitext(x)[0])]
            #outputfile = [x.replace("mask", "src") for x in inputfile]
			outputfile = [x for x in inputfile]
        elif opt in ("-l", "--level"):
            if arg.isdigit():
                level = int(arg)
            else:
                print("参数错误！")
                sys.exit()