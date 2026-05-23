CSS = """
<style>
:root{
  --bg:#070b14;--panel:rgba(14,22,36,.78);--line:rgba(164,183,219,.16);
  --text:#edf4ff;--muted:#9aa8c1;--gold:#d8b86c;--gold2:#b9954c;--cyan:#63d7ff;
}
html,body,[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(circle at 18% -8%,rgba(75,108,255,.14),transparent 29%),
    radial-gradient(circle at 82% -6%,rgba(216,184,108,.11),transparent 26%),
    linear-gradient(180deg,#070b14 0%,#0a1020 46%,#070a12 100%);
  color:var(--text);
}
[data-testid="stHeader"]{background:rgba(8,13,24,0)}
[data-testid="stToolbar"]{display:none}
.block-container{padding-top:1.35rem;padding-bottom:4rem;max-width:1480px}

/* Premium hero: refined signal-room marquee. */
.hero-clean{
  position:relative;display:flex;align-items:center;justify-content:center;
  max-width:1080px;min-height:118px;margin:0 auto 20px auto;
  border-radius:30px;padding:26px 230px 26px 230px;
  background:
    radial-gradient(circle at 18% 0%,rgba(216,184,108,.20),transparent 34%),
    radial-gradient(circle at 82% 8%,rgba(99,215,255,.12),transparent 36%),
    linear-gradient(135deg,rgba(18,29,48,.92),rgba(8,13,24,.96) 52%,rgba(14,23,38,.90));
  box-shadow:
    0 34px 90px rgba(0,0,0,.42),
    inset 0 1px 0 rgba(255,255,255,.10),
    inset 0 -1px 0 rgba(216,184,108,.16);
  overflow:hidden;
}
.hero-clean:before{
  content:"";position:absolute;inset:0;border-radius:30px;padding:1px;
  background:linear-gradient(120deg,rgba(216,184,108,.72),rgba(99,215,255,.14) 42%,rgba(216,184,108,.44));
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;
}
.hero-clean:after{
  content:"";position:absolute;left:18%;right:18%;bottom:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(216,184,108,.72),rgba(99,215,255,.38),transparent);
  pointer-events:none;
}
.hero-inner{position:relative;z-index:2;text-align:center}
.hero-kicker{
  display:inline-flex;align-items:center;justify-content:center;margin-bottom:8px;
  color:#d8b86c;font-size:.70rem;font-weight:900;letter-spacing:.22em;text-transform:uppercase;
}
.hero-title{
  position:relative;z-index:2;font-size:2.56rem;line-height:1.02;font-weight:900;letter-spacing:-.055em;
  color:#fff;text-align:center;text-shadow:0 18px 38px rgba(0,0,0,.50);
  white-space:nowrap;
}
.hero-accent{
  width:124px;height:3px;border-radius:99px;margin:14px auto 0 auto;
  background:linear-gradient(90deg,transparent,rgba(216,184,108,.95),rgba(99,215,255,.56),transparent);
  box-shadow:0 0 22px rgba(216,184,108,.24);
}
.buildwell-emblem{
  position:absolute;right:28px;top:50%;transform:translateY(-50%);
  width:164px;max-width:18vw;height:auto;z-index:2;
  filter:drop-shadow(0 18px 30px rgba(0,0,0,.46));border:0!important;background:transparent!important;
}

.metric-card{border:1px solid var(--line);background:linear-gradient(180deg,rgba(20,31,51,.82),rgba(12,19,33,.72));border-radius:22px;padding:20px;min-height:112px;box-shadow:0 16px 44px rgba(0,0,0,.23)}
.metric-label{color:var(--muted);text-transform:uppercase;letter-spacing:.12em;font-size:.72rem;font-weight:800}.metric-value{color:#fff;font-size:2.2rem;font-weight:800;letter-spacing:-.04em;margin-top:8px}.metric-note{color:#aab6cc;font-size:.87rem;margin-top:7px;line-height:1.35}
.section-title{margin-top:34px;margin-bottom:16px;font-size:1.28rem;font-weight:850;letter-spacing:-.025em;color:#fff}.section-subtitle{display:none}
.lane-card{border:1px solid var(--line);background:rgba(14,22,36,.62);border-radius:18px;padding:16px;min-height:92px}.lane-title{color:#fff;font-weight:850;font-size:1rem}.lane-metrics{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.lane-metrics span{border:1px solid rgba(216,184,108,.18);background:rgba(216,184,108,.055);color:#f2deaa;border-radius:999px;padding:5px 9px;font-size:.76rem}
.signal{border-left:3px solid rgba(99,215,255,.85);background:rgba(99,215,255,.055);border-radius:14px;padding:12px 14px;margin-bottom:10px;color:#dceaff}.signal strong{color:#fff}.caption{display:none}


/* Premium flexible lane picker */
.scan-selector-shell{
  max-width:980px;margin:0 auto 12px auto;text-align:center;border:1px solid rgba(164,183,219,.14);
  border-radius:24px;padding:18px 22px 14px 22px;background:
    radial-gradient(circle at 20% 0%,rgba(99,215,255,.10),transparent 32%),
    radial-gradient(circle at 82% 10%,rgba(216,184,108,.11),transparent 34%),
    linear-gradient(135deg,rgba(14,22,36,.76),rgba(8,13,24,.68));
  box-shadow:0 20px 60px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.07);
}
.scan-selector-kicker{color:#d8b86c;font-size:.66rem;font-weight:900;letter-spacing:.22em;text-transform:uppercase;margin-bottom:6px}
.scan-selector-title{color:#fff;font-size:1.22rem;font-weight:900;letter-spacing:-.035em}
.scan-selector-note{max-width:710px;margin:7px auto 0 auto;color:#9aa8c1;font-size:.88rem;line-height:1.42}
.lane-picker-wrap{
  max-width:820px;margin:0 auto 10px auto;padding:0 18px;display:flex;justify-content:center;align-items:center;
}
.lane-picker-wrap [data-testid="stMultiSelect"]{width:100%!important;max-width:760px!important;margin:0 auto!important}
.lane-picker-wrap [data-testid="stMultiSelect"] > div{width:100%!important;margin:0 auto!important}
.lane-picker-wrap div[data-baseweb="select"]{width:100%!important;max-width:760px!important;margin:0 auto!important}
.lane-picker-wrap div[data-baseweb="select"] > div{
  min-height:58px!important;border-radius:999px!important;padding:8px 14px!important;
  border:1px solid rgba(164,183,219,.20)!important;background:
    radial-gradient(circle at 15% 50%,rgba(216,184,108,.18),transparent 22%),
    linear-gradient(180deg,rgba(17,28,48,.92),rgba(8,13,24,.88))!important;
  box-shadow:0 18px 46px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.07)!important;
}
.lane-picker-wrap div[data-baseweb="select"] input{color:#edf4ff!important}
.lane-picker-wrap div[data-baseweb="select"] span{color:#dceaff!important;font-weight:750!important}
.lane-picker-wrap div[data-baseweb="select"] [role="button"],
.lane-picker-wrap div[data-baseweb="select"] [data-baseweb="tag"]{
  border-radius:999px!important;border:1px solid rgba(216,184,108,.38)!important;
  background:linear-gradient(135deg,rgba(238,211,142,.98),rgba(184,146,67,.96))!important;
  color:#06101d!important;box-shadow:0 8px 22px rgba(0,0,0,.22), inset 0 1px 0 rgba(255,255,255,.28)!important;
}
.lane-picker-wrap div[data-baseweb="select"] [role="button"] span,
.lane-picker-wrap div[data-baseweb="select"] [data-baseweb="tag"] span{color:#06101d!important;font-weight:900!important}
.lane-picker-wrap div[data-baseweb="select"] svg{fill:#edf4ff!important;color:#edf4ff!important}
.lane-picker-wrap div[data-baseweb="select"] [role="button"] svg,
.lane-picker-wrap div[data-baseweb="select"] [data-baseweb="tag"] svg{fill:#06101d!important;color:#06101d!important}
.scan-selector-caption{
  width:fit-content;max-width:880px;margin:12px auto 22px auto;padding:9px 14px;border-radius:999px;
  border:1px solid rgba(99,215,255,.16);background:rgba(99,215,255,.055);color:#cfe8ff;
  font-size:.82rem;text-align:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.05);
}

/* Centered premium action */
.run-button-zone{display:flex;justify-content:center;align-items:center;width:100%;margin:2px auto 34px auto;text-align:center}
.st-key-run_analysis{display:flex!important;justify-content:center!important;align-items:center!important;width:100%!important;margin:0 auto 34px auto!important;text-align:center!important}
.st-key-run_analysis div[data-testid="stButton"]{display:flex!important;justify-content:center!important;width:100%!important;margin:0 auto!important}
.st-key-run_analysis button, div[data-testid="stButton"] button[kind="secondary"]{
  width:190px!important;max-width:190px!important;border-radius:999px!important;min-height:50px!important;
  border:1px solid rgba(216,184,108,.62)!important;
  background:linear-gradient(135deg,rgba(238,211,142,.98),rgba(184,146,67,.98))!important;
  color:#07101e!important;font-weight:900!important;letter-spacing:.01em;
  box-shadow:0 18px 42px rgba(0,0,0,.36), inset 0 1px 0 rgba(255,255,255,.34)!important;
}
.st-key-run_analysis button:hover{border-color:rgba(255,230,165,.92)!important;transform:translateY(-1px);box-shadow:0 22px 52px rgba(0,0,0,.44), inset 0 1px 0 rgba(255,255,255,.40)!important}
.stPlotlyChart{border-radius:22px;overflow:hidden;border:1px solid rgba(164,183,219,.10);background:rgba(7,12,22,.18)}

/* Dark select/dropdown cleanup */
div[data-baseweb="select"]>div, div[data-baseweb="select"] div, div[data-baseweb="input"]>div, input, textarea{
  background-color:rgba(12,19,33,.96)!important;border-color:rgba(164,183,219,.22)!important;color:#edf4ff!important;
}
div[data-baseweb="select"]>div{border-radius:14px!important;box-shadow:none!important}
div[data-baseweb="select"] span, div[data-baseweb="select"] svg, div[data-baseweb="input"] input{color:#edf4ff!important;fill:#edf4ff!important}
div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"], div[role="listbox"]{
  background:#0d1526!important;color:#edf4ff!important;border:1px solid rgba(164,183,219,.22)!important;
}
li[role="option"], div[role="option"]{background:#0d1526!important;color:#edf4ff!important}
li[role="option"]:hover, div[role="option"]:hover{background:rgba(99,215,255,.10)!important}
[data-testid="stSelectbox"], [data-testid="stMultiSelect"]{color:#edf4ff!important}

/* Expander cleanup: remove white header bars across Streamlit versions. */
div[data-testid="stExpander"]{border:1px solid rgba(164,183,219,.16)!important;border-radius:16px!important;background:rgba(10,16,28,.42)!important;overflow:hidden!important;box-shadow:none!important}
div[data-testid="stExpander"] details{background:rgba(10,16,28,.42)!important;color:#edf4ff!important}
div[data-testid="stExpander"] details > summary,
div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary:hover,
div[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"]{
  background:linear-gradient(90deg,rgba(17,27,46,.98),rgba(12,19,33,.96))!important;color:#edf4ff!important;border-bottom:1px solid rgba(164,183,219,.12)!important;
}
div[data-testid="stExpander"] summary *, div[data-testid="stExpander"] svg{color:#edf4ff!important;fill:#edf4ff!important}
div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p{color:#edf4ff!important}

/* Native dataframe fallback styling */
div[data-testid="stDataFrame"], div[data-testid="stDataFrame"] div{background:rgba(10,16,28,.78)!important;color:#edf4ff!important;border-color:rgba(164,183,219,.16)!important}
div[data-testid="stDataFrame"] *{color:#edf4ff!important}
.dark-table-wrap{overflow:auto;border:1px solid var(--line);border-radius:18px;background:rgba(10,16,28,.78);box-shadow:0 16px 42px rgba(0,0,0,.18);margin-bottom:14px}.dark-data-table{border-collapse:separate;border-spacing:0;width:100%;font-size:.82rem;color:#edf4ff}.dark-data-table thead th{position:sticky;top:0;background:#111b2e;color:#fff;text-align:left;padding:10px 12px;border-bottom:1px solid rgba(164,183,219,.22);white-space:nowrap;z-index:2}.dark-data-table tbody td{padding:9px 12px;border-bottom:1px solid rgba(164,183,219,.10);color:#dce7f7;vertical-align:top;max-width:360px}.dark-data-table tbody tr:nth-child(even){background:rgba(255,255,255,.025)}.dark-data-table tbody tr:hover{background:rgba(99,215,255,.06)}

@media(max-width:900px){
  .hero-clean{min-height:126px;padding:20px 22px;justify-content:center;flex-direction:column;gap:12px}
  .hero-title{font-size:2.08rem;white-space:normal}.buildwell-emblem{position:relative;right:auto;top:auto;transform:none;width:146px;max-width:56vw}.hero-kicker{font-size:.64rem}
}
</style>
"""
