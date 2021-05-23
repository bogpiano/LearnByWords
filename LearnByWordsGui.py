import PyQt5.QtWidgets as qtw
from PyQt5.QtWidgets import QMessageBox
import random
import copy
from gtts import gTTS
import subprocess

import HandlerXml as XML

# global constants
WINDOW_TITLE = 'Learn by words'
WINDOW_WIDTH = 312
WINDOW_HEIGHT = 522
BKG_COLOR_GRAY2 = 'background-color: rgba(236, 233, 233, 1)'
COLOR_GREEN = 'color: green'
COLOR_BLUE = 'color: rgba(0, 152, 201, 1)'
COLOR_RED = 'color: #ca3228'
COLOR_BLACK = 'color: rgba(0, 0, 0, 0.9)'
COLOR_GRAY1 = 'color: rgba(197, 195, 194, 1)'
STYLE_RIGHT = 'color: rgba(0, 0, 0, 0.9); background-color: green'
STYLE_WRONG = 'color: rgba(0, 0, 0, 0.9); background-color: #ca3228'

# global variables
level = 1
started = 'False'
langFrom = 'tagalog'
langTo = 'english'
remainingWords = []
guessedWrong = []
guessedRight = []
listLevel = []
wordTLPicked = ""
countWrong = 0
loadLevel = True
withSound = False

class MainWindow(qtw.QWidget):

    # window constructor
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setLayout(qtw.QVBoxLayout())
        self.setFixedWidth(WINDOW_WIDTH)
        self.setFixedHeight(WINDOW_HEIGHT)
        self.show()
        # create container
        self.container = qtw.QWidget()
        self.container.setLayout(qtw.QGridLayout())
        self.container.setStyleSheet(BKG_COLOR_GRAY2)
        self.startTestWindow(self.container)

    def startTest(self, container):
        self.cmb_languages.deleteLater()
        self.btn_level.deleteLater()
        self.btn_Start.deleteLater()
        self.btn_level_1.deleteLater()
        self.btn_level_2.deleteLater()
        self.btn_level_3.deleteLater()
        self.btn_level_4.deleteLater()
        self.btn_level_5.deleteLater()
        self.btn_level_6.deleteLater()
        self.btn_level_7.deleteLater()
        self.btn_level_8.deleteLater()
        self.btn_level_9.deleteLater()
        self.btn_level_10.deleteLater()
        self.btn_level_11.deleteLater()
        self.btn_level_12.deleteLater()
        self.btn_level_13.deleteLater()
        self.btn_level_14.deleteLater()
        self.btn_level_15.deleteLater()
        self.btn_level_16.deleteLater()
        self.btn_level_17.deleteLater()
        self.btn_level_18.deleteLater()
        self.btn_level_19.deleteLater()
        self.btn_level_20.deleteLater()
        self.btn_Listen.deleteLater()
        self.nextWordWindow(self.container)

    def setLevel1(self):
        global level
        level = 1
        self.btn_level.setText('Level ' + str(level))
    def setLevel2(self):
        global level
        level = 2
        self.btn_level.setText('Level ' + str(level))
    def setLevel3(self):
        global level
        level = 3
        self.btn_level.setText('Level ' + str(level))
    def setLevel4(self):
        global level
        level = 4
        self.btn_level.setText('Level ' + str(level))
    def setLevel5(self):
        global level
        level = 5
        self.btn_level.setText('Level ' + str(level))
    def setLevel6(self):
        global level
        level = 6
        self.btn_level.setText('Level ' + str(level))
    def setLevel7(self):
        global level
        level = 7
        self.btn_level.setText('Level ' + str(level))
    def setLevel8(self):
        global level
        level = 8
        self.btn_level.setText('Level ' + str(level))
    def setLevel9(self):
        global level
        level = 9
        self.btn_level.setText('Level ' + str(level))
    def setLevel10(self):
        global level
        level = 10
        self.btn_level.setText('Level ' + str(level))
    def setLevel11(self):
        global level
        level = 11
        self.btn_level.setText('Level ' + str(level))
    def setLevel12(self):
        global level
        level = 12
        self.btn_level.setText('Level ' + str(level))
    def setLevel13(self):
        global level
        level = 13
        self.btn_level.setText('Level ' + str(level))
    def setLevel14(self):
        global level
        level = 14
        self.btn_level.setText('Level ' + str(level))
    def setLevel15(self):
        global level
        level = 15
        self.btn_level.setText('Level ' + str(level))
    def setLevel16(self):
        global level
        level = 16
        self.btn_level.setText('Level ' + str(level))
    def setLevel17(self):
        global level
        level = 17
        self.btn_level.setText('Level ' + str(level))
    def setLevel18(self):
        global level
        level = 18
        self.btn_level.setText('Level ' + str(level))
    def setLevel19(self):
        global level
        level = 19
        self.btn_level.setText('Level ' + str(level))
    def setLevel20(self):
        global level
        level = 20
        self.btn_level.setText('Level ' + str(level))

    def shownRightEN(self):

        if self.option1.text() == wordENRight:
            self.option1.setStyleSheet(STYLE_RIGHT)
        elif self.option2.text() == wordENRight:
            self.option2.setStyleSheet(STYLE_RIGHT)
        elif self.option3.text() == wordENRight:
            self.option3.setStyleSheet(STYLE_RIGHT)
        elif self.option4.text() == wordENRight:
            self.option4.setStyleSheet(STYLE_RIGHT)
        elif self.option5.text() == wordENRight:
            self.option5.setStyleSheet(STYLE_RIGHT)

    def translateOption(self, option):
        if option.text() == wordENRight:
            option.setStyleSheet(COLOR_GREEN)
        global countWrong
        global remainingWords

        if option.text() == wordENRight:
            option.setStyleSheet(STYLE_RIGHT)
            self.lb_validate.setText("Right!")
            self.lb_validate.setStyleSheet(COLOR_GREEN)
            guessedRight.append(remainingWords[indexInList])
        else:
            option.setStyleSheet(STYLE_WRONG)
            self.lb_validate.setText("  Wrong!")
            self.lb_validate.setStyleSheet(COLOR_RED)
            self.shownRightEN()
            guessedWrong.append(remainingWords[indexInList])
            countWrong += 1
        remainingWords.pop(indexInList)
        self.deactivateOpt(True)
        self.btn_Next.setDisabled(False)
        self.btn_Next.setStyleSheet(COLOR_BLUE)
        self.lb_validate.setVisible(True)
        self.lb_count.setText("")

    def translateOpt1(self):
        self.translateOption(self.option1)

    def translateOpt2(self):
        self.translateOption(self.option2)

    def translateOpt3(self):
        self.translateOption(self.option3)

    def translateOpt4(self):
        self.translateOption(self.option4)

    def translateOpt5(self):
        self.translateOption(self.option5)

    def playSound(self):
        global withSound
        if withSound == True:
            try:
                var = gTTS(text=wordTLPicked, lang='tl')
                var.save('sound.mp3')
                subprocess.call(["afplay", "sound.mp3"])
            except:
                msg = QMessageBox()
                msg.setWindowTitle('Error!')
                msg.setText("Error: Cannot load sound! Please check with application support team."
                            " Sounds can be disabled by clicking the 'OFF SOUNDS' button.")
                x = msg.exec_()

    def reTest(self):
        self.lb_header1.deleteLater()
        self.lb_header2.deleteLater()
        self.tagalog_word.deleteLater()
        self.option1.deleteLater()
        self.option2.deleteLater()
        self.option3.deleteLater()
        self.option4.deleteLater()
        self.option5.deleteLater()
        self.lb_count.deleteLater()
        self.lb_validate.deleteLater()
        self.btn_Next.deleteLater()
        self.btn_RePlay.deleteLater()
        self.btn_ReStart.deleteLater()
        global loadLevel
        loadLevel = True
        self.startTestWindow(self.container)
        guessedRight.clear()

    def setDefaults(self):
        self.lb_validate.setText("")
        self.tagalog_word.setText("")
        self.option1.setStyleSheet(COLOR_BLUE)
        self.option2.setStyleSheet(COLOR_BLUE)
        self.option3.setStyleSheet(COLOR_BLUE)
        self.option4.setStyleSheet(COLOR_BLUE)
        self.option5.setStyleSheet(COLOR_BLUE)

    def deactivateOpt(self, active):
        self.option1.setDisabled(active)
        self.option2.setDisabled(active)
        self.option3.setDisabled(active)
        self.option4.setDisabled(active)
        self.option5.setDisabled(active)

    def setPlaySound(self):
        global withSound
        if withSound == True:
            withSound = False
            self.btn_Listen.setText("ON SOUNDS")
        else:
            withSound = True
            self.btn_Listen.setText("OFF SOUNDS")

    def getNext(self):

        global remainingWords
        global loadLevel
        global listLevel
        global level
        self.setDefaults()
        self.deactivateOpt(False)

        # loading level
        if loadLevel:
            XML.loadLevel(langFrom, langTo, 'l'+str(level))
            listLevel = XML.listOfWordsLevel
            remainingWords = copy.deepcopy(listLevel)
            loadLevel = False
            self.btn_Next.setText('Next word')
            self.btn_ReStart.setText('LEVEL ' + str(level) + ' - CLICK TO CHOOSE LEVEL')
            self.lb_header1.setValue(0)

        if (len(guessedWrong) > 0) and (len(remainingWords) == 0):
            remainingWords = copy.deepcopy(guessedWrong)
            guessedWrong.clear()
            self.lb_count.setStyleSheet(COLOR_RED)
        if len(remainingWords) != 0:
            self.btn_Next.setDisabled(True)
            self.btn_Next.setStyleSheet(COLOR_GRAY1)
            self.lb_count.setText("  "+str(len(remainingWords)))
            self.lb_validate.setText("")

            nrRemaining = len(remainingWords)
            global wordTLPicked
            global wordENRight
            global wordCNTPicked
            global optionRight
            global indexInList
            global countWrong

            self.lb_header1.setValue(int(len(guessedRight)/len(listLevel) * 100.0))

            # get a tagalog word to translate algo
            pickRandomNr = random.sample(range(0, nrRemaining), 1)
            indexInList = pickRandomNr[0]
            wordTLPicked = remainingWords[indexInList].wordLang1
            wordENRight = remainingWords[indexInList].wordLang2

            # set 5 random option in English and the tagalog workd picked to translate
            self.tagalog_word.setText(wordTLPicked)
            fiveRandom = random.sample(range(0, len(listLevel)), 5)
            fivePoz = random.sample(range(1, 6), 5)

            def setChoise(x, y):
                if x == 1:
                    self.option1.setText(y)
                elif x == 2:
                    self.option2.setText(y)
                elif x == 3:
                    self.option3.setText(y)
                elif x == 4:
                    self.option4.setText(y)
                elif x == 5:
                    self.option5.setText(y)

            for z in range(5):
                setChoise(fivePoz[z], listLevel[fiveRandom[z]].wordLang2)

            # check if the picked word is in the random list, if not add it
            elemInList = False
            for x in fiveRandom:
                if wordTLPicked == listLevel[x].wordLang1:
                    elemInList = True

            if not elemInList:
                opt5Random = random.sample(range(1, 5), 1)
                if opt5Random[0] == 1:
                    self.option1.setText(wordENRight)
                    optionRight = 1
                elif opt5Random[0] == 2:
                    self.option2.setText(wordENRight)
                    optionRight = 2
                elif opt5Random[0] == 3:
                    self.option3.setText(wordENRight)
                    optionRight = 3
                elif opt5Random[0] == 4:
                    self.option4.setText(wordENRight)
                    optionRight = 4
                elif opt5Random[0] == 5:
                    self.option5.setText(wordENRight)
                    optionRight = 5

            # play the sound if set
            self.playSound()
        else:
            loadLevel = True
            if level == 5: level = 1
            else: level = level + 1
            self.option1.setText('')
            self.option1.setDisabled(True)
            self.option2.setText('')
            self.option2.setDisabled(True)
            self.option3.setText('')
            self.option3.setDisabled(True)
            self.option4.setText('')
            self.option4.setDisabled(True)
            self.option5.setText('')
            self.option5.setDisabled(True)
            self.btn_Next.setText('Next Level '+str(level))
            self.lb_header1.setValue(int(len(guessedRight)/len(listLevel) * 100.0))
            guessedRight.clear()
            self.lb_count.setStyleSheet(COLOR_GREEN)

    # create start window
    def startTestWindow(self, container):
        # create fonts
        font_level = self.font()
        font_level.setPointSize(14)
        font_combo = self.font()
        font_combo.setPointSize(16)
        font_btn_level = self.font()
        font_btn_level.setPointSize(36)
        font_btn_start = self.font()
        font_btn_start.setPointSize(26)

        # create controls: labels, buttons, combos
        # languages
        self.cmb_languages = qtw.QComboBox()
        lang_list = ["Tagalog to English", "Romanian to English"]
        self.cmb_languages.addItems(lang_list)
        self.cmb_languages.setStyleSheet(COLOR_BLUE)
        self.cmb_languages.setFont(font_combo)
        # Level
        self.btn_level = qtw.QPushButton('Level ' + str(level))
        self.btn_level.setStyleSheet(COLOR_GREEN)
        self.btn_level.setFlat(True)
        self.btn_level.setFont(font_btn_level)
        # Start
        self.btn_Start = qtw.QPushButton('START TEST', clicked=self.startTest)
        self.btn_Start.setStyleSheet(COLOR_GREEN)
        self.btn_Start.setFont(font_btn_start)
        # Levels
        # 1
        self.btn_level_1 = qtw.QPushButton('Level 1', clicked=self.setLevel1)
        self.btn_level_1.setStyleSheet(COLOR_BLUE)
        self.btn_level_1.setFont(font_level)
        # 2
        self.btn_level_2 = qtw.QPushButton('Level 2', clicked=self.setLevel2)
        self.btn_level_2.setStyleSheet(COLOR_BLUE)
        self.btn_level_2.setFont(font_level)
        # 3
        self.btn_level_3 = qtw.QPushButton('Level 3', clicked=self.setLevel3)
        self.btn_level_3.setStyleSheet(COLOR_BLUE)
        self.btn_level_3.setFont(font_level)
        # 4
        self.btn_level_4 = qtw.QPushButton('Level 4', clicked=self.setLevel4)
        self.btn_level_4.setStyleSheet(COLOR_BLUE)
        self.btn_level_4.setFont(font_level)
        # 5
        self.btn_level_5 = qtw.QPushButton('Level 5', clicked=self.setLevel5)
        self.btn_level_5.setStyleSheet(COLOR_BLUE)
        self.btn_level_5.setFont(font_level)
        # 6
        self.btn_level_6 = qtw.QPushButton('Level 6', clicked=self.setLevel6)
        self.btn_level_6.setStyleSheet(COLOR_GRAY1)
        self.btn_level_6.setFont(font_level)
        self.btn_level_6.setDisabled(True)
        # 7
        self.btn_level_7 = qtw.QPushButton('Level 7', clicked=self.setLevel7)
        self.btn_level_7.setStyleSheet(COLOR_GRAY1)
        self.btn_level_7.setFont(font_level)
        self.btn_level_7.setDisabled(True)
        # 8
        self.btn_level_8 = qtw.QPushButton('Level 8', clicked=self.setLevel8)
        self.btn_level_8.setStyleSheet(COLOR_GRAY1)
        self.btn_level_8.setFont(font_level)
        self.btn_level_8.setDisabled(True)
        # 9
        self.btn_level_9 = qtw.QPushButton('Level 9', clicked=self.setLevel9)
        self.btn_level_9.setStyleSheet(COLOR_GRAY1)
        self.btn_level_9.setFont(font_level)
        self.btn_level_9.setDisabled(True)
        # 10
        self.btn_level_10 = qtw.QPushButton('Level 10', clicked=self.setLevel10)
        self.btn_level_10.setStyleSheet(COLOR_GRAY1)
        self.btn_level_10.setFont(font_level)
        self.btn_level_10.setDisabled(True)
        # 11
        self.btn_level_11 = qtw.QPushButton('Level 11', clicked=self.setLevel11)
        self.btn_level_11.setStyleSheet(COLOR_GRAY1)
        self.btn_level_11.setFont(font_level)
        self.btn_level_11.setDisabled(True)
        # 12
        self.btn_level_12 = qtw.QPushButton('Level 12', clicked=self.setLevel12)
        self.btn_level_12.setStyleSheet(COLOR_GRAY1)
        self.btn_level_12.setFont(font_level)
        self.btn_level_12.setDisabled(True)
        # 13
        self.btn_level_13 = qtw.QPushButton('Level 13', clicked=self.setLevel13)
        self.btn_level_13.setStyleSheet(COLOR_GRAY1)
        self.btn_level_13.setFont(font_level)
        self.btn_level_13.setDisabled(True)
        # 14
        self.btn_level_14 = qtw.QPushButton('Level 14', clicked=self.setLevel14)
        self.btn_level_14.setStyleSheet(COLOR_GRAY1)
        self.btn_level_14.setFont(font_level)
        self.btn_level_14.setDisabled(True)
        # 15
        self.btn_level_15 = qtw.QPushButton('Level 15', clicked=self.setLevel15)
        self.btn_level_15.setStyleSheet(COLOR_GRAY1)
        self.btn_level_15.setFont(font_level)
        self.btn_level_15.setDisabled(True)
        # 16
        self.btn_level_16 = qtw.QPushButton('Level 16', clicked=self.setLevel16)
        self.btn_level_16.setStyleSheet(COLOR_GRAY1)
        self.btn_level_16.setFont(font_level)
        self.btn_level_16.setDisabled(True)
        # 17
        self.btn_level_17 = qtw.QPushButton('Level 17', clicked=self.setLevel17)
        self.btn_level_17.setStyleSheet(COLOR_GRAY1)
        self.btn_level_17.setFont(font_level)
        self.btn_level_17.setDisabled(True)
        # 18
        self.btn_level_18 = qtw.QPushButton('Level 18', clicked=self.setLevel18)
        self.btn_level_18.setStyleSheet(COLOR_GRAY1)
        self.btn_level_18.setFont(font_level)
        self.btn_level_18.setDisabled(True)
        # 19
        self.btn_level_19 = qtw.QPushButton('Level 19', clicked=self.setLevel19)
        self.btn_level_19.setStyleSheet(COLOR_GRAY1)
        self.btn_level_19.setFont(font_level)
        self.btn_level_19.setDisabled(True)
        # 20
        self.btn_level_20 = qtw.QPushButton('Level 20', clicked=self.setLevel20)
        self.btn_level_20.setStyleSheet(COLOR_GRAY1)
        self.btn_level_20.setFont(font_level)
        self.btn_level_20.setDisabled(True)
        # on/off sounds
        global withSound
        if withSound:
            textSounds = 'OFF SOUNDS'
        else:
            textSounds = 'ON SOUNDS'
        self.btn_Listen = qtw.QPushButton(textSounds, clicked=self.setPlaySound)
        self.btn_Listen.setStyleSheet(COLOR_BLUE)
        self.btn_Listen.setVisible(True)

        # add controls to container
        container.layout().addWidget(self.cmb_languages, 0, 0, 1, 3)
        container.layout().addWidget(self.btn_level, 1, 0, 1, 4)
        container.layout().addWidget(self.btn_Start, 2, 0, 2, 4)
        container.layout().addWidget(self.btn_level_1, 3, 0, 1, 1)
        container.layout().addWidget(self.btn_level_2, 3, 1, 1, 1)
        container.layout().addWidget(self.btn_level_3, 3, 2, 1, 1)
        container.layout().addWidget(self.btn_level_4, 3, 3, 1, 1)
        container.layout().addWidget(self.btn_level_5, 4, 0, 1, 1)
        container.layout().addWidget(self.btn_level_6, 4, 1, 1, 1)
        container.layout().addWidget(self.btn_level_7, 4, 2, 1, 1)
        container.layout().addWidget(self.btn_level_8, 4, 3, 1, 1)
        container.layout().addWidget(self.btn_level_9, 5, 0, 1, 1)
        container.layout().addWidget(self.btn_level_10, 5, 1, 1, 1)
        container.layout().addWidget(self.btn_level_11, 5, 2, 1, 1)
        container.layout().addWidget(self.btn_level_12, 5, 3, 1, 1)
        container.layout().addWidget(self.btn_level_13, 6, 0, 1, 1)
        container.layout().addWidget(self.btn_level_14, 6, 1, 1, 1)
        container.layout().addWidget(self.btn_level_15, 6, 2, 1, 1)
        container.layout().addWidget(self.btn_level_16, 6, 3, 1, 1)
        container.layout().addWidget(self.btn_level_17, 7, 0, 1, 1)
        container.layout().addWidget(self.btn_level_18, 7, 1, 1, 1)
        container.layout().addWidget(self.btn_level_19, 7, 2, 1, 1)
        container.layout().addWidget(self.btn_level_20, 7, 3, 1, 1)
        container.layout().addWidget(self.btn_Listen, 8, 0, 1, 4)

        # add container to MainWindow
        self.layout().addWidget(container)


    # create test window
    def nextWordWindow(self, container):
        # create fonts
        font = self.font()
        font.setPointSize(24)
        font_level = self.font()
        font_level.setPointSize(24)
        font_btn = self.font()
        font_btn.setPointSize(26)
        font_words = self.font()
        font_words.setPointSize(30)

        # create controls: labels, buttons, combos
        # level of user
        #self.lb_header1 = qtw.QLabel("  00%            ")
        self.lb_header1 = qtw.QProgressBar()
        self.lb_header1.setMaximum(100)
        self.lb_header1.setValue(0)
        self.lb_header1.setStyleSheet(COLOR_GREEN)
        self.lb_header1.setFont(font)
        self.lb_header1.setVisible(True)
        # type of word
        self.lb_header2 = qtw.QLabel('  Tagalog(En)')
        self.lb_header2.setStyleSheet(COLOR_GREEN)
        self.lb_header2.setFont(font)
        self.lb_header2.setVisible(True)
        # counting remaining
        self.lb_count= qtw.QLabel("")
        self.lb_count.setVisible(True)
        self.lb_count.setFont(font_btn)
        self.lb_count.setStyleSheet(COLOR_GREEN)
        # validate translation
        self.lb_validate = qtw.QLabel("")
        self.lb_validate.setVisible(True)
        self.lb_validate.setFont(font_btn)
        self.lb_validate.setStyleSheet(COLOR_GREEN)
        # tagalog word
        self.tagalog_word = qtw.QPushButton("")
        self.tagalog_word.setFont(font_words)
        self.tagalog_word.setFlat(True)
        self.tagalog_word.setStyleSheet(COLOR_GREEN) # #690 - green
        self.tagalog_word.setVisible(True)
        # option 1
        self.option1 = qtw.QPushButton(clicked=self.translateOpt1)
        self.option1.setFont(font_words)
        self.option1.setStyleSheet(COLOR_BLUE)
        self.option1.setVisible(True)
        # option 2
        self.option2 = qtw.QPushButton(clicked=self.translateOpt2)
        self.option2.setStyleSheet(COLOR_BLUE)
        self.option2.setFont(font_words)
        self.option2.setVisible(True)
        # option 3
        self.option3 = qtw.QPushButton(clicked=self.translateOpt3)
        self.option3.setStyleSheet(COLOR_BLUE)
        self.option3.setFont(font_words)
        self.option3.setVisible(True)
        # option 4
        self.option4 = qtw.QPushButton(clicked=self.translateOpt4)
        self.option4.setStyleSheet(COLOR_BLUE)
        self.option4.setFont(font_words)
        self.option4.setVisible(True)
        # option 5
        self.option5 = qtw.QPushButton(clicked=self.translateOpt5)
        self.option5.setStyleSheet(COLOR_BLUE)
        self.option5.setFont(font_words)
        self.option5.setVisible(True)
        # reply sound
        self.btn_RePlay = qtw.QPushButton("Replay sound", clicked=self.playSound)
        self.btn_RePlay.setFont(font)
        self.btn_RePlay.setVisible(True)
        self.btn_RePlay.setStyleSheet(COLOR_BLUE)
        if not withSound:
            self.btn_RePlay.setStyleSheet(COLOR_GRAY1)
            self.btn_RePlay.setDisabled(True)
        # next word
        self.btn_Next = qtw.QPushButton("Replay sound", clicked=self.getNext)
        self.btn_Next.setStyleSheet(COLOR_GRAY1)
        self.btn_Next.setFont(font_btn)
        self.btn_Next.setVisible(True)
        # restart test
        self.btn_ReStart = qtw.QPushButton('LEVEL '+str(level)+ ' - CLICK TO CHOOSE LEVEL', clicked=self.reTest)
        self.btn_ReStart.setStyleSheet(COLOR_BLUE)
        self.btn_ReStart.setVisible(True)

        # add controls to container
        container.layout().addWidget(self.lb_header1, 0, 0, 1, 1)
        container.layout().addWidget(self.lb_header2, 0, 1, 1, 3)
        container.layout().addWidget(self.tagalog_word, 2, 0, 1, 4)
        container.layout().addWidget(self.option1, 3, 0, 1, 4)
        container.layout().addWidget(self.option2, 4, 0, 1, 4)
        container.layout().addWidget(self.option3, 5, 0, 1, 4)
        container.layout().addWidget(self.option4, 6, 0, 1, 4)
        container.layout().addWidget(self.option5, 7, 0, 1, 4)
        container.layout().addWidget(self.lb_count, 8, 0, 1, 1)
        container.layout().addWidget(self.lb_validate, 8, 1, 1, 3)
        container.layout().addWidget(self.btn_Next, 9, 0, 1, 4)
        container.layout().addWidget(self.btn_RePlay, 10, 0, 1, 4)
        container.layout().addWidget(self.btn_ReStart, 11, 0, 1, 4)

        # add container to MainWindow
        self.layout().addWidget(container)

        #get next word
        self.getNext()


# main caller
app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion')) # ['Breeze', 'Oxygen', 'QtCurve', 'Windows', 'Fusion']
app.exec_()
