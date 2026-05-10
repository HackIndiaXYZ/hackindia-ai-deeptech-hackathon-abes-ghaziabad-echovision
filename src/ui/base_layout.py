import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

            /* ── Animated gradient background ── */
            @keyframes gradientShift {
                0%   { background-position: 0% 50%; }
                50%  { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .stApp {
                background: linear-gradient(135deg, #2D3FBF, #5865F2, #7B4FE8, #4A54D4, #9B59E8) !important;
                background-size: 300% 300% !important;
                animation: gradientShift 10s ease infinite !important;
            }

            /* ── Floating orbs ── */
            @keyframes floatOrb1 {
                0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.45; }
                33%       { transform: translate(40px, -60px) scale(1.1); opacity: 0.6; }
                66%       { transform: translate(-30px, 30px) scale(0.95); opacity: 0.35; }
            }
            @keyframes floatOrb2 {
                0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.3; }
                40%       { transform: translate(-50px, 40px) scale(1.15); opacity: 0.5; }
                70%       { transform: translate(35px, -25px) scale(0.9); opacity: 0.25; }
            }
            @keyframes floatOrb3 {
                0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.25; }
                50%       { transform: translate(60px, 50px) scale(1.2); opacity: 0.45; }
            }

            .ev-orb {
                position: fixed;
                border-radius: 50%;
                filter: blur(60px);
                pointer-events: none;
                z-index: 0;
            }
            .ev-orb-1 {
                width: 420px; height: 420px;
                background: radial-gradient(circle, rgba(255,255,255,0.18) 0%, transparent 70%);
                top: -120px; left: -100px;
                animation: floatOrb1 12s ease-in-out infinite;
            }
            .ev-orb-2 {
                width: 320px; height: 320px;
                background: radial-gradient(circle, rgba(235,69,158,0.25) 0%, transparent 70%);
                bottom: 60px; right: -80px;
                animation: floatOrb2 15s ease-in-out infinite;
            }
            .ev-orb-3 {
                width: 280px; height: 280px;
                background: radial-gradient(circle, rgba(123,79,232,0.3) 0%, transparent 70%);
                top: 40%; left: 55%;
                animation: floatOrb3 18s ease-in-out infinite;
            }

            /* ── Logo pulse ring ── */
            @keyframes logoPulse {
                0%, 100% { box-shadow: 0 0 0 0 rgba(255,255,255,0.35), 0 8px 32px rgba(0,0,0,0.2); }
                50%       { box-shadow: 0 0 0 10px rgba(255,255,255,0.0), 0 8px 32px rgba(0,0,0,0.2); }
            }
            @keyframes logoFloat {
                0%, 100% { transform: translateY(0px); }
                50%       { transform: translateY(-8px); }
            }

            .stApp img[style*="border-radius:50%"] {
                animation: logoPulse 3s ease-in-out infinite, logoFloat 4s ease-in-out infinite !important;
            }

            /* ── Brand name shimmer ── */
            @keyframes shimmer {
                0%   { background-position: -400px 0; }
                100% { background-position: 400px 0; }
            }

            /* ── Cards: lift + glow + border highlight ── */
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] {
                background: rgba(255,255,255,0.10) !important;
                backdrop-filter: blur(24px) !important;
                -webkit-backdrop-filter: blur(24px) !important;
                padding: 2.5rem 2rem !important;
                border-radius: 2rem !important;
                border: 1px solid rgba(255,255,255,0.22) !important;
                box-shadow: 0 8px 32px rgba(21,30,95,0.25), inset 0 1px 0 rgba(255,255,255,0.18) !important;
                text-align: center !important;
                transition: transform 0.35s cubic-bezier(.22,.68,0,1.2),
                            box-shadow 0.35s ease,
                            border-color 0.35s ease,
                            background 0.35s ease !important;
                position: relative !important;
                overflow: hidden !important;
            }

            /* Shimmer sweep on card hover */
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]::before {
                content: '';
                position: absolute;
                top: 0; left: -100%;
                width: 60%; height: 100%;
                background: linear-gradient(120deg, transparent 0%, rgba(255,255,255,0.12) 50%, transparent 100%);
                transition: left 0.6s ease;
                pointer-events: none;
            }
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover::before {
                left: 150%;
            }

            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover {
                transform: translateY(-10px) scale(1.02) !important;
                box-shadow:
                    0 24px 60px rgba(21,30,95,0.4),
                    0 0 40px rgba(255,255,255,0.1),
                    inset 0 1px 0 rgba(255,255,255,0.35) !important;
                border-color: rgba(255,255,255,0.5) !important;
                background: rgba(255,255,255,0.18) !important;
            }

            /* ── Mascot images float animation ── */
            @keyframes mascotFloat {
                0%, 100% { transform: translateY(0px) rotate(-1deg); }
                50%       { transform: translateY(-10px) rotate(1deg); }
            }
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] img {
                margin: 0.5rem auto 1rem auto !important;
                filter: drop-shadow(0 8px 24px rgba(0,0,0,0.25)) !important;
                animation: mascotFloat 4s ease-in-out infinite !important;
                transition: filter 0.3s ease !important;
            }
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:hover img {
                filter: drop-shadow(0 14px 32px rgba(0,0,0,0.35)) !important;
            }
            /* Stagger the two mascots */
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child(2) img {
                animation-delay: -2s !important;
            }

            /* ── Card headings & text ── */
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] h3 {
                color: #ffffff !important;
                font-weight: 800 !important;
                font-size: 1.6rem !important;
                margin-bottom: 0.5rem !important;
                letter-spacing: 0.02em !important;
            }
            .stApp div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] p {
                color: rgba(255,255,255,0.75) !important;
                font-size: 0.95rem !important;
            }

            /* ── "Who are you today?" subtle fade-in ── */
            @keyframes fadeSlideDown {
                from { opacity: 0; transform: translateY(-12px); }
                to   { opacity: 1; transform: translateY(0); }
            }
            .stApp .block-container > div:first-child {
                animation: fadeSlideDown 0.7s ease both;
            }

        </style>

        <!-- Floating orbs injected into DOM -->
        <div class="ev-orb ev-orb-1"></div>
        <div class="ev-orb ev-orb-2"></div>
        <div class="ev-orb ev-orb-3"></div>

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(160deg, #E8EAFF 0%, #F0F1FF 60%, #EBE8FF 100%) !important;
                }

                /* Text hierarchy — scoped to exclude button labels so button text colors are not overridden */
                .stApp p:not(button p):not(.stButton p) {
                    color: #3A4280 !important;
                }
                /* Ensure button inner text is never overridden by global p rule */
                .stApp button p,
                .stApp .stButton p,
                .stApp button span {
                    color: inherit !important;
                }

                .stApp label {
                    color: #1A2260 !important;
                    font-weight: 600 !important;
                }

                .stApp h1, .stApp h2, .stApp h3, .stApp h4 {
                    color: #1A2260 !important;
                }

                /* Styled inputs with glass feel */
                .stApp div[data-testid="stCameraInput"] > div,
                .stApp div[data-testid="stFileUploader"] > div,
                .stApp div[data-testid="stAudioInput"] > div {
                    border-radius: 1.2rem !important;
                    border: 1.5px solid rgba(88, 101, 242, 0.22) !important;
                    background: rgba(255, 255, 255, 0.7) !important;
                    backdrop-filter: blur(8px) !important;
                    box-shadow: 0 2px 12px rgba(88,101,242,0.06) !important;
                    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
                }

                .stApp div[data-testid="stCameraInput"] > div:focus-within,
                .stApp div[data-testid="stFileUploader"] > div:focus-within,
                .stApp div[data-testid="stAudioInput"] > div:focus-within {
                    border-color: #5865F2 !important;
                    box-shadow: 0 0 0 3px rgba(88,101,242,0.12) !important;
                }

                .stApp div[data-testid="stTextInput"] > div {
                    border-radius: 0.8rem !important;
                    border: 1.5px solid rgba(88, 101, 242, 0.22) !important;
                    background: rgba(255, 255, 255, 0.85) !important;
                    box-shadow: 0 1px 6px rgba(88,101,242,0.05) !important;
                    transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
                }

                .stApp div[data-testid="stTextInput"] > div:focus-within {
                    border-color: #5865F2 !important;
                    box-shadow: 0 0 0 3px rgba(88,101,242,0.12) !important;
                }

                /* Streamlit container borders */
                .stApp div[data-testid="stVerticalBlockBorderWrapper"] {
                    border-radius: 1.25rem !important;
                    border: 1.5px solid rgba(88, 101, 242, 0.18) !important;
                    background: rgba(255, 255, 255, 0.6) !important;
                    backdrop-filter: blur(12px) !important;
                    box-shadow: 0 4px 24px rgba(88,101,242,0.08) !important;
                }

                /* Selectbox styling */
                .stApp div[data-testid="stSelectbox"] > div {
                    border-radius: 0.8rem !important;
                    border: 1.5px solid rgba(88, 101, 242, 0.22) !important;
                    background: rgba(255, 255, 255, 0.85) !important;
                }

                /* Dataframe/table improvements */
                .stApp div[data-testid="stDataFrame"] {
                    border-radius: 1rem !important;
                    overflow: hidden !important;
                    border: 1px solid rgba(88,101,242,0.15) !important;
                    box-shadow: 0 4px 16px rgba(88,101,242,0.08) !important;
                }

                /* ── Override ALL places Streamlit uses its default #383f7c primary color ──
                   This dark navy appears on: focus rings, radio/checkbox fills, links,
                   slider thumbs, tab indicators, select dropdowns, progress bars, etc. */

                /* Focus outline / ring on any interactive element */
                .stApp *:focus-visible {
                    outline-color: #5865F2 !important;
                    box-shadow: 0 0 0 3px rgba(88,101,242,0.18) !important;
                }

                /* Selectbox – focused border and dropdown arrow color */
                .stApp div[data-testid="stSelectbox"] > div:focus-within,
                .stApp div[data-testid="stSelectbox"] [data-baseweb="select"] > div:first-child {
                    border-color: #5865F2 !important;
                }
                .stApp div[data-testid="stSelectbox"] svg {
                    color: #5865F2 !important;
                    fill: #5865F2 !important;
                }
                /* Selectbox popup / dropdown menu */
                .stApp [data-baseweb="popover"] li[aria-selected="true"],
                .stApp [data-baseweb="menu"] li:hover {
                    background-color: rgba(88,101,242,0.1) !important;
                    color: #5865F2 !important;
                }

                /* Radio buttons */
                .stApp div[data-testid="stRadio"] label span[aria-checked="true"] div,
                .stApp input[type="radio"]:checked {
                    background-color: #5865F2 !important;
                    border-color: #5865F2 !important;
                }

                /* Checkboxes */
                .stApp input[type="checkbox"]:checked,
                .stApp div[data-testid="stCheckbox"] span[aria-checked="true"] {
                    background-color: #5865F2 !important;
                    border-color: #5865F2 !important;
                }

                /* Slider thumb and track */
                .stApp div[data-testid="stSlider"] div[data-baseweb="slider"] div[role="slider"] {
                    background-color: #5865F2 !important;
                    border-color: #5865F2 !important;
                }
                .stApp div[data-testid="stSlider"] div[data-baseweb="slider"] div[data-testid="stTickBar"] > div {
                    background: #5865F2 !important;
                }

                /* Progress / spinner bars */
                .stApp div[data-testid="stProgress"] > div > div > div {
                    background-color: #5865F2 !important;
                }

                /* Links */
                .stApp a {
                    color: #5865F2 !important;
                }
                .stApp a:hover {
                    color: #7B4FE8 !important;
                }

                /* Tabs (native st.tabs if used anywhere) */
                .stApp div[data-testid="stTabs"] button[aria-selected="true"] {
                    color: #5865F2 !important;
                    border-bottom-color: #5865F2 !important;
                }

                /* Text input caret */
                .stApp input, .stApp textarea {
                    caret-color: #5865F2 !important;
                    color: #1A2260 !important;
                }

                /* Multiselect tags */
                .stApp span[data-baseweb="tag"] {
                    background-color: rgba(88,101,242,0.12) !important;
                    color: #5865F2 !important;
                    border: 1px solid rgba(88,101,242,0.25) !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)

    


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top: 1.75rem !important;
                padding-bottom: 2rem !important;
                max-width: 1100px !important;
            }

            /* Custom scrollbar */
            ::-webkit-scrollbar { width: 6px; }
            ::-webkit-scrollbar-track { background: transparent; }
            ::-webkit-scrollbar-thumb { background: rgba(88,101,242,0.3); border-radius: 3px; }
            ::-webkit-scrollbar-thumb:hover { background: rgba(88,101,242,0.55); }

            /* Typography */
            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.05 !important;
                margin-bottom: 0rem !important;
                letter-spacing: -0.5px !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }

            label, div, span {
                font-family: 'Outfit', sans-serif;
            }

            /* Divider refinement */
            hr {
                border-color: rgba(88,101,242,0.15) !important;
                margin: 1.25rem 0 !important;
            }

            /* ─── Buttons ─── */

            /* ── SAFE BASE FALLBACK: primary & secondary get white text + purple gradient ──
               Excludes tertiary which uses its own ghost style with dark text */
            .stApp .stButton > button:not([kind="tertiary"]):not([data-testid="stBaseButton-tertiary"]),
            .stApp button[kind="primary"],
            .stApp button[kind="primaryFormSubmit"],
            .stApp button[data-testid="stBaseButton-primary"],
            .stApp button[data-testid="stBaseButton-primaryFormSubmit"] {
                border-radius: 2rem !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                letter-spacing: 0.01em !important;
                color: white !important;
                background: linear-gradient(135deg, #5865F2, #7B4FE8) !important;
                border: none !important;
                padding: 10px 22px !important;
                box-shadow: 0 4px 14px rgba(88,101,242,0.3) !important;
                transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease !important;
            }

            /* All buttons share these base traits */
            .stApp button[kind],
            .stApp button[data-testid^="stBaseButton"] {
                border-radius: 2rem !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                letter-spacing: 0.01em !important;
                padding: 10px 22px !important;
                transition: transform 0.22s ease, box-shadow 0.22s ease, background 0.22s ease !important;
            }

            /* ── Primary ── */
            .stApp button[kind="primary"],
            .stApp button[kind="primaryFormSubmit"],
            .stApp button[data-testid="stBaseButton-primary"],
            .stApp button[data-testid="stBaseButton-primaryFormSubmit"] {
                background: linear-gradient(135deg, #5865F2, #7B4FE8) !important;
                color: white !important;
                box-shadow: 0 4px 14px rgba(88,101,242,0.35) !important;
            }
            .stApp button[kind="primary"]:hover,
            .stApp button[kind="primaryFormSubmit"]:hover,
            .stApp button[data-testid="stBaseButton-primary"]:hover,
            .stApp button[data-testid="stBaseButton-primaryFormSubmit"]:hover {
                transform: translateY(-2px) scale(1.03) !important;
                box-shadow: 0 8px 22px rgba(88,101,242,0.45) !important;
            }

            /* ── Secondary (pink) ── */
            .stApp button[kind="secondary"],
            .stApp button[data-testid="stBaseButton-secondary"] {
                background: linear-gradient(135deg, #EB459E, #C9368A) !important;
                color: white !important;
                box-shadow: 0 4px 14px rgba(235,69,158,0.3) !important;
            }
            .stApp button[kind="secondary"]:hover,
            .stApp button[data-testid="stBaseButton-secondary"]:hover {
                transform: translateY(-2px) scale(1.03) !important;
                box-shadow: 0 8px 22px rgba(235,69,158,0.42) !important;
            }

            /* ── Tertiary (ghost / outline — dark text, always readable) ── */
            .stApp button[kind="tertiary"],
            .stApp button[data-testid="stBaseButton-tertiary"] {
                background: rgba(255, 255, 255, 0.55) !important;
                color: #1A2260 !important;
                border: 1.5px solid rgba(88, 101, 242, 0.3) !important;
                box-shadow: 0 1px 4px rgba(88,101,242,0.08) !important;
                backdrop-filter: blur(8px) !important;
            }
            /* Target the inner p/span that Streamlit wraps button labels in */
            .stApp button[kind="tertiary"] p,
            .stApp button[kind="tertiary"] span,
            .stApp button[data-testid="stBaseButton-tertiary"] p,
            .stApp button[data-testid="stBaseButton-tertiary"] span {
                color: #1A2260 !important;
            }
            .stApp button[kind="tertiary"]:hover,
            .stApp button[data-testid="stBaseButton-tertiary"]:hover {
                transform: translateY(-2px) scale(1.03) !important;
                background: rgba(88, 101, 242, 0.1) !important;
                border-color: rgba(88, 101, 242, 0.5) !important;
                color: #5865F2 !important;
                box-shadow: 0 4px 14px rgba(88,101,242,0.15) !important;
            }
            .stApp button[kind="tertiary"]:hover p,
            .stApp button[kind="tertiary"]:hover span,
            .stApp button[data-testid="stBaseButton-tertiary"]:hover p,
            .stApp button[data-testid="stBaseButton-tertiary"]:hover span {
                color: #5865F2 !important;
            }
            /* Also explicitly reinforce white text inside primary/secondary buttons
               in case the global p rule ever bleeds through */
            .stApp button[kind="primary"] p,
            .stApp button[kind="primary"] span,
            .stApp button[kind="secondary"] p,
            .stApp button[kind="secondary"] span,
            .stApp button[data-testid="stBaseButton-primary"] p,
            .stApp button[data-testid="stBaseButton-primary"] span,
            .stApp button[data-testid="stBaseButton-secondary"] p,
            .stApp button[data-testid="stBaseButton-secondary"] span {
                color: white !important;
            }

            /* ── Disabled ── */
            .stApp button:disabled {
                opacity: 0.45 !important;
                transform: none !important;
                cursor: not-allowed !important;
            }

            /* ─── Tab Navigation Rail ─── */
            .sc-tab-rail {
                background: rgba(255,255,255,0.5);
                backdrop-filter: blur(12px);
                border-radius: 2rem;
                padding: 6px;
                border: 1px solid rgba(88,101,242,0.15);
                box-shadow: 0 2px 12px rgba(88,101,242,0.08);
                display: flex;
                gap: 6px;
                margin-bottom: 1.25rem;
            }

            /* ─── Empty State ─── */
            .sc-empty-state {
                text-align: center;
                padding: 3rem 2rem;
                background: rgba(255,255,255,0.55);
                backdrop-filter: blur(12px);
                border-radius: 1.5rem;
                border: 1.5px dashed rgba(88,101,242,0.25);
                margin: 1rem 0;
            }

            .sc-empty-state .sc-empty-icon {
                font-size: 3rem;
                margin-bottom: 0.75rem;
            }

            .sc-empty-state h4 {
                color: #1A2260 !important;
                font-size: 1.2rem !important;
                font-weight: 700 !important;
                margin: 0 0 0.4rem 0 !important;
            }

            .sc-empty-state p {
                color: #6B73B0 !important;
                font-size: 0.95rem !important;
                margin: 0 !important;
            }

            /* ─── Section Headings ─── */
            .sc-section-header {
                display: flex;
                align-items: center;
                gap: 10px;
                margin-bottom: 1rem;
            }

            .sc-section-header .sc-section-pill {
                width: 5px;
                height: 28px;
                border-radius: 3px;
                background: linear-gradient(180deg, #5865F2, #EB459E);
                flex-shrink: 0;
            }

            /* ─── Info / Warning / Error Banner Overrides ─── */
            .stAlert {
                border-radius: 1rem !important;
                border: none !important;
            }

            /* ─── Toast improvements ─── */
            div[data-testid="stToast"] {
                border-radius: 1rem !important;
                box-shadow: 0 8px 24px rgba(0,0,0,0.15) !important;
            }

            /* ─── Spinner ─── */
            div[data-testid="stSpinner"] {
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                color: #5865F2 !important;
            }

            /* ─── Hide Streamlit image fullscreen expand button ─── */
            button[title="View fullscreen"],
            div[data-testid="stImage"] button,
            div[data-testid="stImageContainer"] button {
                display: none !important;
            }

        </style>  

                """
            ,unsafe_allow_html=True)