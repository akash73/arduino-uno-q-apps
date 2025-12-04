from arduino.app_bricks.mood_detector import MoodDetector

mood = MoodDetector()

print(mood.get_sentiment("Ugh, honestly this hamburger was such a disappointment. The bun was already soggy by the time it got to me, like it had been sitting under a heat lamp for half an hour. The patty tasted bland, almost like it hadn’t been seasoned at all, and they drowned everything in some weird watery sauce that just made the whole thing fall apart. I asked for fresh lettuce and tomato and got two paper-thin, wilted leaves and a tomato slice that looked like it gave up on life yesterday. For what they charge, I expected at least something warm and halfway juicy — instead I got a sad pile of mush in a wrapper. Never again."))  # Negative 

print(mood.get_sentiment(" The hamburger was fairly standard. The patty was cooked through and the portion size was appropriate, though the flavor was quite simple and not particularly distinctive. The bun held together, but it became slightly soft due to the sauce. The toppings were fresh enough, although not especially generous. Overall, it’s an acceptable option if you’re looking for a basic burger without special expectations, but nothing about it really stands out.")) # Neutral


print(mood.get_sentiment(" The hamburger was really enjoyable. The patty was juicy and flavorful, with a good balance of seasoning, and the bun was soft but sturdy enough to hold everything together. The toppings were fresh and added a nice crunch, and the sauce complemented the meat without overpowering it. Overall, it’s a satisfying burger that feels well prepared and worth ordering again.")) # Positive