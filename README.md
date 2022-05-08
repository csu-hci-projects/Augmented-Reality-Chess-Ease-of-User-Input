# Augmented Reality Chess: Ease of User Input

Requirements: Python3, opencv-python, Numpy, Time

###Checkpoint 2:

SetUp(As Of Checkpoint 2): Webcam directed at chessboard, with chessboard taking up full capture. Must be set up with one side of pieces to the right of the capture and one to the left. To get webcam correctly positioned program can be run with flag "capture" to present webcam view. 

Once set up and requirements are in place, program can be run with "python3 ImageReader.py". This will start the process of one turn of chess capturing. On any of the image screens, press a key to move to the next. The images shown will be in order the capture before a move, capture after a move, comparison image, and final read of chess move made. 

Next steps are to set up this process to cycle,reading in moves as the occur, updates stored record of chess board with output, and accomadate variable camera positions through isolating the board in the captures.

###Final Project:

SetUp: Webcam positioned above Chessboard to the right side of board when on the white side. The program can be run as python3 ImageCapture.py capture for a video stream to be used for aligning the board. Once aligned ensure all pieces are in their correct position before starting the game.

Once set up run the program as python3 ARChess.py to start a game. From here moves can be made back and forth and will be recorded on the console after each move is completed. The game will complete once a king is registered as taken from the board by either side.

Short Video:
https://youtu.be/ii_QcxQwOrM

Presentation Video:
https://www.youtube.com/watch?v=fkhvYq1kAjo




