import streamlit as st
from PIL import Image

# Streamlit uygulamasını yapılandırma
st.set_page_config(page_title="Resim ve Metin Girişi", layout="wide")

# Resim ve metin alanlarını kullanıcıya gösterme
st.title("Resim ve Metin Girişi")
st.write("Lütfen bir resim seçin ve bir metin girin:")
uploaded_file = st.file_uploader("Bir resim dosyası seçin", type=["jpg", "jpeg", "png"])
text_input = st.text_input("Metin girişi", "")

# Kullanıcıdan alınan değerlere göre işlem yapma
if uploaded_file is not None and text_input != "":
    # Resim dosyasını açma ve görüntüyü gösterme
    image = Image.open(uploaded_file)
    st.image(image, caption="Yüklenen Resim", use_column_width=True)

    # Metin girişini kullanma
    st.write("Girilen Metin:", text_input)

    # İşlem yapma
    # Burada kullanıcıdan alınan resim ve metin değerleri ile istenilen işlem yapılabilir
    # Örneğin, resim üzerine metni eklemek, resmi analiz etmek, resmi dönüştürmek gibi işlemler yapılabilir
    # İşlemlerinizin mantığına göre buraya kod ekleyebilirsiniz.

    st.write("İşlem sonuçları:")
    # İşlem sonuçlarını kullanıcıya gösterme
    # Örneğin, işlem sonucu bir resim ise, st.image() fonksiyonunu kullanarak sonucu gösterebilirsiniz.
    # Diğer sonuçlar ise st.write() veya st.markdown() fonksiyonları ile gösterilebilir.

else:
    st.write("Lütfen bir resim dosyası seçin ve bir metin girin.")
