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

2. Install the required packages:

   ```bash
   pip install -r requirements.txt

3. Set up your Gemini Pro API key. Create a .streamlit/secrets.toml file in the root directory with the following content:

   ```bash
   [secrets]
   key = "YOUR_GEMINI_PRO_API_KEY"


## Code Explanation

- **Extract Video ID:** The `extract_video_id` function extracts the video ID from the YouTube URL.
- **Fetch Transcript:** The `get_transcript` function fetches the transcript in English and Hindi using the `youtube_transcript_api`.
- **Word Count:** The `count_words` function counts the number of words in the transcript.
- **Encode Image:** The `get_base64_of_bin_file` function encodes an image to base64 for embedding in the Streamlit app.
- **Custom CSS:** The `page_bg_img` variable contains custom CSS for styling the title with the YouTube icon.
- **Streamlit App:** The Streamlit app allows users to input a YouTube video URL, fetch the transcript, and generate a summary using the Gemini Pro API.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for fetching YouTube video transcripts.
- [Streamlit](https://streamlit.io/) for building the web application framework.
- [Gemini Pro API](https://developers.generativeai.com/) for generating text summaries.
