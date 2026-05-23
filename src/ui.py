import datetime as dt
import html
import base64
from pathlib import Path
import pandas as pd
import streamlit as st
from .config import APP_VERSION, TARGET_LANES, LANE_DISPLAY_NAMES, LANE_CAPTIONS
from .analytics import split_multi_rows


def render_sidebar():
    with st.sidebar:
        st.markdown("### BuildWell Control Notes")
        st.caption(f"{APP_VERSION}. Executive-facing flow remains one button only.")
        st.markdown("**Preset lanes**")
        for lane in TARGET_LANES:
            st.caption(f"• {lane}")
        st.caption("Architecture: UI → analytics service → ingestion client → normalization layer. Later the same layers can move behind FastAPI/Postgres without rebuilding the Streamlit UI.")


def _emblem_data_uri() -> str:
    asset = Path(__file__).resolve().parents[1] / "assets" / "buildwell_emblem.png"
    if not asset.exists():
        return ""
    encoded = base64.b64encode(asset.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def render_hero():
    emblem = _emblem_data_uri()
    emblem_html = f'<img class="buildwell-emblem" src="{emblem}" alt="Built by BuildWell" />' if emblem else ""
    st.markdown(f"""
    <div class="hero-clean">
        <div class="hero-inner">
            <div class="hero-kicker">Clinical Intelligence Console</div>
            <div class="hero-title">NextCure Signal Room</div>
            <div class="hero-accent"></div>
        </div>
        {emblem_html}
    </div>
    """, unsafe_allow_html=True)



def render_lane_selector() -> list[str]:
    """Premium first-screen selector for choosing one, several, or all clinical lanes."""
    lane_options = list(TARGET_LANES.keys())
    default_lanes = st.session_state.get("scan_lanes", lane_options)
    if not isinstance(default_lanes, list):
        default_lanes = lane_options
    default_lanes = [lane for lane in default_lanes if lane in lane_options] or lane_options

    st.markdown(
        '<div class="scan-selector-shell">'
        '<div class="scan-selector-kicker">Analysis Scope</div>'
        '<div class="scan-selector-title">Choose the intelligence lanes</div>'
        '<div class="scan-selector-note">Run the complete four-lane view, isolate one lane, or combine selected lanes for a sharper discussion.</div>'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="lane-picker-wrap">', unsafe_allow_html=True)
    selected = st.multiselect(
        "Analysis lanes",
        lane_options,
        default=default_lanes,
        format_func=lambda lane: LANE_DISPLAY_NAMES.get(lane, lane),
        label_visibility="collapsed",
        placeholder="Choose one or more lanes",
        key="scan_lanes",
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if not selected:
        selected = lane_options
        st.session_state.scan_lanes = lane_options

    if len(selected) == len(lane_options):
        caption = "Full executive scan across CDH6, B7-H4, Alzheimer's/ApoE4, and Bone/Siglec-15."
    else:
        caption = "Selected lens: " + " • ".join(LANE_CAPTIONS.get(lane, lane) for lane in selected)
    st.markdown(f'<div class="scan-selector-caption">{html.escape(caption)}</div>', unsafe_allow_html=True)
    return selected

def render_idle_panel():
    # Intentionally blank for the cleaned executive UI. The centered Run Analysis
    # button is the only power-on affordance.
    return None


def metric_card(label: str, value: str, note: str = ""):
    note_html = f'<div class="metric-note">{html.escape(str(note))}</div>' if note else ""
    st.markdown(f"""
    <div class="metric-card"><div class="metric-label">{html.escape(str(label))}</div><div class="metric-value">{html.escape(str(value))}</div>{note_html}</div>
    """, unsafe_allow_html=True)


def section(title: str, subtitle: str = ""):
    st.markdown(f'<div class="section-title">{html.escape(str(title))}</div>', unsafe_allow_html=True)
    # Clean-up pass: do not render explanatory subtitles under every heading.
    return None


def render_snapshot(bundle: dict):
    df, active_df, planned_df = bundle["df"], bundle["active_df"], bundle["planned_df"]
    countries = split_multi_rows(df, "countries", "country")["country"].nunique() if not df.empty else 0
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: metric_card("Trials Captured", f"{len(df):,}")
    with c2: metric_card("Active / Near-Active", f"{len(active_df):,}")
    with c3: metric_card("Planned", f"{len(planned_df):,}")
    with c4: metric_card("Patients Planned", f"{int(df['enrollment'].sum()):,}")
    with c5: metric_card("Countries", f"{countries:,}")


def render_lane_cards(bundle: dict):
    df = bundle["df"]
    cols = st.columns(4)
    for idx, lane in enumerate(bundle["lane_names"]):
        lane_df = df[df["target_lane"] == lane]
        active_lane = lane_df[lane_df["is_active"]]
        enroll = int(lane_df["enrollment"].sum()) if not lane_df.empty else 0
        with cols[idx]:
            st.markdown(
                f'<div class="lane-card"><div class="lane-title">{html.escape(str(lane))}</div>'
                f'<div class="lane-metrics"><span>{len(lane_df)} studies</span><span>{len(active_lane)} active</span><span>{enroll:,} patients</span></div></div>',
                unsafe_allow_html=True,
            )


def render_signal_feed(signals: list[tuple[str, str]]):
    for title, body in signals:
        st.markdown(f'<div class="signal"><strong>{html.escape(str(title))}</strong><br>{html.escape(str(body))}</div>', unsafe_allow_html=True)


def render_dark_table(df: pd.DataFrame, height: int | None = None):
    """Render a dataframe as a dark, scrollable HTML table.

    Native Streamlit dataframes can show up with white interiors on some Cloud
    theme/version combinations. This renderer keeps the executive aesthetic
    consistent for evidence/detail tables.
    """
    if df is None or df.empty:
        st.caption("No records available for this section.")
        return
    d = df.copy()
    # Convert datetimes safely for display.
    for col in d.columns:
        if pd.api.types.is_datetime64_any_dtype(d[col]):
            d[col] = d[col].dt.strftime("%b %d, %Y").fillna("Date not listed")
    d = d.fillna("Not specified")
    max_h = height or 420
    table_html = d.to_html(index=False, escape=True, classes="dark-data-table")
    st.markdown(f'<div class="dark-table-wrap" style="max-height:{max_h}px;">{table_html}</div>', unsafe_allow_html=True)


def render_footer():
    # Footer/source clutter intentionally removed in v2.5 UI cleanup.
    return None
