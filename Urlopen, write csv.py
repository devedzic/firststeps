from urllib import request
# import io

goog_url = "https://ocw.mit.edu/courses/sloan-school-of-management/15-097-prediction-machine-learning-and-statistics-spring-2012/datasets/iris.csv"

def download_iris_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    # print(csv_str)
    csv_str = csv_str[2:-1]                 # get rid of the leading b' and the trailing '
    # print(csv_str)
    lines = csv_str.split("\\n")
    print(lines)                            # see what lines looks like - it's a list
    dest = r'iris.csv'
    fx = open(dest, "w")
    # fx = open(dest, "w", newline='')
    # fx = io.open(dest, "w", newline=None)
    for line in lines:
        line = line.replace("\\r", "")      # important: "\\r", not just "\r"
        print(line)
        # print(line.decode('utf-8'))
        '''
        Tried to use the following to remove the "\r"s in the end of each line, but it did not help.
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        
        line = line.strip()
        '''
        fx.write(line + '\n')
    fx.close()

download_iris_data(goog_url)