import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "order" in user_input:
        return "Your order is being processed. You will receive tracking details soon."

    elif "payment" in user_input:
        return "Payment queries usually involve billing or refunds. Please check your payment method or contact support."

    elif "return" in user_input:
        return "To return your order, please visit the 'Returns' section on our website or contact customer care."

    elif "exit" in user_input:
        return "Thank you for visiting. Goodbye!"

    else:
        return "Sorry, I didn’t understand that. Please ask about 'order', 'payment', or 'return'."

# Streamlit UI
st.title("💬 Customer Support Chatbot")
st.write("Ask me about: **order**, **payment**, or **return**.")

# Keep chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if user_input:
    response = chatbot_response(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")
