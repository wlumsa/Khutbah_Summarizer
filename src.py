# https://pypi.org/project/youtube-transcript-api/

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('SUMMARIZER_API_KEY')

# video_link = input('Please Enter Video Link: ')
video_link = 'https://www.youtube.com/watch?v=voQM-aQHQDI&ab_channel=WLUMSA'

stringToList = list(video_link)
s = stringToList[32:43] #grabs id
video_id = ''.join([str(elem) for elem in s])  #converts id to string
print(f"VideoID = {video_id}")

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'], preserve_formatting=True) #gets a list of dictionaries of the transcript

formatter = TextFormatter()
text_formatted = formatter.format_transcript(transcript)


with open("transcript.txt", "w") as file:

    file.write(text_formatted)


#Now that we got the text we need to summarize it 
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key =  api_key
)


completion = client.chat.completions.create(
  model="meta/llama-3.1-8b-instruct",
  messages=[{"role":"user","content":text_formatted}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

summary = ""
for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    summary += chunk.choices[0].delta.content


print("Summary: ", summary)
with open("summary.txt", "w") as file:
   file.write(summary)







