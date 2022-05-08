from ImageReader import runTurn, captureVideo, runTurnWithError


chessboard = [
["wr","wp","  ","  ","  ","  ","bp","br"],
["wn","wp","  ","  ","  ","  ","bp","bn"],
["wb","wp","  ","  ","  ","  ","bp","bb"],
["wq","wp","  ","  ","  ","  ","bp","bq"],
["wk","wp","  ","  ","  ","  ","bp","bk"],
["wb","wp","  ","  ","  ","  ","bp","bb"],
["wn","wp","  ","  ","  ","  ","bp","bn"],
["wr","wp","  ","  ","  ","  ","bp","br"]]

takenPieces = []

class gameState:
	isTurn = "True"

	def __init__(self,isTurn):
		self.isTurn = isTurn

	def toggle(self):
		if(self.isTurn):
			self.isTurn = False
		else:
			self.isTurn = True

	def getTurn(self):
		if(self.isTurn):
			print("White Turn")
		else:
			print("Black Turn")
		return self.isTurn

#Verifies only two changes occured
def turnImageToCoords():
	result = runTurnWithError()
	print(result)
	totalatmax = 0
	coordstomove = []
	for i in range(0,8):
		for j in range (0,8):
			if (result[i][j] == 255):
				if(totalatmax == 0):
					coordstomove.append([i,j])
				elif(totalatmax == 1):
					coordstomove.append([i,j])
				else:
					return False
				totalatmax = totalatmax + 1
	return coordstomove

#Verifies the two changes are legal moves and makes them
def updateBoardWithCoords(coords,currentGame):
	firstsquare = chessboard[coords[0][0]][coords[0][1]]
	secondsquare = chessboard[coords[1][0]][coords[1][1]]
	print(firstsquare)
	print(secondsquare)
	if(firstsquare == "  "):
		chessboard[coords[0][0]][coords[0][1]] = secondsquare
		chessboard[coords[1][0]][coords[1][1]] = "  "
		currentGame.toggle()
	elif(secondsquare == "  "):
		chessboard[coords[1][0]][coords[1][1]] = firstsquare
		chessboard[coords[0][0]][coords[0][1]] = "  "
		currentGame.toggle()
	elif(currentGame.isTurn):
		if(firstsquare[0] == "w"):
			chessboard[coords[1][0]][coords[1][1]] = firstsquare
			chessboard[coords[0][0]][coords[0][1]] = "  "
			takenPieces.append(secondsquare)
		else:
			chessboard[coords[0][0]][coords[0][1]] = secondsquare
			chessboard[coords[1][0]][coords[1][1]] = "  "
			takenPieces.append(firstsquare)
		currentGame.toggle()
	elif(not currentGame.isTurn):
		if(firstsquare[0] == "b"):
			chessboard[coords[1][0]][coords[1][1]] = firstsquare
			chessboard[coords[0][0]][coords[0][1]] = "  "
			takenPieces.append(secondsquare)
		else:
			chessboard[coords[0][0]][coords[0][1]] = secondsquare
			chessboard[coords[1][0]][coords[1][1]] = "  "
			takenPieces.append(firstsquare)
		currentGame.toggle()
	else:
		return "Bad Result"

def chessPrinter(currentGame):
	print("Now it is:")
	currentGame.getTurn()
	for row in chessboard:
		print(row)
	print("So Far These Pieces Have been Caputured")
	print(takenPieces)


def oneBoardUpdate(currentGame):
	coords = turnImageToCoords()
	if(coords):
		updateBoardWithCoords(coords,currentGame)
	chessPrinter(currentGame)


if __name__ == '__main__':
	currentGame = gameState(True)
	#for i in range(0,3):
	#	oneBoardUpdate(currentGame)
	while(takenPieces.count("wk") == 0 and takenPieces.count('bk') == 0):
		oneBoardUpdate(currentGame)
