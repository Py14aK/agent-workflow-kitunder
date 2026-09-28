#!/usr/bin/env python3
"""Elliptic heart executable demo for Copilot / Codex work.
Wicklin 2024-02-07. Distinct from SaS/Heart Shaped Box.
Run: python3 elliptic_heart_2026-09-28.py
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon

MAX_R = float(np.sqrt(2.0))
MIN_R = float(np.sqrt(2.0 / 3.0))
OUT_DIR = Path(__file__).resolve().parent

@dataclass(frozen=True)
class HeartPolygon:
    theta: np.ndarray
    x: np.ndarray
    y: np.ndarray

def ellipse_radius(theta: np.ndarray) -> np.ndarray:
    den = 1.0 - 0.5 * np.sin(2.0 * theta)
    if np.any(den <= 0):
        raise ValueError("polar denominator non-positive")
    return np.sqrt(1.0 / den)

def elliptic_heart(n: int = 401) -> HeartPolygon:
    t = np.linspace(-0.5 * np.pi, 0.5 * np.pi, n)
    r = ellipse_radius(t)
    x_right = r * np.cos(t)
    y = r * np.sin(t)
    theta = np.concatenate([t, np.pi - t])
    x = np.concatenate([x_right, -x_right])
    y_all = np.concatenate([y, y])
    order = np.argsort(theta, kind="mergesort")
    theta_s, x_s, y_s = theta[order], x[order], y_all[order]
    if not np.isclose(x_s[0], x_s[-1]) or not np.isclose(y_s[0], y_s[-1]):
        theta_s = np.append(theta_s, theta_s[0])
        x_s = np.append(x_s, x_s[0])
        y_s = np.append(y_s, y_s[0])
    return HeartPolygon(theta_s, x_s, y_s)

def main() -> None:
    heart = elliptic_heart()
    right = heart.x >= -1e-12
    resid = np.max(np.abs(heart.x[right]**2 + heart.y[right]**2 - heart.x[right]*heart.y[right] - 1.0))
    closed = np.isclose(heart.x[0], heart.x[-1]) and np.isclose(heart.y[0], heart.y[-1])
    png = OUT_DIR / "elliptic_heart_2026-09-28.png"
    fig, ax = plt.subplots(figsize=(6, 6), dpi=140)
    ax.add_patch(Polygon(np.column_stack([heart.x, heart.y]), closed=True, facecolor="#C3540C", edgecolor="#7A2200"))
    for slope in (1.0, -1.0):
        ax.add_patch(Ellipse((0, 0), 2*MAX_R, 2*MIN_R, angle=np.degrees(np.arctan(slope)), fill=False, edgecolor="#E08080"))
    ax.set_aspect("equal")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    ax.set_title("Elliptic heart")
    fig.tight_layout()
    fig.savefig(png)
    plt.close(fig)
    print("VERIFIED")
    print(f"residual={resid}")
    print(f"closed={closed}")
    print(f"png={png}")
    if resid > 1e-10 or not closed:
        raise SystemExit("verification failed")

if __name__ == "__main__":
    main()
