# OpenSees-Self-centering-frame-IDA
### :panda_face:ATC-63推荐地震波 ###   
**[特别声明]**
所有地震波均进行了归一化处理，时间间隔设为0.02s，敬请放心调用。
---------------------------------------------------------------
* ### 地震波反应谱 ###
<div align=center>
<img height="250" src="https://user-images.githubusercontent.com/98397090/215052423-706f35e6-3e8a-414b-8fba-5f2682c5886d.png"/>
<img height="250" src="https://user-images.githubusercontent.com/98397090/215052469-05645b38-305d-40fd-9ebd-fd08d976df0d.png"/>
</div>

**[特别声明]**
IDA分析模型基于Python3.9.8 | OpenSeespy3.4.0.1
---------------------------------------------------------------
* ### OpenSeespy建模信息 ###
<div align=center><img width="500" height="500" src="https://user-images.githubusercontent.com/98397090/215063645-e698ed05-4f70-49cd-b98b-91d4692649ec.png"/></div>

* ### IDA分析结果展示 ###
<table align="center" border="0" style="border-collapse: collapse;">
  <tr>
    <td><img height="180px" src="https://user-images.githubusercontent.com/98397090/215072316-2d9b1a13-3a98-427c-bf7c-5ef6a4c370b0.png"/></td>
    <td><img height="180px" src="https://user-images.githubusercontent.com/98397090/215072331-f61bb75b-4063-4d79-92d3-0cbed5465fcb.png"/></td>
    <td><img height="180px" src="https://user-images.githubusercontent.com/98397090/215072340-185b5958-b00a-4ad1-95bf-fa0855a7350c.png"/></td>
  </tr>
  <tr>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215634956-6b4a7d32-345c-460e-b06a-c815f36e4093.png"/></td>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215635025-3777f1ca-34e4-484e-a393-a2ab5e7140df.png"/></td>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215635083-e8d100e3-2eed-42f8-a06f-dc1b4c371414.png"/></td>
  </tr>
  <tr>
    <td colspan="2"><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215635931-d155a366-c316-4380-962a-8ceb7c85e802.png"/></td>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215635982-3cde9e03-d8e7-48b9-980e-c2ce72d9cf6e.png"/></td>
  </tr>
  <tr>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215636281-65fc4cff-ab0e-40cd-943b-28c4faebad50.png"/></td>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215636396-54a4d512-6521-416b-b88f-de4df96d1418.png"/></td>
    <td><div align=center><img height="180px" src="https://user-images.githubusercontent.com/98397090/215636431-75e1de08-3a8f-4f44-adff-47b65ee3cb52.png"/></td>
  </tr>
  <tr>
    <td colspan="3"><div align=center><img height="300px" src="https://user-images.githubusercontent.com/98397090/215636562-53c2a2b4-9efb-4e0e-9e8d-01779b488f68.png"/></td>
  </tr>
</table>

* ### Recorder method ###
```diff
+[特别声明] OpenSees输出调用方法
--->记录节点在1方向的位移
ops.recorder('Node','-file',f"{Output_PGA}/Disp.txt","-time",'-node',1001,1002,1003,1004,7001,7011,7021,7031,
                     15001,15011,15021,15031,23001,23011,23021,23031,31001,31011,31021,31031,
                     39001,39011,39021,39031,47001,47011,47021,47031,'-dof',1,'disp')
--->记录节点在1方向的反力
ops.recorder('Node','-file',f"{Output_PGA}/Reaction.txt","-time",'-node',1,2,3,4,'-dof',1,'reaction')
--->记录单元在整体坐标系的力
ops.recorder('Element','-file',f"{Output_PGA}/Force1.txt","-time",'-ele',1001,1002,1003,1004,'globalForce')
--->记录纵筋在第2个积分截面处，距离截面坐标(250,125)最近的纤维处，材料1的应力应变                                [第二个积分点] [纤维坐标] [材料1] [应力应变]
ops.recorder('Element','-file',f"{Output_PGA}/Lbar.txt","-time",'-ele',9013,109013,209013,309013,409013,509013,'section',2,'fiber',250,125,1,'stressStrain')
--->记录保护层混凝土在第2个积分截面处，距离截面坐标(250,125)最近的纤维处，材料2的应力应变                         [第二个积分点] [纤维坐标] [材料1] [应力应变]
ops.recorder('Element','-file',f"{Output_PGA}/CoverC.txt","-time",'-ele',9013,109013,209013,309013,409013,509013,'section',2,'fiber',250,125,2,'stressStrain')
--->记录桁架单元的轴力
ops.recorder('Element','-file',f"{Output_PGA}/EDB1_AF.txt","-time",'-ele',310062,410062,510062,'axialForce')
--->记录桁架单元的变形
ops.recorder('Element','-file',f"{Output_PGA}/EDB1_DEF.txt","-time",'-ele',310062,410062,510062,'deformation')
--->记录阻尼器的变形
ops.recorder('Element','-file',f"{Output_PGA}/REDE1_DEF.txt","-time",'-ele',10050,110050,210050,'deformation')
--->记录阻尼器的出力
ops.recorder('Element','-file',f"{Output_PGA}/REDE1_LF.txt","-time",'-ele',10050,110050,210050,'localForce')
```
