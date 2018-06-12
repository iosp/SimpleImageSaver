# snap

There is a new trend of developing algorithms with deep neural network (dnn).
We are trying to test that idea on data sets produced by in a simulated world and environment.
This python script is an example of how to produce thos kind of data sets.

ATTENTION!!!!
In order to be able to generate pictures, one need to activate the CAMERA(S) on the bobcat.
To activate the cameras on the bobcat, remove comments on the model.sdf of the bobcat regarding the cameras
in the live_bobcat directory:

<!-- CAM Sensors  -->
   <!-- <include>
      <uri>model://FLEA3_L</uri>
      <pose>-0.3 0.25 2.02 0 0 0</pose>
      <name>left_flea3</name>
    </include>
    <joint name='left_flea3_joint' type='revolute'>
      <child>left_flea3::camera_link</child>
      <parent>body</parent>
      <axis>
        <xyz>0 1 0</xyz>
        <limit>
          <lower>0</lower>
          <upper>0</upper>
        </limit>
        <dynamics/>
      </axis>
    </joint>
    
    <include>
      <uri>model://FLEA3_R</uri>
      <pose>-0.3 -0.25 2.02 0 0 0</pose>
      <name>right_flea3</name>
    </include>    
    <joint name='right_flea3_joint' type='revolute'>
      <child>right_flea3::camera_link</child>
      <parent>body</parent>
      <axis>
        <xyz>0 1 0</xyz>
        <limit>
          <lower>0</lower>
          <upper>0</upper>
        </limit>
        <xyz>0 1 0</xyz>
      <dynamics/>
      </axis>
    </joint>
-->
