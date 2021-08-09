# clicker
User-friendly wrapper around Selenium to automate interaction, in particular with "click-to-donate" websites. Links from https://thenonprofits.com/.

# Usage
The main.py script automatically reads the 'links.txt' file in the same directory, then accesses those links, clicking buttons and waiting for the page to change if specified. The format of a line is:
* column 1: url
* column 2: optional css selector of click-to-donate button, if interaction is required
* column 3: optional css selector of an html element to wait for, confirming that the click has been received (usually an element on a 'thank you' page).

```python3 main.py``` is sufficient to get this started. Note most of the listed websites refuse access from tor exit nodes, preventing a single machine from clicking multiple times a day. So all this script does is automate the tedious task of clicking buttons for one IP address per day, aiming to replace a normal person rather than to spam the websites with clicks.
