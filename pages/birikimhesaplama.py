import streamlit as st

st.header(":red[ENFLASYONSUZ BİR YAŞAMIN ACI GERÇEKLERİYLE YÜZLEŞMEYE HAZIR MISINIZ?]")
st.subheader("Enflasyonun olmadığı bir dünyada sabit ev fiyatları ve sabit kira getiri ile yıllar yıllar içerisinde "
             "kaç tane ev alabilirdiniz?")
st.subheader("Aldığınız evlerden kira getiriniz kaç olurdu?")

yasiniz = st.number_input("Yaşın kaç?", step=1)
yasson=st.number_input("Kaç yaşına kadar bu uğurda birikim yapacaksın?",step=1)
maas = st.number_input("Ev almak için her ay ne kadar kenara atabilirsin?", step=1)
evfiyat = st.number_input("Almak istediğin o güzel evin fiyatını gir.")
pesinat=st.number_input("Yüzde kaç peşinat ile evi almak istersin?",step=1)
kira = st.number_input("O güzel evin sana sağlayacağı nefes aldıracak kira getirisini gir.")
evpesinat=evfiyat * (pesinat/100)
evsayisi=0
aylikkredi= (evfiyat-pesinat)/(15*12)
birikim = 0
yasiniz=yasiniz*12
yasson=yasson*12
if st.button("Hesapla"):
    while yasiniz < yasson :
        yasiniz +=1
        birikim = birikim + maas + (kira*evsayisi) - (aylikkredi*evsayisi)
        if birikim >= evpesinat :
            evsayisi += 1
            birikim = (birikim - evpesinat)
    st.subheader(f'Alabileceğin ev sayısı {evsayisi} adettir, çakal seni!. '
                 f'Yatırımın bittiğinde her ay kira gelirin ise {int(evsayisi*kira)} Hadi iyisin!')
