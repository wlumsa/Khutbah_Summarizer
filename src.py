# https://pypi.org/project/youtube-transcript-api/

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# video_link = input('Please Enter Video Link: ')
video_link = 'https://www.youtube.com/watch?v=liJVSwOiiwg&ab_channel=WebbyFan'

stringToList = list(video_link)
s = stringToList[32:43] #grabs id
video_id = ''.join([str(elem) for elem in s])  #converts id to string
print(f"VideoID = {video_id}")

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

formatter = TextFormatter()
text_formatted = formatter.format_transcript(transcript)
print(text_formatted)



#Now that we got the text we need to summarize it 






