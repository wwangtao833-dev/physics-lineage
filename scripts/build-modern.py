"""Curated additions. Run from any directory; no network or dependencies required."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
S = {}
def source(key, title, url):
    S[key] = {'title': title, 'url': url}
for k,ch,title in [('stat','I_40','统计力学原理'),('brown','I_41','布朗运动'),('diff','I_43','扩散'),('thermo','I_44','热力学定律'),('thermo2','I_45','热力学实例'),('identical','III_04','全同粒子'),('operators','III_20','算符'),('super','III_21','超导'),('hydrogen','III_19','氢原子'),('maser','III_09','氨分子微波激射器'),('em','II_18','麦克斯韦方程'),('guide','II_24','波导'),('index','II_32','致密材料的折射率'),('qm','III_16','振幅的位置依赖')]:
    source(k,'Feynman Lectures · '+title,'https://www.feynmanlectures.caltech.edu/'+ch+'.html')
for k,f,title in [('qcd','qcd','量子色动力学'),('ew','standard-model','电弱模型'),('nu','neutrino-mixing','中微子混合与振荡'),('cosmo','bbang-cosmology','大爆炸宇宙学'),('params','cosmological-parameters','宇宙学参数')]:
    source(k,'PDG 2025 Review · '+title,'https://pdg.lbl.gov/2025/reviews/rpp2025-rev-'+f+'.pdf')
for k,ar,title in [('qft','1110.5013','Coleman · Quantum Field Theory'),('gr','gr-qc/9712019','Carroll · General Relativity'),('gw','1602.03837','LIGO/Virgo · 引力波首次直接探测'),('inflation','0907.5424','Baumann · TASI Lectures on Inflation'),('topo','1008.2026','Qi & Zhang · Topological insulators and superconductors'),('berry','0907.2021','Xiao, Chang & Niu · Berry Phase Effects'),('dft','cond-mat/0211443','Capelle · Density-functional theory'),('open','0809.4403','Marquardt & Püttmann · Dissipation and decoherence'),('info','quant-ph/9708022','Steane · Quantum Computing'),('shor','quant-ph/9508027','Shor · Factoring and discrete logarithms'),('grover','quant-ph/9605043','Grover · Quantum database search')]:
    source(k,title,'https://arxiv.org/abs/'+ar)
source('preskill2','Preskill · Quantum states and entanglement','https://www.preskill.caltech.edu/ph219/chap2_15.pdf')
source('preskill3','Preskill · Quantum measurement and evolution','https://www.preskill.caltech.edu/ph219/chap3_15.pdf')
source('plasma','MIT · Introduction to Plasma Physics I, course notes','https://ocw.mit.edu/courses/22-611j-introduction-to-plasma-physics-i-fall-2003/pages/lecture-notes/')
source('chaos','MIT · Nonlinear Dynamics I: Chaos, course materials','https://ocw.mit.edu/courses/18-353j-nonlinear-dynamics-i-chaos-fall-2012/')
for k,title,doi in [('onsager','Onsager (1931) · Reciprocal Relations I','10.1103/PhysRev.37.405'),('fdt','Callen & Welton (1951) · Irreversibility and Generalized Noise','10.1103/PhysRev.83.34'),('gl','Ginzburg · Nobel lecture: superconductivity and superfluidity','10.1103/RevModPhys.76.981'),('qhe','von Klitzing et al. (1980) · Quantized Hall resistance','10.1103/PhysRevLett.45.494'),('bkt','Kosterlitz & Thouless (1973) · Ordering in two dimensions','10.1088/0022-3719/6/7/010'),('hubbard','Hubbard (1963) · Electron correlations in narrow energy bands','10.1098/rspa.1963.0204'),('metropolis','Metropolis et al. (1953) · Equation of State Calculations','10.1063/1.1699114'),('yee','Yee (1966) · Numerical solution of Maxwell equations','10.1109/TAP.1966.1138693'),('verlet','Verlet (1967) · Computer experiments on classical fluids','10.1103/PhysRev.159.98'),('lorenz','Lorenz (1963) · Deterministic nonperiodic flow','10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2'),('kdv','Korteweg & de Vries (1895) · Long waves','10.1080/14786449508620739')]:
    source(k,title,'https://doi.org/'+doi)

ROWS=[]
def add(id,field,topic,year,title,people,formula,summary,conditions,variables,application,significance,refs,related=(),date=None,context=None,kind='理论／关系'):
    ROWS.append(dict(id=id,field=field,topic=topic,year=year,date=date or str(year)+' 年',title=title,people=people,formula=formula,summary=summary,conditions=conditions,variables=variables,application=application,significance=significance,context=context or ('代表节点为'+(date or str(year)+' 年')+'；关键贡献者为'+people+'。该年份用于排序，不表示此前没有相关先驱工作。'),sources=[S[k] for k in refs.split()],related=list(related),kind=kind,editorial='本次新增 · 附参考来源'))

# Statistical physics and irreversible processes.
add('partition','热学与统计','统计系综',1902,'正则系综与配分函数','吉布斯；玻尔兹曼等','Z=Σᵢ exp(−βEᵢ)，pᵢ=exp(−βEᵢ)/Z，F=−k_B T ln Z','配分函数把微观能级与平衡热力学联系起来。','固定温度、体积和粒子数；系统与热库弱耦合并处于平衡。','β=1/(k_B T)，Eᵢ 微观态能量，F 亥姆霍兹自由能','热容、磁化率、分子统计','提供由能谱计算宏观性质的通用起点。','stat',('boltzmann','gibbs-free'))
add('bose-einstein','热学与统计','量子统计',1924,'玻色–爱因斯坦分布','玻色、爱因斯坦','n̄(E)=1/{exp[(E−μ)/(k_B T)]−1}','全同玻色子的单粒子态可以被多个粒子占据。','理想玻色气体或独立准粒子；μ 不高于最低单粒子能量。','n̄ 平均占据数，μ 化学势，E 单粒子能量','冷原子、光子和声子统计','揭示量子统计与经典气体的本质差别。','identical',('fermi-dirac','bose-condensation'),date='1924—1925 年')
add('bose-condensation','凝聚态','超流与冷原子',1925,'玻色–爱因斯坦凝聚','爱因斯坦；玻色提供统计基础','N₀/N=1−(T/T_c)^(3/2)','低温下宏观数量粒子占据同一量子态。','所示公式仅用于三维均匀理想气体且 T≤T_c；陷阱和相互作用改变结果。','N₀ 基态粒子数，N 总粒子数，T_c 临界温度','冷原子模拟、物质波干涉','提供研究宏观量子相干的可控平台；凝聚不自动等于超流。','identical',('bose-einstein','bcs'))
add('third-law','热学与统计','热力学基础',1906,'热力学第三定律','能斯特；普朗克','lim(T→0) S(T)=0（唯一基态的理想纯晶体）','第三定律约束低温极限的熵与可达性。','零熵形式需唯一基态、平衡且无残余无序；简并基态可有残余熵。','S 熵，T 绝对温度','低温制冷、绝对熵计算','补全热力学的低温边界。','thermo2',('zeroth','second-law'),date='1906—1911 年')
add('heat-conduction','热学与统计','输运与非平衡',1822,'傅里叶热传导定律','约瑟夫·傅里叶','j_Q=−κ∇T；∂T/∂t=α∇²T','温度梯度驱动热流，能量守恒产生热扩散方程。','局域平衡、线性各向同性导热；第二式还需常物性、无热源和无对流。','κ 导热率，α=κ/(ρc_p) 热扩散率，j_Q 热流密度','散热、热防护、材料热测量','连接宏观传热与偏微分方程。','diff',('first-law','fourier'))
add('einstein-diffusion','热学与统计','输运与非平衡',1905,'爱因斯坦扩散关系','爱因斯坦；斯莫卢霍夫斯基独立发展','⟨[x(t)−x(0)]²⟩=2Dt，D=μ_m k_B T','热运动导致位移扩散，迁移率与涨落强度相关。','长于动量弛豫时间的一维正常扩散；μ_m 是速度/外力的机械迁移率。','D 扩散系数，μ_m 机械迁移率','粒径测量、软物质、扩散输运','把可见布朗运动与分子热运动联系起来。','brown',('diffusion-fick','fluctuation-dissipation'))
add('diffusion-fick','热学与统计','输运与非平衡',1855,'菲克扩散定律','阿道夫·菲克','J=−D∇n；∂n/∂t=D∇²n','浓度梯度驱动物质扩散。','局域线性输运；第二式需常 D、无反应、无对流。','J 粒子通量，n 数密度，D 扩散系数','掺杂、膜传质、生物物理','用连续方程描述随机微观运动的宏观效果。','diff',('einstein-diffusion',))
add('onsager','热学与统计','输运与非平衡',1931,'昂萨格互易关系','拉尔斯·昂萨格','Jᵢ=ΣⱼLᵢⱼXⱼ；Lᵢⱼ=Lⱼᵢ','不同不可逆通量之间的线性耦合具有互易性。','近平衡与微观可逆性；所示对称式限无破坏时间反演的外场且变量时间反演奇偶性相同。','Jᵢ 通量，Xⱼ 热力学力，Lᵢⱼ 输运系数','热电、扩散耦合、电化学','约束交叉输运系数；磁场下需 Onsager–Casimir 形式。','onsager',('first-law','diffusion-fick'))
add('fluctuation-dissipation','热学与统计','输运与非平衡',1951,'涨落–耗散关系','卡伦、韦尔顿；久保等','S_xx(ω)=2k_B T Imχ(ω)/ω（经典极限）','平衡涨落谱与系统对外扰动的耗散响应相连。','线性响应、热平衡；双边谱 S=∫dt exp(iωt)⟨x(t)x(0)⟩，外力耦合为 −fx。','χ 位移对力的响应函数，ω 角频率；量子高频情形需修正','噪声测量、微流变、热涨落','使无扰动测量能够推断响应特性。','fdt',('einstein-diffusion','onsager'))

# Quantum framework and AMO physics.
add('density-matrix','量子物理','量子态与测量',1927,'密度算符','冯·诺依曼、朗道等','ρ=Σᵢpᵢ|ψᵢ⟩⟨ψᵢ|，⟨A⟩=Tr(ρA)','统一表达纯态、统计混合和子系统状态。','ρ 为正半定算符且 Trρ=1；混合态的分解一般不唯一。','pᵢ 制备概率，A 可观测算符，Tr 迹','开放系统、量子态层析','摆脱仅用单个波函数描述系统的限制。','preskill2',('born-rule','von-neumann-entropy'))
add('von-neumann-entropy','量子信息','量子态与纠缠',1927,'冯·诺依曼熵','约翰·冯·诺依曼','S(ρ)=−Tr(ρ log₂ρ)','量化量子混合程度；双体纯态的约化熵可量化纠缠。','以 bit 为单位；热力学熵使用 −k_B Tr(ρ lnρ)。混合双体态不能直接把约化熵等同纠缠。','ρ 密度矩阵，约定 0 log 0=0','量子信息、纠缠分析','连接信息论、统计物理与量子态结构。','preskill2',('density-matrix','boltzmann'))
add('ehrenfest','量子物理','量子与经典对应',1927,'埃伦费斯特定理','保罗·埃伦费斯特','d⟨x⟩/dt=⟨p⟩/m，d⟨p⟩/dt=−⟨∂V/∂x⟩','量子期望值服从与经典力学相似的演化关系。','非相对论 H=p²/(2m)+V(x)；一般不成立 ⟨V′(x)⟩=V′(⟨x⟩)。','x 位置，p 动量，V 势能','波包运动、半经典近似','说明经典轨迹何时可从量子理论近似恢复。','operators',('heisenberg-eq','newton-laws'))
add('quantum-variational','量子物理','近似与计算',1909,'量子变分原理','瑞利、里兹；量子力学中后续应用','⟨ψ|H|ψ⟩/⟨ψ|ψ⟩≥E₀','试探态的平均能量给出基态能量上界。','H 自伴且有下界；试探态须属于算符定义域，不能为零。','E₀ 基态能量，ψ 试探波函数','原子分子、多体基态、变分量子算法','把求基态转为优化问题；1909 是里兹方法节点，非量子力学创立年。','operators dft',('schrodinger','dft-kohn-sham'),date='1909 年数学方法；1920年代量子应用')
add('rabi','量子物理','原子与量子控制',1937,'拉比振荡','伊西多·拉比','P_e(t)=sin²(Ωt/2)（共振）','相干驱动使两能级系统的布居周期交换。','初态为基态、共振、旋波近似；无显著退相干。','Ω 拉比角频率，P_e 激发态概率','原子钟、核磁共振、量子比特控制','把量子跃迁变成可控的相干操作。','maser',('born-rule','density-matrix'))
add('berry-phase','量子物理','几何相位',1984,'贝里相位','迈克尔·贝里；潘查拉特南等有先驱贡献','γ_n=i∮⟨n(R)|∇_R n(R)⟩·dR','绝热闭合演化除动力学相位外还产生几何相位。','非简并、能隙未闭合且绝热演化；简并情况需非阿贝尔推广。','R 控制参数，γ_n 几何相位（模 2π）','拓扑材料、量子干涉、几何控制','把量子态的几何结构变成可观测效应。','berry',('band-theory','quantum-hall'))

# Collective quantum matter.
add('london','凝聚态','超导',1935,'伦敦方程与穿透深度','弗里茨·伦敦、海因茨·伦敦','∇²B=B/λ_L²，λ_L=√[m*/(μ₀n_s q*²)]','超导电流屏蔽体内磁场，产生有限穿透深度。','局域伦敦极限，远离涡旋核；n_s、m*、q* 必须采用一致的载流子约定。','λ_L 穿透深度，n_s 超流载流子数密度','超导磁屏蔽、微波谐振器','在唯象层面解释迈斯纳效应。','super',('bcs','g-l'))
add('g-l','凝聚态','超导',1950,'金兹堡–朗道超导理论','金兹堡、朗道','f=α|ψ|²+(β/2)|ψ|⁴+|(-iℏ∇−q*A)ψ|²/(2m*)+B²/(2μ₀)','以复序参量和自由能泛函描述超导。','通常为临界温度附近的长波长展开；β>0，ψ 的归一化采用一致约定。','ψ 序参量，A 矢势，α、β 展开系数','涡旋、临界场、超导器件','连接对称性破缺、磁场和宏观量子态。','gl',('landau-phase','london'))
add('josephson','凝聚态','超导',1962,'约瑟夫森效应','布赖恩·约瑟夫森','I=I_c sinφ，dφ/dt=2eV/ℏ','两个弱连接超导体通过相位差产生超流。','常规弱连接及正弦电流相位关系；复杂结可能含高次谐波。','φ 规范不变相位差，I_c 临界电流，V 电压','SQUID、电压基准、超导量子比特','把相位相干直接转为电学测量。','super',('bcs','rabi'))
add('quantum-hall','凝聚态','拓扑与输运',1980,'整数量子霍尔效应','克劳斯·冯·克利青等；TKNN 等解释拓扑结构','σ_xy=C e²/h，C∈ℤ','二维电子体系出现量子化横向电导。','低温、强磁场的量子霍尔平台；纵向电导趋零，C 的符号随约定。','C 占据能带总陈数，σ_xy 霍尔电导','电阻基准、拓扑输运','把整数拓扑量与高精度测量联系起来。','qhe berry',('hall','berry-phase'))
add('bkt','凝聚态','相变与拓扑',1971,'BKT 相变','别列津斯基、科斯特利茨、索利斯','ξ≈ξ₀ exp[b/√(T/T_BKT−1)]（从高温侧趋近）','二维体系中涡旋对解缚导致拓扑相变。','二维、短程相互作用、连续 U(1) 对称的相应模型；并非普通幂律临界行为。','ξ 关联长度，b 非普适常数，T_BKT 转变温度','薄膜超流、二维磁体、冷原子','说明局域序参量之外也存在相变机制。','bkt',('landau-phase','ising'),date='1971—1973 年')
add('dft-kohn-sham','凝聚态','电子结构',1964,'密度泛函理论与 Kohn–Sham 方程','霍恩贝格、科恩、沈吕九','[−ℏ²∇²/(2m)+v_eff[n]]φᵢ=εᵢφᵢ；n=Σᵢfᵢ|φᵢ|²','以电子密度求解多电子基态，辅助轨道用于自洽计算。','基态理论；实际结果取决于交换关联近似。Kohn–Sham 本征值不能普遍当作真实激发能。','n 电子密度，fᵢ 占据数，v_eff 有效势','材料设计、分子结构、能带计算','使第一性原理电子结构计算成为常用工具。','dft',('quantum-variational','band-theory'),date='1964—1965 年')

# Relativity and cosmology.
add('interval','相对论','相对论时空',1908,'闵可夫斯基时空间隔','赫尔曼·闵可夫斯基','ds²=−c²dt²+dx²+dy²+dz²','洛伦兹变换保持四维时空间隔不变。','平直时空；采用 (−,+,+,+) 度规号差，类时路径 dτ²=−ds²/c²。','ds 间隔，τ 固有时，c 光速','相对论运动学、粒子寿命','以几何语言统一时间和空间。','gr',('lorentz-transform','time-dilation'))
add('einstein-hilbert','相对论','引力场论',1915,'爱因斯坦–希尔伯特作用量','希尔伯特、爱因斯坦','S_g=[c³/(16πG)]∫(R−2Λ)√(−g)d⁴x','对度规变分可导出爱因斯坦场方程。','x⁰=ct；完整变分须处理边界项，并加入物质作用量。','R 标量曲率，g 度规行列式，Λ 宇宙学常数','引力理论、数值相对论','将引力置于作用量和对称性的统一框架。','gr',('general-relativity','noether'))
add('gravitational-waves','相对论','引力辐射',1916,'引力波与四极矩辐射','爱因斯坦；LIGO/Virgo 合作组','P=G⟨Q⃛ᵢⱼQ⃛ᵢⱼ⟩/(5c⁵)','变化的质量四极矩能够向外辐射引力波。','公式适用于慢速弱场源；Qᵢⱼ 为去迹质量四极矩，重复指标求和。强场并合需更完整模型。','P 辐射功率，Q⃛ 三阶时间导数','双星演化、引力波天文学','1916年理论预言；2015年首次直接探测，2016年发表。','gw gr',('general-relativity','schwarzschild'),date='1916 年预言；2015 年直接探测')
add('flrw','天体与宇宙','宇宙学背景',1922,'FLRW 时空','弗里德曼、勒梅特、罗伯逊、沃克','ds²=−c²dt²+a²(t)[dr²/(1−kr²)+r²dΩ²]','以均匀、各向同性的几何描述宇宙大尺度背景。','宇宙学原理的背景近似；不描述星系附近的局部非均匀结构。','a 尺度因子，k 空间曲率参数，r 共动径向坐标','宇宙膨胀、距离关系','为膨胀宇宙建立几何基础。','cosmo',('big-bang','general-relativity'),date='1922—1937 年')
add('cosmological-redshift','天体与宇宙','宇宙学观测',1927,'宇宙学红移','勒梅特等','1+z=a(t₀)/a(t_em)','光在宇宙膨胀过程中波长随尺度因子伸长。','FLRW 背景下共动发射者与观测者；实际观测还含本动速度和局部引力效应。','z 红移，t_em 发射时刻，t₀ 接收时刻','星系巡天、宇宙距离','避免把高红移直接当作狭义相对论退行速度。','cosmo',('flrw','hubble-law'))
add('lcdm','天体与宇宙','宇宙学模型',1990,'ΛCDM 宇宙学基准模型','多代宇宙学研究者共同发展','H²/H₀²=Ω_r a⁻⁴+Ω_m a⁻³+Ω_k a⁻²+Ω_Λ','用普通物质、冷暗物质、辐射和宇宙学常数描述背景膨胀。','a₀=1；所示项按理想组分标度；精密中微子处理更复杂，暗物质微观本质仍未知。','Ω 各组分当前密度参数，H 哈勃参数','CMB、BAO、超新星联合分析','提供跨观测的基准模型，并非已知全部宇宙成分的微观理论。','params',('flrw','dark-energy'),date='1990年代形成；后续精密检验',kind='观测支持的基准模型')
add('inflation','天体与宇宙','早期宇宙',1981,'宇宙暴胀','古斯；斯塔罗宾斯基、林德等','ä>0，ε_H=−Ḣ/H²<1','早期加速膨胀可解释平直性，并产生结构形成的初始扰动。','暴胀是一类模型；具体驱动场及势能尚未确认，不能与热大爆炸的观测证据等同。','H=ȧ/a，ε_H 膨胀速率变化参数','原初扰动、CMB 模型检验','把早期宇宙演化与量子涨落联系起来。','inflation',('flrw','lcdm'),date='1980—1982 年',kind='待验证模型族')

# Quantum fields: these are distinct from single-particle quantum mechanics.
add('klein-gordon','量子场论','相对论量子场',1926,'克莱因–戈尔登方程','克莱因、戈尔登等','[(1/c²)∂²_t−∇²+(mc/ℏ)²]φ=0','自由标量场满足相对论能量动量关系。','自由自旋零场；|φ|² 不能直接解释为单粒子位置概率密度。','φ 标量场，m 质量','标量粒子、场量子化','引出粒子与反粒子并存的场论描述。','qft',('rel-energy-momentum','dirac'))
add('canonical-quantization','量子场论','场量子化',1927,'场的正则量子化','狄拉克；海森堡、泡利等','[φ(t,x),π(t,y)]=iℏδ³(x−y)','把经典场及其共轭动量提升为算符。','所示关系用于玻色标量场；费米场使用反对易关系，规范场须处理约束。','π 共轭动量，δ³ 三维狄拉克δ函数','粒子产生湮灭、量子光学','使粒子数变化成为理论内在过程。','qft',('hamilton','klein-gordon'))
add('qed','量子场论','规范相互作用',1948,'量子电动力学 QED','朝永振一郎、施温格、费曼、戴森等','ℒ=−¼F_μνF^μν+ψ̄(iγ^μD_μ−m)ψ','描述带电费米子与电磁场的量子相互作用。','此处 ℏ=c=1，D_μ=∂_μ+iqA_μ；可作弱耦合微扰展开。','F_μν 电磁场张量，ψ 费米场，q 电荷耦合','精密谱学、散射、磁矩','建立极高精度的可重整化量子场论范例。','qft',('maxwell','dirac'),date='1947—1949 年')
add('yang-mills','量子场论','规范相互作用',1954,'杨–米尔斯规范理论','杨振宁、罗伯特·米尔斯','ℒ=−¼Fᵃ_μνFᵃμν；Fᵃ_μν=∂_μAᵃ_ν−∂_νAᵃ_μ+g fᵃᵇᶜAᵇ_μAᶜ_ν','非阿贝尔规范场能够自相互作用。','ℏ=c=1；生成元和耦合符号需一致；规范对称性是描述冗余而非可直接观测的自由度。','fᵃᵇᶜ 结构常数，g 耦合，Aᵃ_μ 规范势','QCD、电弱理论','构成标准模型规范相互作用的数学骨架。','qcd',('qed','standard-model'))
add('qcd-asymptotic','量子场论','强相互作用',1973,'QCD 与渐近自由','格罗斯、维尔切克、波利策；盖尔曼等','α_s(Q)≈4π/[(11−2n_f/3)ln(Q²/Λ_QCD²)]','夸克与胶子的强耦合在高能标减弱。','SU(3) 一圈近似且 Q 远大于 Λ_QCD；n_f 为活跃夸克味数，低能不能使用此公式。','Q 重整化能标，α_s 强耦合常数','强子碰撞、喷注、核子结构','解释高能近自由行为，低能禁闭仍需非微扰方法。','qcd',('yang-mills','standard-model'))
add('electroweak','量子场论','电弱相互作用',1967,'电弱统一','格拉肖、温伯格、萨拉姆','m_W=gv/2，m_Z=v√(g²+g′²)/2，e=g sinθ_W','以 SU(2)_L×U(1)_Y 与自发对称性破缺统一弱作用和电磁作用。','自然单位；所示质量关系为树级，精密比较需辐射修正。','g、g′ 耦合，v 真空期望值，θ_W 弱混合角','W/Z 过程、精密电弱检验','建立可实验检验的统一规范理论。','ew',('higgs','qed'),date='1961—1968 年')

# Plasma hierarchy.
add('debye-screening','等离子体','屏蔽与尺度',1923,'德拜屏蔽','德拜、休克尔；后推广到等离子体','λ_De=√[ε₀k_B T_e/(n_e e²)]','电子重排在德拜尺度上屏蔽缓慢静电扰动。','弱耦合、近麦克斯韦分布、小电势；所示为电子德拜长度，各组分贡献按倒平方相加。','T_e 电子温度，n_e 电子数密度','放电、聚变、电离层','定义集体电荷屏蔽的基本长度。','plasma',('poisson-laplace',))
add('plasma-frequency','等离子体','集体振荡',1920,'电子等离子体频率','朗缪尔、汤克斯等','ω_pe=√[n_e e²/(ε₀m_e)]','电子相对近静止离子背景振荡产生特征频率。','冷、均匀、无磁等离子体的小扰动极限。','ω_pe 角频率，m_e 电子质量','电波反射、放电诊断','区分电磁波可传播和截止的典型尺度。','plasma',('em-wave','debye-screening'),date='1920年代')
add('cyclotron','等离子体','单粒子运动',1895,'回旋运动与拉莫尔半径','洛伦兹及后续等离子体研究者','ω_c=|q|B/m，r_L=v_⊥/ω_c','磁场使带电粒子的垂直速度分量产生回旋。','非相对论、均匀静磁场；相对论情形频率含 γ。','q 电荷，v_⊥ 垂直速度，r_L 回旋半径','磁约束、回旋加速器','为导引中心和磁化条件提供尺度。','plasma',('lorentz-force',),date='19世纪末形成')
add('exb-drift','等离子体','单粒子运动',1900,'E×B 漂移','经典带电粒子理论的共同成果','v_E=E×B/B²','垂直电场使粒子导引中心横跨磁场漂移。','近均匀场、非相对论；E 的平行分量产生加速而非此漂移。','E 电场，B 磁场，v_E 导引中心速度','聚变、空间等离子体','此漂移与粒子质量和电荷符号无关。','plasma',('cyclotron',),date='20世纪初逐步形成')
add('vlasov','等离子体','动理学',1938,'弗拉索夫方程','阿纳托利·弗拉索夫','∂_t f+v·∇_x f+(q/m)(E+v×B)·∇_v f=0','在自洽平均场中演化粒子相空间分布。','无碰撞或碰撞可忽略；E、B 与分布共同满足场方程。','f(x,v,t) 分布函数','空间等离子体、束流、动理学模拟','保留流体模型丢失的速度分布信息。','plasma',('lorentz-force','fluid-continuity'))
add('alfven','等离子体','磁流体力学',1942,'阿尔芬波与理想 MHD','汉尼斯·阿尔芬','v_A=B₀/√(μ₀ρ)，ω=k_∥v_A','磁张力作为恢复力，使导电流体支持横向波动。','理想单流体、长波长低频、小扰动；忽略电阻耗散和相对论效应。','ρ 总质量密度，k_∥ 平行波数','太阳风、日冕、聚变','把流体运动与磁场动力学结合起来。','plasma',('maxwell','euler-fluid'))

# Information, openness and computation.
add('bell-chsh','量子信息','量子关联',1964,'贝尔定理与 CHSH 不等式','贝尔；克劳泽、霍恩、希莫尼、霍尔特','|E(a,b)+E(a,b′)+E(a′,b)−E(a′,b′)|≤2','局域隐变量模型的关联有上界，量子理论可超过它。','二值测量、设置独立等假设；量子上界为 2√2，违背不等式不允许超光速传信。','E 关联期望值，a、b 测量设置','量子基础、器件无关协议','使局域隐变量假设可通过实验检验。','preskill2',('born-rule','density-matrix'),date='1964 年；CHSH 1969 年')
add('no-cloning','量子信息','量子信息原理',1982,'量子不可克隆定理','伍特斯、祖雷克；迪克斯','不存在对任意 |ψ⟩ 均成立的 U|ψ⟩|0⟩=|ψ⟩|ψ⟩','未知的任意量子态不能被完美、确定地复制。','针对通用复制；相互正交且已知集合中的态可复制。','U 酉演化，|0⟩ 辅助态','量子密码、量子通信','约束量子信息的处理方式。','preskill3',('density-matrix',))
add('teleportation','量子信息','量子通信',1993,'量子隐形传态','贝内特、布拉萨尔、克雷波、若萨、佩雷斯、伍特斯','共享纠缠 + 贝尔测量 + 2 个经典比特 → 单量子比特态转移','通过纠缠资源和经典通信重建未知量子态。','理想协议消耗一对纠缠比特；发送方原态被测量，不能超光速。','经典比特决定接收端的泡利校正','量子网络、量子中继','转移的是状态，不是物质或额外复制。','info',('bell-chsh','no-cloning'),kind='协议')
add('shor-algorithm','量子信息','量子算法',1994,'Shor 算法','彼得·肖尔','整数分解 → 模指数周期查找；复杂度 poly(log N)','量子周期查找使整数分解具有多项式时间算法。','需要可扩展、足够低误差的量子电路；不是当前任意小设备都能破解实际密钥。','N 待分解整数，输入长度为 log₂N','量子算法、密码学风险研究','揭示量子计算相对已知经典方法的潜在优势。','shor',('no-cloning',),kind='算法')
add('grover-algorithm','量子信息','量子算法',1996,'Grover 搜索算法','洛夫·格罗弗','查询复杂度 O(√N)（唯一解）','振幅放大可减少无结构搜索的查询次数。','假定相干 oracle 和唯一标记解；不包含数据库装载和 oracle 构造成本。','N 候选数量，oracle 为可逆查询操作','搜索子程序、优化中的振幅放大','提供可证明的二次查询加速。','grover',('shor-algorithm',),kind='算法')
add('lindblad','量子信息','开放量子系统',1976,'GKSL 主方程','戈里尼、科萨科夫斯基、苏达尔尚；林德布拉德','ρ̇=−i[H,ρ]/ℏ+Σⱼ(LⱼρLⱼ†−½{Lⱼ†Lⱼ,ρ})','以保持迹和完全正性的方式描述马尔可夫耗散。','量子动力学半群或适当马尔可夫近似；不适用于所有有记忆环境。','Lⱼ 跃迁算符（吸收速率因子），{,} 反对易子','退相干、量子光学、噪声建模','为开放系统提供受数学约束的演化模型。','open',('density-matrix','rabi'))

# Nonlinear and computational physics.
add('lyapunov','非线性与复杂系统','混沌与稳定性',1892,'李雅普诺夫指数','亚历山大·李雅普诺夫及后续动力系统研究者','λ_max=lim(t→∞) t⁻¹ ln[||δx(t)||/||δx(0)||]','刻画相邻轨迹的渐近指数分离率。','以切空间无穷小扰动定义；正指数须结合有界性等条件判断混沌，不能单独证明。','δx 切向扰动，λ_max 最大指数','混沌判别、可预测性','将对初值的敏感性定量化。','chaos',('hamilton',),date='1892 年稳定性理论；后续发展')
add('lorenz-system','非线性与复杂系统','混沌与稳定性',1963,'洛伦兹混沌系统','爱德华·洛伦兹','ẋ=σ(y−x)，ẏ=x(ρ−z)−y，ż=xy−βz','确定性三维方程可产生非周期、敏感依赖初值的轨迹。','无量纲对流截断模型；行为依赖参数，不能把所有参数区间视为混沌。','σ、ρ、β 参数；此处 ρ 不是密度','非线性教学、预测误差研究','说明确定性不等于长期可预测。','lorenz',('lyapunov','euler-fluid'),kind='模型')
add('logistic-map','非线性与复杂系统','分岔与映射',1976,'Logistic 映射与倍周期分岔','罗伯特·梅等；费根鲍姆发展普适性','x_(n+1)=r x_n(1−x_n)','一个非线性迭代规则可出现定点、周期轨道和混沌。','x∈[0,1]、0≤r≤4；1976为梅的代表性综述节点，不是该映射唯一首次出现年份。','r 控制参数，n 离散步数','复杂系统、分岔教学','揭示简单动力规则也可产生复杂行为。','chaos',('lyapunov','lorenz-system'),kind='模型')
add('kdv','非线性与复杂系统','孤子与非线性波',1895,'KdV 方程与孤子','科特韦赫、德弗里斯；扎布斯基、克鲁斯卡尔等','u_t+6u u_x+u_xxx=0','非线性陡化与色散可平衡形成稳定行波。','所示为无量纲规范形式；浅水长波、弱非线性近似的一类模型。','u 波幅，x 位置，t 时间','浅水波、非线性波、可积系统','孤子扩展了线性波叠加的图景。','kdv',('wave-equation',),date='1895 年方程；1965 年孤子研究',kind='模型')
add('metropolis','计算与数学物理','统计模拟',1953,'Metropolis 蒙特卡洛','Metropolis、Rosenbluth 夫妇、Teller 夫妇','A(x→x′)=min[1,exp(−βΔE)]','通过随机采样估计平衡系综的平均量。','所示接受率要求对称提议分布；需遍历性、热化并估计自相关误差。','ΔE 新旧能量差，β=1/(k_B T)','统计物理、材料模拟','不必枚举全部微观态即可计算宏观量。','metropolis',('partition','ising'),kind='数值方法')
add('yee-fdtd','计算与数学物理','场的数值计算',1966,'Yee 时域有限差分方法','Kane S. Yee','∂_t B=−∇×E，∂_t D=∇×H−J → 交错网格差分','在空间和时间交错采样电磁场，逐步推进麦克斯韦方程。','需满足 CFL 稳定性、足够网格分辨率与正确边界；稳定不等于准确。','Δt 时间步，Δx 网格尺度，E/H 场分量','天线、FSS、波导、散射仿真','把连续场方程变为可执行的全波数值计算。','yee',('maxwell','em-wave'),kind='数值方法')
add('verlet','计算与数学物理','动力学模拟',1967,'Verlet 积分','Loup Verlet；此前存在相同递推思想','r_(n+1)=2r_n−r_(n−1)+a_n Δt²','用位置和加速度推进经典粒子轨迹。','平滑力场与合适步长；位置形式全局二阶精度，不保证任意步长下能量守恒。','r_n 第 n 步位置，a_n 加速度','分子动力学、粒子模拟','是长时间哈密顿动力学计算的重要方法。','verlet',('newton-laws','hamilton'),kind='数值方法')

# Optical and electromagnetic gaps, useful across material and wave physics.
add('planck-spectrum','光学','量子辐射',1900,'普朗克黑体辐射谱','马克斯·普朗克','B_ν(T)=(2hν³/c²)/[exp(hν/(k_B T))−1]','描述热平衡黑体的频率分辨辐亮度。','B_ν 按单位频率、单位立体角定义；波长谱不能简单把 ν 换成 c/λ。','B_ν 光谱辐亮度，ν 频率，T 温度','红外测温、恒星谱、CMB','解决经典紫外灾难并推动量子理论。','stat cosmo',('planck','stefan-boltzmann'))
add('stimulated-emission','光学','量子光学',1917,'受激辐射与 Einstein 系数','阿尔伯特·爱因斯坦','R_st=B₂₁u_ν，R_sp=A₂₁','辐射场诱导激发态向低能级跃迁，产生相干放大。','两能级跃迁与谱密度约定一致；激光净增益还需考虑布居反转及损耗。','A₂₁ 自发辐射率，B₂₁ 受激系数，u_ν 能量谱密度','激光、光放大、微波激射','建立激光工作的微观基础。','maser',('planck-spectrum','rabi'))
add('topological-insulator','凝聚态','拓扑与输运',2005,'时间反演拓扑绝缘体','Kane、Mele；Bernevig、Hughes、Zhang 等','二维 Z₂ 指标 ν∈{0,1}','体能隙与对称性保护的边缘或表面态可以共存。','所示分类用于相应时间反演对称、带隙开放的非相互作用能带体系；破坏保护对称性可开隙。','ν Z₂ 拓扑指标；不是频率','自旋输运、拓扑器件研究','把能带分类从局域结构扩展到全局拓扑。','topo',('band-theory','berry-phase'),date='2005—2007 年')
add('em-boundary','磁学与电磁','界面与散射',1865,'电磁场边界条件','麦克斯韦场论及后续电磁学','n·(D₂−D₁)=σ_f，n·(B₂−B₁)=0；n×(E₂−E₁)=0，n×(H₂−H₁)=K_f','场方程在界面上给出法向和切向分量约束。','固定界面、普通电表面源且无磁表面流；n 从介质1指向介质2。','σ_f 自由面电荷，K_f 自由面电流','介质界面、FSS、波导','把材料和几何界面纳入场方程求解。','em',('maxwell','fresnel-equations'))
add('waveguide-cutoff','磁学与电磁','电磁波',1897,'矩形波导截止频率','瑞利等','f_c,mn=(v/2)√[(m/a)²+(n/b)²]','受边界约束的波导模只有高于截止频率才传播。','均匀理想导体矩形波导；v=1/√(με)，TE 模 m,n 不同时为零，TM 模两者均非零。','a、b 截面尺寸，m、n 模指标','微波传输、滤波、腔体设计','说明横向边界如何产生频率选择。','guide',('em-boundary','em-wave'))
add('lorentz-oscillator','光学','色散与介质',1900,'洛伦兹振子介电模型','亨德里克·洛伦兹及先驱','ε_r(ω)=1+ω_p²/(ω₀²−ω²−iγω)','把束缚电荷的受迫运动转化为频率相关介电响应。','采用 exp(−iωt)，线性局域单共振模型；实际材料常需多个振子。','ω₀ 共振频率，γ 阻尼，ω_p² 振子强度参数','色散、吸收、光学材料','使微观共振与宏观介电函数相连。','index',('drude','resonance-q'),date='19世纪末—20世纪初',kind='模型')

add('hubbard-model','凝聚态','强关联电子',1963,'Hubbard 模型','约翰·哈伯德；古茨维勒、金森等','H=−tΣ⟨ij⟩σ(c†ᵢσcⱼσ+h.c.)+UΣᵢnᵢ↑nᵢ↓','描述电子跃迁与局域相互作用的竞争。','所示为单带、最近邻跃迁及在位相互作用模型；真实材料可能需要多轨道和长程项。','t 跃迁能，U 在位相互作用，n 粒子数算符','莫特绝缘体、强关联与量子模拟','说明独立电子近似不能解释所有固体。','hubbard',('band-theory','fermi-dirac'),kind='模型')

meta={
 '量子场论':{'color':'#da97ed','short':'QFT'},
 '等离子体':{'color':'#5ce1cb','short':'PLASMA'},
 '量子信息':{'color':'#e5a2ff','short':'QINFO'},
 '非线性与复杂系统':{'color':'#efc777','short':'COMPLEX'},
 '计算与数学物理':{'color':'#a7bedb','short':'COMPUTE'}
}
content='// Curated modern-physics additions; generated by scripts/build-modern.py.\n(() => {\n'
content+='Object.assign(FIELD_META, '+json.dumps(meta,ensure_ascii=False,indent=2)+');\n'
content+='const additions = '+json.dumps(ROWS,ensure_ascii=False,indent=2)+';\n'
content+='PHYSICS_DATA.push(...additions);\n})();\n'
(ROOT/'data-modern.js').write_text(content)
print('Generated',len(ROWS),'new records')
