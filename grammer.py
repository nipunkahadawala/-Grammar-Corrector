from textblob import TextBlob

def correct_grammar(input_text):
    """
    Corrects grammar and spelling errors in the given text using TextBlob.
    
    Args:
        input_text (str): The text to be corrected.
    
    Returns:
        str: The corrected text.
    """
    try:
    
        blob = TextBlob(input_text)
        corrected_text = str(blob.correct())
        
        return corrected_text
    except Exception as e:

        print(f"An error occurred while correcting the text: {e}")
        return input_text  



if __name__ == "__main__":

    user_input = input("Enter your sentence: ").strip()
    
    if not user_input:
        print("No input provided. Please enter a valid sentence.")
    else:
        
        corrected_sentence = correct_grammar(user_input)
        
        
        print(f"Original: {user_input}")
        print(f"Corrected: {corrected_sentence}")