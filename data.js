const FIELD_META = {
  "力学": { color: "#68ddfa", short: "MECH" },
  "电学": { color: "#f6c85f", short: "ELEC" },
  "磁学与电磁": { color: "#a993ff", short: "EM" },
  "热学与统计": { color: "#ff846f", short: "THERMO" },
  "光学": { color: "#70e6b2", short: "OPTICS" },
  "声学与波动": { color: "#79a8ff", short: "WAVES" },
  "流体力学": { color: "#4fd1c5", short: "FLUID" },
  "相对论": { color: "#ff9fc7", short: "REL" },
  "量子物理": { color: "#c3a6ff", short: "QUANT" },
  "凝聚态": { color: "#a8db72", short: "MATTER" },
  "核与粒子": { color: "#ffac66", short: "NUCLEAR" },
  "天体与宇宙": { color: "#83b5ff", short: "COSMOS" }
};

const PHYSICS_DATA = [
  {
    id: "galileo-fall", field: "力学", year: 1604, date: "约 1604 年", title: "自由落体定律", people: "伽利略·伽利莱",
    formula: "s = ½gt²", summary: "忽略空气阻力时，所有物体以相同的重力加速度下落。",
    context: "伽利略以斜面实验和数学分析取代亚里士多德式的定性运动观。其手稿约在 1604 年明确平方时间关系，1638 年系统出版。",
    application: "弹道学、运动测量、航天轨迹", significance: "确立实验、理想化模型和数学表达相结合的近代物理方法。"
  },
  {
    id: "kepler", field: "力学", year: 1609, date: "1609—1619 年", title: "开普勒行星运动定律", people: "约翰内斯·开普勒",
    formula: "T² ∝ a³", summary: "行星沿椭圆轨道运动，面积速度恒定，周期平方与半长轴立方成正比。",
    context: "开普勒依据第谷·布拉赫的高精度观测，在 1609 年提出前两定律，1619 年发表第三定律。",
    application: "卫星定轨、天体历表、行星探测", significance: "把日心说变成精确可检验的定量理论，并为万有引力定律提供经验基础。"
  },
  {
    id: "newton-laws", field: "力学", year: 1687, date: "1687 年", title: "牛顿运动定律", people: "艾萨克·牛顿",
    formula: "F = dp/dt　（恒质量时 F = ma）", summary: "以惯性、动力响应和相互作用三条定律建立经典运动学框架。",
    context: "牛顿在《自然哲学的数学原理》中综合伽利略、笛卡尔和惠更斯等人的工作，给出统一动力学体系。",
    application: "机械工程、车辆、机器人、航天", significance: "首次用少数普适定律统一地面运动与天体运动，奠定经典物理骨架。"
  },
  {
    id: "gravitation", field: "力学", year: 1687, date: "1687 年", title: "万有引力定律", people: "艾萨克·牛顿（胡克等人有先驱贡献）",
    formula: "F = Gm₁m₂/r²", summary: "任意两个有质量物体之间存在与质量乘积成正比、与距离平方成反比的引力。",
    context: "平方反比思想已有多位先驱讨论，牛顿完成了从运动定律到行星轨道的系统数学证明。",
    application: "卫星导航、轨道设计、天体质量测量", significance: "实现“天上与人间”的第一次物理统一，展示自然规律的普适性。"
  },
  {
    id: "lagrange", field: "力学", year: 1788, date: "1788 年", title: "拉格朗日力学", people: "约瑟夫-路易·拉格朗日",
    formula: "d/dt(∂L/∂q̇ᵢ) − ∂L/∂qᵢ = 0", summary: "以能量差 L=T−V 和广义坐标描述复杂系统的运动。",
    context: "《分析力学》把牛顿力学重写为统一的变分与坐标形式，减少对几何图示和逐个受力分析的依赖。",
    application: "多体系统、机器人、连续介质、场论", significance: "揭示动力学与最小作用量之间的结构，为现代场论提供通用语言。"
  },
  {
    id: "hamilton", field: "力学", year: 1833, date: "1833—1835 年", title: "哈密顿力学", people: "威廉·罗恩·哈密顿",
    formula: "q̇ᵢ=∂H/∂pᵢ， ṗᵢ=−∂H/∂qᵢ", summary: "在相空间中以位置和动量的对称一阶方程描述系统演化。",
    context: "哈密顿由光学与力学的类比发展正则形式，使守恒量、相空间和变换理论成为核心。",
    application: "轨道动力学、统计物理、量子理论", significance: "连接经典力学、统计力学和量子力学，是现代理论物理的基础结构。"
  },

  {
    id: "coulomb", field: "电学", year: 1785, date: "1785 年", title: "库仑定律", people: "夏尔-奥古斯丁·库仑",
    formula: "F = kq₁q₂/r²", summary: "点电荷之间的静电力服从平方反比关系，方向沿两电荷连线。",
    context: "库仑使用扭秤定量测量微弱电力；普里斯特利、卡文迪许等人的早期工作也提供了重要线索。",
    application: "静电除尘、电容器、电子束控制", significance: "使电学从现象描述走向精确测量，并确立电场理论的经验起点。"
  },
  {
    id: "ohm", field: "电学", year: 1827, date: "1827 年", title: "欧姆定律", people: "格奥尔格·西蒙·欧姆",
    formula: "V = IR", summary: "在一定条件下，导体两端电压与电流成正比，比例系数为电阻。",
    context: "欧姆把傅里叶热传导的数学类比用于电流研究，其成果起初受到质疑，随后成为电路分析基石。",
    application: "电路设计、传感器、功率系统", significance: "建立电压、电流与材料性质的可测关系，使定量电路工程成为可能。"
  },
  {
    id: "gauss-electric", field: "电学", year: 1835, date: "约 1835 年", title: "高斯定律（电）", people: "卡尔·弗里德里希·高斯",
    formula: "∮ E·dA = Qₑₙc/ε₀", summary: "闭合曲面的电通量只由曲面包围的净电荷决定。",
    context: "高斯在 1830 年代形成相关结果，后由麦克斯韦纳入电磁场方程组。它与库仑定律在静电条件下等价。",
    application: "对称电场计算、高压工程、电磁仿真", significance: "把局部电场与整体电荷联系起来，体现场论中的散度结构。"
  },
  {
    id: "kirchhoff", field: "电学", year: 1845, date: "1845 年", title: "基尔霍夫电路定律", people: "古斯塔夫·基尔霍夫",
    formula: "ΣI = 0， ΣV = 0", summary: "节点电流守恒、闭合回路电压代数和为零。",
    context: "基尔霍夫将电荷守恒与能量守恒转化为可直接求解复杂网络的两组规则。",
    application: "集成电路、电网、电子测量", significance: "把基本守恒律变成工程算法，至今仍是电路分析的第一语言。"
  },

  {
    id: "ampere", field: "磁学与电磁", year: 1820, date: "1820—1826 年", title: "安培环路定律", people: "安德烈-马里·安培",
    formula: "∮ B·dl = μ₀Iₑₙc", summary: "稳恒电流产生环绕电流分布的磁场。",
    context: "奥斯特发现电流磁效应后，安培迅速开展定量研究并建立电动力学；麦克斯韦后来补入位移电流项。",
    application: "电磁铁、电机、变压器", significance: "揭示电流是磁场的重要来源，开启电与磁的系统统一。"
  },
  {
    id: "faraday", field: "磁学与电磁", year: 1831, date: "1831 年", title: "法拉第电磁感应定律", people: "迈克尔·法拉第（约瑟夫·亨利独立发现）",
    formula: "ℰ = −dΦᴮ/dt", summary: "穿过回路的磁通量变化会产生感应电动势，其方向反抗磁通变化。",
    context: "法拉第通过线圈与磁铁实验发现感应，并以“力线”形成场的物理图像；负号由楞次定律表达。",
    application: "发电机、无线充电、感应炉", significance: "给出机械能大规模转化为电能的物理原理，奠定现代电气化社会。"
  },
  {
    id: "maxwell", field: "磁学与电磁", year: 1865, date: "1861—1865 年", title: "麦克斯韦方程组", people: "詹姆斯·克拉克·麦克斯韦",
    formula: "∇·E=ρ/ε₀　∇×B=μ₀J+μ₀ε₀∂E/∂t", summary: "四个方程统一描述电场、磁场、电荷与电流，并预言电磁波。",
    context: "麦克斯韦综合库仑、安培与法拉第等成果，引入位移电流；今天常见的矢量形式由赫维赛德等人重写。",
    application: "无线通信、雷达、天线、光电子", significance: "完成电、磁、光的统一，并首次由理论计算出波的传播速度。"
  },
  {
    id: "lorentz-force", field: "磁学与电磁", year: 1895, date: "1895 年", title: "洛伦兹力定律", people: "亨德里克·洛伦兹（多位先驱贡献）",
    formula: "F = q(E + v×B)", summary: "电磁场对运动电荷的作用由电场力与速度相关的磁场力共同构成。",
    context: "洛伦兹在电子理论中给出成熟表达；相关磁力形式可追溯到拉普拉斯、安培和麦克斯韦。",
    application: "粒子加速器、质谱仪、电动机", significance: "把电磁场与带电物质的运动连接起来，是经典电动力学的动力学核心。"
  },

  {
    id: "zeroth", field: "热学与统计", year: 1931, date: "20 世纪初形成，1931 年命名", title: "热力学第零定律", people: "拉尔夫·福勒（命名）；多位热学先驱",
    formula: "Tₐ=Tᵦ 且 Tᵦ=T𝚌 ⇒ Tₐ=T𝚌", summary: "若两个系统分别与第三个系统热平衡，它们彼此也处于热平衡。",
    context: "温度计实践早已隐含这一原理，福勒在其他热力学定律编号固定后称其为“第零定律”。",
    application: "温标、温度计、过程控制", significance: "为温度作为可比较、可测量的状态量提供逻辑基础。"
  },
  {
    id: "first-law", field: "热学与统计", year: 1847, date: "1840 年代", title: "热力学第一定律", people: "焦耳、迈尔、亥姆霍兹等",
    formula: "ΔU = Q − W", summary: "系统内能变化等于输入热量减去系统对外做功。",
    context: "机械功与热等价的实验和能量守恒思想在 1840 年代由多位研究者相互独立地建立。",
    application: "热机、制冷、能源系统", significance: "把热纳入能量守恒的统一框架，终结“热质说”的核心地位。"
  },
  {
    id: "second-law", field: "热学与统计", year: 1850, date: "1824—1865 年", title: "热力学第二定律", people: "卡诺、克劳修斯、开尔文",
    formula: "ΔS ≥ ∫δQ/T", summary: "孤立系统的总熵不会减少，热过程具有宏观方向性。",
    context: "卡诺研究热机效率，克劳修斯与开尔文给出等价表述并建立熵概念。",
    application: "发动机效率、化工过程、信息科学", significance: "给出能量转化的限度和时间箭头，解释为何许多过程不可逆。"
  },
  {
    id: "boltzmann", field: "热学与统计", year: 1877, date: "1877 年", title: "玻尔兹曼熵公式", people: "路德维希·玻尔兹曼",
    formula: "S = kᴮ ln Ω", summary: "宏观熵由与宏观状态相容的微观状态数量决定。",
    context: "玻尔兹曼将概率引入热学，用原子和分子运动解释热力学第二定律。墓碑上的著名公式是后来的简洁表述。",
    application: "材料模拟、气体动力学、信息熵", significance: "架起微观粒子与宏观热现象的桥梁，奠定统计物理。"
  },
  {
    id: "stefan-boltzmann", field: "热学与统计", year: 1879, date: "1879—1884 年", title: "斯特藩–玻尔兹曼定律", people: "约瑟夫·斯特藩、路德维希·玻尔兹曼",
    formula: "P/A = σT⁴", summary: "理想黑体单位面积辐射功率与绝对温度四次方成正比。",
    context: "斯特藩从实验数据归纳关系，玻尔兹曼随后用热力学和电磁理论推导。",
    application: "红外测温、恒星温度、热辐射设计", significance: "把温度和电磁辐射定量相连，为量子论的黑体问题铺路。"
  },

  {
    id: "snell", field: "光学", year: 1621, date: "1621 年", title: "斯涅尔折射定律", people: "威理博·斯涅尔；伊本·萨赫勒有更早发现",
    formula: "n₁sinθ₁ = n₂sinθ₂", summary: "光跨越两种介质界面时，入射角和折射角由折射率决定。",
    context: "斯涅尔在欧洲重新发现这一关系；伊本·萨赫勒约在 984 年已用于透镜几何，笛卡尔后来发表。",
    application: "镜头、光纤、棱镜与成像", significance: "将几何光学变为精确设计工具，也是费马原理的直接结果。"
  },
  {
    id: "huygens", field: "光学", year: 1690, date: "1690 年", title: "惠更斯原理", people: "克里斯蒂安·惠更斯",
    formula: "波前上的每一点都是次级波源", summary: "后续波前可视为原波前各点发出次级波的包络面。",
    context: "惠更斯在《光论》中以波动观点解释传播、反射与折射，后来由菲涅耳加入干涉形成更完整理论。",
    application: "衍射计算、声场、地震波", significance: "提供处理复杂波前传播的几何构造，强化光的波动图景。"
  },
  {
    id: "young", field: "光学", year: 1801, date: "1801—1803 年", title: "双缝干涉", people: "托马斯·杨",
    formula: "Δx ≈ λL/d", summary: "两条相干光路叠加形成明暗条纹，条纹间距由波长和几何决定。",
    context: "杨以干涉实验有力挑战光的单纯粒子说；菲涅耳随后完成波动光学的数学发展。",
    application: "干涉测量、全息、相干成像", significance: "以清晰实验展示光的波动性，并成为量子叠加概念的经典入口。"
  },
  {
    id: "fermat", field: "光学", year: 1662, date: "1662 年", title: "费马原理", people: "皮埃尔·德·费马",
    formula: "δ∫n ds = 0", summary: "实际光路使光程取驻值，常表现为传播时间最短。",
    context: "费马以变分思想统一反射与折射；“最短时间”在一般情况下更准确地说是时间驻值。",
    application: "光学设计、射线追踪、引力透镜", significance: "把光学与最小作用量思想连接，展示物理定律的变分结构。"
  },

  {
    id: "wave-equation", field: "声学与波动", year: 1747, date: "1747—1753 年", title: "波动方程", people: "达朗贝尔、欧拉、伯努利",
    formula: "∂²u/∂t² = c²∇²u", summary: "场的时间曲率与空间曲率相联系，描述扰动以有限速度传播。",
    context: "围绕振动弦问题，达朗贝尔给出方程与行波解，欧拉和伯努利发展边界条件与模态思想。",
    application: "声学、结构振动、地震与通信", significance: "形成跨越机械波、电磁波和量子波的通用数学原型。"
  },
  {
    id: "fourier", field: "声学与波动", year: 1822, date: "1822 年", title: "傅里叶级数与变换", people: "约瑟夫·傅里叶",
    formula: "f(x)=Σ[aₙcos(nx)+bₙsin(nx)]", summary: "复杂周期函数可以分解为不同频率的正弦与余弦成分。",
    context: "傅里叶在研究热传导时系统发表这一思想，促使数学界重新思考函数、收敛和频谱。",
    application: "信号处理、医学成像、频谱分析", significance: "建立时空域与频率域之间的桥梁，成为现代信息技术的核心工具。"
  },
  {
    id: "doppler", field: "声学与波动", year: 1842, date: "1842 年", title: "多普勒效应", people: "克里斯蒂安·多普勒",
    formula: "f′ = f(v±vₒ)/(v∓vₛ)", summary: "波源和观察者相对运动会改变观察到的频率。",
    context: "多普勒最初讨论恒星颜色；效应先在声学中验证，后来广泛用于电磁波。",
    application: "测速雷达、医学超声、天文红移", significance: "让频率成为测量相对运动的无接触探针。"
  },

  {
    id: "archimedes", field: "流体力学", year: -250, date: "约公元前 250 年", title: "阿基米德浮力原理", people: "阿基米德",
    formula: "Fᵦ = ρgV", summary: "浸在流体中的物体受到向上的浮力，等于其排开流体的重量。",
    context: "阿基米德在《论浮体》中以几何方法研究静水平衡；“王冠与浴缸”的流行故事未必是可靠史实。",
    application: "船舶、潜艇、密度测量", significance: "建立最早的定量连续介质理论之一，使浮沉问题可由普适规律解释。"
  },
  {
    id: "bernoulli", field: "流体力学", year: 1738, date: "1738 年", title: "伯努利方程", people: "丹尼尔·伯努利",
    formula: "p + ½ρv² + ρgh = 常量", summary: "理想稳态流中，压力能、动能和重力势能沿流线守恒。",
    context: "伯努利在《流体动力学》中把能量思想用于流体；现代常用形式及其适用条件由后人整理。",
    application: "机翼、管流、流量计", significance: "把流速与压力定量联系，是工程流体力学最常用的近似关系之一。"
  },
  {
    id: "navier-stokes", field: "流体力学", year: 1845, date: "1822—1845 年", title: "纳维–斯托克斯方程", people: "克洛德-路易·纳维、乔治·斯托克斯",
    formula: "ρDv/Dt = −∇p + μ∇²v + ρf", summary: "将动量守恒用于黏性流体，描述速度、压力和外力的时空演化。",
    context: "纳维从分子模型提出方程，斯托克斯用连续介质观点给出成熟形式。其三维解的光滑性仍是数学难题。",
    application: "空气动力学、天气、血流、湍流", significance: "是连续介质与计算流体力学的核心方程，支撑众多工程预测。"
  },

  {
    id: "special-relativity", field: "相对论", year: 1905, date: "1905 年", title: "狭义相对论", people: "阿尔伯特·爱因斯坦（洛伦兹、庞加莱等有先驱贡献）",
    formula: "γ = 1/√(1−v²/c²)", summary: "物理定律在所有惯性系中相同，真空光速对所有惯性观察者恒定。",
    context: "爱因斯坦以两个基本原理重构时空与同时性，洛伦兹变换和相对性思想此前已有重要发展。",
    application: "粒子加速器、卫星导航、核能", significance: "推翻绝对时空，揭示时间膨胀、长度收缩和质能关系。"
  },
  {
    id: "mass-energy", field: "相对论", year: 1905, date: "1905 年", title: "质能等价", people: "阿尔伯特·爱因斯坦",
    formula: "E₀ = mc²", summary: "静质量对应巨大的静止能量，质量是系统总能量的一种表现。",
    context: "爱因斯坦在狭义相对论框架中论证物体辐射能量会造成质量减少，后来形成著名简式。",
    application: "核裂变、核聚变、粒子反应", significance: "重塑质量与能量概念，解释恒星能源和核过程。"
  },
  {
    id: "general-relativity", field: "相对论", year: 1915, date: "1915 年", title: "广义相对论", people: "阿尔伯特·爱因斯坦；希尔伯特等有数学贡献",
    formula: "Gμν + Λgμν = (8πG/c⁴)Tμν", summary: "物质与能量弯曲时空，弯曲的时空决定物体和光如何运动。",
    context: "爱因斯坦把等效原理发展为几何引力理论，于 1915 年完成场方程。黎曼几何提供了数学语言。",
    application: "GPS校正、黑洞、引力波、宇宙学", significance: "以动态时空取代牛顿引力的超距作用，预言多种全新宇宙现象。"
  },

  {
    id: "planck", field: "量子物理", year: 1900, date: "1900 年", title: "普朗克量子假设", people: "马克斯·普朗克",
    formula: "E = hν", summary: "振子与辐射交换能量时，能量以与频率成正比的离散份额出现。",
    context: "普朗克为解释黑体辐射谱引入能量元 hν，最初把它视为计算假设，却开启量子革命。",
    application: "光谱学、温度计、量子器件", significance: "首次把自然中的作用量尺度 h 引入基础物理，打破经典连续性。"
  },
  {
    id: "photoelectric", field: "量子物理", year: 1905, date: "1905 年", title: "光电效应方程", people: "阿尔伯特·爱因斯坦（基于普朗克量子）",
    formula: "Kₘₐₓ = hν − φ", summary: "光以量子传递能量，只有频率超过材料阈值才能逸出电子。",
    context: "爱因斯坦把普朗克量子推广为光本身的能量量子，解释经典波动论无法说明的截止频率。",
    application: "光电探测、太阳能电池、成像传感器", significance: "确立光的粒子性，是量子理论获得实验支撑的关键节点。"
  },
  {
    id: "bohr", field: "量子物理", year: 1913, date: "1913 年", title: "玻尔原子模型", people: "尼尔斯·玻尔",
    formula: "Eₙ = −13.6 eV/n²", summary: "电子只允许处于离散稳定能级，能级跃迁时吸收或发射光子。",
    context: "玻尔把卢瑟福核式原子与量子假设结合，成功解释氢原子谱，但仍是半经典模型。",
    application: "光谱分析、激光原理、原子钟", significance: "把能级量子化引入原子结构，为完整量子力学提供直接目标。"
  },
  {
    id: "de-broglie", field: "量子物理", year: 1924, date: "1924 年", title: "德布罗意物质波", people: "路易·德布罗意",
    formula: "λ = h/p", summary: "任何具有动量的粒子都对应一个波长，物质同样具有波粒二象性。",
    context: "德布罗意把光的波粒二象性对称地推广到物质，随后由电子衍射实验验证。",
    application: "电子显微镜、晶体衍射、量子传感", significance: "把波动性扩展到物质，直接启发薛定谔建立波动力学。"
  },
  {
    id: "schrodinger", field: "量子物理", year: 1926, date: "1926 年", title: "薛定谔方程", people: "埃尔温·薛定谔",
    formula: "iℏ∂ψ/∂t = Ĥψ", summary: "量子态的波函数按照哈密顿算符确定性演化，测量结果由概率给出。",
    context: "薛定谔受德布罗意物质波和哈密顿光机类比启发建立波动力学，与海森堡矩阵力学等价。",
    application: "化学键、半导体、激光、量子计算", significance: "提供非相对论量子系统的基本动力学方程，解释原子与材料微观结构。"
  },
  {
    id: "uncertainty", field: "量子物理", year: 1927, date: "1927 年", title: "海森堡不确定性原理", people: "维尔纳·海森堡",
    formula: "ΔxΔp ≥ ℏ/2", summary: "位置与动量等共轭物理量不能在同一量子态中同时具有任意小的不确定度。",
    context: "它源于量子态的数学结构和不可对易算符，不只是测量仪器对粒子的普通扰动。",
    application: "量子极限测量、隧穿器件、零点能", significance: "表明经典确定轨迹在微观世界失效，概率不是单纯的知识不足。"
  },

  {
    id: "bragg", field: "凝聚态", year: 1913, date: "1913 年", title: "布拉格衍射定律", people: "威廉·亨利·布拉格、威廉·劳伦斯·布拉格",
    formula: "nλ = 2d sinθ", summary: "晶体晶面散射波在特定角度相长干涉，由此反演原子间距。",
    context: "在劳厄发现 X 射线晶体衍射后，布拉格父子给出简洁几何解释并发展结构分析。",
    application: "X射线晶体学、材料鉴定、蛋白结构", significance: "让人类能够实验测定原子排列，改变材料科学、化学与生物学。"
  },
  {
    id: "band-theory", field: "凝聚态", year: 1928, date: "1928—1931 年", title: "固体能带理论", people: "费利克斯·布洛赫、鲁道夫·佩尔斯、莱昂·布里渊等",
    formula: "ψₙₖ(r)=eⁱᵏʳuₙₖ(r)", summary: "周期晶格中的电子形成允许能带和禁带，决定材料导电性质。",
    context: "量子力学建立后，布洛赫定理和能带概念迅速解释金属、绝缘体与半导体的差异。",
    application: "晶体管、芯片、光伏、LED", significance: "为现代电子材料提供统一微观框架，支撑信息时代的硬件基础。"
  },
  {
    id: "bcs", field: "凝聚态", year: 1957, date: "1957 年", title: "BCS 超导理论", people: "巴丁、库珀、施里弗",
    formula: "Δ(0) ≈ 1.76kᴮT𝚌", summary: "电子通过晶格相互作用形成库珀对，并凝聚为具有能隙的相干量子态。",
    context: "理论成功解释常规超导的零电阻、能隙和同位素效应，高温超导仍需要更广泛机制。",
    application: "MRI磁体、量子比特、粒子加速器", significance: "首次以微观量子机制解释宏观超导，是多体物理的里程碑。"
  },

  {
    id: "radioactivity", field: "核与粒子", year: 1896, date: "1896 年", title: "天然放射性", people: "亨利·贝克勒尔；居里夫妇深化研究",
    formula: "N(t)=N₀e⁻ˡᵃᵐᵇᵈᵃᵗ", summary: "不稳定原子核会以统计规律自发衰变，样本数量呈指数下降。",
    context: "贝克勒尔发现铀盐无需光照也能使感光板曝光；玛丽与皮埃尔·居里发现并分离新放射性元素。",
    application: "核医学、测年、无损检测", significance: "揭示原子并非不可分割，打开核物理与核能研究的大门。"
  },
  {
    id: "rutherford", field: "核与粒子", year: 1911, date: "1911 年", title: "核式原子模型", people: "欧内斯特·卢瑟福；盖革、马斯登完成实验",
    formula: "dσ/dΩ ∝ 1/sin⁴(θ/2)", summary: "原子的正电荷和绝大部分质量集中在极小原子核中，周围大多是空旷空间。",
    context: "α 粒子金箔散射出现罕见大角度偏转，推翻汤姆孙的“枣糕模型”。",
    application: "散射谱学、核结构、材料分析", significance: "发现原子核并确立以散射反推微观结构的强大实验范式。"
  },
  {
    id: "fission", field: "核与粒子", year: 1938, date: "1938—1939 年", title: "核裂变", people: "哈恩、斯特拉斯曼；迈特纳、弗里施解释",
    formula: "²³⁵U + n → 裂变碎片 + 2~3n + 能量", summary: "重原子核吸收中子后分裂并释放能量与更多中子，可形成链式反应。",
    context: "哈恩与斯特拉斯曼发现产物中的钡，迈特纳与弗里施用核变形和质能等价解释并命名裂变。",
    application: "核电、同位素生产、核武器", significance: "证明可从核结合能获取巨大能量，同时带来深远技术与伦理后果。"
  },
  {
    id: "standard-model", field: "核与粒子", year: 1973, date: "1960—1970 年代", title: "粒子物理标准模型", people: "盖尔曼、温伯格、萨拉姆、格拉肖及众多研究者",
    formula: "SU(3)𝚌 × SU(2)ᴸ × U(1)ʸ", summary: "以规范场论统一描述基本粒子及强、弱、电磁三种相互作用。",
    context: "夸克模型、电弱统一、量子色动力学和重整化等多条路线在 1970 年代汇合成成熟框架。",
    application: "对撞机、医学成像、辐射探测", significance: "是目前经实验检验最精确的微观理论之一，但不包含量子引力、暗物质解释。"
  },

  {
    id: "hubble-law", field: "天体与宇宙", year: 1929, date: "1929 年", title: "哈勃–勒梅特定律", people: "乔治·勒梅特、埃德温·哈勃等",
    formula: "v = H₀d", summary: "足够大尺度上，星系退行速度与距离近似成正比。",
    context: "勒梅特先从广义相对论推导并估计关系，哈勃结合星系距离与红移数据建立有影响力的观测证据。",
    application: "宇宙距离尺度、宇宙年龄与演化", significance: "确立膨胀宇宙观，是现代宇宙学从静态图景转向演化历史的关键。"
  },
  {
    id: "big-bang", field: "天体与宇宙", year: 1948, date: "1927—1965 年", title: "热大爆炸宇宙模型", people: "勒梅特、伽莫夫、阿尔弗、赫尔曼等",
    formula: "H² = (8πG/3)ρ − kc²/a² + Λc²/3", summary: "宇宙从早期高温高密状态膨胀冷却，形成轻元素、背景辐射和大尺度结构。",
    context: "勒梅特提出膨胀与“原始原子”，伽莫夫团队发展热核合成；1965 年宇宙微波背景被发现。",
    application: "宇宙年龄、元素丰度、背景辐射研究", significance: "提供宇宙整体演化的统一历史框架，并产生大量可检验预言。"
  },
  {
    id: "dark-energy", field: "天体与宇宙", year: 1998, date: "1998 年", title: "宇宙加速膨胀", people: "高红移超新星搜索队、超新星宇宙学项目",
    formula: "q = −äa/ȧ² < 0", summary: "遥远 Ia 型超新星的距离表明，当前宇宙膨胀正在加速。",
    context: "两个独立团队的超新星观测得到一致结论，常以暗能量或宇宙学常数解释，但其物理本质仍未知。",
    application: "精密宇宙学、暗能量巡天", significance: "改写宇宙未来图景，并暴露基础物理中最深刻的能量尺度难题之一。"
  }
];

const ERAS = [
  { id: "ancient", label: "古代", test: y => y < 1500 },
  { id: "revolution", label: "1500–1699", test: y => y >= 1500 && y < 1700 },
  { id: "classical", label: "1700–1849", test: y => y >= 1700 && y < 1850 },
  { id: "field", label: "1850–1899", test: y => y >= 1850 && y < 1900 },
  { id: "modern", label: "1900–1929", test: y => y >= 1900 && y < 1930 },
  { id: "midcentury", label: "1930–1969", test: y => y >= 1930 && y < 1970 },
  { id: "contemporary", label: "1970 至今", test: y => y >= 1970 }
];

const TIMELINE_MILESTONES = [
  { year: "前250", title: "浮力原理", subtitle: "定量自然哲学", color: "#4fd1c5" },
  { year: "1604", title: "自由落体", subtitle: "实验与数学", color: "#68ddfa" },
  { year: "1687", title: "经典力学", subtitle: "统一天地运动", color: "#f6c85f" },
  { year: "1831", title: "电磁感应", subtitle: "场的兴起", color: "#a993ff" },
  { year: "1865", title: "电磁统一", subtitle: "光是电磁波", color: "#a993ff" },
  { year: "1900", title: "能量量子", subtitle: "现代物理开端", color: "#c3a6ff" },
  { year: "1915", title: "弯曲时空", subtitle: "引力几何化", color: "#ff9fc7" },
  { year: "1926", title: "量子力学", subtitle: "微观概率世界", color: "#c3a6ff" }
];
