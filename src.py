from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# video_link = input('Please Enter Video Link: ')
video_link = 'https://www.youtube.com/watch?v=liJVSwOiiwg&ab_channel=WebbyFan'

stringToList = list(video_link)
s = stringToList[32:43]
listToStr = ''.join([str(elem) for elem in s])
print(f"VideoID = {listToStr}")


video_id = listToStr
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

formatter = TextFormatter()
text_formatted = formatter.format_transcript(transcript)
print(text_formatted)






