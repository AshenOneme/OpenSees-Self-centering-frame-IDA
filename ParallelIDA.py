from Model import Model
import numpy as np
import os
import openseespy.opensees as ops
from mpi4py import MPI

Wave_name_list = os.listdir('E:\PyCharm\Master paper-IDA\Caculation file IDA\ATC-63')
Wave_name_list=[os.path.split(p)[-1][:-4] for p in Wave_name_list]
Wave_dt=[0.02 for i in range(13)]
PGA_Target=[0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.18,0.20,0.22,0.24,0.26,0.28,0.30,0.32,0.34,0.36,0.38,0.40,
            0.42,0.44,0.46,0.48,0.50,0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1.00]
def Parallel_OS():
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    txt_name_list = os.listdir('E:\PyCharm\Master paper-IDA\Caculation file IDA\ATC-63')
    Wave_file_path = f"E:\PyCharm\Master paper-IDA\Caculation file IDA\ATC-63\\{txt_name_list[rank]}"
    Output_wave = f'{Wave_name_list[rank]}'
    if not os.path.exists(Output_wave):
        os.makedirs(Output_wave)
    Wave_message = np.loadtxt(Wave_file_path)
    Wave_size = len(Wave_message)
    dt = Wave_dt[rank]
    PGA_Peak = np.max(np.abs(Wave_message))
    Model()
    jjj = 0
    for iii in PGA_Target:
        Output_PGA = f'{Wave_name_list[rank]}\\{PGA_Target[jjj]}g'
        if not os.path.exists(Output_PGA):
            os.makedirs(Output_PGA)
        Amplification_factor = PGA_Target[jjj]/PGA_Peak*10000

        print("****************************************", "Gravity", "****************************************")
        ops.timeSeries('Linear', 11)
        ops.pattern('Plain', 100, 11)

        for i in range(6):
            ops.eleLoad("-ele", 9005 + i * 100000, '-type', '-beamUniform', -20)
            ops.eleLoad("-ele", 9006 + i * 100000, '-type', '-beamUniform', -20)
            ops.eleLoad("-ele", 9015 + i * 100000, '-type', '-beamUniform', -20)
            ops.eleLoad("-ele", 9016 + i * 100000, '-type', '-beamUniform', -20)
            ops.eleLoad("-ele", 9025 + i * 100000, '-type', '-beamUniform', -20)
            ops.eleLoad("-ele", 9026 + i * 100000, '-type', '-beamUniform', -20)

        for i in range(6):
            ops.load(7001 + i * 8000, 0, -400 * 400 * 3300 * 2.5e-9 * 10000, 0)
            ops.load(7011 + i * 8000, 0, -400 * 400 * 3300 * 2.5e-9 * 10000, 0)
            ops.load(7021 + i * 8000, 0, -400 * 400 * 3300 * 2.5e-9 * 10000, 0)
            ops.load(7031 + i * 8000, 0, -400 * 400 * 3300 * 2.5e-9 * 10000, 0)

        ops.constraints("Penalty", 1e8, 1e8)
        ops.numberer("RCM")
        ops.system('UmfPack')
        ops.test('NormDispIncr', 1.e-2, 2000)
        ops.algorithm('NewtonLineSearch')
        ops.integrator("LoadControl", 0.1)
        ops.analysis("Static")
        ops.analyze(10)
        ops.loadConst("-time", 0.0)

        print("****************************************", "Recorder", "****************************************")
        ops.recorder('Node','-file',f"{Output_PGA}/Disp.txt","-time",'-node',1001,1002,1003,1004,7001,7011,7021,7031,
                     15001,15011,15021,15031,23001,23011,23021,23031,31001,31011,31021,31031,
                     39001,39011,39021,39031,47001,47011,47021,47031,'-dof',1,'disp')
        ops.recorder('Node','-file',f"{Output_PGA}/Reaction.txt","-time",'-node',1,2,3,4,'-dof',1,'reaction')
        ops.recorder('Element','-file',f"{Output_PGA}/Force1.txt","-time",'-ele',1001,1002,1003,1004,'globalForce')
        ops.recorder('Element','-file',f"{Output_PGA}/Force2.txt","-time",'-ele',101001,101002,101003,101004,'globalForce')
        ops.recorder('Element','-file',f"{Output_PGA}/Force3.txt","-time",'-ele',201001,201002,201003,201004,'globalForce')
        ops.recorder('Element','-file',f"{Output_PGA}/Force4.txt","-time",'-ele',301001,301002,301003,301004,'globalForce')
        ops.recorder('Element','-file',f"{Output_PGA}/Force5.txt","-time",'-ele',401001,401002,401003,401004,'globalForce')
        ops.recorder('Element','-file',f"{Output_PGA}/Force6.txt","-time",'-ele',501001,501002,501003,501004,'globalForce')
        ops.recorder('Element','-file',f"{Output_PGA}/Lbar.txt","-time",'-ele',9013,109013,209013,309013,409013,509013,'section',2,'fiber',250,125,1,'stressStrain')
        ops.recorder('Element','-file',f"{Output_PGA}/CoverC.txt","-time",'-ele',9013,109013,209013,309013,409013,509013,'section',2,'fiber',250,125,2,'stressStrain')
        ops.recorder('Element','-file',f"{Output_PGA}/CoreC.txt","-time",'-ele',9013,109013,209013,309013,409013,509013,'section',2,'fiber',250,125,3,'stressStrain')
        ops.recorder('Element','-file',f"{Output_PGA}/EDB1_AF.txt","-time",'-ele',310062,410062,510062,'axialForce')
        ops.recorder('Element','-file',f"{Output_PGA}/EDB1_DEF.txt","-time",'-ele',310062,410062,510062,'deformation')
        ops.recorder('Element','-file',f"{Output_PGA}/EDB2_AF.txt","-time",'-ele',310066,410066,510066,'axialForce')
        ops.recorder('Element','-file',f"{Output_PGA}/EDB2_DEF.txt","-time",'-ele',310066,410066,510066,'deformation')
        ops.recorder('Element','-file',f"{Output_PGA}/PT_AF.txt","-time",'-ele',10049,110049,210049,310049,410049,510049,'axialForce')
        ops.recorder('Element','-file',f"{Output_PGA}/PT_DEF.txt","-time",'-ele',10049,110049,210049,310049,410049,510049,'deformation')
        ops.recorder('Element','-file',f"{Output_PGA}/REDE1_DEF.txt","-time",'-ele',10050,110050,210050,'deformation')
        ops.recorder('Element','-file',f"{Output_PGA}/REDE1_LF.txt","-time",'-ele',10050,110050,210050,'localForce')
        ops.recorder('Element','-file',f"{Output_PGA}/REDE2_DEF.txt","-time",'-ele',10051,110051,210051,'deformation')
        ops.recorder('Element','-file',f"{Output_PGA}/REDE2_LF.txt","-time",'-ele',10051,110051,210051,'localForce')


        print("****************************************", "GroundMotion", "****************************************")
        ops.timeSeries('Path',22,'-dt',dt,'-filePath',Wave_file_path,'-factor',Amplification_factor)
        ops.pattern('UniformExcitation', 200, 1, '-accel', 22)
        ops.wipeAnalysis()
        ops.constraints("Penalty", 1e8, 1e8)
        # ops.constraints("Transformation")
        ops.numberer('RCM')
        ops.system('UmfPack')
        ops.test("NormDispIncr", 1.e-1, 1000)
        # ops.algorithm('KrylovNewton')
        # ops.algorithm('ExpressNewton',2,1.0,'-currentTangent','-factorOnce')
        ops.algorithm('NewtonLineSearch')
        ops.integrator('Newmark', 0.5, 0.25)
        ops.analysis('Transient')
        ops.analyze(Wave_size*4,dt/4)

        ops.remove('recorders')
        ops.reset()
        ops.remove('loadPattern',100)
        ops.reset()
        ops.remove('loadPattern',200)
        ops.reset()
        ops.remove('timeSeries',11)
        ops.reset()
        ops.remove('timeSeries',22)
        ops.reset()
        ops.wipeAnalysis()
        print(f"{Wave_name_list[rank]}-PGA={PGA_Target[jjj]}g==>分析完成")
        jjj += 1

Parallel_OS()