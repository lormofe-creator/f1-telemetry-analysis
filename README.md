\# Formula 1 Telemetry Analysis \& Delta Decomposition



A quantitative motorsport engineering pipeline built with Python and the `FastF1` API. This repository analyzes high-frequency vehicle telemetry, isolating aerodynamic and dynamic performance differentials between qualifying laps.



!\[Telemetry Comparison](telemetry\_comparison.png)



\## Overview \& Case Study: Spanish GP 2024 (Q3 Pole Delta)



\* \*\*Session:\*\* 2024 Formula 1 Spanish Grand Prix — Qualifying (Q3)

\* \*\*Vehicles:\*\* McLaren MCL38 (`#4 L. Norris`) vs. Red Bull Racing RB20 (`#1 M. Verstappen`)

\* \*\*Margin:\*\* +0.020 seconds differential across a 4.657 km circuit.



\### Engineering Observations



1\. \*\*Braking Signature \& Trail Braking:\*\* Analysis of deceleration phases at Turn 1 and Turn 10 shows distinct braking profiles. The reference trace displays progressive brake release matched with steering angle input, sustaining apex minimum speeds.

2\. \*\*Throttle Pickup \& Traction Phasing:\*\* Telemetry reveals critical differences in throttle application curves out of low-speed exits, reflecting mechanical grip, diff locking, and rear tire slip ratio.

3\. \*\*Continuous Delta Trace:\*\* The computed time-delta profile ($Delta(s) = t\_{cmp}(d) - t\_{ref}(d)$) decomposes the sector gains, illustrating how micro-sector deltas fluctuate between straight-line top speed and mid-corner lateral loading.



\---



\## Technical Stack \& Libraries



\* \*\*Language:\*\* Python 3.10+

\* \*\*Core APIs:\*\* `FastF1` (FIA official timing data, track markers, and car data)

\* \*\*Scientific Computing:\*\* `NumPy`, `Pandas`

\* \*\*Visualization:\*\* `Matplotlib` (custom multi-channel telemetry workspace)



\---



\## Reproducing the Analysis



1\. \*\*Clone the repository:\*\*

&#x20;  ```bash

&#x20;  git clone \[https://github.com/lormofe/f1-telemetry-analysis.git](https://github.com/lormofe/f1-telemetry-analysis.git)

&#x20;  cd f1-telemetry-analysis

