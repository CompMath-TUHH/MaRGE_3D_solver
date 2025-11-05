# MaRGE_3D_solver
Solver for MaRGE in 3D flow based on the method by Daitche (2013). Analytical solution in simple vortex is provided to validate the method.

MaRGE: Maxey-Riley-Gatignol equation

- "Dtche_J_cls_3D.py" has the class with numerical solver with first second and third order methods based on the scheme by Daitche (2013).
- "Analy_J_cla_3D.py" has the analytical solution class for MaRGE in simple vortex field based on the paper by Candelier et al. (2004).
- "Dtche_obj_3D.py" and "Analy_obj_3D.py" are the obejcts to show how to use the classes.
- "Dtche_J_parameters_3D.py" has all the parameters used in MaRGE.
- "Vortex_Fld_3D.py" is the vortex field.

Note: To compare the numerical solver with analytical solution, the values of parameters should be fixed.
