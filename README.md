# HOW TO START PARSERMAIL ?

1.  INSTALLATION:
```bash 
git clone git@github.com:DrawManG/ParserMail.git
```
2.  CHANGE TO DIRECTORY:
```bash
cd  ParserMail
```
3. INSTALLING ALL LIBRARIES:
```bash
pip install -r requirements.txt
```
4.  GO TO THE INDEX.PY FILE AND CHANGE IT TO THE ONE YOU NEED:
#
+ #### ``text`` - Insert a query into the search engine here (the words for which the mail will be located)
#
+ #### ``how_many`` - Insert the number of links you need here (If there are 10, then there will be 10 links = 10 mails (if there are no errors))
#
+ #### ``txt_file`` - True\False switch, if necessary, download the received information immediately to a txt file (will be saved in the root of the "[Your request].txt" repository)
#
5.  RUN INDEX.PY:
```bash
python3 index.py
```

#
## Information (Python config):
+ ### ``Python 3.10.6``
+ ### ``Pip 22.0.2``

#