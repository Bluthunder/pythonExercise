#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s.split(':')
    if s[-2:] == "PM":
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    else:
        if time[0] == '12':
            time[0] = '00'
        ntime = ':'.join(time)
        return str(ntime[:-2])


if __name__ == '__main__':
    s = '12:40:22AM'
    result = timeConversion(s)
    print(result)

