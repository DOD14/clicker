from clicker import Clicker
from selenium.webdriver.chrome.options import Options
import multiprocessing as mp

def worker(line):
    try:
        clicker.init_driver(chrome_options)
        clicker.process_line(line)
    finally:
        clicker.close_driver()

clicker = Clicker()

# define options and pass to init_driver
chrome_options = Options()
chrome_options.add_argument("--headless")   

# open and read lines from links file
with open('links.txt', 'r') as links_file:
    lines = links_file.read().splitlines()

# for each line spawn a new subprocess and call worker
# see https://stackoverflow.com/questions/38164635/selenium-not-freeing-up-memory-even-after-calling-close-quit
for line in lines:
    if __name__ == '__main__':
        p = mp.Process(target=worker, args=(line,))
        p.start()
        p.join()
