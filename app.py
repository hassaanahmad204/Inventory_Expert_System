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

# Custom CSS Styling for Enhanced Visual Appeal
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    /* Hero section styling */
    .hero-section {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px 0 rgba(30, 64, 175, 0.5);
    }
    
    .hero-title {
        font-size: 2.8em;
        font-weight: 800;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .hero-subtitle {
        font-size: 1.1em;
        opacity: 0.95;
        margin-bottom: 5px;
    }
    
    /* Card styling for sections */
    .info-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #0ea5e9;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin: 15px 0;
        color: #e2e8f0;
    }
    
    .success-card {
        border-left-color: #10b981;
        background-color: #064e3b;
        color: #d1fae5;
    }
    
    .warning-card {
        border-left-color: #f59e0b;
        background-color: #78350f;
        color: #fef3c7;
    }
    
    .critical-card {
        border-left-color: #ef4444;
        background-color: #7f1d1d;
        color: #fee2e2;
    }
    
    /* Sidebar styling - FIXED FOR VISIBILITY */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    }
    
    /* Sidebar text styling */
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] div {
        color: #e2e8f0 !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] h5,
    [data-testid="stSidebar"] h6 {
        color: #0ea5e9 !important;
    }
    
    /* Section headers */
    .section-header {
        color: #0ea5e9;
        font-size: 1.5em;
        font-weight: 700;
        border-bottom: 3px solid #0ea5e9;
        padding-bottom: 10px;
        margin: 20px 0 15px 0;
    }
    
    /* Metric styling */
    .metric-container {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        border: 2px solid #0ea5e9;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
        color: white;
        border: 2px solid #0ea5e9;
        border-radius: 8px;
        padding: 12px 30px;
        font-weight: 600;
        font-size: 1.05em;
        transition: transform 0.2s;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #334155;
        border-radius: 5px;
        color: #0ea5e9 !important;
    }
    
    /* Text color overrides for dark theme */
    body, .stMarkdown {
        color: #e2e8f0 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #94a3b8;
        padding: 20px;
        font-size: 0.9em;
        margin-top: 40px;
        border-top: 2px solid #334155;
    }
    </style>
    """, unsafe_allow_html=True)

# Hero Section with Image and Visual Appeal
col_hero_img, col_hero_text = st.columns([1, 2])
with col_hero_img:
    st.image("https://images.unsplash.com/photo-1553531088-2cc5d0399dcc?w=400&h=300&fit=crop", width=400)

with col_hero_text:
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">🚀 AI Supply Chain Intelligence Hub</div>
            <div class="hero-subtitle">📦 Smart Inventory Replenishment Management System</div>
            <div style="font-size: 0.95em; margin-top: 15px; opacity: 0.9;">
                Advanced Knowledge-Based Expert System | AI-Powered Logistics Optimization
            </div>
        </div>
        """, unsafe_allow_html=True)

# Quick Stats Section
col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
with col_stat1:
    st.markdown("""
        <div class="metric-container">
            <div style="font-size: 2em;">📊</div>
            <div>Real-Time Analytics</div>
        </div>
    """, unsafe_allow_html=True)
with col_stat2:
    st.markdown("""
        <div class="metric-container">
            <div style="font-size: 2em;">🧠</div>
            <div>AI Inference Engine</div>
        </div>
    """, unsafe_allow_html=True)
with col_stat3:
    st.markdown("""
        <div class="metric-container">
            <div style="font-size: 2em;">⚡</div>
            <div>Instant Recommendations</div>
        </div>
    """, unsafe_allow_html=True)
with col_stat4:
    st.markdown("""
        <div class="metric-container">
            <div style="font-size: 2em;">🎯</div>
            <div>Data-Driven Decisions</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Layout Column structures
sidebar_tab = st.sidebar

# Enhanced Sidebar Header
sidebar_tab.markdown("""
    <div style="background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%); 
                color: white; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px; border: 2px solid #0ea5e9;">
        <div style="font-size: 1.5em; font-weight: 700;">📥 Input Warehouse Data</div>
        <div style="font-size: 0.9em; margin-top: 5px; opacity: 0.9;">Configure AI inference parameters</div>
    </div>
    """, unsafe_allow_html=True)

# --- FACT COLLECTION INTERFACE (Knowledge Acquisition Layer) ---
with sidebar_tab.container():
    sidebar_tab.markdown("""
        <div style="background-color: #334155; padding: 12px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #0ea5e9;">
            <span style="font-weight: 700; color: #0ea5e9;">📊 Volumetric Stock Settings</span>
        </div>
        """, unsafe_allow_html=True)
    current_stock = sidebar_tab.slider("📦 Current Physical Stock (Units)", 0, 1000, value=45)
    safety_stock = sidebar_tab.slider("🛡️ Safety Stock Limit (Buffer Threshold)", 10, 200, value=50)
    storage_capacity = sidebar_tab.slider("🏢 Storage Capacity Utilized (%)", 0, 100, value=42)

with sidebar_tab.container():
    sidebar_tab.markdown("""
        <div style="background-color: #334155; padding: 12px; border-radius: 8px; margin: 20px 0 15px 0; border-left: 4px solid #0ea5e9;">
            <span style="font-weight: 700; color: #0ea5e9;">📈 Real-Time Sales Metrics</span>
        </div>
        """, unsafe_allow_html=True)
    recent_sales = sidebar_tab.number_input("💰 Recent 30-Day Unit Sales Volume", min_value=0, max_value=5000, value=185)
    seasonality = sidebar_tab.selectbox("🗓️ Active Market Season Profile", ["Normal Season", "Peak Season", "Off-Season"])
    market_trend = sidebar_tab.selectbox("📉 Algorithmic Market Trend Analysis", ["Stable", "Trending Up", "Trending Down"])

with sidebar_tab.container():
    sidebar_tab.markdown("""
        <div style="background-color: #334155; padding: 12px; border-radius: 8px; margin: 20px 0 15px 0; border-left: 4px solid #0ea5e9;">
            <span style="font-weight: 700; color: #0ea5e9;">🚚 Supply Chain & Lead Times</span>
        </div>
        """, unsafe_allow_html=True)
    supplier_lead_time = sidebar_tab.number_input("⏱️ Supplier Logistics Fulfillment Timeline (Days)", min_value=1, max_value=90, value=16)
    supplier_reliability = sidebar_tab.slider("✅ Supplier Contract Fulfillment Rate (%)", 0, 100, value=65)
    geopolitical = sidebar_tab.checkbox("⚠️ Active Transit Disruption Flag (Customs/Borders)", value=False)

with sidebar_tab.container():
    sidebar_tab.markdown("""
        <div style="background-color: #334155; padding: 12px; border-radius: 8px; margin: 20px 0 15px 0; border-left: 4px solid #0ea5e9;">
            <span style="font-weight: 700; color: #0ea5e9;">🍎 Perishability & Risk Management</span>
        </div>
        """, unsafe_allow_html=True)
    is_perishable = sidebar_tab.checkbox("🥶 Product Belongs to Perishable Class", value=False)
    days_to_expiration = sidebar_tab.number_input("📅 Days Remaining Until Batch Spoilage", min_value=0, max_value=365, value=30)
    holding_cost_rate = sidebar_tab.selectbox("💸 Warehouse Carrying/Holding Cost Overhead", ["Low", "Medium", "High"])
    is_essential = sidebar_tab.checkbox("⭐ Classify Item as Core Revenue Driver", value=True)

# Main Dashboard Execution
col_button_space1, col_button, col_button_space2 = st.columns([1, 2, 1])
with col_button:
    execute_button = st.button("⚡ Execute AI Inference Engine", type="primary", use_container_width=True)
if execute_button:
    with st.spinner("🔄 Running AI Inference Engine..."):
        time.sleep(0.3)
        
        initial_facts = {
            'current_stock': current_stock,
            'safety_stock_limit': safety_stock,
            'storage_capacity_utilized': storage_capacity,
            'recent_sales': recent_sales,
            'seasonality': seasonality,
            'market_trend': market_trend,
            'supplier_lead_time': supplier_lead_time,
            'supplier_reliability': supplier_reliability,
            'geopolitical_disruption': geopolitical,
            'is_perishable': is_perishable,
            'days_to_expiration': days_to_expiration,
            'holding_cost_rate': holding_cost_rate,
            'is_essential_item': is_essential
        }
        
        # Initialize Engine instance and call Forward Chaining logic
        engine = InventoryInferenceEngine()
        final_state = engine.run_forward_chaining(initial_facts)
        fired_rules = engine.get_explanation_data()
        execution_logs = engine.get_execution_logs()
    
    # Success Animation
    st.success("✅ Inference Engine Execution Complete!")
    
    # Results Section Header with Image
    col_result_img, col_result_text = st.columns([1, 2])
    with col_result_img:
        st.image("https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=400&h=300&fit=crop", width=400)
    with col_result_text:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%); 
                        color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 0; border: 2px solid #0ea5e9;">
                <div style="font-size: 1.8em; font-weight: 700;">📊 AI Analysis Results</div>
            </div>
            """, unsafe_allow_html=True)
    
    # UI Layout Distribution for Engine Outputs
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #0ea5e9;">
                <div style="font-size: 1.4em; font-weight: 700; color: #0ea5e9; margin-bottom: 15px;">🎯 Primary Recommendations</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Read final generated replenishment markers
        recommended_action = final_state.get('action', "No Action Required (Maintain State)")
        priority_urgency = final_state.get('priority_level', "ROUTINE")
        
        # Display Alert Status Blocks dynamically based on severity metrics
        if priority_urgency == "CRITICAL":
            st.markdown(f"""
                <div class="info-card critical-card">
                    <div style="color: #ef4444; font-size: 1.1em; font-weight: 700;">🚨 CRITICAL ACTION REQUIRED</div>
                    <div style="color: #dc2626; margin-top: 10px; font-size: 1.05em;">{recommended_action}</div>
                </div>
                """, unsafe_allow_html=True)
        elif priority_urgency == "High":
            st.markdown(f"""
                <div class="info-card warning-card">
                    <div style="color: #f59e0b; font-size: 1.1em; font-weight: 700;">⚠️ HIGH PRIORITY ACTION</div>
                    <div style="color: #d97706; margin-top: 10px; font-size: 1.05em;">{recommended_action}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="info-card success-card">
                    <div style="color: #10b981; font-size: 1.1em; font-weight: 700;">✅ RECOMMENDED ACTION</div>
                    <div style="color: #047857; margin-top: 10px; font-size: 1.05em;">{recommended_action}</div>
                </div>
                """, unsafe_allow_html=True)
        
        # Priority Metric with styling
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%); 
                        color: white; padding: 15px; border-radius: 8px; text-align: center; margin: 15px 0; border: 2px solid #0ea5e9;">
                <div style="font-size: 0.9em; opacity: 0.9;">Urgency Priority Level</div>
                <div style="font-size: 2em; font-weight: 700; margin-top: 5px;">{priority_urgency}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Display Derived Intermediate Facts
        st.markdown("""
            <div style="background-color: #064e3b; padding: 15px; border-radius: 8px; margin-top: 20px; border-left: 5px solid #10b981;">
                <div style="font-weight: 700; color: #86efac; margin-bottom: 12px;">💾 Derived Facts Registry</div>
            </div>
            """, unsafe_allow_html=True)
        
        fact_data = [
            ("Demand Velocity", final_state.get('demand_velocity', 'Unchanged'), "📊"),
            ("Anticipated Demand", final_state.get('anticipated_demand', 'Normal'), "📈"),
            ("Supply Risk", final_state.get('supply_risk', 'Negligible'), "⚠️"),
            ("Stock Status", final_state.get('stock_status', 'Balanced'), "📦")
        ]
        
        for label, value, emoji in fact_data:
            st.markdown(f"<div style='padding: 8px 0; border-bottom: 1px solid #334155; color: #d1fae5;'><strong>{emoji} {label}:</strong> <code style='background: #1e293b; color: #86efac;'>{value}</code></div>", unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 2px solid #0ea5e9;">
                <div style="font-size: 1.4em; font-weight: 700; color: #0ea5e9; margin-bottom: 15px;">🧠 AI Reasoning Trace</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<div style='color: #cbd5e1;'>*The system traced and applied these rules to reach the conclusion:*</div>", unsafe_allow_html=True)
        
        for index, rule in enumerate(fired_rules, start=1):
            with st.expander(f"📋 Rule {index}: [{rule.rule_id}] - {rule.category}"):
                col_exp1, col_exp2 = st.columns([1, 1])
                with col_exp1:
                    st.markdown(f"**📝 Reasoning:** \n{rule.explanation}")
                with col_exp2:
                    st.markdown(f"**✅ Conclusion:** \n`{rule.conclusion}`")
                    st.markdown(f"**🎯 Certainty Factor:** `{rule.certainty}`")

    # --- REASONING VISUALIZATION LOGS (Bonus Marks Feature) ---
    st.markdown("---")
    st.markdown("""
        <div style="background-color: #78350f; padding: 15px; border-radius: 8px; border-left: 5px solid #f59e0b;">
            <div style="font-weight: 700; color: #fef3c7; font-size: 1.1em;">⏳ Inference Execution Trace</div>
            <div style="font-size: 0.9em; margin-top: 5px; color: #fcd34d;">Step-by-step inference engine execution log:</div>
        </div>
        """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("""
            <pre style="background-color: #1e293b; color: #e2e8f0; padding: 15px; border-radius: 8px; 
                       overflow-x: auto; font-size: 0.85em; line-height: 1.6; border: 2px solid #334155;">""" + 
                        "\n".join(execution_logs).replace("<", "&lt;").replace(">", "&gt;") + 
                   """</pre>
            """, unsafe_allow_html=True)
        
else:
    col_welcome_img, col_welcome_text = st.columns([1, 2])
    with col_welcome_img:
        st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=400&h=300&fit=crop", width=400)
    
    with col_welcome_text:
        st.markdown("""
            <div style="background: linear-graIdient(135deg, #1e40af 0%, #1e3a8a 100%); 
                        padding: 30px; border-radius: 12px; text-align: center; color: white; border: 2px solid #0ea5e9;">
                <div style="font-size: 2.5em;">👋</div>
                <div style="font-size: 1.3em; font-weight: 700; margin: 15px 0;">Welcome to AI Inventory Expert System</div>
                <div style="font-size: 1.05em; margin: 10px 0; opacity: 0.95;">
                    📊 <strong>Configure Your Parameters</strong> in the left sidebar
                </div>
                <div style="font-size: 1.05em; margin: 10px 0; opacity: 0.95;">
                    <div style="font-size: 1.05em; margin: 10px 0; opacity: 0.95;">
                    ⚡ <strong>Click Execute</strong> to run the AI inference engine
                </div>
                <div style="font-size: 1.05em; margin: 10px 0; opacity: 0.95;">
                    📈 <strong>Get Recommendations</strong> based on advanced decision logic
                </div>
            </div>
        """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div class="footer">
        <div style="font-size: 0.95em; color: #0ea5e9; font-weight: 600; margin-bottom: 10px;">
            🤖 AI Supply Chain Expert System
        </div>
        <div style="font-size: 0.85em; color: #94a3b8;">
            Powered by Advanced Inference Engine • Real-time Supply Chain Analytics
        </div>
        <div style="font-size: 0.8em; color: #ccc; margin-top: 8px;">
            © 2024 Intelligent Logistics Management Platform
        </div>
    </div>
    """, unsafe_allow_html=True)