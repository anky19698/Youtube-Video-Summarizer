from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import os
import google.generativeai as genai


# Set up gemini pro key
gemini_pro_key = st.secrets['key']
genai.configure(api_key=gemini_pro_key)
model = genai.GenerativeModel('gemini-1.5-flash')


# Function to extract video ID from YouTube URL
def extract_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    else:
        return None

# Function to get transcript
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en', 'hi'])
        return "\n".join([entry['text'] for entry in transcript])
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None

# Function to count words in text
def count_words(text):
    words = text.split()
    return len(words)


# Streamlit app
st.title("YouTube Video Summarizer")

# Input for YouTube video URL
video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    video_id = extract_video_id(video_url)

    if video_id:
        if st.button("Summarize"):
            with st.spinner("Fetching transcript and generating summary..."):
                transcript_text = get_transcript(video_id)

                if transcript_text:
                    st.subheader("Transcript Text")
                    st.text(transcript_text[:300] + "...")  # Display first 1000 characters
                    # word Count
                    word_count = count_words(transcript_text)
                    st.text(f"Total Words: {word_count}")

                    if word_count > 20000:
                        st.warning(f"Word Count {word_count} is Huge, We Will Only Use First 20000 Words for Summarization")
                        transcript_text = transcript_text[:20000]

                    prompt = f"""
                    You are a Summarizer, Dont Generate any Title Text,
                    Summarize the following YouTube video transcript in Bullet Points:
                    {transcript_text}
                    """
                    summary = model.generate_content(prompt)

                    st.subheader("Summary")
                    st.write(summary.text)

                else:
                    st.error("Failed to fetch transcript. Please check the video URL and try again.")
    else:
        st.error("Invalid YouTube URL. Please enter a valid YouTube video URL.")

