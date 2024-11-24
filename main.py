
import random
import streamlit as st

# Game choices
choices = {"s": "Snake", "w": "Water", "g": "Gun"}

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "s" and computer_choice == "w") or \
         (user_choice == "w" and computer_choice == "g") or \
         (user_choice == "g" and computer_choice == "s"):
        return "You win!"
    else:
        return "You lose!"

# Streamlit app
st.title("Snake-Water-Gun Game")

# User input
st.subheader("Make your move:")
user_choice = st.selectbox("Choose:", ["Snake (s)", "Water (w)", "Gun (g)"])

# Map user input to code
if user_choice:
    user_choice_code = user_choice.split(" ")[1][1]  # Extract 's', 'w', or 'g'

    # Computer's move
    computer_choice_code = random.choice(list(choices.keys()))
    computer_choice = choices[computer_choice_code]

    # Display choices
    st.write(f"**Your choice:** {choices[user_choice_code]}")
    st.write(f"**Computer's choice:** {computer_choice}")

    # Determine winner
    result = determine_winner(user_choice_code, computer_choice_code)
    st.subheader(f"Result: {result}")
