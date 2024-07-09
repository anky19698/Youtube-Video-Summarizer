# YouTube Video Summarizer

This Streamlit application allows users to generate a concise summary of YouTube video transcripts using the Gemini Pro API. The application fetches the transcript of a YouTube video, summarizes it, and displays the summary in bullet points.

## Features

- Extracts transcripts from YouTube videos in English and Hindi.
- Utilizes the Gemini Pro API to generate a summary of the transcript.
- Provides a word count of the transcript.
- Displays the first 500 characters of the transcript for preview.
- Handles long transcripts by truncating them to the first 100,000 words.

## Prerequisites

- Python 3.7 or higher
- Streamlit
- `youtube_transcript_api` library
- Gemini Pro API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/youtube-video-summarizer.git
   cd youtube-video-summarizer
