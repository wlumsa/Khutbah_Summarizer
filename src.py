from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'liJVSwOiiwg'
transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])


print(transcript)


