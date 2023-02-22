bd={'top_L':' ','top_M':' ','top_R':' ',
    'mid_L':' ','mid_M':' ','mid_R':' ',
    'bot_L':' ','bot_M':' ','bot_R':' ',
    }
def printboard(bd):
    {
        print(bd['top_L'] + '|' + bd['top_M'] + '|' + bd['top_R'])
        print('-')
        print(bd['mid_L'] + '|' + bd['mid_M'] + '|' + bd['mid_R'])
        print('-+-+-')
        print(bd['bot_L'] + '|' + bd['bot_M'] + '|' + bd['bot_R'])
    }
