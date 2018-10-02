def convertSec(second)
    hour = int((second3600))
    minute =int((second%3600)60)
    sec = float((second%3600)%60)
    string = str(hour)
    if hour == 1
        string = string + ' hour, '
    else
        string = string + ' hours, '
    string = string + str(minute)
    if minute == 1
        string = string + ' minute, '
    else
        string = string + ' minutes, '
    string = string + str(sec)
    if sec == 1
        string = string + ' second'
    else
        string = string + ' seconds'
    return string
def download_time(fileSize, unitFS, bandwi, unitbw)
    switcher = {
        'kb' 210,
        'kB' 2108,
        'Mb' 220,
        'MB' 2208,
        'Gb' 230,
        'GB' 2308,
        'Tb' 240,
        'TB' 2408,
    }
    fileSize = fileSize  switcher.get(unitFS)
    bandwi = bandwi  switcher.get(unitbw)
    sec = fileSize  (bandwi  1.0 )
    return convertSec(sec)