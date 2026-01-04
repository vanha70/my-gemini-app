import streamlit as st
import google.generativeai as genai

# Cấu hình trang
st.set_page_config(page_title="My AI App", page_icon="🤖")

st.title("🤖 Ứng dụng AI từ Google Studio")

# Lấy API Key từ hệ thống bảo mật của Streamlit (sẽ làm ở Bước 4)
# LƯU Ý: Không được dán trực tiếp API Key vào đây để tránh lộ thông tin
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Chưa tìm thấy API Key. Vui lòng cấu hình trong Streamlit Secrets.")

# Khởi tạo model (Ví dụ: gemini-1.5-flash hoặc gemini-pro)
model = genai.GenerativeModel('gemini-1.5-flash')

# Giao diện chat đơn giản
user_input = st.text_area("Nhập nội dung bạn muốn hỏi:", height=150)

if st.button("Gửi yêu cầu"):
    if not user_input:
        st.warning("Vui lòng nhập nội dung.")
    else:
        with st.spinner("Đang suy nghĩ..."):
            try:
                response = model.generate_content(user_input)
                st.success("Kết quả:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {e}")