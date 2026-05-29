# app.py
import streamlit as st
from inference_engine import InventoryInferenceEngine
import time

st.set_page_config(
    page_title="AI Supply Chain Expert System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@300;400;500;600;700&display=swap');

    /* ── Base ── */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background-color: #0b1120; }
    .block-container { padding: 2rem 2.5rem 3rem; }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1a2e 0%, #0b1120 100%);
        border-right: 1px solid #1e3050;
    }
    [data-testid="stSidebar"] * { color: #cbd5e8 !important; }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 { color: #ffffff !important; }

    /* ── Hero Banner ── */
    .hero-banner {
        position: relative;
        border-radius: 18px;
        overflow: hidden;
        margin-bottom: 28px;
        min-height: 200px;
        display: flex;
        align-items: stretch;
    }
    .hero-img {
        width: 38%;
        object-fit: cover;
        display: block;
        border-radius: 0;
        flex-shrink: 0;
    }
    .hero-content {
        flex: 1;
        background: linear-gradient(135deg, #0f2d5e 0%, #0b1a3a 100%);
        padding: 36px 40px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-left: 4px solid #f59e0b;
    }
    .hero-eyebrow {
        font-family: 'Space Mono', monospace;
        font-size: 0.68rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #f59e0b;
        margin-bottom: 10px;
    }
    .hero-title {
        font-size: 1.9rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 10px;
    }
    .hero-sub {
        font-size: 0.95rem;
        color: #93afd4;
        line-height: 1.6;
    }
    .hero-badge {
        display: inline-block;
        margin-top: 18px;
        background: rgba(245,158,11,0.15);
        border: 1px solid rgba(245,158,11,0.4);
        color: #fbbf24;
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        padding: 5px 14px;
        border-radius: 20px;
        letter-spacing: 1px;
    }

    /* ── Stat Chips ── */
    .stat-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 14px;
        margin-bottom: 28px;
    }
    .stat-chip {
        background: #0f1e36;
        border: 1px solid #1e3050;
        border-radius: 14px;
        padding: 20px 18px;
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .stat-chip-icon {
        font-size: 1.7rem;
        background: #162848;
        width: 48px; height: 48px;
        display: flex; align-items: center; justify-content: center;
        border-radius: 12px;
        flex-shrink: 0;
    }
    .stat-chip-label {
        font-size: 0.75rem;
        color: #5b7fa6;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        font-weight: 600;
    }
    .stat-chip-value {
        font-family: 'Space Mono', monospace;
        font-size: 0.88rem;
        color: #e2ecf8;
        font-weight: 700;
        margin-top: 3px;
    }

    /* ── Sidebar Section Labels ── */
    .sidebar-section {
        font-family: 'Space Mono', monospace;
        font-size: 0.68rem;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        color: #f59e0b !important;
        border-bottom: 1px solid #1e3050;
        padding-bottom: 7px;
        margin: 22px 0 14px;
    }

    /* ── Execute Button ── */
    .stButton > button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #0b1120;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-family: 'Space Mono', monospace;
        font-weight: 700;
        font-size: 0.92rem;
        letter-spacing: 0.5px;
        transition: opacity 0.2s, transform 0.15s;
        width: 100%;
    }
    .stButton > button:hover { opacity: 0.9; transform: translateY(-1px); }
    .stButton > button:active { transform: translateY(0); }

    /* ── Results Header ── */
    .results-header {
        border-radius: 14px;
        overflow: hidden;
        display: flex;
        align-items: stretch;
        margin-bottom: 24px;
        border: 1px solid #1e3050;
    }
    .results-img {
        width: 35%;
        object-fit: cover;
        display: block;
    }
    .results-content {
        flex: 1;
        background: #0f1e36;
        padding: 28px 32px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        border-left: 4px solid #38bdf8;
    }
    .results-title {
        font-family: 'Space Mono', monospace;
        font-size: 1.3rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 6px;
    }
    .results-sub {
        font-size: 0.88rem;
        color: #5b7fa6;
    }

    /* ── Alert Cards ── */
    .alert-card {
        border-radius: 12px;
        padding: 20px 22px;
        margin: 16px 0;
        border-left: 5px solid;
    }
    .alert-critical { background: rgba(239,68,68,0.12); border-left-color: #ef4444; }
    .alert-high     { background: rgba(245,158,11,0.10); border-left-color: #f59e0b; }
    .alert-ok       { background: rgba(56,189,248,0.08); border-left-color: #38bdf8; }
    .alert-tag {
        font-family: 'Space Mono', monospace;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 1.4px;
        text-transform: uppercase;
        margin-bottom: 8px;
    }
    .alert-critical .alert-tag { color: #f87171; }
    .alert-high .alert-tag     { color: #fbbf24; }
    .alert-ok .alert-tag       { color: #38bdf8; }
    .alert-body {
        font-size: 1rem;
        font-weight: 500;
        color: #e2ecf8;
        line-height: 1.55;
    }

    /* ── Priority Badge ── */
    .priority-badge {
        display: inline-block;
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
        font-weight: 700;
        padding: 5px 16px;
        border-radius: 20px;
        letter-spacing: 1px;
        margin-top: 12px;
    }
    .badge-critical { background: rgba(239,68,68,0.18); color: #f87171; border: 1px solid rgba(239,68,68,0.35); }
    .badge-high     { background: rgba(245,158,11,0.18); color: #fbbf24; border: 1px solid rgba(245,158,11,0.35); }
    .badge-medium   { background: rgba(56,189,248,0.15); color: #38bdf8; border: 1px solid rgba(56,189,248,0.3); }
    .badge-low      { background: rgba(107,115,133,0.18); color: #94a3b8; border: 1px solid rgba(107,115,133,0.3); }
    .badge-routine  { background: rgba(52,211,153,0.12); color: #34d399; border: 1px solid rgba(52,211,153,0.28); }

    /* ── Section Panels ── */
    .panel {
        background: #0f1e36;
        border: 1px solid #1e3050;
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .panel-title {
        font-family: 'Space Mono', monospace;
        font-size: 0.73rem;
        color: #5b7fa6;
        text-transform: uppercase;
        letter-spacing: 1.6px;
        margin-bottom: 18px;
        font-weight: 700;
    }

    /* ── Derived Facts ── */
    .fact-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 11px 0;
        border-bottom: 1px solid #162848;
    }
    .fact-row:last-child { border-bottom: none; }
    .fact-key {
        font-size: 0.85rem;
        color: #7da0c4;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .fact-val {
        font-family: 'Space Mono', monospace;
        font-size: 0.82rem;
        color: #e2ecf8;
        background: rgba(56,189,248,0.1);
        padding: 3px 11px;
        border-radius: 6px;
        border: 1px solid rgba(56,189,248,0.2);
    }

    /* ── Execution Log ── */
    .exec-log {
        background: #07101f;
        border: 1px solid #162848;
        border-radius: 12px;
        padding: 20px;
        font-family: 'Space Mono', monospace;
        font-size: 0.78rem;
        color: #7da0c4;
        line-height: 2;
        overflow-x: auto;
        white-space: pre-wrap;
        word-break: break-word;
    }

    /* ── Expanders ── */
    .streamlit-expanderHeader {
        background: #162848 !important;
        border-radius: 8px !important;
        color: #e2ecf8 !important;
        font-size: 0.85rem !important;
    }

    /* ── Welcome State ── */
    .welcome-box {
        border-radius: 18px;
        overflow: hidden;
        border: 1px solid #1e3050;
        margin-top: 10px;
        display: flex;
        align-items: stretch;
        min-height: 320px;
    }
    .welcome-img {
        width: 40%;
        object-fit: cover;
        display: block;
    }
    .welcome-content {
        flex: 1;
        background: #0f1e36;
        padding: 48px 40px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .welcome-title {
        font-family: 'Space Mono', monospace;
        font-size: 1.25rem;
        color: #ffffff;
        font-weight: 700;
        margin-bottom: 12px;
    }
    .welcome-sub {
        font-size: 0.92rem;
        color: #7da0c4;
        max-width: 400px;
        line-height: 1.75;
        margin-bottom: 28px;
    }
    .welcome-steps {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
    }
    .welcome-step {
        background: #162848;
        border: 1px solid #1e3050;
        border-radius: 10px;
        padding: 14px 18px;
        min-width: 130px;
    }
    .step-num {
        font-family: 'Space Mono', monospace;
        font-size: 1.4rem;
        font-weight: 700;
        color: #f59e0b;
    }
    .step-desc {
        font-size: 0.79rem;
        color: #7da0c4;
        margin-top: 5px;
        line-height: 1.5;
    }

    /* ── Divider & Footer ── */
    hr { border-color: #1e3050; margin: 26px 0; }
    .footer {
        text-align: center;
        padding: 28px 0 10px;
        border-top: 1px solid #1e3050;
        margin-top: 40px;
    }
    .footer-title {
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
        color: #f59e0b;
        letter-spacing: 1.4px;
        text-transform: uppercase;
        margin-bottom: 6px;
    }
    .footer-sub { font-size: 0.77rem; color: #2d4a6b; }

    /* ── Global text overrides ── */
    .stMarkdown p, .stMarkdown li { color: #c8d8ec; }
    .stMarkdown strong { color: #e2ecf8; }
    code { background: #162848 !important; color: #93c5fd !important; }
    </style>
""", unsafe_allow_html=True)


# ── Hero Banner ───────────────────────────────────────────────────────────────
st.markdown("""
    <div class="hero-banner">
        <img class="hero-img"
             src="https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=900&q=80"
             alt="Warehouse operations" />
        <div class="hero-content">
            <div class="hero-eyebrow">Knowledge-Based Expert System</div>
            <div class="hero-title">AI Supply Chain<br>Intelligence Hub</div>
            <div class="hero-sub">Smart inventory replenishment powered by forward-chaining inference over a 75-rule knowledge base with certainty factor reasoning.</div>
            <span class="hero-badge">⚡ LIVE INFERENCE ENGINE</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ── Stat Chips ────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="stat-row">
        <div class="stat-chip">
            <div class="stat-chip-icon">📊</div>
            <div>
                <div class="stat-chip-label">Analytics</div>
                <div class="stat-chip-value">Real-Time</div>
            </div>
        </div>
        <div class="stat-chip">
            <div class="stat-chip-icon">⚙️</div>
            <div>
                <div class="stat-chip-label">Inference</div>
                <div class="stat-chip-value">Forward Chain</div>
            </div>
        </div>
        <div class="stat-chip">
            <div class="stat-chip-icon">📦</div>
            <div>
                <div class="stat-chip-label">Rule Base</div>
                <div class="stat-chip-value">75 Rules</div>
            </div>
        </div>
        <div class="stat-chip">
            <div class="stat-chip-icon">🎯</div>
            <div>
                <div class="stat-chip-label">Output</div>
                <div class="stat-chip-value">Actionable</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
sidebar_tab = st.sidebar

sidebar_tab.markdown("""
    <div style="padding: 16px 4px 10px;">
        <div style="font-family:'Space Mono',monospace; font-size:1rem; font-weight:700; color:#ffffff;">
            ⚙ Configure Parameters
        </div>
        <div style="font-size:0.78rem; color:#5b7fa6; margin-top:5px;">
            Set warehouse & market facts for the inference engine
        </div>
    </div>
""", unsafe_allow_html=True)

sidebar_tab.markdown('<div class="sidebar-section">Stock Levels</div>', unsafe_allow_html=True)
current_stock    = sidebar_tab.slider("Current Stock (units)", 0, 1000, value=45)
safety_stock     = sidebar_tab.slider("Safety Stock Limit", 10, 200, value=50)
storage_capacity = sidebar_tab.slider("Storage Capacity Used (%)", 0, 100, value=42)

sidebar_tab.markdown('<div class="sidebar-section">Sales & Market</div>', unsafe_allow_html=True)
recent_sales = sidebar_tab.number_input("Recent 30-Day Sales (units)", min_value=0, max_value=5000, value=185)
seasonality  = sidebar_tab.selectbox("Market Season", ["Normal Season", "Peak Season", "Off-Season"])
market_trend = sidebar_tab.selectbox("Market Trend", ["Stable", "Trending Up", "Trending Down"])

sidebar_tab.markdown('<div class="sidebar-section">Supply Chain</div>', unsafe_allow_html=True)
supplier_lead_time   = sidebar_tab.number_input("Supplier Lead Time (days)", min_value=1, max_value=90, value=16)
supplier_reliability = sidebar_tab.slider("Supplier Reliability (%)", 0, 100, value=65)
geopolitical         = sidebar_tab.checkbox("Active Transit Disruption", value=False)

sidebar_tab.markdown('<div class="sidebar-section">Perishability & Risk</div>', unsafe_allow_html=True)
is_perishable      = sidebar_tab.checkbox("Perishable Product", value=False)
days_to_expiration = sidebar_tab.number_input("Days Until Expiry", min_value=0, max_value=365, value=30)
holding_cost_rate  = sidebar_tab.selectbox("Holding Cost Rate", ["Low", "Medium", "High"])
is_essential       = sidebar_tab.checkbox("Essential / Core Item", value=True)


# ── Execute Button ────────────────────────────────────────────────────────────
col_l, col_mid, col_r = st.columns([1, 2, 1])
with col_mid:
    execute_button = st.button("▶  Run Inference Engine", type="primary", use_container_width=True)


# ── Results ───────────────────────────────────────────────────────────────────
if execute_button:
    with st.spinner("Running forward chaining inference…"):
        time.sleep(0.3)

        initial_facts = {
            'current_stock':             current_stock,
            'safety_stock_limit':        safety_stock,
            'storage_capacity_utilized': storage_capacity,
            'recent_sales':              recent_sales,
            'seasonality':               seasonality,
            'market_trend':              market_trend,
            'supplier_lead_time':        supplier_lead_time,
            'supplier_reliability':      supplier_reliability,
            'geopolitical_disruption':   geopolitical,
            'is_perishable':             is_perishable,
            'days_to_expiration':        days_to_expiration,
            'holding_cost_rate':         holding_cost_rate,
            'is_essential_item':         is_essential
        }

        engine         = InventoryInferenceEngine()
        final_state    = engine.run_forward_chaining(initial_facts)
        fired_rules    = engine.get_explanation_data()
        execution_logs = engine.get_execution_logs()

    st.success("✅ Inference complete — working memory stabilised.")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Results image + header
    st.markdown("""
        <div class="results-header">
            <img class="results-img"
                 src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80"
                 alt="Analytics dashboard" />
            <div class="results-content">
                <div class="results-title">📊 AI Analysis Results</div>
                <div class="results-sub">Inference engine has processed all input facts and derived the following recommendations.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        recommended_action = final_state.get('action', "No Action Required (Maintain State)")
        priority_urgency   = final_state.get('priority_level', "ROUTINE")

        if priority_urgency == "CRITICAL":
            card_cls = "alert-critical"
            tag_text = "🚨 Critical Action Required"
        elif priority_urgency == "High":
            card_cls = "alert-high"
            tag_text = "⚠️ High Priority Action"
        else:
            card_cls = "alert-ok"
            tag_text = "✅ Recommended Action"

        badge_map = {
            "CRITICAL": "badge-critical",
            "High":     "badge-high",
            "Medium":   "badge-medium",
            "Low":      "badge-low",
        }
        badge_cls = badge_map.get(priority_urgency, "badge-routine")

        st.markdown(f"""
            <div class="panel">
                <div class="panel-title">Primary Recommendation</div>
                <div class="alert-card {card_cls}">
                    <div class="alert-tag">{tag_text}</div>
                    <div class="alert-body">{recommended_action}</div>
                </div>
                <div style="margin-top:14px;">
                    <span style="font-size:0.78rem; color:#5b7fa6; font-weight:500; text-transform:uppercase; letter-spacing:0.6px;">Priority Level &nbsp;</span>
                    <span class="priority-badge {badge_cls}">{priority_urgency}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        fact_data = [
            ("Demand Velocity",   final_state.get('demand_velocity',   '—')),
            ("Anticipated Demand", final_state.get('anticipated_demand', '—')),
            ("Supply Risk",       final_state.get('supply_risk',       '—')),
            ("Stock Status",      final_state.get('stock_status',      '—')),
        ]
        facts_html = "".join(f"""
            <div class="fact-row">
                <span class="fact-key">{label}</span>
                <span class="fact-val">{value}</span>
            </div>
        """ for label, value in fact_data)

        st.markdown(f"""
            <div class="panel">
                <div class="panel-title">Derived Facts Registry</div>
                {facts_html}
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="panel">
                <div class="panel-title">AI Reasoning Trace</div>
            </div>
        """, unsafe_allow_html=True)
        st.caption(f"{len(fired_rules)} rule(s) fired during inference")

        for index, rule in enumerate(fired_rules, start=1):
            with st.expander(f"Rule {index}  ·  [{rule.rule_id}]  ·  {rule.category}"):
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"**Reasoning**\n\n{rule.explanation}")
                with c2:
                    st.markdown(f"**Conclusion**\n\n`{rule.conclusion}`")
                    st.markdown(f"**Certainty Factor:** `{rule.certainty}`")

    # Execution trace
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
        <div style="font-family:'Space Mono',monospace; font-size:0.7rem; text-transform:uppercase;
                    letter-spacing:1.8px; color:#5b7fa6; margin-bottom:12px; font-weight:700;">
            ⏳ Inference Execution Trace
        </div>
    """, unsafe_allow_html=True)

    log_text = "\n".join(execution_logs).replace("<", "&lt;").replace(">", "&gt;")
    st.markdown(f'<div class="exec-log">{log_text}</div>', unsafe_allow_html=True)


# ── Welcome / Idle State ──────────────────────────────────────────────────────
else:
    st.markdown("""
        <div class="welcome-box">
            <img class="welcome-img"
                 src="https://images.unsplash.com/photo-1553413077-190dd305871c?auto=format&fit=crop&w=800&q=80"
                 alt="Warehouse inventory" />
            <div class="welcome-content">
                <div class="welcome-title">📦 Inventory Intelligence Engine</div>
                <div class="welcome-sub">
                    Configure your warehouse and market parameters in the sidebar,
                    then run the inference engine to receive AI-generated replenishment recommendations.
                </div>
                <div class="welcome-steps">
                    <div class="welcome-step">
                        <div class="step-num">01</div>
                        <div class="step-desc">Set parameters<br>in the sidebar</div>
                    </div>
                    <div class="welcome-step">
                        <div class="step-num">02</div>
                        <div class="step-desc">Click<br><strong>Run Inference</strong></div>
                    </div>
                    <div class="welcome-step">
                        <div class="step-num">03</div>
                        <div class="step-desc">Review AI<br>recommendations</div>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="footer">
        <div class="footer-title">AI Supply Chain Expert System</div>
        <div class="footer-sub">Forward Chaining · 75-Rule Knowledge Base · Certainty Factor Reasoning · © 2026</div>
    </div>
""", unsafe_allow_html=True)