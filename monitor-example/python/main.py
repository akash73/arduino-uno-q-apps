from arduino.app_bricks.mood_detector import MoodDetector

mood = MoodDetector()

print(mood.get_sentiment("This is a wonderful and amazing product!"))  # positive
print(mood.get_sentiment("I am feeling very sad and disappointed today."))  # negative
print(mood.get_sentiment("The report will be ready by 5 PM."))  # neutral

# Edge cases
print(mood.get_sentiment(""))                 # neutral (empty input)
print(mood.get_sentiment("Questo è bello"))   # neutral (non-English)