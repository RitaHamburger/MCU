import streamlit as st
from PIL import Image

st.markdown('<h1><center>Vũ trụ siêu anh hùng - MCU</center></h1>', unsafe_allow_html=True)
st.markdown('<h2><center>Dòng thời gian và các sự kiện nổi bật</center></h2>', unsafe_allow_html=True)
nam = st.slider('Bạn muốn xem sự kiện của năm nào?', 2008, 2023, step=1)
col_1, col_2 = st.columns(2)
col_3, col_4 = st.columns(2)
col_5, col_6 = st.columns(2)
if nam == 2008:
    with col_1:
        st.markdown('''<p style="text-align: justify">Iron Man: Tony Stark, một tỷ phú thiên tài và nhà sản xuất vũ khí, trở thành Anh hùng Sắt sau khi bị bắt cóc và phát triển bộ giáp siêu năng.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Iron_Man.jfif', width = 300)
    with col_3:
        st.image('picture/Hulk.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">The Incredible Hulk: Bruce Banner trở thành người khổng lồ xanh sau khi bị tác động bởi chất biến đổi và phải đối mặt với quá khứ và truy lùng.</p>''', unsafe_allow_html=True)
elif nam == 2010:
    with col_1:
        st.markdown('''<p style="text-align: justify">Iron Man 2 (2010): Tony Stark đối đầu với Ivan Vanko và suýt mất bộ giáp và công ty của mình.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Iron_Man_1.jfif', width = 300)
elif nam == 2011:
    with col_1:
        st.markdown('''<p style="text-align: justify">Thor (2011): Thor trở thành người trần, mất quyền lực và phải học cách trở thành người tốt để lấy lại Mjolnir của mình.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Thor.jfif', width = 300)
    with col_3:
        st.image('picture/Captain_America.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify"> Captain America: The First Avenger (2011): Steve Rogers trở thành Captain America, người anh hùng mang biểu tượng của Mỹ và chiến đấu chống lại Red Skull trong Thế chiến II.</p>''', unsafe_allow_html=True)
elif nam == 2012:
    with col_3:
        st.image('picture/Avengers.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">The Avengers (2012): Iron Man, Captain America, Thor, Hulk, Black Widow, Hawkeye hợp tác để ngăn chặn Loki và đội quân Chitauri xâm lược Trái Đất.</p>''', unsafe_allow_html=True)
elif nam == 2013:
    with col_1:
        st.markdown('''<p style="text-align: justify">Iron Man 3 (2013): Tony Stark chiến đấu với Mandarin và phải đối mặt với quá khứ cùng sự lo lắng cá nhân.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Iron_Man_2.jfif', width = 300)
    with col_3:
        st.image('picture/Thor_1.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify"> Thor: The Dark World (2013): Thor ngăn chặn Malekith và đối mặt với việc mất mát trong gia đình.</p>''', unsafe_allow_html=True)
elif nam == 2014:
    with col_1:
        st.markdown('''<p style="text-align: justify">Captain America: The Winter Soldier (2014): Captain America phát hiện S.H.I.E.L.D. đã bị xâm phạm và phải đối đầu với Winter Soldier.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Captain_America_1.jfif', width = 300)
    with col_3:
        st.image('picture/Guardians of the Galaxy.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">Guardians of the Galaxy (2014): Peter Quill, Gamora, Rocket, Groot cùng Drax thành lập Guardians of the Galaxy để ngăn chặn Ronan và Thanos.</p>''', unsafe_allow_html=True)
elif nam == 2015:
    with col_1:
        st.markdown('''<p style="text-align: justify">Avengers: Age of Ultron (2015): Avengers tạo ra Ultron nhưng phải đối đầu với sự phản bội và khám phá sức mạnh của Wanda Maximoff.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Avengers.jfif', width = 300)
    with col_3:
        st.image('picture/Ant_Man.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">Ant-Man (2015): Scott Lang trở thành Ant-Man và tham gia cướp một công nghệ nguy hiểm.</p>''', unsafe_allow_html=True)
elif nam == 2016:
    with col_1:
        st.markdown('''<p style="text-align: justify">Captain America: Civil War (2016): Cuộc nội chiến xảy ra giữa các siêu anh hùng khi họ tranh luận về việc quản lý và độc lập.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Captain_America_2.jfif', width = 300)
    with col_3:
        st.image('picture/Doctor_Strange.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">Doctor Strange (2016): Stephen Strange học cách sử dụng ma thuật và trở thành Sorcerer Supreme.</p>''', unsafe_allow_html=True)
elif nam == 2017:
    with col_1:
        st.markdown('''<p style="text-align: justify">Guardians of the Galaxy Vol. 2 (2017): Nhóm Guardians phải đối mặt với những nguy hiểm mới và tìm hiểu về quá khứ của Star-Lord.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Guardians of the Galaxy_1.jfif', width = 300)
    with col_3:
        st.image('picture/Spider_Man.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">Spider-Man: Homecoming (2017): Peter Parker đối mặt với Vulture và học cách trở thành người hùng thực thụ dưới sự hướng dẫn của Tony Stark.</p>''', unsafe_allow_html=True)
    with col_5:
        st.markdown('''<p style="text-align: justify">Thor: Ragnarok (2017): Thor ngăn chặn Ragnarok và đánh bại Hela, chị gái của mình.</p>''', unsafe_allow_html=True)        
    with col_6:  
        st.image('picture/Thor_2.jfif', width = 300)
elif nam == 2018:
    with col_1:
        st.markdown('''<p style="text-align: justify">Black Panther (2018): T'Challa trở thành vị vua tiếp theo của Wakanda và đối mặt với việc bảo vệ ngôi vương và nguồn vibranium của Wakanda khỏi những thế lực đen tối.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Black_Panther.jfif', width = 300)
    with col_3:
        st.image('picture/Avengers_3.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">Avengers: Infinity War (2018): Avengers và đồng minh chiến đấu chống lại Thanos, người muốn sở hữu tất cả các viên Đá Vô Cực để tiêu diệt nửa dân số.</p>''', unsafe_allow_html=True)
    with col_5:
        st.markdown('''<p style="text-align: justify">Ant-Man and The Wasp (2018): Scott Lang và Hope van Dyne hợp tác để tìm kiếm Janet van Dyne nhằm ngăn chặn Ghost.</p>''', unsafe_allow_html=True)        
    with col_6:  
        st.image('picture/Ant_Man_1.jfif', width = 300)
elif nam == 2019:
    with col_1:
        st.markdown('''<p style="text-align: justify">Captain Marvel (2019): Carol Danvers trở lại Trái Đất và phải đối mặt với kẻ thù lâu đời của cô.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Captain_Marvel.jfif', width = 300)
    with col_3:
        st.image('picture/Avengers_4.jfif', width = 300)
    with col_4:
        st.markdown('''<p style="text-align: justify">Avengers: Endgame (2019): Nhóm Avengers còn sống cố gắng đảo ngược tình thế để đánh bại Thanos một lần và mãi mãi.</p>''', unsafe_allow_html=True)
    with col_5:
        st.markdown('''<p style="text-align: justify">Spider-Man: Far From Home (2019): Peter Parker đối mặt với Mysterio rồi dần học cách vượt qua sự mất mát và trách nhiệm.</p>''', unsafe_allow_html=True)        
    with col_6:  
        st.image('picture/Spider_Man_1.jfif', width = 300)
elif nam == 2021:
    with col_1:
        st.markdown('''<p style="text-align: justify">Black Widow (2021): Natasha Romanoff đối mặt với quá khứ của mình và gặp các đồng đội cũ trong cuộc chiến chống lại một thế lực nguy hiểm.</p>''', unsafe_allow_html=True)        
    with col_2:  
        st.image('picture/Black_Widow.jfif', width = 300)
    st.markdown('Hiện tại, MCU vẫn tiếp tục phát triển với nhiều dự án tiếp theo như <b><i>Spider-Man: No Way Home, Thor: Love and Thunder, Doctor Strange in the Multiverse of Madness</b></i> và nhiều hơn nữa. Đây chỉ là một tóm tắt ngắn gọn của MCU, và câu chuyện vẫn đang tiếp tục!', unsafe_allow_html=True)
else:
    st.write('Chúng tôi đang cập nhật các sự kiện!')