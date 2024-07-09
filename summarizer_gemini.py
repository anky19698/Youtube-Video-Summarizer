from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
import google.generativeai as genai
import base64

# Set up Gemini Pro API key from Streamlit secrets
gemini_pro_key = st.secrets['key']
genai.configure(api_key=gemini_pro_key)

# Define the generative model to use
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to extract video ID from YouTube URL
def extract_video_id(url):
    if "youtu.be" in url:
        return url.split("/")[-1]
    elif "youtube.com" in url:
        return url.split("v=")[-1].split("&")[0]
    else:
        return None

# Function to get the transcript of a YouTube video
def get_transcript(video_id):
    try:
        # Attempt to fetch the transcript in English and Hindi
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en', 'hi'])
        # Join all the text entries from the transcript
        return "\n".join([entry['text'] for entry in transcript])
    except Exception as e:
        # Handle errors gracefully
        st.error(f"Error fetching transcript: {str(e)}")
        return None

# Function to count the number of words in a text
def count_words(text):
    words = text.split()
    return len(words)


# Function to encode image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Custom CSS for background image
page_bg_img = f"""
<style>
.title-icon {{
    display: flex;
    align-items: center;
}}
.title-icon img {{
    width: 50px;  /* Adjust width as needed */
    height: 35px; /* Adjust height as needed */
    margin-right: 10px;
}}
</style>
"""

# Streamlit app title
# st.title("YouTube Video Summarizer")

# YouTube icon image URL or Base64
youtube_icon_url = "https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png"

st.markdown(page_bg_img, unsafe_allow_html=True)
# Title with YouTube icon
st.markdown(f"""
<div class="title-icon">
    <img src="{youtube_icon_url}" alt="YouTube Icon">
    <h1> YouTube Video Summarizer</h1>
</div>
""", unsafe_allow_html=True)


# Input field for YouTube video URL
video_url = st.text_input("Enter YouTube Video URL:")

try:
    if video_url:
        video_id = extract_video_id(video_url)
    
        if video_id:
            if st.button("Summarize"):
                with st.spinner("Fetching transcript and generating summary..."):
                    transcript_text = get_transcript(video_id)
    
                    if transcript_text:
                        # Display a subheader and the first 500 characters of the transcript
                        st.markdown("---")
                        st.subheader("Transcript Text")
                        st.text(transcript_text[:500] + "...")
    
                        # Count and display the total number of words in the transcript
                        word_count = count_words(transcript_text)
                        st.text(f"Total Words: {word_count}")
    
                        # Warn the user if the transcript is too long and truncate if necessary
                        if word_count > 100000:
                            st.warning(f"Word Count {word_count} is Huge, We Will Only Use First 20000 Words for Summarization")
                            transcript_text = transcript_text[:100000]
    
                        # Define the prompt for the generative model
                        prompt = f"""
                        You are a Summarizer, Don't Generate any Title Text,
                        Summarize the following YouTube video transcript in Bullet Points:
                        {transcript_text}
                        """
                        # Generate the summary using the generative model
                        summary = model.generate_content(prompt)
    
                        # Display the generated summary
                        st.markdown("---")
                        st.subheader("Summary")
                        st.write(summary.text)
    
                    else:
                        # Display an error message if transcript fetching fails
                        st.error("Failed to fetch transcript. Please check the video URL and try again.")
        else:
            # Display an error message if the YouTube URL is invalid
            st.error("Invalid YouTube URL. Please enter a valid YouTube video URL.")
except:
    st.warning("Please enter a valid YouTube video URL.")
