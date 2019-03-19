letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]



letter_to_points = dict(zip(letters,points))
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for i in word:
    point_total += letter_to_points[i]
  return point_total

player_to_words = {"player1":["BLUE", "TENNIS","EXIT"],"wordNerd":["EARTH","EYES","MACHINE"],"Lexi Con":["ERASER","BELLY","HUSKY"],"Prof Reader":["ZAP","COMA","PERIOD"]}

player_to_points = {}

for keys, values in player_to_words.items():
  player_points = 0
  for i in values:
      print(i)
      player_points+=score_word(i)
print(player_points)
