import streamlit as st 

def set_custom_style():
    st.markdown("""
        <style>
         # main page
        .stApp {
            background: linear-gradient(135deg,rgb(253, 173, 235) 0%,rgb(78, 110, 135) 100%);
        }
         
        .stTextArea textarea {
            font-size: 16px;
            background-color: white;
            border: 3px solid rgb(28, 3, 3);
            border-radius: 8px;
        }
        
        # button style 
        div.stButton > button {
            background: linear-gradient(135deg,rgb(253, 173, 235) 0%,rgb(78, 110, 135) 100%);
            color: black;
            padding: 8px 16px;
            font-size: 16px;
            border-radius: 6px;
            border : none;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1)
        } 
    
        div.stButton > button:hover {
            background: linear-gradient(135deg,rgb(58, 55, 55) 0%,rgb(251, 255, 245) 100%);
            box-shadow: 0 3px 7px rgba(0,0,0,0.15); 
        }
        #Headimg style
        h1 {
            color: rgb(65, 102, 140);
            text-align: center;
            padding: 20px;
            margin-bottom: 30px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        #Metrics styling
        div[data-testid="stMetricValue"] {
            font-size: 24px;
            color: #2c3e50
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
         div[data-testid="metric-container"] {
            background-color: white;
            padding: 10px;
            border-radius: 10px;
            margin: 10px 0;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
    
        # subheader styling
        .stSubheader {
            color:rgb(14, 64, 113);
            font-weight: 600;
            padding; 10px 0;
        }
        # warning message styling
        .stAlert {
            background-color:#fff3cd;
            coloe- #856404;
            border-radius: 8px;
            border: 1px solid #ffeeba;
        }
         </style>           
    """, unsafe_allow_html=True)
        
def analyze_paragraph(paragraph):
    
    #convert paragraph to string (demonstrating type casting)
    text = str(paragraph).strip()
    
    # basic count using string
    
    letter_count = len(text.replace(" " , ""))
    words = text.split()
    word_count = len(words)
    
    #calculate average word length
    
    avg_word_length = letter_count / word_count if word_count > 0 else 0.0
    
    #count uppercase and lowercase
    
    uppercase_count = sum (1 for char in text if char.isupper())
    lowercase_count = sum(1 for char in text if char.islower())
    
    digit_count =  sum(1 for char in text if char.isdigit())
    space_count =  sum(1 for char in text if char.isspace())
    
    unique_words = len(set(word.lower() for word in words))
    
    sentences = text.count('.') + text.count('!') + text.count('?')
    sentences = max(1, sentences) if text else 0
    
    return {
        'letter_count': letter_count,
        'word_count': word_count,
        'uppercase_count' : uppercase_count,
        'lowercase_count': lowercase_count,
        'digit_count': digit_count,
        'space_count': space_count,
        'unique_words': unique_words,
        'sentence_count': sentences,
    }
    
def main():
    set_custom_style()
    
    st.title("📝 Text Analyzer")
    paragraph = st.text_area(
            "Enter your text for analysis:",
            height=150,
            placeholder="Type or paste your text here..."
        )
    if st.button("🔎 Analyze Text", key="analyze_button"):
            if not paragraph:
                st.warning("Please enter some text to analyze!")
            else:
                results = analyze_paragraph(paragraph)
                
                st.subheader("📉Analysis Result")
                col1, col2 = st.columns(2)
               
            with col1: 
                st.metric("📝Letter Count", results['letter_count'])
                st.metric("🔤words Count", results['word_count'])
                st.metric("⭐Unique Words", results['unique_words'])
                st.metric("🧾Sentence Count", results['sentence_count'])
                
            with col2:
                st.metric("🔠Uppercase Letters", results['uppercase_count'])
                st.metric("🔡Lowercase Letters", results['lowercase_count'])
                st.metric("🎰Digits", results['digit_count'])
                st.metric("Spaces", results['space_count'])
                
            # StopIteration
if __name__ == "__main__":
    main()    