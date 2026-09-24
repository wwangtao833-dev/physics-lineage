"""Build the second curated expansion without changing the site's data model."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = {}


def source(key, title, url):
    SOURCES[key] = {"title": title, "url": url}


# Official course notes used for broad, established frameworks.
source("mit-mech", "MIT OCW 8.09 · Classical Mechanics III lecture notes", "https://ocw.mit.edu/courses/8-09-classical-mechanics-iii-fall-2014/pages/lecture-notes/")
source("mit-elastic", "MIT OCW 2.080J · Structural Mechanics lecture notes", "https://ocw.mit.edu/courses/2-080j-structural-mechanics-fall-2013/pages/lecture-notes/")
source("mit-circuit", "MIT OCW 6.002 · Circuits and Electronics", "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/")
source("mit-em", "MIT OCW 8.07 · Electromagnetism II lecture notes", "https://ocw.mit.edu/courses/8-07-electromagnetism-ii-fall-2012/pages/lecture-notes/")
source("mit-transmission", "MIT OCW 6.013 · Electromagnetics and Applications", "https://ocw.mit.edu/courses/6-013-electromagnetics-and-applications-fall-2005/pages/lecture-notes/")
source("mit-stat", "MIT OCW 8.333 · Statistical Mechanics I lecture notes", "https://ocw.mit.edu/courses/8-333-statistical-mechanics-i-statistical-mechanics-of-particles-fall-2013/pages/lecture-notes/")
source("mit-optics", "MIT OCW 2.71 · Optics", "https://ocw.mit.edu/courses/2-71-optics-spring-2009/")
source("mit-waves", "MIT OCW 8.03SC · Vibrations and Waves", "https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/")
source("mit-fluid", "MIT OCW 2.25 · Advanced Fluid Mechanics", "https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/pages/syllabus/")
source("mit-interface", "MIT OCW 18.357 · Interfacial Phenomena lecture notes", "https://ocw.mit.edu/courses/18-357-interfacial-phenomena-fall-2010/pages/lecture-notes/")
source("carroll-gr", "Carroll · Lecture Notes on General Relativity", "https://arxiv.org/abs/gr-qc/9712019")
source("mit-qm1", "MIT OCW 8.04 · Quantum Physics I lecture notes", "https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/pages/lecture-notes/")
source("mit-qm2", "MIT OCW 8.05 · Quantum Physics II lecture notes", "https://ocw.mit.edu/courses/8-05-quantum-physics-ii-fall-2013/pages/lecture-notes/")
source("mit-qm3", "MIT OCW 8.06 · Quantum Physics III lecture notes", "https://ocw.mit.edu/courses/8-06-quantum-physics-iii-spring-2018/pages/lecture-notes/")
source("mit-solid", "MIT OCW 8.231 · Physics of Solids I", "https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/")
source("preskill", "Preskill · Ph219/CS219 Quantum Computation", "https://www.preskill.caltech.edu/ph219/ph219_2018.html")
source("mit-plasma", "MIT OCW 22.611J · Introduction to Plasma Physics I", "https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/")
source("mit-chaos", "MIT OCW 18.353J · Nonlinear Dynamics I: Chaos", "https://ocw.mit.edu/courses/18-353j-nonlinear-dynamics-i-chaos-fall-2012/")
source("mit-numerical", "MIT OCW 16.920J · Numerical Methods for Partial Differential Equations", "https://ocw.mit.edu/courses/16-920j-numerical-methods-for-partial-differential-equations-sma-5212-spring-2003/")
source("pdg-bbn", "PDG 2025 Review · Big-Bang Nucleosynthesis", "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-bbang-nucleosynthesis.pdf")
source("pdg-quark", "PDG 2025 Review · Quark Model", "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-quark-model.pdf")
source("pdg-ckm", "PDG 2025 Review · CKM Quark-Mixing Matrix", "https://pdg.lbl.gov/2025/reviews/rpp2025-rev-ckm-matrix.pdf")

# Original papers and primary reviews for named discoveries or algorithms.
for key, title, doi in [
    ("nyquist", "Nyquist (1928) · Thermal Agitation of Electric Charge in Conductors", "10.1103/PhysRev.32.110"),
    ("kk", "Toll (1956) · Causality and the Dispersion Relation", "10.1103/PhysRev.104.1760"),
    ("langevin", "Langevin (1908) · On the Theory of Brownian Motion, translated", "10.1016/j.crhy.2004.02.015"),
    ("jones", "Jones (1941) · A New Calculus for Optical Systems", "10.1364/JOSA.31.000488"),
    ("shg", "Franken et al. (1961) · Generation of Optical Harmonics", "10.1103/PhysRevLett.7.118"),
    ("kolmogorov", "Kolmogorov (1941) · Local Structure of Turbulence", "10.1098/rspa.1991.0075"),
    ("kerr", "Kerr (1963) · Gravitational Field of a Spinning Mass", "10.1103/PhysRevLett.11.237"),
    ("hawking", "Hawking (1975) · Particle Creation by Black Holes", "10.1007/BF02345020"),
    ("bloch", "Bloch (1929) · Quantum Mechanics of Electrons in Crystal Lattices", "10.1007/BF01339455"),
    ("tight-binding", "Slater & Koster (1954) · Simplified LCAO Method", "10.1103/PhysRev.94.1498"),
    ("landauer", "Landauer (1957) · Spatial Variation of Currents and Fields", "10.1147/rd.153.0269"),
    ("fqhe", "Tsui, Stormer & Gossard (1982) · Two-Dimensional Magnetotransport", "10.1103/PhysRevLett.48.1559"),
    ("shell", "Mayer (1949) · On Closed Shells in Nuclei II", "10.1103/PhysRev.75.1969"),
    ("breit-wigner", "Breit & Wigner (1936) · Capture of Slow Neutrons", "10.1103/PhysRev.49.519"),
    ("quark", "Gell-Mann (1964) · A Schematic Model of Baryons and Mesons", "10.1016/S0031-9163(64)92001-3"),
    ("ckm", "Kobayashi & Maskawa (1973) · CP-Violation in the Renormalizable Theory", "10.1143/PTP.49.652"),
    ("tov", "Oppenheimer & Volkoff (1939) · On Massive Neutron Cores", "10.1103/PhysRev.55.374"),
    ("lensing", "Einstein (1936) · Lens-Like Action of a Star", "10.1126/science.84.2188.506"),
    ("cmb", "Fixsen et al. (1996) · The Cosmic Microwave Background Spectrum", "10.1086/177482"),
    ("qec", "Knill & Laflamme (1997) · Theory of Quantum Error-Correcting Codes", "10.1103/PhysRevA.55.900"),
    ("holevo", "Holevo (1973) · Bounds for the Quantity of Information", "10.1007/BF01007420"),
    ("path-integral", "Feynman (1948) · Space-Time Approach to Non-Relativistic Quantum Mechanics", "10.1103/RevModPhys.20.367"),
    ("rg", "Wilson (1971) · Renormalization Group and Critical Phenomena I", "10.1103/PhysRevB.4.3174"),
    ("eft", "Weinberg (1979) · Phenomenological Lagrangians", "10.1016/0370-1573(79)90023-1"),
    ("reconnection", "Parker (1957) · Sweet's Mechanism for Merging Magnetic Fields", "10.1029/JZ062i004p00509"),
    ("kuramoto", "Strogatz (2000) · From Kuramoto to Crawford", "10.1016/S0167-2789(00)00094-4"),
    ("turing", "Turing (1952) · The Chemical Basis of Morphogenesis", "10.1098/rstb.1952.0012"),
    ("fem", "Courant (1943) · Variational Methods for Problems of Equilibrium and Vibrations", "10.1090/S0002-9947-1943-0009918-6"),
    ("fft", "Cooley & Tukey (1965) · An Algorithm for Machine Calculation of Complex Fourier Series", "10.1090/S0025-5718-1965-0178586-1"),
    ("lbm", "McNamara & Zanetti (1988) · Use of the Boltzmann Equation to Simulate Lattice-Gas Automata", "10.1103/PhysRevLett.61.2332"),
]:
    source(key, title, "https://doi.org/" + doi)


ROWS = []


def add(identifier, field, topic, year, title, people, formula, summary, conditions,
        variables, application, significance, refs, related=(), date=None,
        context=None, kind="理论／关系"):
    label = date or f"{year} 年"
    ROWS.append({
        "id": identifier,
        "field": field,
        "topic": topic,
        "year": year,
        "date": label,
        "title": title,
        "people": people,
        "formula": formula,
        "summary": summary,
        "conditions": conditions,
        "variables": variables,
        "application": application,
        "significance": significance,
        "context": context or f"代表节点为{label}；关键贡献者为{people}。该年份用于排序，不表示此前没有相关先驱工作。",
        "sources": [SOURCES[key] for key in refs.split()],
        "related": list(related),
        "kind": kind,
        "editorial": "第二轮新增 · 附参考来源",
    })


# Mechanics: rigid bodies, continua and analytical mechanics.
add("rigid-body-euler", "力学", "刚体动力学", 1758, "刚体欧拉方程", "莱昂哈德·欧拉", "I₁ω̇₁+(I₃−I₂)ω₂ω₃=τ₁（其余两式循环置换）", "在随体主轴系中描述刚体角速度如何受力矩驱动。", "刚体、质心随体系且坐标轴取惯量主轴；Iᵢ 可视为常数。", "Iᵢ 主惯量，ωᵢ 角速度分量，τᵢ 外力矩分量", "航天器姿态、陀螺、转子动力学", "把角动量守恒推广为可计算的三维刚体动力学。", "mit-mech", ("angular-momentum", "hamilton"))
add("elasticity-cauchy", "力学", "连续介质与弹性", 1822, "各向同性线弹性本构", "奥古斯丁-路易·柯西；拉梅等", "σ=λ tr(ε)I+2με，ε=[∇u+(∇u)ᵀ]/2", "应力与小应变在线性各向同性固体中由两个拉梅常数联系。", "小变形、线性、均匀各向同性弹性；塑性、黏弹性和大变形不适用。", "σ 应力张量，ε 小应变张量，λ、μ 拉梅常数，u 位移", "结构分析、声弹性、材料力学", "把标量胡克定律扩展到三维连续介质。", "mit-elastic", ("hooke", "navier-stokes"), date="1822—1852 年")
add("hamilton-jacobi", "力学", "分析力学", 1834, "哈密顿–雅可比方程", "威廉·哈密顿；卡尔·雅可比", "∂S/∂t+H(q,∂S/∂q,t)=0", "用主函数 S 的一阶偏微分方程编码完整经典动力学。", "哈密顿系统；完整积分存在性取决于系统和边界条件。", "S 哈密顿主函数，H 哈密顿量，q 广义坐标", "轨道动力学、几何光学、半经典近似", "直接连接经典作用量、费马原理与量子相位。", "mit-mech", ("hamilton", "fermat"))

# Circuits and distributed electrical systems.
add("thevenin-norton", "电学", "电路等效", 1883, "戴维南–诺顿等效定理", "莱昂·戴维南；爱德华·诺顿等", "V=V_th−IR_th；I_N=V_th/R_th", "任意线性二端网络可化为电压源串联阻抗或电流源并联阻抗。", "线性二端网络；交流情形以复阻抗替代电阻，受控源求等效阻抗时需保留。", "V_th 开路电压，R_th 等效电阻，I_N 诺顿电流", "电源建模、负载匹配、电路测试", "把复杂网络压缩为保持端口行为的最小模型。", "mit-circuit", ("ohm", "kirchhoff"), date="1883 年；1926 年诺顿形式")
add("telegrapher", "电学", "分布参数电路", 1887, "电报方程与传输线", "奥利弗·赫维赛德等", "∂V/∂x=−L′∂I/∂t−R′I；∂I/∂x=−C′∂V/∂t−G′V", "分布电感、电容、电阻和漏导共同决定电压电流沿传输线传播。", "均匀准 TEM 传输线的单位长度参数模型；高阶模需全波描述。", "R′、L′、G′、C′ 为单位长度参数", "同轴线、PCB、脉冲与射频互连", "在集总电路和麦克斯韦场之间建立工程桥梁。", "mit-transmission", ("kirchhoff", "em-wave"))
add("johnson-nyquist", "电学", "噪声与测量", 1928, "约翰逊–奈奎斯特热噪声", "约翰·约翰逊、哈里·奈奎斯特", "S_V(f)=4k_BTR（单边低频谱）", "电阻中的热涨落产生与温度和电阻成正比的白噪声电压谱。", "经典极限 hf≪k_BT、热平衡、理想电阻；双边谱或角频率谱的系数不同。", "S_V 电压功率谱密度，T 温度，R 电阻", "低噪声电路、温度计、计量学", "给出耗散元件不可避免的噪声底，并成为涨落耗散思想的经典实例。", "nyquist", ("ohm", "fluctuation-dissipation"))

# Electromagnetic radiation and causal response.
add("lienard-wiechert", "磁学与电磁", "辐射与推迟场", 1898, "李纳–维谢尔势", "阿尔弗雷德-马里·李纳、埃米尔·维谢尔", "φ(r,t)=q/[4πε₀(1−n·β)R]_ret，A=βφ/c", "运动点电荷的电磁势由其推迟时刻的位置和速度决定。", "真空中的点电荷、洛伦兹规范；所有括号量在满足 t_ret=t−R/c 的推迟时刻取值。", "R 源到观测点距离，n 方向单位矢量，β=v/c", "同步辐射、天线、带电粒子动力学", "把有限传播速度明确写入运动电荷的场。", "mit-em", ("lorentz-force", "maxwell"), date="1898—1900 年")
add("larmor-radiation", "磁学与电磁", "辐射与推迟场", 1897, "拉莫尔辐射公式", "约瑟夫·拉莫尔", "P=q²a²/(6πε₀c³)", "非相对论加速点电荷以与加速度平方成正比的功率辐射。", "真空、点电荷、v≪c；相对论运动需 Liénard 推广，辐射反作用需另行处理。", "P 总辐射功率，q 电荷，a 瞬时加速度", "回旋辐射、加速器、天体辐射", "说明恒速电荷与加速电荷在辐射行为上的根本差别。", "mit-em", ("lienard-wiechert", "dipole-radiation"))
add("dipole-radiation", "磁学与电磁", "辐射与天线", 1888, "振荡电偶极辐射", "海因里希·赫兹；经典电动力学后续发展", "⟨P⟩=p₀²ω⁴/(12πε₀c³)", "谐振电偶极矩在远区产生横向辐射，功率强烈依赖频率。", "点偶极与远场近似，p(t)=Re[p₀e^(−iωt)]；介质和近场会改变关系。", "p₀ 偶极矩幅值，ω 角频率", "短天线、分子辐射、散射", "给出天线与原子辐射的共同最低阶多极结构。", "mit-em", ("maxwell", "larmor-radiation"))
add("kramers-kronig", "磁学与电磁", "介质响应", 1926, "克拉默斯–克勒尼希关系", "拉尔夫·克勒尼希、亨德里克·克拉默斯", "Reχ(ω)=P/π ∫[Imχ(ω′)/(ω′−ω)]dω′", "因果线性响应的实部与虚部并非独立，而由主值积分互相决定。", "线性、时不变、因果且响应满足适当高频收敛；积分范围为全部实频率。", "χ 复响应函数，P 表示柯西主值", "光谱反演、介电函数、材料表征", "把因果性转化为色散与吸收之间的定量约束。", "kk", ("lorentz-oscillator", "fluctuation-dissipation"), date="1926—1927 年")

# Statistical ensembles, kinetic theory and stochastic dynamics.
add("grand-canonical", "热学与统计", "统计系综", 1902, "巨正则系综", "约西亚·吉布斯等", "Ξ=Tr exp[−β(H−μN)]，Ω=−k_BT lnΞ", "允许能量和粒子同时与环境交换的平衡系综。", "固定温度、体积和化学势；系统与热库、粒子库处于平衡。", "Ξ 巨配分函数，μ 化学势，N 粒子数算符，Ω 巨势", "量子气体、吸附、粒子数涨落", "补全微正则、正则与巨正则三类基本平衡系综。", "mit-stat", ("partition", "bose-einstein"))
add("liouville-phase", "热学与统计", "相空间动力学", 1838, "刘维尔定理", "约瑟夫·刘维尔；统计力学后续发展", "∂ρ/∂t+{ρ,H}=0", "哈密顿流保持相空间体积，分布函数沿经典轨迹不变。", "经典哈密顿系统；耗散或随机系统一般不满足简单的体积保持。", "ρ 相空间密度，{,} 泊松括号，H 哈密顿量", "统计系综、束流、混沌动力学", "把微观可逆动力学与统计分布演化联系起来。", "mit-stat", ("hamilton", "boltzmann"))
add("boltzmann-equation", "热学与统计", "动理学与输运", 1872, "玻尔兹曼输运方程与 H 定理", "路德维希·玻尔兹曼", "∂_t f+v·∇_r f+(F/m)·∇_v f=C[f]", "单粒子分布在自由输运、外力与碰撞共同作用下演化。", "稀薄气体与分子混沌近似；H 定理的单调性依赖碰撞项的微观可逆性等假设。", "f 单粒子分布，C[f] 碰撞积分，F 外力", "稀薄气体、半导体、等离子体输运", "从微观碰撞推导宏观不可逆输运和局域平衡。", "mit-stat", ("maxwell-boltzmann", "onsager"))
add("langevin-equation", "热学与统计", "随机过程", 1908, "朗之万方程", "保罗·朗之万", "m v̇=−γv+ξ(t)，⟨ξ(t)ξ(t′)⟩=2γk_BTδ(t−t′)", "用确定性阻尼与随机力共同描述热浴中的布朗粒子。", "白噪声、马尔可夫、热平衡及线性阻尼模型；惯性可忽略时得到过阻尼极限。", "γ 阻尼系数，ξ 随机力，T 热浴温度", "软物质、随机热力学、噪声驱动系统", "将概率过程直接写成动力学方程，并显式体现涨落与耗散配对。", "langevin", ("einstein-diffusion", "fluctuation-dissipation"))

# Wave optics and polarization.
add("fraunhofer-diffraction", "光学", "衍射与傅里叶光学", 1821, "夫琅禾费衍射与傅里叶光学", "约瑟夫·夫琅禾费；傅里叶光学后续发展", "U(k_x,k_y)∝∬A(x,y)e^(−i(k_xx+k_yy))dxdy", "远场衍射振幅等于孔径复振幅的空间傅里叶变换。", "标量、傍轴、单色相干光及远场条件，或由透镜在焦平面实现等效变换。", "A 孔径场，U 远场复振幅，k_x、k_y 横向波数", "光学成像、空间滤波、衍射测量", "把孔径几何与远场频谱建立一一对应。", "mit-optics", ("grating", "fourier"))
add("jones-calculus", "光学", "偏振", 1941, "琼斯矩阵偏振计算", "R. Clark Jones", "E_out=J E_in", "用二维复矢量和 2×2 复矩阵表示相干偏振态与光学元件。", "准单色、完全偏振、确定性非退偏系统；部分偏振需 Stokes–Mueller 方法。", "E 琼斯矢量，J 光学系统琼斯矩阵", "波片、偏振器、椭偏测量", "把连续偏振变化转化为可组合的线性代数。", "jones", ("malus", "fresnel-equations"))
add("nonlinear-polarization", "光学", "非线性光学", 1961, "非线性极化与谐波产生", "彼得·弗兰肯等；非线性光学共同发展", "P=ε₀[χ⁽¹⁾E+χ⁽²⁾:EE+χ⁽³⁾:EEE+⋯]", "强光场使介质极化对电场呈高阶响应，从而产生新频率。", "电偶极近似下中心对称介质体内 χ⁽²⁾ 为零；张量对称性、相位匹配和色散决定效率。", "χ⁽ⁿ⁾ n 阶极化率张量，P 极化强度", "倍频、参量转换、超快光学", "把光从被动传播探针扩展为可改变介质并相互混频的强场。", "shg", ("stimulated-emission", "lorentz-oscillator"))

# General wave concepts and acoustics.
add("acoustic-impedance", "声学与波动", "声场与界面", 1877, "声阻抗", "瑞利勋爵等系统发展", "Z=p/u；平面行波中 Z=ρc", "声压与质点速度之比控制能流与界面反射。", "Z=ρc 只适用于均匀无耗介质中的平面行波；近场与有耗系统的阻抗通常为复数。", "p 声压，u 质点速度，ρ 密度，c 声速", "换能器、超声、吸声与阻抗匹配", "把声场动力学变量压缩为可测的端口关系。", "mit-waves", ("acoustic-intensity", "wave-equation"))
add("normal-modes", "声学与波动", "模态与振动", 1753, "简正模与模态展开", "丹尼尔·伯努利、欧拉等；线性代数后续发展", "K a_n=ω_n² M a_n，u(t)=Σ_n q_n(t)a_n", "线性耦合系统可分解为彼此独立振荡的本征模。", "线性、小振幅、时间不变系统；阻尼非比例或非线性时需推广。", "M 质量矩阵，K 刚度矩阵，a_n 模态，ω_n 固有频率", "结构振动、腔体声学、晶格动力学", "把复杂多自由度振动化为一组独立谐振子。", "mit-waves", ("standing-wave", "simple-harmonic"))
add("phase-group-velocity", "声学与波动", "色散与波包", 1877, "相速度与群速度", "瑞利勋爵；汉密尔顿等有先驱贡献", "v_p=ω/k，v_g=dω/dk", "单色相位和窄带波包包络在色散介质中可具有不同传播速度。", "群速度描述弱畸变窄带波包；强吸收、异常色散时不能简单等同信息或能量速度。", "ω 角频率，k 波数", "光纤、波导、色散工程", "区分载波相位传播与波包、能量和信息传播。", "mit-waves", ("traveling-wave", "lorentz-oscillator"))

# Fluid circulation, viscous drag, turbulence and interfaces.
add("kelvin-circulation", "流体力学", "涡量与环量", 1869, "开尔文环量定理", "威廉·汤姆孙（开尔文）", "dΓ/dt=0，Γ=∮_C(t) v·dl", "随流体运动的闭合物质曲线环量在理想条件下守恒。", "无黏、正压流体，体力可由势导出；黏性、非正压效应和冲击可产生涡量。", "Γ 环量，C(t) 物质闭合曲线", "机翼起动涡、地球流体、涡动力学", "把涡量演化与守恒律联系起来。", "mit-fluid", ("euler-fluid", "navier-stokes"))
add("stokes-drag", "流体力学", "低雷诺数流", 1851, "斯托克斯阻力", "乔治·斯托克斯", "F_D=6πηav", "小球在黏性流体中的低速阻力与速度、黏度和半径成正比。", "孤立刚性球、不可压牛顿流体、稳态爬流 Re≪1，远离边界。", "η 动力黏度，a 球半径，v 相对速度", "落球黏度计、微流控、颗粒沉降", "给出惯性可忽略时黏性主导运动的标准解。", "mit-fluid", ("reynolds", "navier-stokes"))
add("kolmogorov-spectrum", "流体力学", "湍流", 1941, "Kolmogorov −5/3 能谱", "安德雷·柯尔莫哥洛夫", "E(k)=C_K ε^(2/3)k^(−5/3)", "高雷诺数湍流惯性区的能谱由能量级联率和尺度决定。", "统计均匀、各向同性、充分远离驱动与耗散尺度的惯性区；C_K 非普适精确常数。", "E(k) 一维能谱约定，ε 单位质量耗散率，k 波数", "大气海洋、工程湍流、数值模型", "提出跨尺度能量级联的定量标度。", "kolmogorov", ("reynolds", "navier-stokes"))
add("young-laplace", "流体力学", "界面与毛细", 1805, "Young–Laplace 压差", "托马斯·杨、皮埃尔-西蒙·拉普拉斯", "Δp=γ(1/R₁+1/R₂)", "曲面界面上的表面张力产生与平均曲率成正比的压差。", "静态、各向同性表面张力；曲率和压差符号取决于法向约定。", "γ 表面张力，R₁、R₂ 主曲率半径", "液滴、气泡、微流控与润湿", "把分子界面能转化为宏观曲率压力。", "mit-interface", ("pascal", "navier-stokes"), date="1805—1806 年")

# Relativistic foundations and black holes.
add("equivalence-principle", "相对论", "引力基础", 1907, "等效原理", "阿尔伯特·爱因斯坦；伽利略、厄缶等有实验先驱", "m_g/m_i=常数；局域自由落体系中引力可被消去", "惯性质量与引力质量的普适等价使引力能够解释为时空几何。", "局域表述；有限区域仍可测到潮汐曲率，强等效原理的适用范围比弱等效原理更严格。", "m_g 引力质量，m_i 惯性质量", "精密落体、卫星检验、引力理论", "成为从狭义相对论走向广义相对论的概念起点。", "carroll-gr", ("general-relativity", "grav-redshift"))
add("kerr-metric", "相对论", "黑洞时空", 1963, "克尔旋转黑洞", "罗伊·克尔", "r_±=GM/c²±√[(GM/c²)²−a²]，a=J/(Mc)", "真空、轴对称、稳态旋转黑洞具有内外视界和拖曳效应。", "无电荷克尔解；存在视界要求 |a|≤GM/c²，实际天体外部仅近似满足理想条件。", "M 质量，J 角动量，a 自旋长度参数", "黑洞成像、吸积盘、引力波模型", "给出天体物理黑洞比史瓦西解更现实的旋转几何。", "kerr", ("schwarzschild", "general-relativity"))
add("black-hole-thermodynamics", "相对论", "黑洞与量子", 1975, "黑洞热力学与霍金温度", "贝肯斯坦、霍金；黑洞力学研究者", "T_H=ℏκ/(2πk_Bc)，S_BH=k_Bc³A/(4Gℏ)", "事件视界的表面引力和面积分别对应温度与熵。", "半经典量子场论、近稳态黑洞；完整量子引力微观解释仍非单一已证实理论。", "κ 表面引力，A 视界面积", "黑洞蒸发、量子引力、信息问题", "首次把引力、量子理论、热力学和信息同时置于一个公式中。", "hawking", ("kerr-metric", "second-law"), date="1972—1975 年")

# Quantum mechanics: model systems and controlled approximations.
add("quantum-oscillator", "量子物理", "基本模型", 1926, "量子谐振子", "海森堡、薛定谔、狄拉克等", "E_n=ℏω(n+1/2)，n=0,1,2,…", "简谐势中的能级等间隔，并具有不可消除的零点能。", "一维非相对论理想谐振子；非谐系统只可在平衡点附近近似。", "ω 角频率，n 量子数，ℏ 约化普朗克常数", "量子光学、分子振动、场量子化", "成为量子理论中可精确求解且可推广到无穷场模的核心模型。", "mit-qm1", ("simple-harmonic", "schrodinger"))
add("quantum-angular-momentum", "量子物理", "角动量与自旋", 1925, "量子角动量与自旋", "乌伦贝克、古德斯米特；泡利、狄拉克等", "[J_i,J_j]=iℏε_ijkJ_k，J²|jm⟩=ℏ²j(j+1)|jm⟩", "空间旋转的量子生成元具有离散本征值，并包含无经典轨道对应的内禀自旋。", "孤立角动量代数；具体耦合、测量轴和粒子统计需另行指定。", "j 总角动量量子数，m 磁量子数，ε_ijk Levi-Civita 符号", "原子谱、磁共振、量子比特", "把旋转对称性与量子态分类直接联系起来。", "mit-qm2", ("bohr", "pauli"), date="1925—1927 年")
add("perturbation-theory", "量子物理", "近似与计算", 1926, "定态微扰理论", "薛定谔、泡利等早期量子理论研究者", "E_n^(1)=⟨n⁽⁰⁾|V|n⁽⁰⁾⟩", "将难解哈密顿量写成可解部分加小扰动，逐阶修正能量和态。", "所示为非简并一阶结果；需扰动展开收敛或至少渐近有效，简并能级须先对角化扰动。", "V 扰动算符，|n⁽⁰⁾⟩ 未扰动态", "精细结构、Stark/Zeeman 效应、材料能级", "提供量子理论从理想模型走向真实系统的系统近似语言。", "mit-qm3", ("quantum-variational", "fermi-golden"))
add("wkb", "量子物理", "半经典近似", 1926, "WKB 近似", "温策尔、克拉默斯、布里渊；杰弗里斯等有先驱", "ψ(x)≈C/√|p(x)| exp[±(i/ℏ)∫p(x)dx]", "当势能变化相对局域波长缓慢时，量子波函数可由经典动量构造。", "远离转向点且 |ℏp′/p²|≪1；转向点需连接公式，禁阻区指数改为实衰减。", "p(x)=√[2m(E−V)]，C 归一化常数", "隧穿、束缚态量子化、半经典传播", "定量连接经典作用量与量子相位。", "mit-qm3", ("tunneling", "schrodinger"))
add("born-scattering", "量子物理", "散射", 1926, "散射的第一 Born 近似", "马克斯·玻恩", "f⁽¹⁾(q)=−m/(2πℏ²)∫e^(−iq·r)V(r)d³r", "弱势散射振幅近似为势能的空间傅里叶变换。", "非相对论、弱散射或高入射能；该归一化中 q 是波矢转移，长程库仑势需谨慎处理。", "f 散射振幅，V 势能，q=k_f−k_i", "中子散射、原子碰撞、结构反演", "把可测散射角分布与相互作用势的空间结构直接联系起来。", "mit-qm3", ("fermi-golden", "rutherford"))

# Condensed matter: periodic solids, quasiparticles and mesoscopic transport.
add("bloch-theorem", "凝聚态", "能带与晶体", 1928, "布洛赫定理", "费利克斯·布洛赫", "ψ_nk(r)=e^(ik·r)u_nk(r)，u_nk(r+R)=u_nk(r)", "周期势中的单电子态是平面波与晶格周期函数的乘积。", "无限或采用周期边界条件的理想晶体；无序、强相互作用和有限边界需推广。", "k 晶体动量，R 晶格矢量，n 能带指标", "能带计算、电子与光子晶体", "把晶格平移对称性转化为能带和布里渊区结构。", "bloch mit-solid", ("band-theory", "bragg"), date="1928—1929 年")
add("phonon", "凝聚态", "晶格动力学", 1932, "声子与晶格振动量子化", "塔姆、弗伦克尔等；玻恩晶格理论奠基", "H=Σ_qs ℏω_qs(n_qs+1/2)", "晶格简正模量子化后形成携带能量和晶体动量的声子准粒子。", "谐近似晶体；非谐相互作用决定有限寿命、热膨胀和热阻。", "q 波矢，s 支指标，n_qs 占据数", "热容、导热、拉曼与中子散射", "为固体中的热和机械波提供统一量子描述。", "mit-solid", ("debye", "bose-einstein"))
add("tight-binding", "凝聚态", "电子结构", 1954, "紧束缚模型", "斯莱特、科斯特等；LCAO 方法有更早发展", "E(k)=ε₀−2t cos(ka)（一维最近邻）", "局域原子轨道之间的跃迁展宽为晶体能带。", "所示为单轨道一维最近邻模型；真实材料常需多轨道、更远跃迁和自旋轨道耦合。", "t 跃迁积分，a 晶格常数，ε₀ 在位能", "能带、石墨烯、拓扑与莫特模型", "为化学成键直觉和晶体能带之间建立可计算桥梁。", "tight-binding", ("bloch-theorem", "hubbard-model"))
add("landauer-conductance", "凝聚态", "介观输运", 1957, "Landauer 电导公式", "罗尔夫·朗道尔；Büttiker 等推广", "G=(2e²/h)Σ_n T_n", "相干导体的电导由各传播通道的透射率决定。", "线性响应、低温弹性相干输运；因子2表示自旋简并，非简并或相互作用体系需修改。", "T_n 第 n 通道透射概率，G 二端电导", "量子点、纳米线、弹道输运", "把电阻理解为散射与接触共同产生的量子输运性质。", "landauer", ("quantum-hall", "fermi-dirac"))
add("fractional-quantum-hall", "凝聚态", "拓扑与强关联", 1982, "分数量子霍尔效应", "崔琦、施特默、戈萨德；Laughlin 等解释", "σ_xy=νe²/h，ν 为特定分数", "强磁场二维电子体系因相互作用形成具有分数电荷激发的拓扑量子液体。", "高迁移率二维电子气、低温强磁场；具体分数和能隙依赖填充与相互作用。", "ν 填充因子，σ_xy 霍尔电导", "拓扑量子态、任意子、量子计量", "证明电子关联可产生超越单粒子能带的拓扑序。", "fqhe", ("quantum-hall", "topological-insulator"))

# Nuclear and particle structure.
add("nuclear-shell-model", "核与粒子", "核结构", 1949, "核壳模型与幻数", "玛丽亚·格佩特-梅耶、延森等", "H≈Σ_i[p_i²/(2m)+U(r_i)+ξ(r_i)l_i·s_i]", "核子在平均势与强自旋轨道耦合中占据离散壳层。", "独立粒子平均场近似；剩余核子相互作用和集体运动需超越简单壳模型。", "U 平均势，l·s 自旋轨道耦合", "核自旋、磁矩、稳定性与跃迁", "解释 2、8、20、28、50、82、126 等幻数及核结构规律。", "shell", ("semi-empirical-mass", "pauli"))
add("breit-wigner", "核与粒子", "共振与散射", 1936, "Breit–Wigner 共振线形", "格雷戈里·布赖特、尤金·维格纳", "σ(E)∝Γ_inΓ_out/[(E−E_R)²+(Γ/2)²]", "短寿命中间态在散射截面中产生以共振能量为中心的峰。", "孤立窄共振、背景缓慢变化；精确归一化含自旋、波数和分波因子。", "E_R 共振能，Γ 总宽度，Γ_in/out 分宽度", "核反应、粒子共振、谱线寿命", "把共振峰宽与不稳定态寿命、衰变道联系起来。", "breit-wigner", ("fermi-golden", "rutherford"))
add("quark-model", "核与粒子", "强子结构", 1964, "夸克模型", "盖尔曼、茨威格", "重子∼qqq，介子∼q q̄；Q_u=+2e/3，Q_d=−e/3", "强子可按具有分数电荷、味和色自由度的夸克组成分类。", "这是强子价夸克分类的简图；真实强子态还含胶子和海夸克，由 QCD 动力学决定。", "q 夸克，q̄ 反夸克，Q 电荷", "强子谱、衰变分类、对撞机物理", "把大量强子整理为少数基本自由度，并为 QCD 奠定对象基础。", "quark pdg-quark", ("qcd-asymptotic", "standard-model"))
add("ckm-matrix", "核与粒子", "味物理与 CP 破坏", 1973, "CKM 夸克混合矩阵", "小林诚、益川敏英；卡比博先驱", "d′_i=Σ_jV_ij d_j，J=Im(V_ijV_klV*_ilV*_kj)", "弱相互作用本征态与夸克质量本征态之间存在三代酉混合。", "三代标准模型；Jarlskog 不变量 J 刻画不可通过重定义去除的 CP 相位。", "V_ij CKM 元素，J CP 破坏不变量", "B/K 介子、味物理、宇称与 CP 检验", "说明三代夸克即可在标准模型内产生 CP 破坏。", "ckm pdg-ckm", ("electroweak", "standard-model"))

# Relativistic stars and observational cosmology.
add("tov-equation", "天体与宇宙", "致密星", 1939, "TOV 相对论静力平衡方程", "理查德·托尔曼、奥本海默、沃尔科夫", "dp/dr=−G(ρ+p/c²)(m+4πr³p/c²)/[r²(1−2Gm/(rc²))]", "球对称恒星中压力梯度平衡广义相对论引力。", "静态、球对称、各向同性流体；还需状态方程和 dm/dr=4πr²ρ。", "p 压力，ρ 质量密度，m(r) 包含质量", "中子星质量半径、致密物质状态方程", "把牛顿恒星结构推广到强引力并给出最大质量问题。", "tov", ("hydrostatic-star", "general-relativity"), date="1934—1939 年")
add("gravitational-lensing", "天体与宇宙", "引力透镜", 1936, "引力透镜与爱因斯坦角", "爱因斯坦；埃丁顿、兹维基等有关键贡献", "θ_E=√[(4GM/c²)D_ls/(D_lD_s)]", "质量弯曲光路，使背景源出现多像、放大或形变。", "薄透镜、小角度、点质量及适当距离定义；扩展质量需用面密度积分。", "D_l、D_s、D_ls 为角直径距离，M 透镜质量", "暗物质测绘、系外行星、宇宙距离", "把时空曲率变成跨尺度质量分布探针。", "lensing carroll-gr", ("geodesic", "fermat"))
add("cmb-blackbody", "天体与宇宙", "早期宇宙观测", 1965, "宇宙微波背景辐射", "彭齐亚斯、威尔逊；迪克团队等；COBE/FIRAS 精密测谱", "T₀≈2.7255 K，ΔT/T∼10⁻⁵", "全天微波背景具有近乎完美黑体谱，并含记录早期密度扰动的微小各向异性。", "温度为今日单极谱温度；前景辐射和观测系统需分离，各向异性随角尺度变化。", "T₀ 平均温度，ΔT 温度涨落", "宇宙参数、结构形成、早期宇宙检验", "提供热大爆炸最关键的观测证据之一。", "cmb", ("planck-spectrum", "big-bang"), date="1965 年发现；1990年代精密黑体谱")
add("big-bang-nucleosynthesis", "天体与宇宙", "早期宇宙", 1948, "大爆炸核合成", "伽莫夫、阿尔弗、赫尔曼等；现代网络计算发展", "n/p≈exp[−Δmc²/(k_BT)]，Y_p≈2(n/p)/(1+n/p)", "早期宇宙在数分钟内合成氘、氦和少量锂，丰度取决于膨胀率与重子密度。", "所示为直观近似；精密丰度需弱反应冻结、核反应网络、核数据和中子衰变。", "n/p 中子质子比，Y_p 氦-4 质量分数", "重子密度、额外辐射组分、早期宇宙检验", "把标准模型微观反应与可观测原初元素丰度联系起来。", "pdg-bbn", ("big-bang", "fermi-beta"), date="1948 年理论起点；后续精密化")

# Quantum information: recoverability and communication limits.
add("quantum-error-correction", "量子信息", "纠错与容错", 1995, "量子纠错与 Knill–Laflamme 条件", "Shor、Steane；Knill、Laflamme等", "P E_a†E_b P=c_ab P", "若所有可纠正误差在编码子空间内不可区分，量子信息可在不测量逻辑态的情况下恢复。", "针对给定误差集合和编码投影 P 的精确条件；实际容错还需综合门、测量和相关噪声。", "E_a 误差算符，P 编码空间投影，c_ab 厄米矩阵", "容错量子计算、量子存储、通信", "说明不可克隆并不阻止通过冗余纠缠保护未知量子态。", "qec preskill", ("no-cloning", "lindblad"), date="1995—1997 年")
add("holevo-bound", "量子信息", "量子通信", 1973, "Holevo 信息界", "亚历山大·霍列沃", "I(X:Y)≤χ=S(Σ_xp_xρ_x)−Σ_xp_xS(ρ_x)", "从量子态集合中通过任意测量可获得的经典互信息受到 Holevo 量限制。", "单次编码集合及一般 POVM；达到上界不总是可能，多次联合编码测量需使用相应渐近理论。", "p_x 先验概率，ρ_x 编码态，S 冯·诺依曼熵", "量子信道容量、编码与安全通信", "给出量子载体承载可读经典信息的基本上限。", "holevo preskill", ("von-neumann-entropy", "density-matrix"))

# Quantum field theory: sums over histories and scale-dependent descriptions.
add("path-integral", "量子场论", "量子化方法", 1948, "费曼路径积分", "理查德·费曼；狄拉克有先驱思想", "K(b,a)=∫𝒟x exp[iS[x]/ℏ]", "量子振幅由所有连接初末态的历史按作用量相位叠加得到。", "形式表达需通过离散化、解析延拓或其他正则化定义；规范场还需处理规范冗余。", "K 传播子，S[x] 作用量，𝒟x 路径测度", "量子场论、统计场论、半经典近似", "以作用量为中心统一量子力学、场论和统计配分函数。", "path-integral", ("einstein-hilbert", "schrodinger"))
add("renormalization-group", "量子场论", "尺度与重整化", 1971, "重整化群流", "肯尼斯·威尔逊；盖尔曼、洛等有先驱", "μ dg/dμ=β(g)", "理论参数随观察能标流动，不同微观系统可趋向相同低能固定点。", "耦合和 β 函数依方案与截断定义；临界指数等物理量在适当条件下具有普适性。", "μ 重整化能标，g 耦合，β(g) 流函数", "临界现象、QCD、连续相变", "解释有效理论为何依赖尺度以及普适性如何出现。", "rg", ("qcd-asymptotic", "landau-phase"))
add("effective-field-theory", "量子场论", "有效理论", 1979, "有效场论展开", "史蒂文·温伯格等", "ℒ_eff=Σ_i C_i O_i/Λ^(d_i−4)", "低能物理可按对称性写成局域算符并按高能尺度的幂系统排序。", "能量 E≪Λ，且已保留相关低能自由度；截断误差按展开参数估计。", "O_i 维数 d_i 的算符，C_i Wilson 系数，Λ 截止尺度", "核力、弱衰变、引力与新物理搜索", "将“不知道高能细节”转化为可控、可改进的低能预测。", "eft", ("qcd-asymptotic", "fermi-beta"))

# Plasma physics: kinetic damping, fluid closure and topology change.
add("landau-damping", "等离子体", "动理学效应", 1946, "Landau 阻尼", "列夫·朗道", "ε(ω,k)=1+(ω_p²/k²)∫[∂f₀/∂v]/(v−ω/k)dv=0（Landau 路径）", "无碰撞等离子体通过与波相速度附近粒子的相位混合使电场宏观衰减。", "线性化 Vlasov–Poisson、均匀稳定分布；积分极点需按因果 Landau 轮廓处理。", "f₀ 平衡速度分布，ω 复频率，k 波数", "束流稳定性、空间等离子体、聚变波加热", "揭示无碰撞、微观可逆体系也可出现宏观阻尼。", "mit-plasma", ("vlasov", "plasma-frequency"))
add("ideal-mhd", "等离子体", "磁流体", 1942, "理想磁流体力学与冻结磁通", "汉内斯·阿尔芬等", "∂B/∂t=∇×(v×B)，E+v×B=0，∇·B=0", "高电导流体中的磁场随等离子体运动，磁通在理想极限下冻结。", "单流体、局域热力学闭合、尺度远大于动力学尺度且电阻率可忽略；冲击和小尺度层需扩展。", "B 磁场，v 流速，E 电场", "太阳风、磁约束聚变、天体喷流", "把麦克斯韦场与流体动量方程耦合成跨尺度等离子体模型。", "mit-plasma", ("alfven", "navier-stokes"))
add("magnetic-reconnection", "等离子体", "磁拓扑与耗散", 1957, "磁重联", "彼得·斯威特、尤金·帕克等", "E_rec≈v_inB；扩散区内 E+v×B≠0", "非理想区域允许磁力线连接关系改变并将磁能快速转化为热和粒子能量。", "重联率和微观机制依电阻、Hall 项、压力张量及三维结构；理想 MHD 本身不能改变拓扑。", "E_rec 重联电场，v_in 入流速度，B 上游磁场", "太阳耀斑、磁层亚暴、聚变装置", "解释磁场拓扑突变与爆发式能量释放。", "reconnection", ("ideal-mhd", "faraday"), date="1956—1957 年")

# Nonlinear dynamics: local bifurcations, synchronization and pattern formation.
add("bifurcation-normal-form", "非线性与复杂系统", "分岔与稳定性", 1892, "鞍结分岔正规形", "庞加莱、李雅普诺夫及后续分岔理论", "ẋ=μ−x²", "控制参数穿过临界值时，一对稳定与不稳定定点产生或湮灭。", "一维连续动力系统在非退化鞍结附近的局部正规形；高维全局行为需中心流形等推广。", "x 状态变量，μ 控制参数", "阈值、跳变、灾变与生态模型", "用少数普适正规形分类看似不同系统的定性突变。", "mit-chaos", ("logistic-map", "lyapunov"), date="19世纪末奠基；20世纪系统化")
add("kuramoto-model", "非线性与复杂系统", "同步", 1975, "Kuramoto 相位振子模型", "藏本由纪；Winfree 等有先驱", "θ̇_i=ω_i+(K/N)Σ_j sin(θ_j−θ_i)", "具有不同本征频率的弱耦合振子可在耦合超过阈值后集体同步。", "全连接、正弦相位耦合的简化模型；网络结构、惯性和噪声会改变转变。", "θ_i 相位，ω_i 本征频率，K 耦合强度", "电网、神经节律、激光阵列", "给出从个体节律到宏观同步的可解析最小模型。", "kuramoto", ("simple-harmonic", "lorenz-system"))
add("turing-pattern", "非线性与复杂系统", "反应扩散与模式", 1952, "Turing 反应–扩散失稳", "艾伦·图灵", "∂_t u=D_u∇²u+f(u,v)，∂_t v=D_v∇²v+g(u,v)", "均匀稳定反应态可因不同扩散速率而对有限波数扰动失稳并形成空间图案。", "至少两个耦合组分并满足相应雅可比与扩散失稳条件；不是所有反应扩散系统都会形成 Turing 图案。", "u、v 组分场，D_u、D_v 扩散系数", "形态发生、化学斑图、生态空间结构", "说明扩散不仅平滑差异，也能与反应共同创造有序结构。", "turing", ("diffusion-fick", "logistic-map"))

# Numerical physics: discretization, transforms and kinetic solvers.
add("finite-element", "计算与数学物理", "偏微分方程数值方法", 1943, "有限元方法与弱形式", "理查德·库朗；工程界后续发展", "求 u_h∈V_h：a(u_h,v_h)=ℓ(v_h)，∀v_h∈V_h", "将偏微分方程的弱形式限制到分片有限维函数空间。", "需选择相容弱形式、网格、基函数和边界条件；误差与稳定性取决于空间及问题类型。", "V_h 离散函数空间，a 双线性形式，ℓ 载荷泛函", "结构、电磁、传热与多物理场", "使复杂几何上的连续场方程能够统一离散求解。", "fem mit-numerical", ("elasticity-cauchy", "yee-fdtd"), kind="数值方法")
add("fast-fourier-transform", "计算与数学物理", "快速算法", 1965, "快速傅里叶变换 FFT", "库利、图基；高斯等有早期算法思想", "X_k=Σ_(n=0)^(N−1)x_n e^(−i2πkn/N)，计算量 O(N logN)", "利用离散傅里叶变换的因子分解显著减少运算量。", "快速复杂度依 N 的可分解结构和具体算法；FFT 不改变采样、窗函数与混叠限制。", "x_n 样本，X_k 离散频谱，N 点数", "谱分析、卷积、成像与 PDE", "让频域方法从理论工具成为大规模计算基础设施。", "fft", ("fourier", "yee-fdtd"), kind="数值方法")
add("spectral-method", "计算与数学物理", "偏微分方程数值方法", 1971, "谱方法", "Orszag、Gottlieb 等；傅里叶与切比雪夫方法奠基", "u_N(x,t)=Σ_(n=0)^N a_n(t)φ_n(x)", "用全局正交基展开解，对光滑问题可获得随阶数快速下降的误差。", "解和几何足够光滑时最有效；间断产生 Gibbs 现象，复杂几何与非线性混叠需专门处理。", "φ_n 基函数，a_n 模态系数，N 截断阶数", "湍流 DNS、波动、量子与气候模型", "把傅里叶分析直接转化为高精度场方程求解器。", "mit-numerical", ("fourier", "navier-stokes"), date="20世纪60—70年代", kind="数值方法")
add("lattice-boltzmann", "计算与数学物理", "介观流体数值方法", 1988, "格子 Boltzmann 方法", "麦克纳马拉、扎内蒂；Higuera、Succi 等发展", "f_i(x+c_iΔt,t+Δt)−f_i(x,t)=−(Δt/τ)[f_i−f_i^eq]", "离散速度分布通过迁移和碰撞恢复宏观流体方程。", "所示为单松弛时间 BGK 格式；低马赫、网格各向同性和稳定性限制须满足。", "f_i 离散分布，c_i 格子速度，τ 松弛时间", "多相流、孔隙流、复杂边界流动", "在粒子动理学和连续流体求解之间建立高并行介观算法。", "lbm", ("boltzmann-equation", "navier-stokes"), kind="数值方法")


content = "// Second curated expansion; generated by scripts/build-expansion.py.\n(() => {\n"
content += "const additions = " + json.dumps(ROWS, ensure_ascii=False, indent=2) + ";\n"
content += "PHYSICS_DATA.push(...additions);\n})();\n"
(ROOT / "data-expansion.js").write_text(content, encoding="utf-8")
print("Generated", len(ROWS), "new records")
