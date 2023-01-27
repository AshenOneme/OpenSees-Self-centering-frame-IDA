# -*- coding: UTF-8 -*-
import openseespy.opensees as ops
import math
import vfo.vfo as vfo
def Model():
    ops.wipe()
    ops.model('basic', '-ndm', 2, '-ndf', 3)  # frame 2D

    print("****************************************","Material","****************************************")
    IDSteel = 1
    Fy_Steel = 481
    E0_Steel = 210000
    bs_Steel = 0.005
    R0 = 12.5
    cR1 = 0.925
    cR2 = 0.15
    ops.uniaxialMaterial('Steel02', IDSteel, Fy_Steel, E0_Steel, bs_Steel, R0, cR1, cR2)

    IDCoverC = 2
    fpc_cover = -45
    epsc0_cover = -0.0038
    fpcu_cover = -8
    epsU_cover = -0.06
    ops.uniaxialMaterial('Concrete01', IDCoverC, fpc_cover, epsc0_cover, fpcu_cover, epsU_cover)

    IDCoreC = 3
    fpc_core = -58
    epsc0_core = -0.0044
    fpcu_core = -22
    epsU_core = -0.06
    ops.uniaxialMaterial('Concrete01', IDCoreC, fpc_core, epsc0_core, fpcu_core, epsU_core)

    # GAP
    IDGap = 4
    ops.uniaxialMaterial('ElasticPPGap', IDGap, 210000, -481, 0, 1 / 1000, "noDamage")

    IDPT = 5
    Fy_PT = 1720
    E0_PT = 210000
    bs_PT = 0.001
    R0 = 18
    cR1 = 0.925
    cR2 = 0.15
    a1 = 0
    a2 = 1
    a3 = 0
    a4 = 1
    sigInit = 928.57
    ops.uniaxialMaterial('Steel02', IDPT, Fy_PT, E0_PT, bs_PT, R0, cR1, cR2, a1, a2, a3, a4, sigInit)

    IDDamper = 6
    Fy_Damper = 45160
    E0_Damper = 70780
    bs_Damper = 0.02769
    R0 = 18
    cR1 = 0.925
    cR2 = 0.15
    ops.uniaxialMaterial('Steel02', IDDamper, Fy_Damper, E0_Damper, bs_Damper, R0, cR1, cR2)

    IDEDB = 7
    Fy_Steel = 400
    E0_Steel = 210000
    bs_Steel = 0.005
    R0 = 12.5
    cR1 = 0.925
    cR2 = 0.15
    ops.uniaxialMaterial('Steel02', IDEDB, Fy_Steel, E0_Steel, bs_Steel, R0, cR1, cR2)

    print("****************************************","Section","****************************************")
    Bcol = 500
    Hcol = Bcol
    c=30
    y1col = Hcol/2.0
    z1col = Bcol/2.0
    y2col = (Hcol-2*c)/5
    nFibZ=1
    nFib=20
    nFibCover, nFibCore = 2, 16
    As_bar = 200.96
    fiber_column_section=1
    ops.section('Fiber', fiber_column_section)
    ops.patch('rect', IDCoreC, nFibCore, nFibZ, c-y1col, c-z1col, y1col-c, z1col-c)
    ops.patch('rect', IDCoverC, nFib, nFibZ, -y1col, -z1col, y1col, c-z1col)
    ops.patch('rect', IDCoverC, nFib, nFibZ, -y1col, z1col-c, y1col, z1col)
    ops.patch('rect', IDCoverC, nFibCover, nFibZ, -y1col, c-z1col, c-y1col, z1col-c)
    ops.patch('rect', IDCoverC, nFibCover, nFibZ, y1col-c, c-z1col, y1col, z1col-c)
    ops.layer('straight', IDSteel, 6, As_bar, y1col-c, z1col-c, y1col-c, c-z1col)
    ops.layer('straight', IDSteel, 2, As_bar, y2col/2, z1col-c, y2col/2, c-z1col)
    ops.layer('straight', IDSteel, 2, As_bar, -y2col/2, z1col-c, -y2col/2, c-z1col)
    ops.layer('straight', IDSteel, 2, As_bar, y2col*1.5, z1col-c, y2col*1.5, c-z1col)
    ops.layer('straight', IDSteel, 2, As_bar, -y2col*1.5, z1col-c, -y2col*1.5, c-z1col)
    ops.layer('straight', IDSteel, 6, As_bar, c-y1col, z1col-c, c-y1col, c-z1col)

    Bcol = 500
    Hcol = Bcol
    c = 30
    y1col = Hcol / 2.0
    z1col = Bcol / 2.0
    y2col = (Hcol - 2 * c) / 5
    nFibZ = 1
    nFibZ2 = 5
    nFib = 20
    nFibCover, nFibCore = 2, 16
    As_bar = 200.96
    fiber_column_section2 = 2
    ops.section('Fiber', fiber_column_section2)
    ops.patch('rect', IDCoreC, nFibCore, nFibZ2, c - y1col, c - z1col, y1col - c, z1col - c)
    ops.patch('rect', IDCoverC, nFib, nFibZ, -y1col, -z1col, y1col, c - z1col)
    ops.patch('rect', IDCoverC, nFib, nFibZ, -y1col, z1col - c, y1col, z1col)
    ops.patch('rect', IDCoverC, nFibCover, nFibZ2, -y1col, c - z1col, c - y1col, z1col - c)
    ops.patch('rect', IDCoverC, nFibCover, nFibZ2, y1col - c, c - z1col, y1col, z1col - c)
    ops.layer('straight', IDSteel, 4, As_bar, y1col - c, z1col - c, y1col - c, c - z1col)
    ops.layer('straight', IDSteel, 2, As_bar, y2col, z1col - c, y2col, c - z1col)
    ops.layer('straight', IDSteel, 2, As_bar, -y2col, z1col - c, -y2col, c - z1col)
    ops.layer('straight', IDSteel, 4, As_bar, c - y1col, z1col - c, c - y1col, c - z1col)

    Bbeam = 250
    Hbeam = 500
    c=30
    y1beam = Hbeam/2.0
    z1beam = Bbeam/2.0
    y2beam = (Hbeam-2*c)/5.0
    nFibZ=1
    nFibZ2 = 5
    nFib=20
    nFibCover, nFibCore = 2, 16
    As_bar = 3.14*8*8
    fiber_beam_section=3
    ops.section('Fiber', fiber_beam_section)
    ops.patch('rect', IDCoreC, nFibCore, nFibZ2, c-y1beam, c-z1beam, y1beam-c, z1beam-c)
    ops.patch('rect', IDCoverC, nFib, nFibZ, -y1beam, -z1beam, y1beam, c-z1beam)
    ops.patch('rect', IDCoverC, nFib, nFibZ, -y1beam, z1beam-c, y1beam, z1beam)
    ops.patch('rect', IDCoverC, nFibCover, nFibZ2, -y1beam, c-z1beam, c-y1beam, z1beam-c)
    ops.patch('rect', IDCoverC, nFibCover, nFibZ2, y1beam-c, c-z1beam, y1beam, z1beam-c)
    ops.layer('straight', IDSteel, 2, As_bar, y1beam - c, z1beam - c, y1beam - c, c - z1beam)
    ops.layer('straight', IDSteel, 2, As_bar, y2beam, z1beam - c, y2beam, c - z1beam)
    ops.layer('straight', IDSteel, 2, As_bar, -y2beam, z1beam - c, -y2beam, c - z1beam)
    ops.layer('straight', IDSteel, 2, As_bar, c - y1beam, z1beam - c, c - y1beam, c - z1beam)

    #Gap
    fiber_beam_gap_section=4
    ops.section('Fiber', fiber_beam_gap_section)
    ops.patch('rect', IDGap, nFibCore, nFibZ2, c-y1beam, c-z1beam, y1beam-c, z1beam-c)
    ops.patch('rect', IDGap, nFib, nFibZ, -y1beam, -z1beam, y1beam, c-z1beam)
    ops.patch('rect', IDGap, nFib, nFibZ, -y1beam, z1beam-c, y1beam, z1beam)
    ops.patch('rect', IDGap, nFibCover, nFibZ2, -y1beam, c-z1beam, c-y1beam, z1beam-c)
    ops.patch('rect', IDGap, nFibCover, nFibZ2, y1beam-c, c-z1beam, y1beam, z1beam-c)
    ops.layer('straight', IDGap, 2, As_bar, y1beam - c, z1beam - c, y1beam - c, c - z1beam)
    ops.layer('straight', IDGap, 2, As_bar, y2beam, z1beam - c, y2beam, c - z1beam)
    ops.layer('straight', IDGap, 2, As_bar, -y2beam, z1beam - c, -y2beam, c - z1beam)
    ops.layer('straight', IDGap, 2, As_bar, c - y1beam, z1beam - c, c - y1beam, c - z1beam)

    print("****************************************", "Node", "****************************************")
    ops.node(1,0,0)
    ops.node(2,6000,0)
    ops.node(3,6000+6000, 0)
    ops.node(4,6000+6000+6000,0)

    ops.fix(1,1,1,1)
    ops.fix(2,1,1,1)
    ops.fix(3,1,1,1)
    ops.fix(4,1,1,1)

    ops.node(1001,0,50)
    ops.node(1002,6000,50)
    ops.node(1003,6000+6000,50)
    ops.node(1004,6000+6000+6000,50)

    for i in range(6):
        ops.node(2001+i*8000,0,1650+i*3300)
        ops.node(2002+i*8000,6000,1650+i*3300)
        ops.node(2003+i*8000,6000+6000,1650+i*3300)
        ops.node(2004+i*8000,6000+6000+6000,1650+i*3300)

        ops.node(3001+i*8000,0,2890+i*3300)
        ops.node(3002+i*8000,440,2890+i*3300)
        ops.node(3003+i*8000,440,2890+i*3300)
        ops.node(3004+i*8000,5560,2890+i*3300)
        ops.node(3005+i*8000,5560,2890+i*3300)
        ops.node(3006+i*8000,6000,2890+i*3300)
        ops.node(3007+i*8000,6440,2890+i*3300)
        ops.node(3008+i*8000,6440,2890+i*3300)
        ops.node(3009+i*8000,11560,2890+i*3300)
        ops.node(3010+i*8000,11560,2890+i*3300)
        ops.node(3011+i*8000,12000,2890+i*3300)
        ops.node(3012+i*8000,12440,2890+i*3300)
        ops.node(3013+i*8000,12440,2890+i*3300)
        ops.node(3014+i*8000,17560,2890+i*3300)
        ops.node(3015+i*8000,17560,2890+i*3300)
        ops.node(3016+i*8000,18000,2890+i*3300)

        ops.node(4001+i*8000,0,2980+i*3300)
        ops.node(4002+i*8000,440,2980+i*3300)
        ops.node(4003+i*8000,440,2980+i*3300)
        ops.node(4004+i*8000,5560,2980+i*3300)
        ops.node(4005+i*8000,5560,2980+i*3300)
        ops.node(4006+i*8000,6000,2980+i*3300)
        ops.node(4007+i*8000,6440,2980+i*3300)
        ops.node(4008+i*8000,6440,2980+i*3300)
        ops.node(4009+i*8000,11560,2980+i*3300)
        ops.node(4010+i*8000,11560,2980+i*3300)
        ops.node(4011+i*8000,12000,2980+i*3300)
        ops.node(4012+i*8000,12440,2980+i*3300)
        ops.node(4013+i*8000,12440,2980+i*3300)
        ops.node(4014+i*8000,17560,2980+i*3300)
        ops.node(4015+i*8000,17560,2980+i*3300)
        ops.node(4016+i*8000,18000,2980+i*3300)

        ops.node(5001+i*8000,0,3050+i*3300)
        ops.node(5002+i*8000,6000,3050+i*3300)
        ops.node(5003+i*8000,12000,3050+i*3300)
        ops.node(5004+i*8000,18000,3050+i*3300)

        ops.node(6001+i*8000,0,3100+i*3300)
        ops.node(6002+i*8000,220,3100+i*3300)
        ops.node(6003+i*8000,320,3100+i*3300)
        ops.node(6004+i*8000,5680,3100+i*3300)
        ops.node(6005+i*8000,5780,3100+i*3300)
        ops.node(6006+i*8000,6000,3100+i*3300)
        ops.node(6007+i*8000,6220,3100+i*3300)
        ops.node(6008+i*8000,6320,3100+i*3300)
        ops.node(6009+i*8000,11680,3100+i*3300)
        ops.node(6010+i*8000,11780,3100+i*3300)
        ops.node(6011+i*8000,12000,3100+i*3300)
        ops.node(6012+i*8000,12220,3100+i*3300)
        ops.node(6013+i*8000,12320,3100+i*3300)
        ops.node(6014+i*8000,17680,3100+i*3300)
        ops.node(6015+i*8000,17780,3100+i*3300)
        ops.node(6016+i*8000,18000,3100+i*3300)

        ops.node(7001+i*8000,0,3300+i*3300)
        ops.node(7002+i*8000,200,3300+i*3300)#保护层
        ops.node(7003+i*8000,220,3300+i*3300)#保护层
        ops.node(7004+i*8000,320,3300+i*3300)
        ops.node(7005+i*8000,440,3300+i*3300)
        ops.node(7006+i*8000,3000,3300+i*3300)
        ops.node(7007+i*8000,5560,3300+i*3300)
        ops.node(7008+i*8000,5680,3300+i*3300)
        ops.node(7009+i*8000,5780,3300+i*3300)#保护层
        ops.node(7010+i*8000,5800,3300+i*3300)#保护层
        ops.node(7011+i*8000,6000,3300+i*3300)
        ops.node(7012+i*8000,6200,3300+i*3300)#保护层
        ops.node(7013+i*8000,6220,3300+i*3300)#保护层
        ops.node(7014+i*8000,6320,3300+i*3300)
        ops.node(7015+i*8000,6440,3300+i*3300)
        ops.node(7016+i*8000,9000,3300+i*3300)
        ops.node(7017+i*8000,11560,3300+i*3300)
        ops.node(7018+i*8000,11680,3300+i*3300)
        ops.node(7019+i*8000,11780,3300+i*3300)#保护层
        ops.node(7020+i*8000,11800,3300+i*3300)#保护层
        ops.node(7021+i*8000,12000,3300+i*3300)
        ops.node(7022+i*8000,12200,3300+i*3300)#保护层
        ops.node(7023+i*8000,12220,3300+i*3300)#保护层
        ops.node(7024+i*8000,12320,3300+i*3300)
        ops.node(7025+i*8000,12440,3300+i*3300)
        ops.node(7026+i*8000,15000,3300+i*3300)
        ops.node(7027+i*8000,17560,3300+i*3300)
        ops.node(7028+i*8000,17680,3300+i*3300)
        ops.node(7029+i*8000,17780,3300+i*3300)#保护层
        ops.node(7030+i*8000,17800,3300+i*3300)#保护层
        ops.node(7031+i*8000,18000,3300+i*3300)

        ops.equalDOF(7002+i*8000,7003+i*8000,2)
        ops.equalDOF(7010+i*8000,7009+i*8000,2)
        ops.equalDOF(7012+i*8000,7013+i*8000,2)
        ops.equalDOF(7020+i*8000,7019+i*8000,2)
        ops.equalDOF(7022+i*8000,7023+i*8000,2)
        ops.equalDOF(7030+i*8000,7029+i*8000,2)

        ops.node(8001+i*8000,0,3500+i*3300)
        ops.node(8002+i*8000,220,3500+i*3300)
        ops.node(8003+i*8000,320,3500+i*3300)
        ops.node(8004+i*8000,5680,3500+i*3300)
        ops.node(8005+i*8000,5780,3500+i*3300)
        ops.node(8006+i*8000,6000,3500+i*3300)
        ops.node(8007+i*8000,6220,3500+i*3300)
        ops.node(8008+i*8000,6320,3500+i*3300)
        ops.node(8009+i*8000,11680,3500+i*3300)
        ops.node(8010+i*8000,11780,3500+i*3300)
        ops.node(8011+i*8000,12000,3500+i*3300)
        ops.node(8012+i*8000,12220,3500+i*3300)
        ops.node(8013+i*8000,12320,3500+i*3300)
        ops.node(8014+i*8000,17680,3500+i*3300)
        ops.node(8015+i*8000,17780,3500+i*3300)
        ops.node(8016+i*8000,18000,3500+i*3300)

        ops.node(9001+i*8000,0,3550+i*3300)
        ops.node(9002+i*8000,6000,3550+i*3300)
        ops.node(9003+i*8000,12000,3550+i*3300)
        ops.node(9004+i*8000,18000,3550+i*3300)

    print("****************************************", "coordTransf", "****************************************")
    coordTransf = "PDelta"  # Linear, PDelta, Corotational
    IDColumnTransf = 1
    ops.geomTransf(coordTransf, IDColumnTransf)
    IDBeamTransf = 2
    ops.geomTransf(coordTransf, IDBeamTransf)

    print("****************************************", "beamIntegration", "****************************************")
    IDFCSIntegration = 1
    ops.beamIntegration('Trapezoidal', IDFCSIntegration, fiber_column_section,3)
    IDFCSIntegration2 = 2
    ops.beamIntegration('Trapezoidal', IDFCSIntegration2, fiber_column_section2,3)
    IDFBSIntegration = 3
    ops.beamIntegration('Trapezoidal', IDFBSIntegration, fiber_beam_section,3)
    IDFBGSIntegration = 4
    ops.beamIntegration('Trapezoidal', IDFBGSIntegration, fiber_beam_gap_section,3)

    print("****************************************", "Column", "****************************************")
    ops.element('elasticBeamColumn',1,1,1001,500*500,35000,500**4/12,IDColumnTransf)
    ops.element('elasticBeamColumn',2,2,1002,500*500,35000,500**4/12,IDColumnTransf)
    ops.element('elasticBeamColumn',3,3,1003,500*500,35000,500**4/12,IDColumnTransf)
    ops.element('elasticBeamColumn',4,4,1004,500*500,35000,500**4/12,IDColumnTransf)

    for i in range(6):
        if i==0:
            ops.element('dispBeamColumn',1001+i*100000,1001+i*8000,2001+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',1002+i*100000,1002+i*8000,2002+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',1003+i*100000,1003+i*8000,2003+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',1004+i*100000,1004+i*8000,2004+i*8000,IDColumnTransf,IDFCSIntegration)

            ops.element('dispBeamColumn',2001+i*100000,2001+i*8000,3001+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',2002+i*100000,2002+i*8000,3006+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',2003+i*100000,2003+i*8000,3011+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',2004+i*100000,2004+i*8000,3016+i*8000,IDColumnTransf,IDFCSIntegration)

            ops.element('dispBeamColumn',3001+i*100000,3001+i*8000,4001+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',3002+i*100000,3006+i*8000,4006+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',3003+i*100000,3011+i*8000,4011+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',3004+i*100000,3016+i*8000,4016+i*8000,IDColumnTransf,IDFCSIntegration)

            ops.element('dispBeamColumn',4001+i*100000,4001+i*8000,5001+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',4002+i*100000,4006+i*8000,5002+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',4003+i*100000,4011+i*8000,5003+i*8000,IDColumnTransf,IDFCSIntegration)
            ops.element('dispBeamColumn',4004+i*100000,4016+i*8000,5004+i*8000,IDColumnTransf,IDFCSIntegration)

            ops.element('elasticBeamColumn',5001+i*100000,5001+i*8000,6001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',5002+i*100000,5002+i*8000,6006+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',5003+i*100000,5003+i*8000,6011+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',5004+i*100000,5004+i*8000,6016+i*8000,500*500,35000,500**4/12,IDColumnTransf)

            ops.element('elasticBeamColumn',6001+i*100000,6001+i*8000,7001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',6002+i*100000,6006+i*8000,7011+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',6003+i*100000,6011+i*8000,7021+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',6004+i*100000,6016+i*8000,7031+i*8000,500*500,35000,500**4/12,IDColumnTransf)

            ops.element('elasticBeamColumn',7001+i*100000,7001+i*8000,8001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',7002+i*100000,7011+i*8000,8006+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',7003+i*100000,7021+i*8000,8011+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',7004+i*100000,7031+i*8000,8016+i*8000,500*500,35000,500**4/12,IDColumnTransf)

            ops.element('elasticBeamColumn',8001+i*100000,8001+i*8000,9001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',8002+i*100000,8006+i*8000,9002+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',8003+i*100000,8011+i*8000,9003+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',8004+i*100000,8016+i*8000,9004+i*8000,500*500,35000,500**4/12,IDColumnTransf)
        else:
            ops.element('dispBeamColumn',1001+i*100000,1001+i*8000,2001+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',1002+i*100000,1002+i*8000,2002+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',1003+i*100000,1003+i*8000,2003+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',1004+i*100000,1004+i*8000,2004+i*8000,IDColumnTransf,IDFCSIntegration2)

            ops.element('dispBeamColumn',2001+i*100000,2001+i*8000,3001+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',2002+i*100000,2002+i*8000,3006+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',2003+i*100000,2003+i*8000,3011+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',2004+i*100000,2004+i*8000,3016+i*8000,IDColumnTransf,IDFCSIntegration2)

            ops.element('dispBeamColumn',3001+i*100000,3001+i*8000,4001+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',3002+i*100000,3006+i*8000,4006+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',3003+i*100000,3011+i*8000,4011+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',3004+i*100000,3016+i*8000,4016+i*8000,IDColumnTransf,IDFCSIntegration2)

            ops.element('dispBeamColumn',4001+i*100000,4001+i*8000,5001+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',4002+i*100000,4006+i*8000,5002+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',4003+i*100000,4011+i*8000,5003+i*8000,IDColumnTransf,IDFCSIntegration2)
            ops.element('dispBeamColumn',4004+i*100000,4016+i*8000,5004+i*8000,IDColumnTransf,IDFCSIntegration2)

            ops.element('elasticBeamColumn',5001+i*100000,5001+i*8000,6001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',5002+i*100000,5002+i*8000,6006+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',5003+i*100000,5003+i*8000,6011+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',5004+i*100000,5004+i*8000,6016+i*8000,500*500,35000,500**4/12,IDColumnTransf)

            ops.element('elasticBeamColumn',6001+i*100000,6001+i*8000,7001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',6002+i*100000,6006+i*8000,7011+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',6003+i*100000,6011+i*8000,7021+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',6004+i*100000,6016+i*8000,7031+i*8000,500*500,35000,500**4/12,IDColumnTransf)

            ops.element('elasticBeamColumn',7001+i*100000,7001+i*8000,8001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',7002+i*100000,7011+i*8000,8006+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',7003+i*100000,7021+i*8000,8011+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',7004+i*100000,7031+i*8000,8016+i*8000,500*500,35000,500**4/12,IDColumnTransf)

            ops.element('elasticBeamColumn',8001+i*100000,8001+i*8000,9001+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',8002+i*100000,8006+i*8000,9002+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',8003+i*100000,8011+i*8000,9003+i*8000,500*500,35000,500**4/12,IDColumnTransf)
            ops.element('elasticBeamColumn',8004+i*100000,8016+i*8000,9004+i*8000,500*500,35000,500**4/12,IDColumnTransf)

    print("****************************************", "Beam", "****************************************")
    for i in range(6):
        ops.element('elasticBeamColumn',9001+i*100000,7001+i*8000,7002+i*8000,250*500,35000,250*500**3/12,IDBeamTransf)
        ops.element('dispBeamColumn',9002+i*100000,7002+i*8000,7003+i*8000,IDBeamTransf,IDFBGSIntegration)
        ops.element('dispBeamColumn',9003+i*100000,7003+i*8000,7004+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9004+i*100000,7004+i*8000,7005+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9005+i*100000,7005+i*8000,7006+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9006+i*100000,7006+i*8000,7007+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9007+i*100000,7007+i*8000,7008+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9008+i*100000,7008+i*8000,7009+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9009+i*100000,7009+i*8000,7010+i*8000,IDBeamTransf,IDFBGSIntegration)
        ops.element('elasticBeamColumn',9010+i*100000,7010+i*8000,7011+i*8000,250*500,35000,500*250**3/12,IDBeamTransf)

        ops.element('elasticBeamColumn',9011+i*100000,7011+i*8000,7012+i*8000,250*500,35000,500*250**3/12,IDBeamTransf)
        ops.element('dispBeamColumn',9012+i*100000,7012+i*8000,7013+i*8000,IDBeamTransf,IDFBGSIntegration)
        ops.element('dispBeamColumn',9013+i*100000,7013+i*8000,7014+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9014+i*100000,7014+i*8000,7015+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9015+i*100000,7015+i*8000,7016+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9016+i*100000,7016+i*8000,7017+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9017+i*100000,7017+i*8000,7018+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9018+i*100000,7018+i*8000,7019+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9019+i*100000,7019+i*8000,7020+i*8000,IDBeamTransf,IDFBGSIntegration)
        ops.element('elasticBeamColumn',9020+i*100000,7020+i*8000,7021+i*8000,250*500,35000,500*250**3/12,IDBeamTransf)

        ops.element('elasticBeamColumn',9021+i*100000,7021+i*8000,7022+i*8000,250*500,35000,500*250**3/12,IDBeamTransf)
        ops.element('dispBeamColumn',9022+i*100000,7022+i*8000,7023+i*8000,IDBeamTransf,IDFBGSIntegration)
        ops.element('dispBeamColumn',9023+i*100000,7023+i*8000,7024+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9024+i*100000,7024+i*8000,7025+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9025+i*100000,7025+i*8000,7026+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9026+i*100000,7026+i*8000,7027+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9027+i*100000,7027+i*8000,7028+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9028+i*100000,7028+i*8000,7029+i*8000,IDBeamTransf,IDFBSIntegration)
        ops.element('dispBeamColumn',9029+i*100000,7029+i*8000,7030+i*8000,IDBeamTransf,IDFBGSIntegration)
        ops.element('elasticBeamColumn',9030+i*100000,7030+i*8000,7031+i*8000,250*500,35000,500*250**3/12,IDBeamTransf)

    print("****************************************", "RigidLink", "****************************************")
    D = 200
    for i in range(6):
        ops.element('elasticBeamColumn',10001+i*100000,3001+i*8000,3002+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10002+i*100000,7005+i*8000,3003+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10003+i*100000,4001+i*8000,4002+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10004+i*100000,7005+i*8000,4003+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10005+i*100000,6001+i*8000,6002+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10006+i*100000,7004+i*8000,6003+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10007+i*100000,8001+i*8000,8002+i*8000,3.14*D**2/4,1e10,3.14*D**4/64, IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10008+i*100000,7004+i*8000,8003+i*8000,3.14*D**2/4,1e10,3.14*D**4/64, IDColumnTransf)#EDB

        ops.element('elasticBeamColumn',10009+i*100000,3004+i*8000,3006+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10010+i*100000,7007+i*8000,3005+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10011+i*100000,4004+i*8000,4006+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10012+i*100000,7007+i*8000,4005+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10013+i*100000,6005+i*8000,6006+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10014+i*100000,7008+i*8000,6004+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10015+i*100000,8005+i*8000,8006+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10016+i*100000,7008+i*8000,8004+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB

        ops.element('elasticBeamColumn',10017+i*100000,3006+i*8000,3007+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10018+i*100000,7015+i*8000,3008+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10019+i*100000,4006+i*8000,4007+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10020+i*100000,7015+i*8000,4008+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10021+i*100000,6006+i*8000,6007+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10022+i*100000,7014+i*8000,6008+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10023+i*100000,8006+i*8000,8007+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10024+i*100000,7014+i*8000,8008+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB

        ops.element('elasticBeamColumn',10025+i*100000,3009+i*8000,3011+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10026+i*100000,7017+i*8000,3010+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10027+i*100000,4009+i*8000,4011+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10028+i*100000,7017+i*8000,4010+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10029+i*100000,6010+i*8000,6011+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10030+i*100000,7018+i*8000,6009+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10031+i*100000,8010+i*8000,8011+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10032+i*100000,7018+i*8000,8009+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB

        ops.element('elasticBeamColumn',10033+i*100000,3011+i*8000,3012+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10034+i*100000,7025+i*8000,3013+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10035+i*100000,4011+i*8000,4012+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10036+i*100000,7025+i*8000,4013+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10037+i*100000,6011+i*8000,6012+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10038+i*100000,7024+i*8000,6013+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10039+i*100000,8011+i*8000,8012+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10040+i*100000,7024+i*8000,8013+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB

        ops.element('elasticBeamColumn',10041+i*100000,3016+i*8000,3014+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10042+i*100000,7027+i*8000,3015+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10043+i*100000,4016+i*8000,4014+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10044+i*100000,7027+i*8000,4015+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#REDE
        ops.element('elasticBeamColumn',10045+i*100000,6016+i*8000,6015+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10046+i*100000,7028+i*8000,6014+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10047+i*100000,8016+i*8000,8015+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB
        ops.element('elasticBeamColumn',10048+i*100000,7028+i*8000,8014+i*8000,3.14*D**2/4,1e10,3.14*D**4/64,IDColumnTransf)#EDB

    print("****************************************", "PT Strands", "****************************************")
    for i in range(6):
        ops.element('truss',10049+i*100000,7001+i*8000,7031+i*8000,560,IDPT)

    print("****************************************", "Dampers", "****************************************")
    for i in range(0,3):
        ops.element('zeroLength',10050+i*100000,3002+i*8000,3003+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10051+i*100000,4002+i*8000,4003+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10052+i*100000,3004+i*8000,3005+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10053+i*100000,4004+i*8000,4005+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10054+i*100000,3007+i*8000,3008+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10055+i*100000,4007+i*8000,4008+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10056+i*100000,3009+i*8000,3010+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10057+i*100000,4009+i*8000,4010+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10058+i*100000,3012+i*8000,3013+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10059+i*100000,4012+i*8000,4013+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10060+i*100000,3014+i*8000,3015+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)
        ops.element('zeroLength',10061+i*100000,4014+i*8000,4015+i*8000,'-mat',IDDamper,IDDamper,'-dir',1,2)

    print("****************************************", "EDBs", "****************************************")
    D=12
    N=1
    for i in range(3,6):
        ops.element('truss',10062+i*100000,6002+i*8000,6003+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10063+i*100000,8002+i*8000,8003+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10064+i*100000,6004+i*8000,6005+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10065+i*100000,8004+i*8000,8005+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10066+i*100000,6007+i*8000,6008+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10067+i*100000,8007+i*8000,8008+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10068+i*100000,6009+i*8000,6010+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10069+i*100000,8009+i*8000,8010+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10070+i*100000,6012+i*8000,6013+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10071+i*100000,8012+i*8000,8013+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10072+i*100000,6014+i*8000,6015+i*8000,3.14*D**2/4*N,IDEDB)
        ops.element('truss',10073+i*100000,8014+i*8000,8015+i*8000,3.14*D**2/4*N,IDEDB)
    vfo.plot_model(show_nodes='yes', show_nodetags='yes',show_eletags='no', line_width=1)
    print("****************************************", "Mass", "****************************************")
    MASS_SIDE=(Hbeam*Bbeam*3000*3+Hcol*Bcol*3300+6000*3000*200)*2.5e-9
    MASS_CENTER=(Hbeam*Bbeam*6000*2+Hcol*Bcol*3300+6000*6000*200)*2.5e-9
    MASS_SIDE_TOP=(Hbeam*Bbeam*3000*3+Hcol*Bcol*3300/2+6000*3000*200)*2.5e-9
    MASS_CENTER_TOP=(Hbeam*Bbeam*6000*2+Hcol*Bcol*3300/2+6000*6000*200)*2.5e-9

    ops.mass(2001,Hcol*Bcol*3300*2.5e-9,Hcol*Bcol*3300*2.5e-9,0)
    ops.mass(2002,Hcol*Bcol*3300*2.5e-9,Hcol*Bcol*3300*2.5e-9,0)
    ops.mass(2003,Hcol*Bcol*3300*2.5e-9,Hcol*Bcol*3300*2.5e-9,0)
    ops.mass(2004,Hcol*Bcol*3300*2.5e-9,Hcol*Bcol*3300*2.5e-9,0)

    for i in range(0,5):
        ops.mass(7001+i*8000,MASS_SIDE,MASS_SIDE,0)
        ops.mass(7011+i*8000,MASS_CENTER,MASS_CENTER,0)
        ops.mass(7021+i*8000,MASS_CENTER,MASS_CENTER,0)
        ops.mass(7031+i*8000,MASS_SIDE,MASS_SIDE,0)
    for i in range(5,6):
        ops.mass(7001+i*8000,MASS_SIDE_TOP,MASS_SIDE_TOP,0)
        ops.mass(7011+i*8000,MASS_CENTER_TOP,MASS_CENTER_TOP,0)
        ops.mass(7021+i*8000,MASS_CENTER_TOP,MASS_CENTER_TOP,0)
        ops.mass(7031+i*8000,MASS_SIDE_TOP,MASS_SIDE_TOP,0)


    print("****************************************", "Rayleigh", "****************************************")
    xDamper=0.05
    nEigenI=1
    nEigenJ=2
    nEigenK=3
    lambdaN=ops.eigen('-genBandArpack',nEigenK)
    # lambdaN = ops.eigen('-fullGenLapack', nEigenK)
    lambdaI=lambdaN[nEigenI-1]
    lambdaJ=lambdaN[nEigenJ-1]
    lambdaK=lambdaN[nEigenK-1]
    omegaI=math.pow(lambdaI,0.5)
    omegaJ=math.pow(lambdaJ,0.5)
    omegaK=math.pow(lambdaK,0.5)
    alphaM=xDamper*(2*omegaI*omegaJ)/(omegaI+omegaJ)
    betaKcurr=2.0*xDamper/(omegaI+omegaJ)
    ops.rayleigh(alphaM,0,0,betaKcurr)

if __name__=="__main__":
    Model()