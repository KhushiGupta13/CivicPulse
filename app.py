
from pathlib import Path

import pandas as pd
import streamlit as st

# =========================================================
# CIVICPULSE | DELHI WATERLOGGING ANALYTICS DASHBOARD
# =========================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data" / "processed"

st.set_page_config(
    page_title="CivicPulse | Waterlogging Analytics",
    page_icon="🌧️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROFESSIONAL UI THEME
# =========================================================

st.markdown("""
<style>

/* Main background */

.stApp {
    background: #f3f6fc;
    color: #17243b;
}

.block-container {
    max-width: 1500px;
    padding-top: 1.8rem;
    padding-bottom: 3rem;
}

/* Sidebar */

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #101d35, #183653);
    border-right: 1px solid #263d5d;
}

[data-testid="stSidebar"] * {
    color: #eaf2ff;
}

[data-testid="stSidebar"] label {
    font-size: 14px;
    font-weight: 600;
}

[data-testid="stSidebar"] hr {
    border-color: #354967;
}

/* Headings */

h1 {
    color: #142744 !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #1c3556 !important;
    font-weight: 700 !important;
}

p, li {
    color: #53647d;
}

/* Hero banner */

.hero {
    background: linear-gradient(115deg, #15365c, #087d87);
    border-radius: 22px;
    padding: 34px;
    margin-bottom: 28px;
    box-shadow: 0 10px 30px rgba(20,54,92,0.15);
}

.hero h1 {
    color: white !important;
    font-size: 40px !important;
    margin: 8px 0;
}

.hero p {
    color: #d8f2f2 !important;
    font-size: 15px;
}

/* Native Streamlit hero container */

[data-testid="stVerticalBlockBorderWrapper"]:has(.st-key-civicpulse_hero),
.st-key-civicpulse_hero {
    background: linear-gradient(115deg, #15365c, #087d87);
    border-radius: 22px;
    padding: 28px 34px;
    margin-bottom: 28px;
    box-shadow: 0 10px 30px rgba(20,54,92,0.15);
}

.st-key-civicpulse_hero h1,
.st-key-civicpulse_hero h2,
.st-key-civicpulse_hero p,
.st-key-civicpulse_hero [data-testid="stMarkdownContainer"] {
    color: white !important;
}

.st-key-civicpulse_hero [data-testid="stCaptionContainer"] {
    color: #d8f2f2 !important;
}

.hero-kicker {
    color: #a5eeee;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3px;
}

/* Metric cards */

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e2eaf4;
    border-radius: 17px;
    padding: 20px;
    box-shadow: 0 5px 18px rgba(35,58,91,0.06);
    transition: 0.2s ease;
}

[data-testid="stMetric"]:hover {
    border-color: #5bb8bd;
    box-shadow: 0 8px 22px rgba(35,58,91,0.11);
}

[data-testid="stMetricLabel"] {
    color: #65758d !important;
    font-size: 14px;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #153b60 !important;
    font-size: 29px;
    font-weight: 800;
}

/* Information cards */

.info-card {
    background: white;
    border: 1px solid #e3ebf5;
    border-radius: 17px;
    padding: 23px;
    margin-bottom: 15px;
    min-height: 140px;
    box-shadow: 0 5px 18px rgba(35,58,91,0.05);
    transition: 0.2s ease;
}

.info-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(35,58,91,0.10);
}

.info-card h4 {
    color: #087e8b;
    font-size: 17px;
    margin-top: 0;
}

.info-card p {
    color: #63738a;
    font-size: 14px;
    line-height: 1.7;
}

/* Section labels */

.section-label {
    color: #078b91;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

/* Charts */

[data-testid="stVegaLiteChart"],
[data-testid="stArrowVegaLiteChart"] {
    background: white;
    border: 1px solid #e4ebf4;
    border-radius: 17px;
    padding: 12px;
    box-shadow: 0 5px 18px rgba(35,58,91,0.04);
}


/* Premium KPI cards - native Streamlit containers */

[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #e1eaf3 !important;
    border-radius: 18px !important;
    background: #ffffff !important;
    box-shadow: 0 5px 18px rgba(35,58,91,0.055);
    transition: all 0.2s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #70c6c4 !important;
    box-shadow: 0 9px 24px rgba(35,58,91,0.10);
}

/* KPI text */

[data-testid="stCaptionContainer"] {
    color: #687b92;
    font-size: 13px;
}

/* Main content typography */

[data-testid="stMain"] h2 {
    letter-spacing: -0.4px;
}

[data-testid="stMain"] h3,
[data-testid="stMain"] h4 {
    letter-spacing: -0.2px;
}

/* Navigation radio buttons */

[data-testid="stSidebar"] [role="radiogroup"] {
    gap: 7px;
}

[data-testid="stSidebar"] [role="radiogroup"] label {
    border-radius: 10px;
    padding: 7px 10px;
    transition: background 0.2s ease;
}

/* Better chart spacing */

[data-testid="stVegaLiteChart"] {
    margin-top: 8px;
    margin-bottom: 12px;
}

/* Smooth page appearance */

.block-container {
    padding-left: 2.2rem;
    padding-right: 2.2rem;
}


/* Tables */

[data-testid="stDataFrame"] {
    background: white;
    border: 1px solid #e1e9f3;
    border-radius: 15px;
    overflow: hidden;
}

/* Alerts */

[data-testid="stAlert"] {
    border-radius: 13px;
}

/* Dividers */

hr {
    border-color: #dce6f1 !important;
    margin-top: 25px;
    margin-bottom: 25px;
}

/* Footer */

.footer {
    text-align: center;
    color: #8090a5;
    font-size: 13px;
    padding: 25px 10px;
    line-height: 2;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA LOADING
# =========================================================

@st.cache_data
def load_csv(file_path):

    if file_path.exists():
        return pd.read_csv(file_path)

    return None

rainfall = load_csv(
    DATA_DIR / "delhi_daily_rainfall_clean.csv"
)

risk = load_csv(
    DATA_DIR / "delhi_rainfall_risk_indicator.csv"
)

mcd = load_csv(
    DATA_DIR / "mcd_locations_final.csv"
)

coverage = load_csv(
    DATA_DIR / "final_geocoding_coverage_by_zone.csv"
)

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def section_heading(label, heading, description=None):

    st.markdown(
        f'<div class="section-label">{label}</div>',
        unsafe_allow_html=True
    )

    st.subheader(heading)

    if description:
        st.caption(description)

def show_missing_file(filename):

    st.error(
        f"File not found: {filename}. "
        "Please check the data/processed folder."
    )


def metric_row(items):

    cols = st.columns(len(items), gap="medium")

    for col, (label, value, help_text) in zip(cols, items):

        with col:
            with st.container(border=True):

                st.caption(label)

                st.markdown(
                    f"""
                    <div style="
                        font-size: 30px;
                        font-weight: 800;
                        color: #0f766e;
                        margin: 2px 0 5px 0;
                    ">
                        {value}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.caption(help_text)

# =========================================================
# SIDEBAR
# =========================================================


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="padding: 12px 0 8px 0;"></div>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("🌧️ CivicPulse")
st.sidebar.caption("WATERLOGGING ANALYTICS")

st.sidebar.divider()

st.sidebar.markdown("### MAIN MENU")

page = st.sidebar.radio(
    "Navigate Dashboard",
    [
        "Project Overview",
        "Rainfall Analysis",
        "Risk Analysis",
        "MCD Location Map",
        "Geocoding Coverage"
    ]
)

st.sidebar.divider()

with st.sidebar.container():
    st.sidebar.markdown("### PROJECT DETAILS")
    st.sidebar.markdown("**Data Analytics Minor Project**")
    st.sidebar.markdown("Noida International University")
    st.sidebar.caption("B.Tech | Data Science")

st.sidebar.divider()

st.sidebar.caption("CivicPulse | Academic Prototype")

# =========================================================
# COMMON HERO HEADER
# Use native Streamlit text inside a styled container.
# This avoids raw HTML tags appearing in the browser.
# =========================================================

with st.container(key="civicpulse_hero"):
    st.markdown(
        "<div class='hero-kicker'>DELHI • DATA ANALYTICS • SMART INSIGHTS</div>",
        unsafe_allow_html=True
    )
    st.title("🌧️ CivicPulse")
    st.markdown(
        "**Waterlogging Risk Assessment Dashboard**"
    )
    st.write(
        "Explore rainfall trends, geospatial locations and "
        "historical rainfall-based risk indicators through "
        "an integrated data analytics platform."
    )
    st.caption("✦ ACADEMIC DATA ANALYTICS PROJECT")

# =========================================================
# PAGE 1: PROJECT OVERVIEW
# =========================================================

if page == "Project Overview":

    section_heading(
        "DASHBOARD OVERVIEW",
        "Welcome to CivicPulse",
        "A data analytics approach to understanding rainfall "
        "patterns and reported waterlogging-vulnerable locations."
    )

    total_locations = len(mcd) if mcd is not None else 76

    total_rainfall = (
        len(rainfall) if rainfall is not None else 2192
    )

    if mcd is not None:

        mapped = mcd.dropna(
            subset=["latitude", "longitude"]
        )

        mapped_count = len(mapped)

        verified_count = (
            mcd["verification_status"].eq("Verified").sum()
            if "verification_status" in mcd.columns
            else 0
        )

        pending_count = (
            mcd["verification_status"].eq("Pending").sum()
            if "verification_status" in mcd.columns
            else 0
        )

        not_found_count = (
            mcd["geocoding_status"].eq("Not Found").sum()
            if "geocoding_status" in mcd.columns
            else 0
        )

    else:

        mapped_count = 33
        verified_count = 4
        pending_count = 29
        not_found_count = 43

    metric_row([
        (
            "MCD Locations",
            f"{total_locations}",
            "Locations listed in the MCD dataset"
        ),
        (
            "Coordinates Available",
            f"{mapped_count}",
            "Locations with coordinates"
        ),
        (
            "Manually Verified",
            f"{verified_count}",
            "Manually checked locations"
        ),
        (
            "Rainfall Records",
            f"{total_rainfall:,}",
            "Daily rainfall records"
        )
    ])

    st.divider()

    section_heading(
        "PROJECT INFORMATION",
        "Understanding the Project"
    )

    
    col1, col2 = st.columns(2, gap="large")

    with col1:

        with st.container(border=True):
            st.markdown("#### 🎯 Project Objective")
            st.write(
                "Analyze Delhi rainfall patterns and study "
                "reported waterlogging-vulnerable locations "
                "using data cleaning, visualization and "
                "geospatial analysis."
            )

        with st.container(border=True):
            st.markdown("#### 🌧️ Rainfall Analytics")
            st.write(
                "Analyze daily rainfall estimates from 2020 to 2025, "
                "identify rainfall patterns and calculate "
                "historical rainfall features."
            )

    with col2:

        with st.container(border=True):
            st.markdown("#### 📍 Location Mapping")
            st.write(
                "Visualize MCD-listed vulnerable locations "
                "for which geographic coordinates are available."
            )

        with st.container(border=True):
            st.markdown("#### 📊 Risk Assessment")
            st.write(
                "Apply initial project-defined rainfall thresholds "
                "to classify historical rainfall records into "
                "Low, Moderate, High and Insufficient Data."
            )


    st.divider()

    section_heading(
        "DATA QUALITY",
        "Geocoding Progress"
    )

    metric_row([
        (
            "Coordinates Found",
            mapped_count,
            "Coordinates available"
        ),
        (
            "Pending Verification",
            pending_count,
            "Require manual checking"
        ),
        (
            "Not Found",
            not_found_count,
            "Locations without coordinates"
        )
    ])

    st.info(
        "Rainfall records represent one Delhi reference "
        "coordinate (28.6139, 77.2090), not individual "
        "MCD locations or zones."
    )

# =========================================================
# PAGE 2: RAINFALL ANALYSIS
# =========================================================

elif page == "Rainfall Analysis":

    section_heading(
        "RAINFALL INTELLIGENCE",
        "Rainfall Analysis",
        "Historical daily rainfall estimates from 2020 to 2025."
    )

    if rainfall is None:

        show_missing_file(
            "delhi_daily_rainfall_clean.csv"
        )

    else:

        rainfall = rainfall.copy()

        rainfall["date"] = pd.to_datetime(
            rainfall["date"],
            errors="coerce"
        )

        rainfall["rainfall_mm"] = pd.to_numeric(
            rainfall["rainfall_mm"],
            errors="coerce"
        )

        rainfall = rainfall.dropna(
            subset=["date", "rainfall_mm"]
        ).sort_values("date")

        metric_row([
            (
                "Total Records",
                f"{len(rainfall):,}",
                "Daily observations"
            ),
            (
                "Average Rainfall",
                f"{rainfall['rainfall_mm'].mean():.2f} mm",
                "Mean daily estimate"
            ),
            (
                "Maximum Daily Rainfall",
                f"{rainfall['rainfall_mm'].max():.2f} mm",
                "Highest daily estimate"
            )
        ])

        st.divider()

        section_heading(
            "TREND VISUALIZATION",
            "Daily Rainfall Trend",
            "Daily precipitation estimates throughout the study period."
        )

        st.line_chart(
            rainfall.set_index("date")[["rainfall_mm"]],
            height=350,
            color="#079EAA"
        )

        st.divider()

        section_heading(
            "YEARLY COMPARISON",
            "Year-wise Rainfall"
        )

        yearly = (
            rainfall.assign(
                year=rainfall["date"].dt.year
            )
            .groupby("year")["rainfall_mm"]
            .sum()
        )

        st.bar_chart(
            yearly,
            height=300,
            color="#2588D8"
        )

        with st.expander("📋 View Rainfall Data Table"):

            st.dataframe(
                rainfall.tail(20),
                width="stretch",
                hide_index=True
            )

        st.caption(
            "Source: NASA POWER PRECTOTCORR. These are "
            "satellite/model-based corrected precipitation "
            "estimates, not direct rain-gauge observations."
        )

# =========================================================
# PAGE 3: RISK ANALYSIS
# =========================================================

elif page == "Risk Analysis":

    section_heading(
        "RISK INTELLIGENCE",
        "Rainfall-Based Risk Analysis",
        "Historical rainfall records classified using initial "
        "project-defined screening thresholds."
    )

    if risk is None:

        show_missing_file(
            "delhi_rainfall_risk_indicator.csv"
        )

    else:

        risk_column = "rainfall_risk_level"

        if risk_column not in risk.columns:

            st.error(
                f"Column '{risk_column}' not found. "
                f"Available columns: {risk.columns.tolist()}"
            )

        else:

            counts = (
                risk[risk_column]
                .value_counts()
                .reindex(
                    [
                        "Low",
                        "Moderate",
                        "High",
                        "Insufficient Data"
                    ],
                    fill_value=0
                )
            )

            metric_row([
                (
                    "🟢 Low Risk",
                    f"{int(counts['Low']):,}",
                    "Below moderate thresholds"
                ),
                (
                    "🟡 Moderate Risk",
                    f"{int(counts['Moderate']):,}",
                    "Moderate screening category"
                ),
                (
                    "🔴 High Risk",
                    f"{int(counts['High']):,}",
                    "High screening category"
                ),
                (
                    "⚪ Insufficient Data",
                    f"{int(counts['Insufficient Data']):,}",
                    "Required lag values unavailable"
                )
            ])

            st.divider()

            section_heading(
                "RISK DISTRIBUTION",
                "Distribution of Risk Categories"
            )

            st.bar_chart(
                counts,
                height=350,
                color="#079EAA"
            )

            st.divider()

            section_heading(
                "CLASSIFICATION LOGIC",
                "Risk Classification Rules"
            )

            st.markdown("""
            | Risk Level | Initial Screening Criteria |
            |---|---|
            | High | Today >= 50 mm OR previous 3-day >= 100 mm OR previous 7-day >= 150 mm |
            | Moderate | Today >= 25 mm OR previous 3-day >= 50 mm OR previous 7-day >= 75 mm |
            | Low | Below Moderate thresholds |
            | Insufficient Data | Required previous rainfall values unavailable |
            """)

            st.warning(
                "These are initial project-defined screening "
                "thresholds, not empirically validated flood "
                "thresholds. This is a rule-based rainfall risk "
                "indicator, not a trained ML prediction model "
                "or live weather forecast."
            )

# =========================================================
# PAGE 4: MCD LOCATION MAP
# =========================================================

elif page == "MCD Location Map":

    section_heading(
        "GEOSPATIAL ANALYTICS",
        "MCD Waterlogging-Vulnerable Locations",
        "Geographic view of MCD-listed locations with available coordinates."
    )

    if mcd is None:

        show_missing_file(
            "mcd_locations_final.csv"
        )

    else:

        required = {"latitude", "longitude"}

        if not required.issubset(mcd.columns):

            st.error(
                "Latitude or longitude columns are missing."
            )

        else:

            mapped = mcd.dropna(
                subset=["latitude", "longitude"]
            ).copy()

            mapped["latitude"] = pd.to_numeric(
                mapped["latitude"],
                errors="coerce"
            )

            mapped["longitude"] = pd.to_numeric(
                mapped["longitude"],
                errors="coerce"
            )

            mapped = mapped.dropna(
                subset=["latitude", "longitude"]
            )

            verified = (
                mapped["verification_status"].eq("Verified").sum()
                if "verification_status" in mapped.columns
                else 0
            )

            pending = (
                mapped["verification_status"].eq("Pending").sum()
                if "verification_status" in mapped.columns
                else 0
            )

            metric_row([
                (
                    "Coordinates Available",
                    len(mapped),
                    "Locations with coordinates"
                ),
                (
                    "Verified",
                    int(verified),
                    "Manually verified locations"
                ),
                (
                    "Pending",
                    int(pending),
                    "Awaiting manual verification"
                )
            ])

            st.divider()

            section_heading(
                "LOCATION VISUALIZATION",
                "Delhi Location Map"
            )

            if not mapped.empty:

                st.map(
                    mapped,
                    latitude="latitude",
                    longitude="longitude",
                    size=35
                )

            st.info(
                "Only 4 locations have been manually verified. "
                "29 are pending verification. Coordinate "
                "availability does not guarantee exact location accuracy."
            )

            display_columns = [
                col for col in [
                    "zone",
                    "location_clean",
                    "latitude",
                    "longitude",
                    "verification_status"
                ]
                if col in mapped.columns
            ]

            section_heading(
                "LOCATION RECORDS",
                "Mapped Location Details"
            )

            st.dataframe(
                mapped[display_columns],
                width="stretch",
                hide_index=True
            )

# =========================================================
# PAGE 5: GEOCODING COVERAGE
# =========================================================

elif page == "Geocoding Coverage":

    section_heading(
        "DATA QUALITY ANALYTICS",
        "Zone-wise Geocoding Coverage",
        "Comparison of coordinate availability across MCD zones."
    )

    if coverage is None:

        show_missing_file(
            "final_geocoding_coverage_by_zone.csv"
        )

    else:

        required_columns = {
            "zone",
            "coverage_percentage"
        }

        if not required_columns.issubset(coverage.columns):

            st.error(
                "Expected columns zone and coverage_percentage "
                "were not found in the coverage file."
            )

        else:

            total = (
                coverage["total"].sum()
                if "total" in coverage.columns
                else 76
            )

            geocoded = (
                coverage["geocoded"].sum()
                if "geocoded" in coverage.columns
                else 33
            )

            overall = (
                geocoded / total * 100
                if total else 0
            )

            metric_row([
                (
                    "Total Locations",
                    int(total),
                    "MCD-listed locations"
                ),
                (
                    "Geocoded Locations",
                    int(geocoded),
                    "Coordinates available"
                ),
                (
                    "Overall Coverage",
                    f"{overall:.2f}%",
                    "Geocoding coverage"
                )
            ])

            st.divider()

            section_heading(
                "ZONE COMPARISON",
                "Geocoding Coverage by Zone"
            )

            chart = coverage.set_index("zone")[
                ["coverage_percentage"]
            ]

            st.bar_chart(
                chart,
                height=400,
                color="#079EAA"
            )

            st.divider()

            section_heading(
                "DETAILED STATISTICS",
                "Zone-wise Coverage Table"
            )

            st.dataframe(
                coverage,
                width="stretch",
                hide_index=True
            )

            st.info(
                "Overall geocoding coverage is partial. "
                "Only 33 out of 76 locations have coordinates, "
                "and only 4 have been manually verified. "
                "Coverage should not be treated as representative "
                "of all MCD locations or zones."
            )

# =========================================================
# FOOTER
# =========================================================


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown("### 🌧️ CivicPulse")
st.caption("Data Analytics Minor Project")

st.markdown(
    "**Noida International University** | B.Tech Data Science"
)

st.caption(
    "Academic analysis prototype. "
    "Not an official emergency alert system."
)
