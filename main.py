import streamlit as st


def main():
    st.title("Text Uppercaser")
    st.write("Enter some text and see it transformed to uppercase!")

    # テキスト入力
    user_input = st.text_input("Enter text here:")

    if user_input:
        # 入力されたテキストを大文字に変換
        uppercase_text = user_input.upper()
        st.write("Transformed text:")
        st.text(uppercase_text)


if __name__ == '__main__':
    main()
