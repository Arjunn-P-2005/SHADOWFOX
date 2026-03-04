import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("Sample_Cricket_Fielding_Data.xlsx")

df.columns = df.columns.str.strip()

df["Runs"] = pd.to_numeric(df["Runs"], errors="coerce").fillna(0)

df["Clean Picks"] = df["Pick"].apply(lambda x: 1 if str(x).lower() == "clean pick" else 0)
df["Good Throws"] = df["Pick"].apply(lambda x: 1 if str(x).lower() == "good throw" else 0)
df["Catches"] = df["Pick"].apply(lambda x: 1 if str(x).lower() == "catch" else 0)
df["Dropped Catches"] = df["Pick"].apply(lambda x: 1 if str(x).lower() == "drop catch" else 0)
df["Fumbles"] = df["Pick"].apply(lambda x: 1 if str(x).lower() == "fumble" else 0)

df["Run Outs"] = df["Throw"].apply(lambda x: 1 if str(x).lower() == "run out" else 0)
df["Missed Run Outs"] = df["Throw"].apply(lambda x: 1 if str(x).lower() == "missed run out" else 0)
df["Stumpings"] = df["Throw"].apply(lambda x: 1 if str(x).lower() == "stumping" else 0)

WCP = 2
WGT = 1.5
WC = 3
WDC = -3
WST = 4
WRO = 5
WMRO = -2
WF = -1

df["Performance Score"] = (
    df["Clean Picks"] * WCP +
    df["Good Throws"] * WGT +
    df["Catches"] * WC +
    df["Dropped Catches"] * WDC +
    df["Stumpings"] * WST +
    df["Run Outs"] * WRO +
    df["Missed Run Outs"] * WMRO +
    df["Fumbles"] * WF +
    df["Runs"]
)

player_summary = df.groupby("Player Name").agg({
    "Clean Picks": "sum",
    "Good Throws": "sum",
    "Catches": "sum",
    "Dropped Catches": "sum",
    "Fumbles": "sum",
    "Stumpings": "sum",
    "Run Outs": "sum",
    "Missed Run Outs": "sum",
    "Runs": "sum",
    "Performance Score": "sum"
}).reset_index()

player_summary = player_summary.sort_values("Performance Score", ascending=False)
player_summary["Rank"] = range(1, len(player_summary) + 1)

print("\nFinal Fielding Performance Summary\n")
print(player_summary)

plt.figure(figsize=(10, 6))
plt.bar(player_summary["Player Name"], player_summary["Performance Score"])
plt.title("Fielding Performance Score Comparison")
plt.xlabel("Player")
plt.ylabel("Performance Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("performance_comparison.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(player_summary["Runs"], player_summary["Performance Score"])
plt.title("Runs Saved vs Performance Score")
plt.xlabel("Runs Saved")
plt.ylabel("Performance Score")
plt.tight_layout()
plt.savefig("runs_vs_score.png")
plt.show()

top3 = player_summary.head(3)

plt.figure(figsize=(8, 5))
plt.bar(top3["Player Name"], top3["Performance Score"])
plt.title("Top 3 Fielders")
plt.tight_layout()
plt.savefig("top3_fielders.png")
plt.show()

player_summary.to_excel("Advanced_Fielding_Analysis_Output.xlsx", index=False)