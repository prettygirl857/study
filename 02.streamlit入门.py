import streamlit as st
from contextlib import nullcontext
from html import escape
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent


def columns(spec):
    """Return Streamlit columns, compatible with older Streamlit versions."""
    if hasattr(st, "columns"):
        return st.columns(spec)
    if hasattr(st, "beta_columns"):
        return st.beta_columns(spec)
    count = spec if isinstance(spec, int) else len(spec)
    return [nullcontext() for _ in range(count)]


def image(path, caption=None, **kwargs):
    """Show an image with both new and old Streamlit image arguments."""
    try:
        st.image(str(path), caption=caption, use_container_width=True)
    except TypeError:
        st.image(str(path), caption=caption, use_column_width=True)


def metric(label, value, delta=None):
    """Fallback for Streamlit versions before st.metric."""
    if hasattr(st, "metric"):
        st.metric(label, value, delta=delta)
        return
    st.markdown(
        f"""
        <div style="background:linear-gradient(135deg,#fff9f0,#fff5f5); border:1px solid #f0e0d0;
        border-radius:14px; padding:1rem; text-align:center; min-height:120px;">
            <div style="color:#8B7355;font-size:0.9rem;">{label}</div>
            <div style="color:#CD5C5C;font-size:1.8rem;font-weight:800;margin-top:0.4rem;">{value}</div>
            <div style="color:#999;font-size:0.8rem;margin-top:0.3rem;">{delta or ""}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )




def dataframe(data, **kwargs):
    """Render a small table without depending on old Streamlit dataframe internals."""
    if isinstance(data, dict) and data:
        headers = list(data.keys())
        rows = zip(*[data[key] for key in headers])
        head_html = "".join(f"<th>{escape(str(header))}</th>" for header in headers)
        body_html = "".join(
            "<tr>" + "".join(f"<td>{escape(str(cell))}</td>" for cell in row) + "</tr>"
            for row in rows
        )
        st.markdown(
            f"""
            <table style="width:100%; border-collapse:collapse; font-size:0.95rem;">
                <thead><tr style="background:#fff5f5; color:#5D3A1A;">{head_html}</tr></thead>
                <tbody>{body_html}</tbody>
            </table>
            <style>
                table th, table td {{ border:1px solid #f0e0d0; padding:0.55rem 0.7rem; text-align:left; }}
                table tbody tr:nth-child(even) {{ background:#fffaf5; }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.text(str(data))
def divider():
    if hasattr(st, "divider"):
        st.divider()
    else:
        st.markdown("---")


def tabs(labels):
    """Use tabs when available; otherwise show sections in expanders."""
    if hasattr(st, "tabs"):
        return st.tabs(labels)
    expander = getattr(st, "expander", None) or getattr(st, "beta_expander", None)
    if expander:
        return [expander(label, expanded=(idx == 0)) for idx, label in enumerate(labels)]
    return [nullcontext() for _ in labels]

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="🏛️ 武汉大学 · 珞珈山下",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==================== 自定义 CSS ====================
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* ===== 英雄区 ===== */
    .hero {
        text-align: center;
        padding: 3rem 2rem 2rem 2rem;
        background: linear-gradient(180deg, #fef9f0 0%, #fff5f5 40%, #ffffff 100%);
        border-radius: 0 0 60px 60px;
        margin-bottom: 2rem;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #8B4513 0%, #CD5C5C 30%, #FFB6C1 70%, #8B4513 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.3rem;
        color: #8B7355;
        letter-spacing: 0.3em;
        margin-bottom: 0.5rem;
    }
    .hero-motto {
        font-size: 1.8rem;
        font-weight: 700;
        color: #CD5C5C;
        letter-spacing: 0.2em;
        margin-top: 1rem;
        font-style: italic;
    }
    .hero-line {
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, #FFB6C1, #CD5C5C);
        margin: 1rem auto;
        border-radius: 2px;
    }

    /* ===== 章节标题 ===== */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #5D3A1A;
        border-left: 6px solid #CD5C5C;
        padding-left: 1.2rem;
        margin: 2.5rem 0 1.5rem 0;
    }
    .section-subtitle {
        font-size: 1.3rem;
        font-weight: 600;
        color: #8B4513;
        margin: 1.5rem 0 0.8rem 0;
    }

    /* ===== 卡片 ===== */
    .info-card {
        background: linear-gradient(135deg, #fff9f0, #fff5f5);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid #f0e0d0;
        height: 100%;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .info-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 40px rgba(139, 69, 19, 0.12);
    }
    .info-card h3 {
        font-size: 1.4rem;
        color: #8B4513;
        margin-bottom: 1rem;
    }
    .info-card p {
        color: #666;
        line-height: 1.8;
        font-size: 1rem;
    }

    /* ===== 数据数字 ===== */
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        color: #CD5C5C;
        line-height: 1;
    }
    .stat-label {
        font-size: 0.95rem;
        color: #999;
        margin-top: 0.3rem;
    }

    /* ===== 名言引用 ===== */
    .quote-box {
        background: linear-gradient(135deg, #fff5f5, #fef9f0);
        border-left: 4px solid #CD5C5C;
        padding: 2rem 2.5rem;
        margin: 2rem 0;
        border-radius: 0 16px 16px 0;
    }
    .quote-text {
        font-size: 1.15rem;
        color: #5D3A1A;
        line-height: 2;
        font-style: italic;
    }
    .quote-author {
        text-align: right;
        color: #999;
        margin-top: 1rem;
        font-size: 0.9rem;
    }

    /* ===== 时间线 ===== */
    .timeline-item {
        padding: 1rem 0 1rem 2rem;
        border-left: 2px solid #f0d0c0;
        margin-left: 1rem;
        position: relative;
    }
    .timeline-item::before {
        content: "◆";
        position: absolute;
        left: -9px;
        top: 1.2rem;
        color: #CD5C5C;
        font-size: 0.9rem;
    }
    .timeline-year {
        font-weight: 700;
        color: #8B4513;
        font-size: 1.1rem;
    }
    .timeline-desc {
        color: #666;
        margin-top: 0.3rem;
        line-height: 1.6;
    }

    /* ===== 樱花色强调文字 ===== */
    .highlight {
        background: linear-gradient(180deg, transparent 60%, #FFB6C166 60%);
        padding: 0 4px;
    }

    /* ===== 建筑卡片 ===== */
    .building-name {
        text-align: center;
        font-weight: 700;
        color: #8B4513;
        font-size: 1.1rem;
        margin-top: 0.8rem;
    }
    .building-desc {
        text-align: center;
        color: #999;
        font-size: 0.85rem;
        margin-top: 0.3rem;
    }

    /* ===== 页脚 ===== */
    .footer-custom {
        text-align: center;
        padding: 3rem 0 1.5rem 0;
        color: #bbb;
        font-size: 0.85rem;
        border-top: 1px solid #f5e8e0;
        margin-top: 3rem;
    }

    /* ===== 图片容器 ===== */
    .img-caption {
        text-align: center;
        color: #aaa;
        font-size: 0.8rem;
        margin-top: 0.5rem;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# ==================== 图片资源（本地 photo resources 目录）====================
IMG_DIR = APP_DIR / "photo resources"
IMG_GATE = f"{IMG_DIR}/01_wuhan_university_gate.jpg"
IMG_PAIFANG = f"{IMG_DIR}/02_wuhan_university_paifang_2024.jpg"
IMG_OLD_LIBRARY_FRONT = f"{IMG_DIR}/03_old_library_front_view.jpg"
IMG_OLD_LIBRARY = f"{IMG_DIR}/04_wuhan_university_old_library.jpg"
IMG_NEW_LIBRARY = f"{IMG_DIR}/05_new_library_01.jpg"
IMG_ADMIN = f"{IMG_DIR}/06_administrative_building.jpg"
IMG_SCIENCE = f"{IMG_DIR}/07_old_school_of_science.jpg"
IMG_SAKURA_AREA = f"{IMG_DIR}/08_sakura_area.jpg"
IMG_CHERRY_AVENUE = f"{IMG_DIR}/09_cherry_blossom_avenue_20240321.jpg"
IMG_LUOJIA = f"{IMG_DIR}/10_luojia_shan_panorama.jpg"

# ==================== 英雄区（Hero Section）====================
st.markdown("""
<div class="hero">
    <p class="hero-subtitle">🏛️ 中国 · 武汉 · 珞珈山</p>
    <h1 class="hero-title">武汉大学</h1>
    <div class="hero-line"></div>
    <p class="hero-subtitle">Wuhan University · 1893</p>
    <p class="hero-motto">自强 &nbsp; 弘毅 &nbsp; 求是 &nbsp; 拓新</p>
</div>
""", unsafe_allow_html=True)

# ==================== 学校概况 ====================
st.markdown('<p class="section-title">📖 学校概况</p>', unsafe_allow_html=True)

col1, col2 = columns([3, 2])

with col1:
    st.markdown("""
    <div class="info-card">
        <p style="font-size:1.1rem; line-height:2; color:#444;">
        武汉大学坐落于<span class="highlight">湖北省武汉市</span>，是中华人民共和国教育部直属的
        综合性<span class="highlight">全国重点大学</span>。学校溯源于1893年清末湖广总督张之洞奏请清政府
        创办的<span class="highlight">自强学堂</span>，历经传承演变，1928年定名为国立武汉大学，
        是近代中国第一批国立大学。
        </p>
        <p style="font-size:1.1rem; line-height:2; color:#444; margin-top:1rem;">
        学校坐拥<span class="highlight">珞珈山</span>，环绕<span class="highlight">东湖水</span>，
        占地面积5195亩，建筑面积295万平方米。校园内中西合璧的宫殿式早期建筑群古朴典雅、巍峨壮观，
        被誉为<span class="highlight">"中国最美丽的大学"</span>。
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    image(IMG_GATE, caption="国立武汉大学牌坊", use_container_width=True)

# ==================== 核心数据指标 ====================
st.markdown("")
c1, c2, c3, c4, c5 = columns(5)
with c1:
    metric("📅 建校年份", "1893 年", delta="130+ 年历史")
with c2:
    metric("🎓 在校学生", "58,000+", delta="含本硕博留学生")
with c3:
    metric("🏫 学院设置", "6 大学部", delta="34 个学院")
with c4:
    metric("📚 图书馆藏", "700 万+", delta="册")
with c5:
    metric("🌳 校园面积", "5,195 亩", delta="珞珈山+东湖")

divider()

# ==================== 历史沿革 ====================
st.markdown('<p class="section-title">📜 历史沿革</p>', unsafe_allow_html=True)

col_hist, col_img = columns([3, 2])

with col_hist:
    st.markdown("""
    <div class="timeline-item">
        <span class="timeline-year">1893 年</span>
        <div class="timeline-desc">湖广总督<span class="highlight">张之洞</span>奏请创办<strong>自强学堂</strong>，设方言、算学、格致、商务四门</div>
    </div>
    <div class="timeline-item">
        <span class="timeline-year">1913 年</span>
        <div class="timeline-desc">国民政府决定成立<strong>国立武昌高等师范学校</strong></div>
    </div>
    <div class="timeline-item">
        <span class="timeline-year">1928 年</span>
        <div class="timeline-desc">正式定名为<strong>国立武汉大学</strong>，开始在珞珈山兴建新校舍</div>
    </div>
    <div class="timeline-item">
        <span class="timeline-year">1932 年</span>
        <div class="timeline-desc">珞珈山新校舍落成，<strong>老图书馆、老斋舍</strong>等标志性建筑建成</div>
    </div>
    <div class="timeline-item">
        <span class="timeline-year">1946 年</span>
        <div class="timeline-desc">抗战胜利后复校，设<strong>文、法、理、工、农、医</strong>六大学院</div>
    </div>
    <div class="timeline-item">
        <span class="timeline-year">2000 年</span>
        <div class="timeline-desc">与武汉水利电力大学、武汉测绘科技大学、湖北医科大学<strong>合并</strong>，组建新的武汉大学</div>
    </div>
    <div class="timeline-item">
        <span class="timeline-year">2022 年</span>
        <div class="timeline-desc">入选国家<strong>"双一流"建设高校</strong>A类名单，11个学科入选</div>
    </div>
    """, unsafe_allow_html=True)

with col_img:
    image(IMG_OLD_LIBRARY, caption="武汉大学老图书馆（校史馆）", use_container_width=True)
    image(IMG_ADMIN, caption="国立武汉大学行政楼", use_container_width=True)

# ==================== 标志性建筑 ====================
st.markdown('<p class="section-title">🏛️ 珞珈地标</p>', unsafe_allow_html=True)

buildings = columns(4)

with buildings[0]:
    image(IMG_OLD_LIBRARY, use_container_width=True)
    st.markdown('<p class="building-name">老图书馆</p>', unsafe_allow_html=True)
    st.markdown('<p class="building-desc">1935年建成 · 皇冠形仿故宫建筑<br>珞珈山制高点 · 现为校史馆</p>', unsafe_allow_html=True)

with buildings[1]:
    image(IMG_PAIFANG, use_container_width=True)
    st.markdown('<p class="building-name">牌坊</p>', unsafe_allow_html=True)
    st.markdown('<p class="building-desc">四柱三间歇山式<br>正面"国立武汉大学"<br>背面"文法理工农医"</p>', unsafe_allow_html=True)

with buildings[2]:
    image(IMG_ADMIN, use_container_width=True)
    st.markdown('<p class="building-name">行政楼</p>', unsafe_allow_html=True)
    st.markdown('<p class="building-desc">原工学院大楼<br>中西合璧宫殿式建筑<br>珞珈山南麓</p>', unsafe_allow_html=True)

with buildings[3]:
    image(IMG_SCIENCE, use_container_width=True)
    st.markdown('<p class="building-name">老理学院</p>', unsafe_allow_html=True)
    st.markdown('<p class="building-desc">1930年建成 · 拜占庭风格<br>穹顶礼堂 · 中西合璧典范<br>珞珈山早期建筑群</p>', unsafe_allow_html=True)

# ==================== 樱花季 ====================
st.markdown('<p class="section-title">🌸 樱花季 · 珞珈春日</p>', unsafe_allow_html=True)

col_cherry_l, col_cherry_r = columns([2, 3])

with col_cherry_l:
    image(IMG_CHERRY_AVENUE, caption="樱花大道 · 2024年3月", use_container_width=True)

with col_cherry_r:
    st.markdown("""
    <div class="info-card">
        <h3>🌸 关于武大樱花</h3>
        <p>
        武汉大学的<span class="highlight">樱花大道</span>位于老斋舍和老图书馆下方，
        是校园内最著名的景观之一。每年<span class="highlight">三月中下旬</span>，
        3000余株樱花竞相绽放，花期约<span class="highlight">15-20天</span>。
        </p>
        <p>
        樱花与古朴的建筑交相辉映，形成了"<span class="highlight">樱顶赏樱</span>"的独特意境。
        每年樱花季吸引数十万游客前来观赏，被誉为
        "<span class="highlight">中国最美樱花校园</span>"。
        </p>
        <p style="color:#999; font-size:0.9rem;">
        📌 赏樱提示：每年3月中下旬为最佳观赏期，需提前预约入校。<br>
        📌 最佳机位：樱顶（老斋舍屋顶）、樱花大道、行政楼前。
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== 学科实力 ====================
st.markdown('<p class="section-title">🎓 学科实力</p>', unsafe_allow_html=True)

tab1, tab2, tab3 = tabs(["🏆 双一流学科", "📊 学科评估", "🔬 科研平台"])

with tab1:
    st.markdown('<p class="section-subtitle">11 个学科入选国家"双一流"建设名单</p>', unsafe_allow_html=True)
    subjects = columns(4)
    disciplines = [
        ("📐", "测绘科学与技术", "A+ 全国第一"),
        ("📚", "图书情报与档案管理", "A+ 全国第一"),
        ("⚖️", "法学", "A 全国前列"),
        ("🌍", "地球物理学", "A+ 全国第一"),
        ("🧬", "生物学", "A 全国前列"),
        ("💻", "计算机科学与技术", "A- 实力强劲"),
        ("💊", "口腔医学", "B+ 特色鲜明"),
        ("📝", "马克思主义理论", "A+ 全国第一"),
    ]
    for i, (icon, name, rank) in enumerate(disciplines):
        with subjects[i % 4]:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#fff9f0,#fff5f5); border-radius:12px;
            padding:1.2rem; text-align:center; margin-bottom:1rem; border:1px solid #f0e0d0;">
                <div style="font-size:2rem;">{icon}</div>
                <div style="font-weight:700;color:#5D3A1A;margin-top:0.5rem;">{name}</div>
                <div style="color:#CD5C5C;font-size:0.85rem;margin-top:0.3rem;">{rank}</div>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    col_a, col_b = columns(2)
    with col_a:
        st.markdown("**第四轮学科评估 A 类学科（19个）**")
        dataframe(
            {"评级": ["A+", "A+", "A+", "A+", "A", "A", "A", "A", "A-", "A-"],
             "学科": ["测绘", "图情档", "地球物理", "马克思", "法学", "生物学", "水利工程", "公共管理", "哲学", "理论经济学"]},
            use_container_width=True, hide_index=True
        )
    with col_b:
        st.markdown("**ESI 全球前 1‰ 学科（8个）**")
        st.markdown("""
        - 🔬 **化学** · Chemistry
        - 🧬 **材料科学** · Materials Science
        - 🏥 **临床医学** · Clinical Medicine
        - 🌿 **工程科学** · Engineering
        - 🌾 **环境/生态学** · Environment/Ecology
        - 💻 **计算机科学** · Computer Science
        - 🌍 **地球科学** · Geosciences
        - 🧪 **药理学与毒理学** · Pharmacology
        """)

with tab3:
    st.markdown("""
    | 级别 | 平台名称 |
    |------|---------|
    | 🔴 国家级 | 测绘遥感信息工程国家重点实验室 |
    | 🔴 国家级 | 水资源工程与调度全国重点实验室 |
    | 🔴 国家级 | 病毒学国家重点实验室 |
    | 🔴 国家级 | 杂交水稻全国重点实验室（共建） |
    | 🟡 省部级 | 教育部重点实验室 10 个 |
    | 🟡 省部级 | 教育部人文社科重点研究基地 7 个 |
    """)

# ==================== 名人名言 ====================
st.markdown('<p class="section-title">💬 珞珈之声</p>', unsafe_allow_html=True)

st.markdown("""
<div class="quote-box">
    <p class="quote-text">
    "珞珈之山，东湖之水，山高水长，流风甚美。"
    </p>
    <p class="quote-author">—— 董必武（中共一大代表，武汉大学校友）</p>
</div>
""", unsafe_allow_html=True)

col_q1, col_q2 = columns(2)
with col_q1:
    st.markdown("""
    <div class="quote-box">
        <p class="quote-text">
        "武汉大学不仅有最美的校园，更有最美的学术传统。"
        </p>
        <p class="quote-author">—— 胡适</p>
    </div>
    """, unsafe_allow_html=True)
with col_q2:
    st.markdown("""
    <div class="quote-box">
        <p class="quote-text">
        "来到武大，方知大学之大，不在大楼，而在大师。"
        </p>
        <p class="quote-author">—— 郭沫若</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== 知名校友 ====================
st.markdown('<p class="section-title">🌟 知名校友</p>', unsafe_allow_html=True)

alumni_cols = columns(5)
alumni = [
    ("🌾", "雷军", "小米科技创始人\n1991届计算机系"),
    ("🔬", "查全性", "中国科学院院士\n电化学领域泰斗"),
    ("✍️", "易中天", "著名学者、作家\n武汉大学历史系"),
    ("⚖️", "韩德培", "中国国际法学一代宗师\n法学院教授"),
    ("🏥", "桂希恩", "艾滋病防治专家\n感动中国年度人物"),
]
for i, (icon, name, desc) in enumerate(alumni):
    with alumni_cols[i]:
        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#fff9f0,#fff5f5); border-radius:16px;
        padding:1.5rem; text-align:center; border:1px solid #f0e0d0;">
            <div style="font-size:2.5rem;">{icon}</div>
            <div style="font-weight:700;color:#5D3A1A;font-size:1.1rem;margin-top:0.5rem;">{name}</div>
            <div style="color:#999;font-size:0.8rem;margin-top:0.5rem;line-height:1.6;">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

# ==================== 校园风光 ====================
st.markdown('<p class="section-title">📷 珞珈印象</p>', unsafe_allow_html=True)

gallery = columns(3)
with gallery[0]:
    image(IMG_SAKURA_AREA, caption="樱花区域 · 春日盛景", use_container_width=True)
with gallery[1]:
    image(IMG_LUOJIA, caption="珞珈山全景", use_container_width=True)
with gallery[2]:
    image(IMG_NEW_LIBRARY, caption="新图书馆 · 现代化学术殿堂", use_container_width=True)

# ==================== 页脚 ====================
st.markdown("""
<div class="footer-custom">
    <p style="font-size:1.2rem;">🌸 自强 &nbsp; 弘毅 &nbsp; 求是 &nbsp; 拓新 🌸</p>
    <p>武汉大学 Wuhan University · Since 1893 · 珞珈山 · 东湖水</p>
    <p style="margin-top:1rem;">图片来自 Wikimedia Commons · 自由版权 · 页面由 Streamlit 构建</p>
</div>
""", unsafe_allow_html=True)
