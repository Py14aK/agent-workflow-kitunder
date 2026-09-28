<pre style='color:#cfcfc2;background-color:#232629;'>
<span style='color:#c45b00;'>    # Research Architecture for a Ten-Minute Nonlinear Portfolio Optimizer Built on Py14aK</span>

<span style='color:#c45b00;'>    ## Executive summary</span>

<span style='color:#c45b00;'>    The right next step is **not** to add isolated indicators to the existing account chart. The Py14aK repository already contains pieces of a much more ambitious system: SAS hash-based moving calculations, `PROC EXPAND` moving averages and EWMA, explicit finite-state Markov propagation, bootstrap/time-series resampling, path reconstruction, `tanh`/`1-\tanh^2` nonlinear transforms, RBF-kernel ideas, velocity/acceleration notes, covariance structures, Legendre/wavelet ideas, and geometric/stochastic modeling notes. fileciteturn5file0L2-L4 fileciteturn9file0L2-L7 fileciteturn10file0L1-L2 fileciteturn14file0L2-L4</span>

<span style='color:#c45b00;'>    The proposed research system should therefore be built as a **layered state-space optimizer**:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \text{10-min OHLCV}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{causal linear state}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{factor decomposition}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{residual state}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{nonlinear state}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{regime probabilities}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{return/risk forecasts}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{constrained portfolio weights}</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The important methodological choice is to **preserve the linear/autocovariant structure before adding nonlinearity**. That addresses your earlier objection directly. We should not immediately throw every feature through `tanh`, PCA, a kernel, or a Poincaré ball. We should first estimate the systematic linear subspace,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    r_t=B F_t+\epsilon_t,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and its lag structure,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    C_\tau</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    E[(X_t-\mu)(X_{t+\tau}-\mu)^\top],</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    then investigate whether the residual field \(\epsilon_t\) contains stable nonlinear structure. Ledoit and Wolf's shrinkage framework is particularly relevant because the ordinary sample covariance becomes poorly conditioned when dimension is large relative to observations. citeturn0search1turn0search6</span>

<span style='color:#c45b00;'>    The recommended production optimizer is consequently **much more conservative than the research layer**. The production signal should combine: robust factor/residual returns, multiscale `tanh` state and magnitude, local-polynomial velocity/acceleration, volatility, causal Ichimoku, Markov-state probabilities, and a Random Forest forecast. Kernel PCA, diffusion maps, Poincaré geometry, Lyapunov analysis, Kramers–Moyal drift/diffusion, Morse potentials, Witten operators, N-body diagnostics and fractional methods should run as **challenger models**. They enter portfolio weights only after demonstrating incremental out-of-sample value over the linear baseline. Kernel PCA is explicitly a nonlinear extension of PCA through kernel eigenproblems, while diffusion maps derive coordinates from eigenfunctions of a Markov transition operator; both provide principled nonlinear baselines before adopting stronger geometric assumptions. citeturn1search16turn1search3turn1search13</span>

<span style='color:#c45b00;'>    The portfolio layer itself should solve something close to</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \max_w\;</span>
<span style='color:#c45b00;'>    \hat\mu_t^\top w</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \frac{\lambda}{2}w^\top\hat\Sigma_t w</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \eta\|w-w_{t-1}\|_1</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \kappa\|B_t^\top w-b^\star\|_2^2</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    subject to</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \mathbf1^\top w=1,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    position limits, gross-exposure limits, liquidity limits, optional beta constraints, and transaction-cost constraints. This preserves the mean–variance structure pioneered by Markowitz while explicitly penalizing unstable factor exposure and turnover. citeturn7search0 A parallel CVaR optimizer should be maintained as a tail-risk challenger because the Rockafellar–Uryasev formulation makes CVaR optimization tractable. citeturn7search6</span>

<span style='color:#c45b00;'>    Crucially, **the nonlinear research program should not presume a market manifold**. A Poincaré embedding is an empirical representation to be compared with Euclidean, Mahalanobis, kernel and diffusion distances. Nickel and Kiela introduced Poincaré embeddings specifically to exploit latent hierarchical structure; that does not establish that stock states are intrinsically hyperbolic. The market version earns negative curvature only if it improves out-of-sample neighborhood stability, state-transition prediction or portfolio results. citeturn1search5turn1search9</span>

<span style='color:#c45b00;'>    The complete proposed pipeline is:</span>

<span style='color:#c45b00;'>    ```mermaid</span>
<span style='color:#c45b00;'>    flowchart LR</span>
<span style='color:#c45b00;'>        A[Tiingo 10-min OHLCV] --&gt; B[Cleaning / session alignment]</span>
<span style='color:#c45b00;'>        B --&gt; C[Returns + SMA EMA + volatility + Ichimoku]</span>
<span style='color:#c45b00;'>        C --&gt; D[Local causal polynomial derivatives]</span>
<span style='color:#c45b00;'>        D --&gt; E[Past-only robust scaling]</span>

<span style='color:#c45b00;'>        E --&gt; F[Linear autocovariance / covariance layer]</span>
<span style='color:#c45b00;'>        F --&gt; G[Ledoit-Wolf PCA + multi-beta factors]</span>
<span style='color:#c45b00;'>        G --&gt; H[Systematic component]</span>
<span style='color:#c45b00;'>        G --&gt; I[Residual component]</span>

<span style='color:#c45b00;'>        I --&gt; J[Multiscale tanh bank]</span>
<span style='color:#c45b00;'>        I --&gt; K[Strength / tail channel]</span>
<span style='color:#c45b00;'>        J --&gt; L[Joint nonlinear state]</span>
<span style='color:#c45b00;'>        K --&gt; L</span>

<span style='color:#c45b00;'>        L --&gt; M[Euclidean / Mahalanobis baseline]</span>
<span style='color:#c45b00;'>        L --&gt; N[Kernel PCA]</span>
<span style='color:#c45b00;'>        L --&gt; O[Diffusion maps]</span>
<span style='color:#c45b00;'>        L --&gt; P[Poincare challenger]</span>

<span style='color:#c45b00;'>        M --&gt; Q[kNN state graph]</span>
<span style='color:#c45b00;'>        N --&gt; Q</span>
<span style='color:#c45b00;'>        O --&gt; Q</span>
<span style='color:#c45b00;'>        P --&gt; Q</span>

<span style='color:#c45b00;'>        Q --&gt; R[Markov lattice]</span>
<span style='color:#c45b00;'>        Q --&gt; S[Local barycentres / N-body diagnostics]</span>
<span style='color:#c45b00;'>        Q --&gt; T[Drift-diffusion / Kramers-Moyal]</span>
<span style='color:#c45b00;'>        Q --&gt; U[Lyapunov / Hurst diagnostics]</span>

<span style='color:#c45b00;'>        R --&gt; V[RF + state probability ensemble]</span>
<span style='color:#c45b00;'>        S --&gt; V</span>
<span style='color:#c45b00;'>        T --&gt; V</span>
<span style='color:#c45b00;'>        U --&gt; V</span>

<span style='color:#c45b00;'>        V --&gt; W[Expected return / risk forecasts]</span>
<span style='color:#c45b00;'>        F --&gt; W</span>
<span style='color:#c45b00;'>        W --&gt; X[Constrained portfolio optimizer]</span>
<span style='color:#c45b00;'>        X --&gt; Y[Cash-flow-adjusted walk-forward backtest]</span>
<span style='color:#c45b00;'>        Y --&gt; Z[Research report + charts + CSV outputs]</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The data pipeline can use Tiingo's current consolidated equity intraday endpoint where available; Tiingo documents historical intraday OHLCV with configurable minute resampling and describes that consolidated feed as drawing from multiple equity venues. Its IEX historical endpoint is suitable as a fallback/check, but Tiingo notes that IEX historical volume is IEX-only. citeturn0search5turn0search0</span>

<span style='color:#c45b00;'>    ## Repository and data foundation</span>

<span style='color:#c45b00;'>    The existing repository should be treated as the **research ancestor**, not discarded.</span>

<span style='color:#c45b00;'>    `Risk/Moving averages` already demonstrates two useful patterns: a SAS hash lookup around dates and `PROC EXPAND` calculations for simple, weighted and exponentially weighted averages; the explicit EWMA alpha in that artifact is `0.37`, while the WMA uses a long custom weight sequence. fileciteturn5file0L2-L4 The translated Python module says it consolidates the repository's bootstrap, fair-coin Markov, moving-average, moving-block bootstrap, and hash/path logic, and implements `compute_moving_averages`, autoregressive block bootstrap and path reconstruction functions. fileciteturn9file0L2-L7</span>

<span style='color:#c45b00;'>    The `Fair coins` artifact is particularly relevant to the proposed state lattice: it explicitly defines rows as current states, columns as next states, propagates a state distribution by multiplying it by \(P\), and repeatedly computes</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    s_{t+1}=s_tP.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    fileciteturn14file0L2-L4 That mechanism maps almost directly to a market regime matrix once empirical transition probabilities replace coin-transition probabilities.</span>

<span style='color:#c45b00;'>    The `Dynamic Geometric Spaces` notes contain the ideas that now need to be made falsifiable: `tanh`, the derivative \(1-f^2\), `sech(wavelet)`, phase and group velocity, a Legendre differential equation, covariance dynamics, RBF kernels, cluster analysis, geometric modeling, HMM/ARIMAX, velocity and acceleration formulas, and path/geometric hypotheses. fileciteturn10file0L1-L2 The correct research response is not to accept all of those physical analogies; it is to translate each into an empirical statistic with a null model.</span>

<span style='color:#c45b00;'>    **Data schema.** Each raw 10-minute record should contain at minimum</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    ticker</span>
<span style='color:#c45b00;'>    datetime_utc</span>
<span style='color:#c45b00;'>    datetime_exchange</span>
<span style='color:#c45b00;'>    session_date</span>
<span style='color:#c45b00;'>    open</span>
<span style='color:#c45b00;'>    high</span>
<span style='color:#c45b00;'>    low</span>
<span style='color:#c45b00;'>    close</span>
<span style='color:#c45b00;'>    volume</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    with optional bid/ask or Tiingo liquidity-reference fields when available. Tiingo's current consolidated intraday documentation describes historical intraday OHLCV with minute/hour resampling and liquidity/reference metrics, while its IEX documentation separately describes historical OHLC and IEX-specific volume. citeturn0search5turn0search0</span>

<span style='color:#c45b00;'>    Do **not** restrict estimation history to the one month that is plotted. A normal U.S. regular session has only a few dozen 10-minute observations per day, so covariance, nonlinear state transitions, RF training and diffusion estimation need substantially more historical observations than the display interval. The report can remain one month while the fit window uses much longer history. This follows directly from the high-dimensional estimation problem that motivates covariance shrinkage. citeturn0search1</span>

<span style='color:#c45b00;'>    A canonical panel should be indexed as</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    X[t,i,f],</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    where \(t\) is a 10-minute timestamp, \(i\) is a stock, and \(f\) is a feature.</span>

<span style='color:#c45b00;'>    Missing bars should not automatically be force-filled for statistical estimation. A synthetic zero return can create false autocorrelation and correlation. Maintain both a raw activity mask</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    A_{i,t}\in\{0,1\}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and an aligned analytical matrix. This is especially important at high frequency because Epps showed that measured stock comovement changes materially as the sampling interval shortens, and subsequent work has identified asynchronous observations as an important contributor. citeturn4search13turn0academia48</span>

<span style='color:#c45b00;'>    The initial repository structure should become:</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    Py14aK/</span>
<span style='color:#c45b00;'>    ├── sas/</span>
<span style='color:#c45b00;'>    │   ├── moving_averages.sas</span>
<span style='color:#c45b00;'>    │   ├── ichimoku.sas</span>
<span style='color:#c45b00;'>    │   ├── markov_lattice.sas</span>
<span style='color:#c45b00;'>    │   └── validation_freq.sas</span>
<span style='color:#c45b00;'>    ├── src/</span>
<span style='color:#c45b00;'>    │   ├── data/</span>
<span style='color:#c45b00;'>    │   │   ├── tiingo.py</span>
<span style='color:#c45b00;'>    │   │   ├── sessions.py</span>
<span style='color:#c45b00;'>    │   │   └── transactions.py</span>
<span style='color:#c45b00;'>    │   ├── features/</span>
<span style='color:#c45b00;'>    │   │   ├── linear.py</span>
<span style='color:#c45b00;'>    │   │   ├── tanh_bank.py</span>
<span style='color:#c45b00;'>    │   │   ├── derivatives.py</span>
<span style='color:#c45b00;'>    │   │   ├── volatility.py</span>
<span style='color:#c45b00;'>    │   │   └── ichimoku.py</span>
<span style='color:#c45b00;'>    │   ├── risk/</span>
<span style='color:#c45b00;'>    │   │   ├── covariance.py</span>
<span style='color:#c45b00;'>    │   │   ├── factors.py</span>
<span style='color:#c45b00;'>    │   │   └── residuals.py</span>
<span style='color:#c45b00;'>    │   ├── geometry/</span>
<span style='color:#c45b00;'>    │   │   ├── kernel.py</span>
<span style='color:#c45b00;'>    │   │   ├── diffusion.py</span>
<span style='color:#c45b00;'>    │   │   ├── poincare.py</span>
<span style='color:#c45b00;'>    │   │   └── neighbours.py</span>
<span style='color:#c45b00;'>    │   ├── dynamics/</span>
<span style='color:#c45b00;'>    │   │   ├── markov.py</span>
<span style='color:#c45b00;'>    │   │   ├── lyapunov.py</span>
<span style='color:#c45b00;'>    │   │   ├── fractional.py</span>
<span style='color:#c45b00;'>    │   │   ├── kramers_moyal.py</span>
<span style='color:#c45b00;'>    │   │   └── morse.py</span>
<span style='color:#c45b00;'>    │   ├── models/</span>
<span style='color:#c45b00;'>    │   │   ├── random_forest.py</span>
<span style='color:#c45b00;'>    │   │   ├── woe_iv.py</span>
<span style='color:#c45b00;'>    │   │   └── ensemble.py</span>
<span style='color:#c45b00;'>    │   ├── portfolio/</span>
<span style='color:#c45b00;'>    │   │   ├── optimize.py</span>
<span style='color:#c45b00;'>    │   │   ├── costs.py</span>
<span style='color:#c45b00;'>    │   │   └── backtest.py</span>
<span style='color:#c45b00;'>    │   └── reporting/</span>
<span style='color:#c45b00;'>    │       └── charts.py</span>
<span style='color:#c45b00;'>    ├── notebooks/</span>
<span style='color:#c45b00;'>    │   ├── feature_audit.ipynb</span>
<span style='color:#c45b00;'>    │   ├── factor_geometry.ipynb</span>
<span style='color:#c45b00;'>    │   ├── stochastic_surface.ipynb</span>
<span style='color:#c45b00;'>    │   └── portfolio_walkforward.ipynb</span>
<span style='color:#c45b00;'>    └── outputs/</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    A reproducible local ingestion command should look like:</span>

<span style='color:#c45b00;'>    ```bash</span>
<span style='color:#c45b00;'>    export TIINGO_API_KEY=&quot;YOUR_LOCAL_TOKEN&quot;</span>

<span style='color:#c45b00;'>    python -m src.data.tiingo \</span>
<span style='color:#c45b00;'>    --universe config/universe.csv \</span>
<span style='color:#c45b00;'>    --bar-size 10min \</span>
<span style='color:#c45b00;'>    --start 2025-01-01 \</span>
<span style='color:#c45b00;'>    --end 2026-08-24 \</span>
<span style='color:#c45b00;'>    --output data/ohlcv_10min.parquet</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    Tiingo requires a token for API access and currently documents both historical IEX and consolidated intraday endpoints. citeturn0search0turn0search5turn0search18</span>

<span style='color:#c45b00;'>    ## Feature and state engine</span>

<span style='color:#c45b00;'>    The feature engine should explicitly implement your idea of **linear/autocovariant structure first, nonlinearity second**.</span>

<span style='color:#c45b00;'>    Let</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    r_{i,t}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \log P_{i,t}-\log P_{i,t-1}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Construct multiscale returns,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    r_{i,t}^{(h)}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \log P_{i,t}</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \log P_{i,t-h},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    for candidate horizons</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    h\in\{1,3,6,9,13,26,39,52,78\}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    On 10-minute observations these span immediate motion through intraday and multi-session structures.</span>

<span style='color:#c45b00;'>    The first state is **not nonlinear**:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    X_{i,t}^{L}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    [</span>
<span style='color:#c45b00;'>    r^{(1)},</span>
<span style='color:#c45b00;'>    r^{(3)},</span>
<span style='color:#c45b00;'>    r^{(6)},</span>
<span style='color:#c45b00;'>    SMA,</span>
<span style='color:#c45b00;'>    EMA,</span>
<span style='color:#c45b00;'>    v,</span>
<span style='color:#c45b00;'>    a,</span>
<span style='color:#c45b00;'>    \sigma,</span>
<span style='color:#c45b00;'>    \text{range},</span>
<span style='color:#c45b00;'>    \text{volume},</span>
<span style='color:#c45b00;'>    \text{Ichimoku}</span>
<span style='color:#c45b00;'>    ].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    SMA and EMA should be retained because they are interpretable low-pass filters and because the repository already has both SAS and Python implementations. fileciteturn5file0L2-L4 fileciteturn9file0L2-L7</span>

<span style='color:#c45b00;'>    For derivative-like information, use **causal local polynomial fits**, not naïve second differences. Savitzky and Golay's original method estimates smoothed values and derivatives through local least-squares polynomial procedures. citeturn4search0 For trading, however, the ordinary centered filter must be modified to use only information available at \(t\).</span>

<span style='color:#c45b00;'>    Fit on the trailing window:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    x(t-k)</span>
<span style='color:#c45b00;'>    \approx</span>
<span style='color:#c45b00;'>    a_0+a_1(-k\Delta t)+a_2(-k\Delta t)^2+a_3(-k\Delta t)^3.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Then</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    v_t=a_1,\qquad</span>
<span style='color:#c45b00;'>    a_t=2a_2,\qquad</span>
<span style='color:#c45b00;'>    j_t=6a_3.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Candidate settings:</span>

<span style='color:#c45b00;'>    | Feature | Parameter grid | Purpose | Complexity per series | Principal failure |</span>
<span style='color:#c45b00;'>    |---|---|---|---:|---|</span>
<span style='color:#c45b00;'>    | SMA | 3, 6, 9, 13, 26, 39, 52 | slow/fast level | \(O(T)\) with rolling sums | lag |</span>
<span style='color:#c45b00;'>    | EMA | half-life 3, 6, 13, 39, 195 bars | adaptive trend | \(O(T)\) | arbitrary decay |</span>
<span style='color:#c45b00;'>    | Local polynomial | trailing 7, 9, 13, 21; degree 2–3 | velocity/acceleration | \(O(Twp^2)\), reducible with fixed filter coefficients | derivative noise, edge bias |</span>
<span style='color:#c45b00;'>    | Realized volatility | 6, 13, 39, 78, 195 | local risk | \(O(T)\) | jumps/microstructure contamination |</span>
<span style='color:#c45b00;'>    | Ichimoku | 9/26/52 | range equilibrium/state | \(O(T)\) with rolling extrema | displaced plotting values can cause leakage |</span>
<span style='color:#c45b00;'>    | FFT/wavelet | window 128–1024 bars | scale diagnostics | FFT \(O(T\log T)\) | nonstationarity/leakage |</span>
<span style='color:#c45b00;'>    | Fractional features | rolling long-memory windows | persistent memory | implementation dependent | spurious \(H\) from regime changes |</span>

<span style='color:#c45b00;'>    The FFT is computationally real—Cooley and Tukey's algorithm reduced Fourier-series calculation to the now-familiar fast transform structure—but frequencies should be interpreted as observed time scales rather than literal market wavelengths. citeturn4search7turn4search19 Wavelets are the stronger multiscale challenger because Mallat's framework explicitly constructs resolution-dependent representations through translated and dilated bases. citeturn8search0</span>

<span style='color:#c45b00;'>    **Normalization must be causal.** For each continuous feature \(x_{i,t}\), fit robust scale from past observations only:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    z_{i,t}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{x_{i,t}-\operatorname{median}_{\mathcal W_t}(x_i)}</span>
<span style='color:#c45b00;'>    {1.4826\,MAD_{\mathcal W_t}(x_i)+\epsilon}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Maintain two normalizations rather than conflating them:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    z^{TS}_{i,t}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    for a stock's own historical state, and</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    z^{XS}_{i,t}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    for its contemporaneous cross-sectional state relative to other stocks.</span>

<span style='color:#c45b00;'>    That distinction is important. A stock can be extreme relative to itself but ordinary relative to the market.</span>

<span style='color:#c45b00;'>    **The `tanh` bank should be explicitly dual-channel.** For each normalized input \(z\),</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    S_\beta(z)=\tanh(\beta z),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    with</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \beta\in\{0.25,0.5,1,2,4\}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Large \(\beta\) approximates a soft sign and therefore highlights persistent \(+/-\) pattern agreement. Small \(\beta\) retains substantially more amplitude sensitivity.</span>

<span style='color:#c45b00;'>    At the same time preserve strength:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    M(z)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \operatorname{sign}(z)\log(1+|z|)</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    or simply the robust \(z\) itself.</span>

<span style='color:#c45b00;'>    Add</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    G_\beta</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{\partial S_\beta}{\partial z}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \beta(1-S_\beta^2),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    plus</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \Delta S_\beta,\qquad</span>
<span style='color:#c45b00;'>    \Delta M.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    This directly fixes the loss you identified in the older `tanh` construction: **state synchronization and strength synchronization become separate quantities**. The repository's geometric notes explicitly contain the `tanh` derivative \(1-f^2\), making this an extension rather than a replacement of the original idea. fileciteturn10file0L1-L2</span>

<span style='color:#c45b00;'>    The nonlinear feature map is therefore</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \Phi_i(t)=</span>
<span style='color:#c45b00;'>    [</span>
<span style='color:#c45b00;'>    S_{0.25},</span>
<span style='color:#c45b00;'>    S_{0.5},</span>
<span style='color:#c45b00;'>    S_1,</span>
<span style='color:#c45b00;'>    S_2,</span>
<span style='color:#c45b00;'>    S_4,</span>
<span style='color:#c45b00;'>    M,</span>
<span style='color:#c45b00;'>    G_{0.25},\ldots,G_4,</span>
<span style='color:#c45b00;'>    \Delta S,</span>
<span style='color:#c45b00;'>    \Delta M</span>
<span style='color:#c45b00;'>    ].</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Then compute not only ordinary covariance but a multiscale nonlinear cross-covariance:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    C_{ij}^{ab}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \operatorname{Cov}</span>
<span style='color:#c45b00;'>    [</span>
<span style='color:#c45b00;'>    S_{\beta_a,i},</span>
<span style='color:#c45b00;'>    S_{\beta_b,j}</span>
<span style='color:#c45b00;'>    ],</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and the lagged version</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \Gamma_{ij}^{ab}(\ell)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \operatorname{Cov}</span>
<span style='color:#c45b00;'>    [</span>
<span style='color:#c45b00;'>    S_{\beta_a,i,t},</span>
<span style='color:#c45b00;'>    S_{\beta_b,j,t+\ell}</span>
<span style='color:#c45b00;'>    ].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    This is especially relevant at 10-minute frequency because zero-lag correlation can decline or shift with sampling interval and lead/lag structure; the original Epps result found decreasing short-interval comovement, and later studies explicitly analyzed asynchronous effects. citeturn4search13turn0academia48</span>

<span style='color:#c45b00;'>    A compact implementation:</span>

<span style='color:#c45b00;'>    ```python</span>
<span style='color:#c45b00;'>    import numpy as np</span>
<span style='color:#c45b00;'>    import pandas as pd</span>

<span style='color:#c45b00;'>    BETAS = np.array([0.25, 0.5, 1.0, 2.0, 4.0])</span>

<span style='color:#c45b00;'>    def rolling_robust_z(</span>
<span style='color:#c45b00;'>        s: pd.Series,</span>
<span style='color:#c45b00;'>        window: int = 390,</span>
<span style='color:#c45b00;'>        min_periods: int = 78,</span>
<span style='color:#c45b00;'>    ) -&gt; pd.Series:</span>
<span style='color:#c45b00;'>        &quot;&quot;&quot;Past-only rolling robust z-score.&quot;&quot;&quot;</span>
<span style='color:#c45b00;'>        med = s.shift(1).rolling(window, min_periods=min_periods).median()</span>
<span style='color:#c45b00;'>        mad = (</span>
<span style='color:#c45b00;'>            (s.shift(1) - med)</span>
<span style='color:#c45b00;'>            .abs()</span>
<span style='color:#c45b00;'>            .rolling(window, min_periods=min_periods)</span>
<span style='color:#c45b00;'>            .median()</span>
<span style='color:#c45b00;'>        )</span>
<span style='color:#c45b00;'>        return (s - med) / (1.4826 * mad + 1e-12)</span>


<span style='color:#c45b00;'>    def tanh_bank(z: pd.Series) -&gt; pd.DataFrame:</span>
<span style='color:#c45b00;'>        x = z.to_numpy(dtype=float)</span>
<span style='color:#c45b00;'>        out = {}</span>

<span style='color:#c45b00;'>        for beta in BETAS:</span>
<span style='color:#c45b00;'>            s = np.tanh(beta * x)</span>
<span style='color:#c45b00;'>            out[f&quot;tanh_{beta:g}&quot;] = s</span>
<span style='color:#c45b00;'>            out[f&quot;sensitivity_{beta:g}&quot;] = beta * (1.0 - s * s)</span>
<span style='color:#c45b00;'>            out[f&quot;dtanh_{beta:g}&quot;] = pd.Series(s, index=z.index).diff().to_numpy()</span>

<span style='color:#c45b00;'>        # Parallel magnitude channel prevents saturation from erasing strength.</span>
<span style='color:#c45b00;'>        out[&quot;strength&quot;] = np.sign(x) * np.log1p(np.abs(x))</span>
<span style='color:#c45b00;'>        out[&quot;dstrength&quot;] = pd.Series(out[&quot;strength&quot;], index=z.index).diff().to_numpy()</span>

<span style='color:#c45b00;'>        return pd.DataFrame(out, index=z.index)</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    For Ichimoku, use the supplied 9/26/52 rolling maxima/minima, but enforce a strict distinction between a **plot displacement** and a **predictor**. A Chikou value requiring future close when aligned on today's timestamp cannot enter a causal forecast. Similarly, the cloud that affects today's decision must be the cloud calculable from information available by today.</span>

<span style='color:#c45b00;'>    The first feature deliverable should therefore be:</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    outputs/features_10min.parquet</span>
<span style='color:#c45b00;'>    outputs/feature_dictionary.csv</span>
<span style='color:#c45b00;'>    outputs/feature_missingness.csv</span>
<span style='color:#c45b00;'>    outputs/feature_autocovariance.csv</span>
<span style='color:#c45b00;'>    outputs/tanh_covariance_tensor.npz</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    with a synchronized state chart containing price/account return, SMA/EMA, velocity, acceleration, volatility, Ichimoku state, tanh state and strength.</span>

<span style='color:#c45b00;'>    ## Dependence geometry, covariance and embeddings</span>

<span style='color:#c45b00;'>    The linear dependence layer is the anchor of the whole project.</span>

<span style='color:#c45b00;'>    Let</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    R_t=(r_{1,t},\ldots,r_{N,t})^\top.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Estimate three covariance matrices concurrently.</span>

<span style='color:#c45b00;'>    The rolling sample estimator is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \hat\Sigma_t^{roll}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{1}{W-1}</span>
<span style='color:#c45b00;'>    \sum_{s=t-W+1}^{t}</span>
<span style='color:#c45b00;'>    (R_s-\bar R)(R_s-\bar R)^\top.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    EWMA uses</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \hat\Sigma_t^{EWMA}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \lambda\hat\Sigma_{t-1}^{EWMA}</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    (1-\lambda)</span>
<span style='color:#c45b00;'>    (R_t-\mu_t)(R_t-\mu_t)^\top.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Rather than hard-coding arbitrary \(\lambda\), specify half-life \(h\):</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \lambda</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    2^{-1/h}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Test</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    h\in</span>
<span style='color:#c45b00;'>    \{39,195,780\}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    bars, roughly corresponding to increasingly slow intraday/multi-session regimes.</span>

<span style='color:#c45b00;'>    Ledoit–Wolf shrinkage uses a convex combination between the sample covariance and a structured target. Ledoit and Wolf developed the estimator to improve conditioning and accuracy when the dimension is large relative to available observations. citeturn0search1turn0search6</span>

<span style='color:#c45b00;'>    | Covariance method | Hyperparameters | Update cost | Robustness | Portfolio role |</span>
<span style='color:#c45b00;'>    |---|---|---:|---|---|</span>
<span style='color:#c45b00;'>    | Rolling sample | \(W=195,390,780,1560\) | \(O(N^2)\) incremental | Low–medium | diagnostic |</span>
<span style='color:#c45b00;'>    | EWMA | half-life 39,195,780 | \(O(N^2)\) | Medium | fast regime risk |</span>
<span style='color:#c45b00;'>    | Ledoit–Wolf | estimated shrinkage | \(O(TN^2)\) fit | High relative to raw sample | primary optimization matrix |</span>
<span style='color:#c45b00;'>    | Nonlinear Ledoit–Wolf challenger | bandwidth/eigen corrections | higher | potentially high in high-dimensional setting | research |</span>
<span style='color:#c45b00;'>    | Factor covariance | factor count \(K\) | \(O(TNK+K^3)\) | high if factors stable | large universe |</span>

<span style='color:#c45b00;'>    The nonlinear shrinkage literature extends linear shrinkage by transforming sample eigenvalues nonlinearly, and Ledoit and Wolf report improvements over both raw and linear-shrinkage estimators in their asymptotic/Monte Carlo framework. citeturn0search13</span>

<span style='color:#c45b00;'>    Next perform eigendecomposition:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \hat\Sigma_t</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    V_t\Lambda_tV_t^\top.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Choose \(K\) with a combination of explained variance, cross-validation and eigenvalue stability rather than a fixed percentage alone.</span>

<span style='color:#c45b00;'>    The factor representation is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    F_t</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    V_K^\top R_t.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    For each stock:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    r_{i,t}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \alpha_i</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \sum_{k=1}^K</span>
<span style='color:#c45b00;'>    \beta_{ik}F_{k,t}</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \epsilon_{i,t}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The critical object is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{\epsilon_{i,t}},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    because it separates common linear motion from stock-specific/residual structure.</span>

<span style='color:#c45b00;'>    The portfolio beta vector is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \beta_p</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    B^\top w.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    This enables explicit decisions such as</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    B^\top w=0</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    for selected factor-neutral portfolios, rather than confusing “non-beta” with “non-Euclidean.”</span>

<span style='color:#c45b00;'>    A particularly useful extension of your “autocovariant first” idea is the lagged generalized eigenproblem</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    C_\tau v</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \lambda C_0v,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    where</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    C_0=E[X_tX_t^\top],\qquad</span>
<span style='color:#c45b00;'>    C_\tau=E[X_tX_{t+\tau}^\top].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Those vectors isolate linear directions that remain coherent through time rather than merely explaining instantaneous variance. Compare them with ordinary PCA factors before entering a nonlinear model.</span>

<span style='color:#c45b00;'>    **Reverse-correlated securities** should be discovered after factor stripping. Rank candidates using</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \rho_{ij}^{raw},</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    \rho_{ij}^{residual},</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    \rho_{ij}^{partial},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    plus lagged correlations</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \rho_{ij}(\ell).</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    A candidate hedge that looks unrelated in raw correlation but strongly negatively correlated in \(\epsilon\)-space can be more interesting than a security chosen manually because it belongs to the same named sector.</span>

<span style='color:#c45b00;'>    Then establish nonlinear baselines.</span>

<span style='color:#c45b00;'>    Kernel PCA applies ordinary PCA in an implicit feature space defined by a kernel; Schölkopf, Smola and Müller formulated this as a kernel eigenvalue problem. citeturn1search16</span>

<span style='color:#c45b00;'>    For an RBF kernel,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    K_{ab}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \exp</span>
<span style='color:#c45b00;'>    \left(</span>
<span style='color:#c45b00;'>    -\gamma</span>
<span style='color:#c45b00;'>    \|\Phi(X_a)-\Phi(X_b)\|^2</span>
<span style='color:#c45b00;'>    \right).</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Test</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \gamma</span>
<span style='color:#c45b00;'>    \in</span>
<span style='color:#c45b00;'>    \left\{</span>
<span style='color:#c45b00;'>    \frac{0.25}{m_d^2},</span>
<span style='color:#c45b00;'>    \frac{0.5}{m_d^2},</span>
<span style='color:#c45b00;'>    \frac1{m_d^2},</span>
<span style='color:#c45b00;'>    \frac2{m_d^2}</span>
<span style='color:#c45b00;'>    \right\},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    where \(m_d\) is a robust median pairwise distance. This avoids meaningless absolute \(\gamma\) values after feature-scale changes.</span>

<span style='color:#c45b00;'>    Diffusion maps should be the next challenger. Coifman and Lafon's formulation builds a Markov matrix from local similarities and uses its eigenfunctions as coordinates, producing multiscale diffusion distances. citeturn1search3turn1search13 For market states, that is conceptually attractive because it asks whether two states are connected through many high-probability local paths, not just whether their coordinate vectors are close.</span>

<span style='color:#c45b00;'>    The Poincaré pipeline comes only after those baselines.</span>

<span style='color:#c45b00;'>    Given a low-dimensional vector</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    z\in\mathbb R^d,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    map from the tangent space at the origin into curvature \(-c\) Poincaré space:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    y=</span>
<span style='color:#c45b00;'>    \exp_0^c(z)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \tanh(\sqrt c\|z\|)</span>
<span style='color:#c45b00;'>    \frac{z}</span>
<span style='color:#c45b00;'>    {\sqrt c\|z\|}</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    with \(y=0\) at \(z=0\).</span>

<span style='color:#c45b00;'>    Then</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \|y\|&lt;1/\sqrt c.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Distance can be written through Möbius addition as</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    d_c(x,y)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{2}{\sqrt c}</span>
<span style='color:#c45b00;'>    \operatorname{artanh}</span>
<span style='color:#c45b00;'>    \left(</span>
<span style='color:#c45b00;'>    \sqrt c\,\|-x\oplus_c y\|</span>
<span style='color:#c45b00;'>    \right).</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    But this deterministic exponential map **does not prove anything is hyperbolic**. Nickel and Kiela's Poincaré method was designed to learn hierarchical representations via Riemannian optimization; our market hypothesis must be validated against Euclidean alternatives. citeturn1search5turn1search9</span>

<span style='color:#c45b00;'>    Test curvature</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    c\in\{0.01,0.1,0.5,1,2,5\}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Select it entirely inside training/validation windows using:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{kNN Jaccard stability},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{next-state log loss},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{forward residual-return rank IC},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and eventual portfolio utility.</span>

<span style='color:#c45b00;'>    For each stock \(i\), find</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    N_k(i,t),</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    k\in\{5,8,12,16\}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Your original \(k=8\) becomes an explicit candidate, not a sacred constant.</span>

<span style='color:#c45b00;'>    The “gravity center” becomes a weighted Fréchet mean:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    m_i(t)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \arg\min_z</span>
<span style='color:#c45b00;'>    \sum_{j\in N_k(i,t)}</span>
<span style='color:#c45b00;'>    w_jd^2(z,y_j(t)).</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Use three mass definitions as challengers:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    w_j=1/k,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    w_j\propto1/\hat\sigma_{\epsilon,j}^2,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    w_j\propto |w_j^{portfolio}|.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Then calculate</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    D_i(t)=d(y_i(t),m_i(t)),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \Delta D_i(t),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and local dispersion</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    R_i^2(t)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{\sum_jw_jd^2(y_j,m_i)}</span>
<span style='color:#c45b00;'>    {\sum_jw_j}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Those are defensible “N-body” statistics.</span>

<span style='color:#c45b00;'>    Literal Newtonian gravity should remain an optional diagnostic:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    U(t)=</span>
<span style='color:#c45b00;'>    -\sum_{i&lt;j}</span>
<span style='color:#c45b00;'>    \frac{Gm_im_j}</span>
<span style='color:#c45b00;'>    {\sqrt{d_{ij}^2+\varepsilon^2}},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    because the market supplies no conservation law that justifies a physical \(1/r\) force. A more statistically defensible N-body feature is the pair-distance spectrum, local simplex volume, neighborhood radius, graph energy, neighbor turnover and covariance log-determinant.</span>

<span style='color:#c45b00;'>    | Representation | Main parameter | Approximate scaling | Robustness expectation | Gate to production |</span>
<span style='color:#c45b00;'>    |---|---|---:|---|---|</span>
<span style='color:#c45b00;'>    | PCA | \(K\) | \(O(TN^2+N^3)\) | high baseline | required |</span>
<span style='color:#c45b00;'>    | Lagged covariance subspace | \(\tau,K\) | \(O(Tp^2+p^3)\) | medium–high | required challenger |</span>
<span style='color:#c45b00;'>    | RBF kernel PCA | \(\gamma,m\) samples | \(O(m^2p+m^3)\) exact | medium | incremental OOS value |</span>
<span style='color:#c45b00;'>    | Diffusion maps | bandwidth, neighbors | sparse \(O(mk)\) graph + eigensolve | medium–high if local structure real | stable diffusion spectrum |</span>
<span style='color:#c45b00;'>    | Poincaré | \(c,d\) | distance \(O(md)\); learning more costly | unknown | must beat Euclidean/Mahalanobis |</span>
<span style='color:#c45b00;'>    | kNN | \(k\) | brute \(O(mNd)\), indexed lower in favorable dimensions | medium | neighbor stability |</span>
<span style='color:#c45b00;'>    | Fréchet mean | iterations, weights | \(O(kdI)\) locally | medium | stable center |</span>
<span style='color:#c45b00;'>    | N-body diagnostics | neighborhood size | \(O(k^2d)\) local / \(O(N^2d)\) global | exploratory | regime value OOS |</span>

<span style='color:#c45b00;'>    The principal geometry charts are:</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    corr_rolling_heatmap.png</span>
<span style='color:#c45b00;'>    corr_ewma_heatmap.png</span>
<span style='color:#c45b00;'>    corr_ledoitwolf_heatmap.png</span>
<span style='color:#c45b00;'>    pca_eigenvalue_timeline.png</span>
<span style='color:#c45b00;'>    pca_loading_heatmap.png</span>
<span style='color:#c45b00;'>    residual_corr_heatmap.png</span>
<span style='color:#c45b00;'>    kernel_pca_2d.png</span>
<span style='color:#c45b00;'>    diffusion_map_2d.png</span>
<span style='color:#c45b00;'>    poincare_2d.html</span>
<span style='color:#c45b00;'>    poincare_3d.html</span>
<span style='color:#c45b00;'>    knn_neighbour_turnover.png</span>
<span style='color:#c45b00;'>    local_barycentre_distance.png</span>
<span style='color:#c45b00;'>    nbody_dispersion.png</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    No Poincaré chart should be labelled “market manifold.” The correct label is **hyperbolic state embedding challenger**.</span>

<span style='color:#c45b00;'>    ## Stochastic dynamics, Markov structure and nonlinear regime tests</span>

<span style='color:#c45b00;'>    The `PROC FREQ` idea should become the simplest forward stochastic model in the stack.</span>

<span style='color:#c45b00;'>    Start with a deliberately small state lattice. For example:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    S_t</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    (</span>
<span style='color:#c45b00;'>    q_{\text{tanh}},</span>
<span style='color:#c45b00;'>    q_{\text{strength}},</span>
<span style='color:#c45b00;'>    q_{\sigma}</span>
<span style='color:#c45b00;'>    ),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    where each coordinate has three bins:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \{-1,0,+1\}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    This creates at most</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    3^3=27</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    states.</span>

<span style='color:#c45b00;'>    Estimate</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    N_{ij}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \sum_t</span>
<span style='color:#c45b00;'>    1(S_t=i,S_{t+1}=j),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    P_{ij}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{N_{ij}+\alpha}</span>
<span style='color:#c45b00;'>    {\sum_jN_{ij}+K\alpha}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Use a small Dirichlet pseudocount such as</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \alpha\in\{0.1,0.5,1\}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    to avoid impossible zero-probability transitions.</span>

<span style='color:#c45b00;'>    Python analogue:</span>

<span style='color:#c45b00;'>    ```python</span>
<span style='color:#c45b00;'>    def transition_matrix(df, state_col=&quot;state&quot;):</span>
<span style='color:#c45b00;'>        x = df.sort_values([&quot;ticker&quot;, &quot;datetime&quot;]).copy()</span>
<span style='color:#c45b00;'>        x[&quot;next_state&quot;] = x.groupby(&quot;ticker&quot;)[state_col].shift(-1)</span>
<span style='color:#c45b00;'>        x = x.dropna(subset=[&quot;next_state&quot;])</span>

<span style='color:#c45b00;'>        counts = pd.crosstab(x[state_col], x[&quot;next_state&quot;])</span>
<span style='color:#c45b00;'>        counts = counts.astype(float)</span>

<span style='color:#c45b00;'>        alpha = 0.5</span>
<span style='color:#c45b00;'>        counts += alpha</span>

<span style='color:#c45b00;'>        P = counts.div(counts.sum(axis=1), axis=0)</span>
<span style='color:#c45b00;'>        return counts, P</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    SAS analogue:</span>

<span style='color:#c45b00;'>    ```sas</span>
<span style='color:#c45b00;'>    proc sort data=work.states out=work.states_desc;</span>
<span style='color:#c45b00;'>        by ticker descending datetime;</span>
<span style='color:#c45b00;'>    run;</span>

<span style='color:#c45b00;'>    /* In descending time, LAG(state) is the chronological next state. */</span>
<span style='color:#c45b00;'>    data work.transitions;</span>
<span style='color:#c45b00;'>        set work.states_desc;</span>
<span style='color:#c45b00;'>        by ticker;</span>
<span style='color:#c45b00;'>        next_state = lag(state);</span>
<span style='color:#c45b00;'>        if first.ticker then next_state = .;</span>
<span style='color:#c45b00;'>        if not missing(next_state);</span>
<span style='color:#c45b00;'>    run;</span>

<span style='color:#c45b00;'>    proc freq data=work.transitions noprint;</span>
<span style='color:#c45b00;'>        tables state * next_state / out=work.transition_counts;</span>
<span style='color:#c45b00;'>    run;</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The existing Py14aK `Fair coins` program already demonstrates explicit transition matrices and repeated propagation \(s_{t+1}=s_tP\), while `risk_translated.py` includes a Python translation of that logic. fileciteturn14file0L2-L4 fileciteturn9file0L2-L7</span>

<span style='color:#c45b00;'>    Forward distributions are</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \pi_{t+h}=\pi_tP^h.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The transition graph should store on each node:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{occupancy},</span>
<span style='color:#c45b00;'>    \quad</span>
<span style='color:#c45b00;'>    E[r_{t+h}\mid S_t],</span>
<span style='color:#c45b00;'>    \quad</span>
<span style='color:#c45b00;'>    \sigma[r_{t+h}\mid S_t],</span>
<span style='color:#c45b00;'>    \quad</span>
<span style='color:#c45b00;'>    P(r_{t+h}&gt;c\mid S_t),</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and on each edge:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    P_{ij}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The requested “boxes/pixels” visualization then becomes precise: cell area is occupancy, cell shade is conditional forward return, uncertainty controls outline/opacity, and transition probability determines edge width.</span>

<span style='color:#c45b00;'>    **Hurst and fractional differencing.** Mandelbrot and Van Ness formalized fractional Brownian motion and fractional noise, while Granger and Joyeux introduced fractional differencing via the expansion of \((1-B)^d\) for long-memory time-series models. citeturn2search3turn5search0 Geweke and Porter-Hudak subsequently proposed a low-frequency log-periodogram estimator for the long-memory parameter. citeturn5search2</span>

<span style='color:#c45b00;'>    Test Hurst/memory on returns, absolute returns, squared returns, residual returns and volatility separately. Do **not** infer that \(H&gt;1/2\) automatically gives a tradeable price trend.</span>

<span style='color:#c45b00;'>    Fractional differencing is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    (1-L)^dx_t</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \sum_{k=0}^{\infty}</span>
<span style='color:#c45b00;'>    (-1)^k</span>
<span style='color:#c45b00;'>    {d\choose k}</span>
<span style='color:#c45b00;'>    x_{t-k}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Test</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    d\in</span>
<span style='color:#c45b00;'>    \{0,0.1,0.2,\ldots,0.9\}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    inside each training fold and choose the smallest \(d\) that materially improves stationarity while preserving signal stability. The original Granger–Joyeux formulation is specifically an infinite fractional filter, which is why truncation error and low-frequency behavior must be monitored. citeturn5search0</span>

<span style='color:#c45b00;'>    **Chaos diagnostics require hostile null tests.** Rosenstein, Collins and De Luca proposed estimating the largest Lyapunov exponent from divergence of nearby reconstructed trajectories. citeturn1search0turn1search11 For a scalar regime series \(x_t\), form delay vectors</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    X_t=</span>
<span style='color:#c45b00;'>    (x_t,x_{t-\tau},\ldots,x_{t-(m-1)\tau})</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and estimate</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \lambda</span>
<span style='color:#c45b00;'>    \approx</span>
<span style='color:#c45b00;'>    \frac{d}{dt}</span>
<span style='color:#c45b00;'>    E[</span>
<span style='color:#c45b00;'>    \log d(X_t,X_t^\text{neighbor})</span>
<span style='color:#c45b00;'>    ].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Test candidate</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    m\in\{3,4,5,6,8\},</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    \tau</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    from autocorrelation or mutual-information scales.</span>

<span style='color:#c45b00;'>    But a positive estimated Lyapunov slope is **not sufficient evidence of deterministic chaos** in financial data. Repeat the same estimator on:</span>

<span style='color:#c45b00;'>    1. shuffled returns;</span>
<span style='color:#c45b00;'>    2. phase-randomized surrogates;</span>
<span style='color:#c45b00;'>    3. Gaussian correlated Brownian simulations;</span>
<span style='color:#c45b00;'>    4. fitted stochastic-volatility/GARCH-like simulations;</span>
<span style='color:#c45b00;'>    5. block-bootstrap data.</span>

<span style='color:#c45b00;'>    The existing Py14aK translation already contains moving-block bootstrap machinery, making this null-testing program particularly natural. fileciteturn9file0L2-L7</span>

<span style='color:#c45b00;'>    **Kramers–Moyal/stochastic surface estimation** is one of the more interesting research branches because it can be stated without pretending the raw path is differentiable.</span>

<span style='color:#c45b00;'>    For low-dimensional state \(X_t\),</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    D_i^{(1)}(x)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \lim_{\Delta t\to0}</span>
<span style='color:#c45b00;'>    \frac{</span>
<span style='color:#c45b00;'>    E[\Delta X_i\mid X_t=x]</span>
<span style='color:#c45b00;'>    }{\Delta t},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    D_{ij}^{(2)}(x)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac12</span>
<span style='color:#c45b00;'>    \lim_{\Delta t\to0}</span>
<span style='color:#c45b00;'>    \frac{</span>
<span style='color:#c45b00;'>    E[\Delta X_i\Delta X_j\mid X_t=x]</span>
<span style='color:#c45b00;'>    }{\Delta t}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    A recent APS study reconstructs multivariate Langevin drift and diffusion nonparametrically through Kramers–Moyal coefficients and demonstrates the framework on financial-market examples; earlier finance-oriented Langevin work likewise estimated financial potential structures. citeturn8search1turn8search2</span>

<span style='color:#c45b00;'>    Estimate those fields with local-kernel regression in **two or three dimensions first**. High-dimensional Kramers–Moyal estimation will suffer severe sample sparsity.</span>

<span style='color:#c45b00;'>    The resulting stochastic model is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    dX_t</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    b(X_t)\,dt</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \sigma(X_t)\,dW_t,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    with</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    b=D^{(1)},</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    a=\sigma\sigma^\top=2D^{(2)}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The associated Fokker–Planck form is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \frac{\partial p}{\partial t}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    -\sum_i</span>
<span style='color:#c45b00;'>    \partial_i(b_ip)</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \frac12</span>
<span style='color:#c45b00;'>    \sum_{ij}</span>
<span style='color:#c45b00;'>    \partial_i\partial_j(a_{ij}p).</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    This produces the requested **Brownian/stochastic surfaces**:</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    drift_surface_D1.html</span>
<span style='color:#c45b00;'>    diffusion_surface_D2.html</span>
<span style='color:#c45b00;'>    conditional_density_surface.html</span>
<span style='color:#c45b00;'>    probability_current_surface.html</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The next question is whether the drift is approximately gradient-like.</span>

<span style='color:#c45b00;'>    Fit</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    b(x)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    -\nabla_gV(x)</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    r(x).</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Estimate \(V\) by minimizing, over a smooth basis,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \sum_n</span>
<span style='color:#c45b00;'>    \left\|</span>
<span style='color:#c45b00;'>    b(x_n)+g^{-1}(x_n)\nabla V(x_n)</span>
<span style='color:#c45b00;'>    \right\|^2</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \lambda_V\mathcal R[V].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The residual</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    r(x)</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    is the non-gradient/rotational component.</span>

<span style='color:#c45b00;'>    A still safer discrete version uses the kNN graph and performs a **graph Hodge decomposition** of edge flows into gradient and cyclic components. That avoids claiming a smooth manifold before the data justify one.</span>

<span style='color:#c45b00;'>    Only after this stage should we invoke Morse structure.</span>

<span style='color:#c45b00;'>    A smooth estimated \(V\) has a candidate critical point where</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \nabla V(x^\star)=0.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Calculate</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    H_V(x^\star)</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \nabla^2V(x^\star).</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    A candidate Morse critical point must be nondegenerate:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \det H_V(x^\star)\neq0.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Its index is the number of negative Hessian eigenvalues.</span>

<span style='color:#c45b00;'>    Bootstrap these critical points across historical windows. A “market basin” that disappears under tiny changes of the sample should not be interpreted as a metastable regime.</span>

<span style='color:#c45b00;'>    Witten's 1982 construction connects Morse theory with a supersymmetric deformation of differential operators and relates low-lying structure to critical points of a Morse function. citeturn9view0turn0search15 The optional research operator is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    d_\tau</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    e^{-\tau V}d\,e^{\tau V}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    d+\tau\,dV\wedge,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    with Witten Laplacian</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \Delta_\tau</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    d_\tau d_\tau^\dagger</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    d_\tau^\dagger d_\tau.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    This should **not** be a trading indicator. Its legitimate use here is as a metastability/topological challenger after a reproducible potential \(V\) has been estimated.</span>

<span style='color:#c45b00;'>    For rare state transitions, the appropriate link is Freidlin–Wentzell large-deviation theory. Their monograph explicitly develops the action functional for randomly perturbed dynamical systems. citeturn3search0turn3search2 For nonsingular diffusion,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    S[\phi]</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac12</span>
<span style='color:#c45b00;'>    \int</span>
<span style='color:#c45b00;'>    (\dot\phi-b(\phi))^\top</span>
<span style='color:#c45b00;'>    a(\phi)^{-1}</span>
<span style='color:#c45b00;'>    (\dot\phi-b(\phi))</span>
<span style='color:#c45b00;'>    \,dt.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Minimum-action paths between stable regimes become the rigorous version of the “instanton” idea.</span>

<span style='color:#c45b00;'>    The stochastic/chaos component comparison is:</span>

<span style='color:#c45b00;'>    | Method | Primary use | Parameters | Scaling | Main failure mode |</span>
<span style='color:#c45b00;'>    |---|---|---|---:|---|</span>
<span style='color:#c45b00;'>    | Markov lattice | discrete forward state | bins, \(\alpha\), horizon | \(O(T)\) | state explosion/nonstationarity |</span>
<span style='color:#c45b00;'>    | Hurst/GP-H | long memory | frequency range/window | near \(O(T\log T)\) | trends mimic memory |</span>
<span style='color:#c45b00;'>    | Fractional differencing | memory-preserving stationarity | \(d\), truncation | \(O(TL)\) | over-differencing |</span>
<span style='color:#c45b00;'>    | Rosenstein LLE | trajectory divergence | \(m,\tau,\) Theiler window | naive \(O(T^2)\) | stochastic noise mimics chaos |</span>
<span style='color:#c45b00;'>    | Kramers–Moyal | drift/diffusion surfaces | bandwidth, dimension | \(O(Tq)\) local or worse | curse of dimensionality |</span>
<span style='color:#c45b00;'>    | Gradient/rotational decomposition | equilibrium vs current | basis, regularization | basis-dependent | nonidentifiability |</span>
<span style='color:#c45b00;'>    | Morse analysis | stable points/saddles | smooth \(V\) | Hessian/basis dependent | unstable fake critical points |</span>
<span style='color:#c45b00;'>    | Freidlin–Wentzell | rare transition path | estimated \(b,a\) | numerically intensive | poor small-noise assumption |</span>
<span style='color:#c45b00;'>    | Witten layer | metastability/topology research | \(\tau,V\) | high | unjustified geometry/potential |</span>

<span style='color:#c45b00;'>    The key evaluation metric here is **stability**, not visual beauty:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{ID-stability}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \operatorname{CV}</span>
<span style='color:#c45b00;'>    [</span>
<span style='color:#c45b00;'>    \hat d_{\mathrm{intrinsic}}(t)</span>
<span style='color:#c45b00;'>    ],</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    plus critical-point bootstrap persistence, neighbor Jaccard stability, diffusion-eigenvalue stability and Markov transition drift.</span>

<span style='color:#c45b00;'>    ## Predictive models, portfolio optimization and backtesting</span>

<span style='color:#c45b00;'>    The predictive layer should be deliberately simpler than the feature layer.</span>

<span style='color:#c45b00;'>    The principal supervised targets should be residual returns rather than raw returns:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    y_{i,t}^{(h)}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \sum_{j=1}^{h}</span>
<span style='color:#c45b00;'>    \epsilon_{i,t+j},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and a cost-adjusted binary target:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    Y_{i,t}^{(h)}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    1[</span>
<span style='color:#c45b00;'>    y_{i,t}^{(h)}&gt;c_{i,t}^{trade}</span>
<span style='color:#c45b00;'>    ].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Test</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    h\in\{3,6,13,39\}</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    bars.</span>

<span style='color:#c45b00;'>    This prevents the RF from “predicting” a market beta that could have been handled transparently in the factor layer.</span>

<span style='color:#c45b00;'>    Random Forests are an appropriate nonlinear challenger because Breiman's construction combines randomized tree predictors and was explicitly designed to reduce the instability of individual trees through ensemble averaging. citeturn2search0</span>

<span style='color:#c45b00;'>    Candidate RF grid:</span>

<span style='color:#c45b00;'>    | Parameter | Grid |</span>
<span style='color:#c45b00;'>    |---|---|</span>
<span style='color:#c45b00;'>    | `n_estimators` | 500, 1000, 2000 |</span>
<span style='color:#c45b00;'>    | `max_depth` | 3, 5, 8, 12, None |</span>
<span style='color:#c45b00;'>    | `min_samples_leaf` | 20, 50, 100, 200 |</span>
<span style='color:#c45b00;'>    | `max_features` | `sqrt`, 0.3, 0.5, 0.7 |</span>
<span style='color:#c45b00;'>    | target horizon | 3, 6, 13, 39 bars |</span>
<span style='color:#c45b00;'>    | training lookback | 60, 120, 250 sessions |</span>
<span style='color:#c45b00;'>    | gap/embargo | at least forecast horizon |</span>

<span style='color:#c45b00;'>    The inner RF bootstrap should be treated carefully because adjacent 10-minute rows are dependent. Compare ordinary tree bootstrap against block/subsample variants informed by the repository's moving-block bootstrap functions. fileciteturn9file0L2-L7</span>

<span style='color:#c45b00;'>    The walk-forward structure is:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \text{train}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{validation}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{gap}</span>
<span style='color:#c45b00;'>    \rightarrow</span>
<span style='color:#c45b00;'>    \text{test}</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and every scaler, binning rule, PCA basis, covariance matrix, kernel bandwidth, Poincaré curvature, state definition and RF parameter is fit **inside the training segment**.</span>

<span style='color:#c45b00;'>    Overlapping forward-return labels require a gap at least as long as \(h\). Otherwise adjacent train/test observations share future prices.</span>

<span style='color:#c45b00;'>    WoE and Information Value should remain **screening diagnostics**, not the optimizer.</span>

<span style='color:#c45b00;'>    For bin \(b\),</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    WoE_b</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \log</span>
<span style='color:#c45b00;'>    \frac{</span>
<span style='color:#c45b00;'>    P(X\in b\mid Y=1)</span>
<span style='color:#c45b00;'>    }{</span>
<span style='color:#c45b00;'>    P(X\in b\mid Y=0)</span>
<span style='color:#c45b00;'>    }.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Then</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    IV</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \sum_b</span>
<span style='color:#c45b00;'>    \left[</span>
<span style='color:#c45b00;'>    P(X\in b\mid Y=1)</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    P(X\in b\mid Y=0)</span>
<span style='color:#c45b00;'>    \right]</span>
<span style='color:#c45b00;'>    WoE_b.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Fit bins on training data, freeze them, and compute</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    IV_{\text{train}},</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    IV_{\text{validation}},</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    IV_{\text{OOS}}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Do not rely on conventional generic “IV &gt; X is good” scorecard rules. The useful statistic here is stability:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{IV stability}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{</span>
<span style='color:#c45b00;'>    IV_{OOS}</span>
<span style='color:#c45b00;'>    }{</span>
<span style='color:#c45b00;'>    IV_{train}+\epsilon</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    along with preservation of WoE ordering/sign.</span>

<span style='color:#c45b00;'>    The feature gate should require at minimum one of:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{OOS IV stability},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{permutation importance stability},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{OOS rank correlation},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \text{incremental log-loss reduction}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The model ensemble then produces</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \hat\mu_{i,t}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    I would combine estimates conservatively:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \hat\mu</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \omega_M\hat\mu^{Markov}</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \omega_{RF}\hat\mu^{RF}</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \omega_K\hat\mu^{kernel}</span>
<span style='color:#c45b00;'>    +</span>
<span style='color:#c45b00;'>    \omega_D\hat\mu^{diffusion},</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    with</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \omega_j\ge0,\qquad</span>
<span style='color:#c45b00;'>    \sum_j\omega_j=1,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    and then shrink toward zero:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \tilde\mu</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \rho\hat\mu,</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    \rho\in[0,1].</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    The shrinkage \(\rho\) is selected by walk-forward portfolio performance; estimated returns are substantially less statistically stable than covariance and should not be allowed to overpower the risk model.</span>

<span style='color:#c45b00;'>    The production optimizer is:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \max_w</span>
<span style='color:#c45b00;'>    \left[</span>
<span style='color:#c45b00;'>    \tilde\mu_t^\top w</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \frac{\lambda}{2}</span>
<span style='color:#c45b00;'>    w^\top\hat\Sigma_t^{LW}w</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \eta\|w-w_{t-1}\|_1</span>
<span style='color:#c45b00;'>    -</span>
<span style='color:#c45b00;'>    \kappa</span>
<span style='color:#c45b00;'>    \|B_t^\top w-b^\star\|_2^2</span>
<span style='color:#c45b00;'>    \right].</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Markowitz's original formulation established the expected-return/variance portfolio framework. citeturn7search0 Here the additions explicitly address modern implementation problems: turnover, factor exposures and unstable forecasts.</span>

<span style='color:#c45b00;'>    Constraints:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \mathbf1^\top w=1,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    l_i\le w_i\le u_i,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \|w\|_1\le L,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    |B^\top w-b^\star|\le\delta,</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    |\Delta w_i|</span>
<span style='color:#c45b00;'>    \le</span>
<span style='color:#c45b00;'>    \text{liquidity limit}_i.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    For long-only research:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    0\le w_i\le 0.10</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    is a reasonable **grid candidate**, not a universal recommendation.</span>

<span style='color:#c45b00;'>    For a market-neutral experiment:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \mathbf1^\top w=0,</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    \|w\|_1=1,</span>
<span style='color:#c45b00;'>    \qquad</span>
<span style='color:#c45b00;'>    \beta_p\approx0.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    A CVaR challenger should minimize</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \operatorname{CVaR}_\alpha(L)</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    at</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \alpha\in\{0.95,0.975,0.99\}.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Rockafellar and Uryasev's formulation is the relevant optimization foundation. citeturn7search6</span>

<span style='color:#c45b00;'>    A compact Python objective:</span>

<span style='color:#c45b00;'>    ```python</span>
<span style='color:#c45b00;'>    import cvxpy as cp</span>
<span style='color:#c45b00;'>    import numpy as np</span>

<span style='color:#c45b00;'>    def optimize_portfolio(</span>
<span style='color:#c45b00;'>        mu: np.ndarray,</span>
<span style='color:#c45b00;'>        cov: np.ndarray,</span>
<span style='color:#c45b00;'>        w_prev: np.ndarray,</span>
<span style='color:#c45b00;'>        betas: np.ndarray | None = None,</span>
<span style='color:#c45b00;'>        target_beta: np.ndarray | None = None,</span>
<span style='color:#c45b00;'>        risk_aversion: float = 10.0,</span>
<span style='color:#c45b00;'>        turnover_penalty: float = 0.002,</span>
<span style='color:#c45b00;'>        factor_penalty: float = 5.0,</span>
<span style='color:#c45b00;'>        max_weight: float = 0.10,</span>
<span style='color:#c45b00;'>    ):</span>
<span style='color:#c45b00;'>        n = len(mu)</span>
<span style='color:#c45b00;'>        w = cp.Variable(n)</span>

<span style='color:#c45b00;'>        objective = (</span>
<span style='color:#c45b00;'>            mu @ w</span>
<span style='color:#c45b00;'>            - 0.5 * risk_aversion * cp.quad_form(w, cov)</span>
<span style='color:#c45b00;'>            - turnover_penalty * cp.norm1(w - w_prev)</span>
<span style='color:#c45b00;'>        )</span>

<span style='color:#c45b00;'>        if betas is not None and target_beta is not None:</span>
<span style='color:#c45b00;'>            objective -= factor_penalty * cp.sum_squares(</span>
<span style='color:#c45b00;'>                betas.T @ w - target_beta</span>
<span style='color:#c45b00;'>            )</span>

<span style='color:#c45b00;'>        constraints = [</span>
<span style='color:#c45b00;'>            cp.sum(w) == 1,</span>
<span style='color:#c45b00;'>            w &gt;= 0,</span>
<span style='color:#c45b00;'>            w &lt;= max_weight,</span>
<span style='color:#c45b00;'>        ]</span>

<span style='color:#c45b00;'>        problem = cp.Problem(cp.Maximize(objective), constraints)</span>
<span style='color:#c45b00;'>        problem.solve()</span>

<span style='color:#c45b00;'>        if w.value is None:</span>
<span style='color:#c45b00;'>            raise RuntimeError(f&quot;Optimization failed: {problem.status}&quot;)</span>

<span style='color:#c45b00;'>        return np.asarray(w.value).ravel()</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    **Backtesting must be account-aware.** Let \(V_t\) denote marked-to-market account value and \(F_t\) an external cash flow. At a clean bar boundary,</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    r_t^{acct}</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \frac{V_t-F_t}{V_{t-1}}-1.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    Then time-weighted cumulative return is</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    R_T</span>
<span style='color:#c45b00;'>    =</span>
<span style='color:#c45b00;'>    \prod_{t=1}^{T}</span>
<span style='color:#c45b00;'>    (1+r_t^{acct})-1.</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    A stock purchase is not \(F_t\): cash became an asset. A deposit or withdrawal is an external flow. If a cash flow occurs inside a bar, split the valuation interval around the flow where possible rather than pretending it occurred at the endpoint.</span>

<span style='color:#c45b00;'>    Trades should be executed in the simulation only at the first price that was actually available **after** the decision timestamp. Include spread/slippage, commissions/fees where applicable, turnover and liquidity assumptions. Tiingo's consolidated intraday product currently exposes reference and liquidity fields that can help with the trading-cost layer, while the IEX endpoint provides exchange-specific market data. citeturn0search5turn0search0</span>

<span style='color:#c45b00;'>    Core OOS metrics:</span>

<span style='color:#c45b00;'>    | Category | Metrics |</span>
<span style='color:#c45b00;'>    |---|---|</span>
<span style='color:#c45b00;'>    | Return | annualized return, cumulative return, hit rate |</span>
<span style='color:#c45b00;'>    | Risk | annualized vol, max drawdown, CVaR/expected shortfall |</span>
<span style='color:#c45b00;'>    | Risk-adjusted | Sharpe, Sortino, Calmar |</span>
<span style='color:#c45b00;'>    | Trading | turnover, cost drag, holding period |</span>
<span style='color:#c45b00;'>    | Forecast | log loss, Brier score, ROC-AUC only as secondary, rank IC |</span>
<span style='color:#c45b00;'>    | Feature | OOS IV, WoE stability, RF permutation stability |</span>
<span style='color:#c45b00;'>    | Factor | realized beta, factor contribution, residual share |</span>
<span style='color:#c45b00;'>    | Covariance | realized portfolio variance vs forecast, condition number |</span>
<span style='color:#c45b00;'>    | Geometry | kNN Jaccard stability, intrinsic-dimension stability |</span>
<span style='color:#c45b00;'>    | Markov | transition log loss, calibration, state occupancy |</span>
<span style='color:#c45b00;'>    | Chaos | LLE relative to surrogate-null distribution |</span>
<span style='color:#c45b00;'>    | Stochastic | drift/diffusion bootstrap error, Markov consistency |</span>
<span style='color:#c45b00;'>    | Portfolio | Sharpe after cost, max drawdown, weight concentration |</span>

<span style='color:#c45b00;'>    The **primary acceptance criteria** should be:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \text{positive OOS performance after realistic costs}</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    together with</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \text{stable behavior over multiple chronological test periods}.</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    A nonlinear method is rejected even if it looks spectacular in-sample when it fails to improve either OOS forecast loss, covariance/risk prediction, or final cost-adjusted portfolio utility.</span>

<span style='color:#c45b00;'>    The required charts are:</span>

<span style='color:#c45b00;'>    | Chart | What it must show |</span>
<span style='color:#c45b00;'>    |---|---|</span>
<span style='color:#c45b00;'>    | `account_state_panels.png` | account TWR, price, trades, SMA/EMA, derivative state, volatility, Ichimoku |</span>
<span style='color:#c45b00;'>    | `correlation_heatmaps.png` | rolling, EWMA, Ledoit-Wolf, residual correlation |</span>
<span style='color:#c45b00;'>    | `pca_eigenvalue_timeline.png` | \(\lambda_k(t)\), explained variance, effective dimension |</span>
<span style='color:#c45b00;'>    | `pca_loading_timeline.png` | changing stock-factor exposures |</span>
<span style='color:#c45b00;'>    | `poincare_2d.html` | stock-state points, nearest neighbors, Fréchet center |</span>
<span style='color:#c45b00;'>    | `poincare_3d.html` | same in 3-D challenger |</span>
<span style='color:#c45b00;'>    | `markov_transition_graph.png` | state size, expected return, edge probabilities |</span>
<span style='color:#c45b00;'>    | `lyapunov_timeline.png` | rolling LLE plus stochastic surrogate bands |</span>
<span style='color:#c45b00;'>    | `hurst_timeline.png` | returns vs vol/residual Hurst estimates |</span>
<span style='color:#c45b00;'>    | `kramers_moyal_drift.html` | \(D^{(1)}(x)\) |</span>
<span style='color:#c45b00;'>    | `kramers_moyal_diffusion.html` | \(D^{(2)}(x)\) |</span>
<span style='color:#c45b00;'>    | `morse_potential.html` | estimated \(V\), minima and saddles |</span>
<span style='color:#c45b00;'>    | `portfolio_weights.png` | realized dynamic weights |</span>
<span style='color:#c45b00;'>    | `portfolio_factor_exposure.png` | beta/factor exposure through time |</span>
<span style='color:#c45b00;'>    | `portfolio_drawdown.png` | strategy vs baselines |</span>

<span style='color:#c45b00;'>    ## Implementation roadmap and deliverables</span>

<span style='color:#c45b00;'>    The order matters more than the calendar. Each later layer must be able to fail without breaking the earlier optimizer.</span>

<span style='color:#c45b00;'>    ```mermaid</span>
<span style='color:#c45b00;'>    flowchart TD</span>
<span style='color:#c45b00;'>        M0[Repository audit and deterministic tests]</span>
<span style='color:#c45b00;'>        M1[Tiingo + transaction canonical data store]</span>
<span style='color:#c45b00;'>        M2[Causal linear feature engine]</span>
<span style='color:#c45b00;'>        M3[Covariance + PCA + multi-beta residual model]</span>
<span style='color:#c45b00;'>        M4[Tanh bank + strength channel]</span>
<span style='color:#c45b00;'>        M5[Markov lattice + RF walk-forward baseline]</span>
<span style='color:#c45b00;'>        M6[Portfolio optimizer + cost-aware account backtest]</span>
<span style='color:#c45b00;'>        M7[Kernel PCA + diffusion challenger]</span>
<span style='color:#c45b00;'>        M8[Poincare + kNN + barycentre challenger]</span>
<span style='color:#c45b00;'>        M9[Hurst + Lyapunov + surrogate diagnostics]</span>
<span style='color:#c45b00;'>        M10[Kramers-Moyal drift-diffusion surfaces]</span>
<span style='color:#c45b00;'>        M11[Morse / rotational decomposition]</span>
<span style='color:#c45b00;'>        M12[Freidlin-Wentzell + Witten research layer]</span>
<span style='color:#c45b00;'>        M13[Champion-challenger comparison]</span>

<span style='color:#c45b00;'>        M0 --&gt; M1 --&gt; M2 --&gt; M3 --&gt; M4 --&gt; M5 --&gt; M6</span>
<span style='color:#c45b00;'>        M6 --&gt; M7 --&gt; M8</span>
<span style='color:#c45b00;'>        M6 --&gt; M9</span>
<span style='color:#c45b00;'>        M8 --&gt; M10</span>
<span style='color:#c45b00;'>        M9 --&gt; M10</span>
<span style='color:#c45b00;'>        M10 --&gt; M11 --&gt; M12</span>
<span style='color:#c45b00;'>        M7 --&gt; M13</span>
<span style='color:#c45b00;'>        M8 --&gt; M13</span>
<span style='color:#c45b00;'>        M9 --&gt; M13</span>
<span style='color:#c45b00;'>        M12 --&gt; M13</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The milestone gates should be:</span>

<span style='color:#c45b00;'>    | Milestone | Deliverable | Gate |</span>
<span style='color:#c45b00;'>    |---|---|---|</span>
<span style='color:#c45b00;'>    | Canonical data | `ohlcv_10min.parquet`, transaction ledger, QA tables | no duplicate/misaligned timestamps |</span>
<span style='color:#c45b00;'>    | Linear features | SMA/EMA, derivatives, vol, Ichimoku | zero future leakage |</span>
<span style='color:#c45b00;'>    | Risk model | rolling/EWMA/LW covariance, PCA, betas, residuals | stable condition number and OOS variance |</span>
<span style='color:#c45b00;'>    | Tanh state | beta bank, strength, sensitivity, lagged covariance | incremental state information |</span>
<span style='color:#c45b00;'>    | Markov/RF | probabilities and residual-return forecasts | OOS calibration/IV |</span>
<span style='color:#c45b00;'>    | Portfolio | optimized weights, account TWR | beats simple baselines after cost |</span>
<span style='color:#c45b00;'>    | Kernel/diffusion | nonlinear coordinates | OOS improvement over PCA |</span>
<span style='color:#c45b00;'>    | Hyperbolic | Poincaré distances and centers | beats Euclidean/Mahalanobis |</span>
<span style='color:#c45b00;'>    | Chaos/memory | LLE, Hurst, fractional results | exceeds surrogate/null evidence |</span>
<span style='color:#c45b00;'>    | Stochastic surface | \(D^{(1)},D^{(2)}\) | bootstrap-stable fields |</span>
<span style='color:#c45b00;'>    | Morse/Witten | stable potential, critical points, path analysis | reproducible across windows |</span>

<span style='color:#c45b00;'>    The method-comparison master table should be emitted as `outputs/model_registry.csv` with columns:</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    model</span>
<span style='color:#c45b00;'>    feature_set</span>
<span style='color:#c45b00;'>    fit_window</span>
<span style='color:#c45b00;'>    forecast_horizon</span>
<span style='color:#c45b00;'>    parameters</span>
<span style='color:#c45b00;'>    train_metric</span>
<span style='color:#c45b00;'>    validation_metric</span>
<span style='color:#c45b00;'>    test_metric</span>
<span style='color:#c45b00;'>    oos_iv</span>
<span style='color:#c45b00;'>    sharpe_net</span>
<span style='color:#c45b00;'>    max_drawdown</span>
<span style='color:#c45b00;'>    turnover</span>
<span style='color:#c45b00;'>    realized_beta</span>
<span style='color:#c45b00;'>    intrinsic_dimension</span>
<span style='color:#c45b00;'>    neighbor_stability</span>
<span style='color:#c45b00;'>    runtime_class</span>
<span style='color:#c45b00;'>    accepted</span>
<span style='color:#c45b00;'>    rejection_reason</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The computational burden is approximately:</span>

<span style='color:#c45b00;'>    | Layer | Scaling | Runtime class | Optimization |</span>
<span style='color:#c45b00;'>    |---|---:|---|---|</span>
<span style='color:#c45b00;'>    | OHLCV features | \(O(TNF)\) | low | vectorize/groupby |</span>
<span style='color:#c45b00;'>    | EWMA covariance | \(O(TN^2)\) | low–medium | recursive update |</span>
<span style='color:#c45b00;'>    | Ledoit-Wolf | \(O(TN^2)\) plus eigensolve | medium | refit less often |</span>
<span style='color:#c45b00;'>    | PCA | \(O(TN^2+N^3)\) | medium | randomized/truncated when large |</span>
<span style='color:#c45b00;'>    | tanh bank | \(O(TNK)\) | low | vectorized |</span>
<span style='color:#c45b00;'>    | Markov lattice | \(O(T)\) | low | sparse matrix |</span>
<span style='color:#c45b00;'>    | RF | roughly trees × samples × split work | medium–high | parallel trees |</span>
<span style='color:#c45b00;'>    | exact kernel PCA | \(O(T^2F+T^3)\) | high | subsample/Nyström |</span>
<span style='color:#c45b00;'>    | diffusion maps | sparse graph + eigensolve | medium–high | kNN sparse graph |</span>
<span style='color:#c45b00;'>    | Poincaré kNN | \(O(TNd)\) brute | medium | prefilter/approximate NN |</span>
<span style='color:#c45b00;'>    | Lyapunov | \(O(T^2)\) naïve | medium–high | neighbor index |</span>
<span style='color:#c45b00;'>    | Kramers–Moyal | rapidly grows with dimension | high | restrict to 2–3 coordinates |</span>
<span style='color:#c45b00;'>    | Morse/Witten | basis/discretization dependent | high | challenger only |</span>
<span style='color:#c45b00;'>    | Freidlin–Wentzell paths | iterative path optimization | very high | selected regime pairs only |</span>

<span style='color:#c45b00;'>    This ranking is intentionally relative rather than hardware-specific. Kernel PCA's exact Gram matrix and eigenproblem are intrinsically quadratic/cubic in sample count, while FFT-based spectral calculations are dramatically cheaper; the original kernel-PCA and Cooley–Tukey formulations make that computational contrast clear. citeturn1search16turn4search7</span>

<span style='color:#c45b00;'>    A reproducible top-level run should eventually be:</span>

<span style='color:#c45b00;'>    ```bash</span>
<span style='color:#c45b00;'>    # Data</span>
<span style='color:#c45b00;'>    python -m src.data.tiingo \</span>
<span style='color:#c45b00;'>    --universe config/universe.csv \</span>
<span style='color:#c45b00;'>    --bar-size 10min \</span>
<span style='color:#c45b00;'>    --start 2025-01-01 \</span>
<span style='color:#c45b00;'>    --end 2026-08-24</span>

<span style='color:#c45b00;'>    # Causal features</span>
<span style='color:#c45b00;'>    python -m src.features.build \</span>
<span style='color:#c45b00;'>    --input data/ohlcv_10min.parquet \</span>
<span style='color:#c45b00;'>    --config config/features.yaml</span>

<span style='color:#c45b00;'>    # Linear factors and covariance</span>
<span style='color:#c45b00;'>    python -m src.risk.fit \</span>
<span style='color:#c45b00;'>    --config config/risk.yaml</span>

<span style='color:#c45b00;'>    # Nonlinear state</span>
<span style='color:#c45b00;'>    python -m src.geometry.build \</span>
<span style='color:#c45b00;'>    --config config/geometry.yaml</span>

<span style='color:#c45b00;'>    # Markov + RF walk-forward</span>
<span style='color:#c45b00;'>    python -m src.models.walk_forward \</span>
<span style='color:#c45b00;'>    --config config/models.yaml</span>

<span style='color:#c45b00;'>    # Portfolio and account-aware backtest</span>
<span style='color:#c45b00;'>    python -m src.portfolio.backtest \</span>
<span style='color:#c45b00;'>    --transactions data/account_transactions.csv \</span>
<span style='color:#c45b00;'>    --config config/portfolio.yaml</span>

<span style='color:#c45b00;'>    # Research diagnostics</span>
<span style='color:#c45b00;'>    python -m src.dynamics.run \</span>
<span style='color:#c45b00;'>    --config config/dynamics.yaml</span>

<span style='color:#c45b00;'>    # All tables/charts</span>
<span style='color:#c45b00;'>    python -m src.reporting.render \</span>
<span style='color:#c45b00;'>    --output outputs/report/</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    For SAS validation:</span>

<span style='color:#c45b00;'>    ```bash</span>
<span style='color:#c45b00;'>    sas -sysin sas/moving_averages.sas</span>
<span style='color:#c45b00;'>    sas -sysin sas/ichimoku.sas</span>
<span style='color:#c45b00;'>    sas -sysin sas/markov_lattice.sas</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The final deliverable bundle should contain:</span>

<span style='color:#c45b00;'>    ```text</span>
<span style='color:#c45b00;'>    outputs/report/</span>
<span style='color:#c45b00;'>    ├── tables/</span>
<span style='color:#c45b00;'>    │   ├── covariance_method_comparison.csv</span>
<span style='color:#c45b00;'>    │   ├── pca_factor_loadings.csv</span>
<span style='color:#c45b00;'>    │   ├── residual_correlations.csv</span>
<span style='color:#c45b00;'>    │   ├── inverse_hedge_candidates.csv</span>
<span style='color:#c45b00;'>    │   ├── tanh_covariance_summary.csv</span>
<span style='color:#c45b00;'>    │   ├── woe_iv_oos.csv</span>
<span style='color:#c45b00;'>    │   ├── markov_transition_matrix.csv</span>
<span style='color:#c45b00;'>    │   ├── model_registry.csv</span>
<span style='color:#c45b00;'>    │   ├── backtest_summary.csv</span>
<span style='color:#c45b00;'>    │   └── portfolio_weights.csv</span>
<span style='color:#c45b00;'>    ├── charts/</span>
<span style='color:#c45b00;'>    │   ├── account_state_panels.png</span>
<span style='color:#c45b00;'>    │   ├── correlation_heatmaps.png</span>
<span style='color:#c45b00;'>    │   ├── pca_eigenvalue_timeline.png</span>
<span style='color:#c45b00;'>    │   ├── pca_loading_timeline.png</span>
<span style='color:#c45b00;'>    │   ├── poincare_2d.html</span>
<span style='color:#c45b00;'>    │   ├── poincare_3d.html</span>
<span style='color:#c45b00;'>    │   ├── markov_transition_graph.png</span>
<span style='color:#c45b00;'>    │   ├── lyapunov_timeline.png</span>
<span style='color:#c45b00;'>    │   ├── hurst_timeline.png</span>
<span style='color:#c45b00;'>    │   ├── kramers_moyal_drift.html</span>
<span style='color:#c45b00;'>    │   ├── kramers_moyal_diffusion.html</span>
<span style='color:#c45b00;'>    │   ├── morse_potential.html</span>
<span style='color:#c45b00;'>    │   ├── portfolio_weights.png</span>
<span style='color:#c45b00;'>    │   └── portfolio_drawdown.png</span>
<span style='color:#c45b00;'>    └── diagnostics/</span>
<span style='color:#c45b00;'>        ├── leakage_checks.csv</span>
<span style='color:#c45b00;'>        ├── surrogate_chaos_tests.csv</span>
<span style='color:#c45b00;'>        ├── intrinsic_dimension_stability.csv</span>
<span style='color:#c45b00;'>        ├── neighbour_stability.csv</span>
<span style='color:#c45b00;'>        └── feature_drift.csv</span>
<span style='color:#c45b00;'>    ```</span>

<span style='color:#c45b00;'>    The decisive research hierarchy should be:</span>

<span style='color:#c45b00;'>    \[</span>
<span style='color:#c45b00;'>    \boxed{</span>
<span style='color:#c45b00;'>    \text{raw returns}</span>
<span style='color:#c45b00;'>    &lt;</span>
<span style='color:#c45b00;'>    \text{linear factor/residual}</span>
<span style='color:#c45b00;'>    &lt;</span>
<span style='color:#c45b00;'>    \text{linear + tanh/strength}</span>
<span style='color:#c45b00;'>    &lt;</span>
<span style='color:#c45b00;'>    \text{Markov/RF}</span>
<span style='color:#c45b00;'>    &lt;</span>
<span style='color:#c45b00;'>    \text{kernel/diffusion}</span>
<span style='color:#c45b00;'>    &lt;</span>
<span style='color:#c45b00;'>    \text{hyperbolic/stochastic/Morse challengers}</span>
<span style='color:#c45b00;'>    }</span>
<span style='color:#c45b00;'>    \]</span>

<span style='color:#c45b00;'>    where “&lt;” means **the next model must empirically beat the previous one**, not that it is mathematically more sophisticated.</span>

<span style='color:#c45b00;'>    That distinction is central to this project. The repo contains enough ideas to build something extraordinarily complicated. The optimizer should instead be designed so that complexity has to **earn its survival**. The most promising synthesis is your original one: preserve a linear/autocovariant backbone, separate beta from residual motion, use multiscale `tanh` as a bounded state/pattern representation **without throwing away strength**, detect conditional relationships through Markov and nearest-neighbor structures, and let the geometric/stochastic constructions explain only the residual structure that the simpler models demonstrably fail to capture. Ledoit–Wolf, kernel PCA, diffusion maps, Poincaré embeddings, Random Forests, long-memory models, Lyapunov estimation, Freidlin–Wentzell theory and Witten's Morse construction each have rigorous mathematical foundations; none of them, by itself, proves that financial data satisfy the assumptions that made the method successful in its original domain. citeturn0search1turn1search16turn1search3turn1search9turn2search0turn5search0turn1search0turn3search2turn9view0</span></pre>
